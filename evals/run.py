#!/usr/bin/env python3
"""Run the verve corpus and report what held.

The skill itself is prose and stays that way. This lives outside skills/ so the
CI check that keeps the skill free of executable code still passes.

Usage:
    python3 evals/run.py --dry-run     # assemble and validate, no API calls
    python3 evals/run.py               # run the corpus, costs money
    python3 evals/run.py --only triage
    python3 evals/run.py --runs 3      # repeat each case, report worst result
    python3 evals/run.py --via cli --runs 3 --save evals/runs/NAME

--via api (the default) needs ANTHROPIC_API_KEY and the anthropic package.
--via cli drives the Claude Code CLI instead, one fresh `claude -p` per case,
with the skill as the whole system prompt, no tools, no settings files and no
CLAUDE.md. It runs on whatever the CLI is logged in as, so a run needs no key.
Needs Python 3.11 or newer.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "verve" / "SKILL.md"
REFERENCES = ROOT / "skills" / "verve" / "references"
CORPUS = Path(__file__).resolve().parent / "corpus.toml"

DEFAULT_MODEL = "claude-opus-5"
MAX_TOKENS = 4096


# --------------------------------------------------------------------------
# Assembling the skill
# --------------------------------------------------------------------------


def strip_frontmatter(text: str) -> str:
    return re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S)


def build_system_prompt() -> str:
    """Inline SKILL.md and every reference it names.

    A real session reads references on demand. Inlining them is a deliberate
    difference: it removes retrieval as a variable, so a failure is the
    instructions failing rather than the model declining to open a file. That
    makes this a floor rather than a simulation, and the README says so.
    """
    if not SKILL.is_file():
        sys.exit(f"No SKILL.md at {SKILL}")

    parts = [strip_frontmatter(SKILL.read_text(encoding="utf-8")).strip()]

    named = sorted(set(re.findall(r"references/([a-z0-9_-]+\.md)", parts[0])))
    if not named:
        sys.exit("SKILL.md names no reference files. Check the path pattern.")

    for name in named:
        path = REFERENCES / name
        if not path.is_file():
            sys.exit(f"SKILL.md names references/{name}, which does not exist")
        body = path.read_text(encoding="utf-8").strip()
        parts.append(f"\n\n===== references/{name} =====\n\n{body}")

    return "".join(parts)


# --------------------------------------------------------------------------
# Cases
# --------------------------------------------------------------------------


@dataclass
class Case:
    id: str
    kind: str
    request: str
    text: str
    why: str
    unchanged: bool = False
    must_survive: list[str] = field(default_factory=list)
    must_survive_any_case: list[str] = field(default_factory=list)
    must_go: list[str] = field(default_factory=list)
    must_match: list[str] = field(default_factory=list)
    must_not_match: list[str] = field(default_factory=list)
    claims: list[str] = field(default_factory=list)
    max_loss: float | None = None
    max_gain: float | None = None

    def prompt(self) -> str:
        return f"{self.request}\n\n{self.text.strip()}"


def load_cases() -> list[Case]:
    with CORPUS.open("rb") as fh:
        raw = tomllib.load(fh)

    cases: list[Case] = []
    seen: set[str] = set()
    for entry in raw.get("case", []):
        case = Case(**entry)
        if case.id in seen:
            sys.exit(f"Duplicate case id: {case.id}")
        seen.add(case.id)
        asserts = (case.unchanged or case.must_survive
                   or case.must_survive_any_case or case.must_go
                   or case.must_match or case.must_not_match)
        if not asserts:
            sys.exit(f"Case {case.id} asserts nothing")
        for pattern in case.must_match + case.must_not_match:
            try:
                re.compile(pattern)
            except re.error as exc:
                sys.exit(f"Case {case.id}: bad must_match pattern {pattern!r}: {exc}")
        if case.max_loss is not None and not 0 < case.max_loss < 1:
            sys.exit(f"Case {case.id}: max_loss must be between 0 and 1")
        if case.max_gain is not None and case.max_gain <= 0:
            sys.exit(f"Case {case.id}: max_gain must be above 0")
        if case.unchanged and (case.max_loss is not None or case.max_gain is not None):
            sys.exit(f"Case {case.id}: a triage case cannot set max_loss or max_gain")
        cases.append(case)

    if not cases:
        sys.exit("Corpus is empty")
    return cases


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------


def normalise(text: str) -> str:
    """Collapse whitespace and casing, for containment checks that should err
    towards firing."""
    return re.sub(r"\s+", " ", text).strip().lower()


def normalise_ws(text: str) -> str:
    """Collapse whitespace only. Casing is kept, because a triage pass that
    re-cased the text has changed it, and a check that lowercased both sides
    would call that unchanged."""
    return re.sub(r"\s+", " ", text).strip()


def words(text: str) -> int:
    return len(text.split())


# The one line SKILL.md permits a triage case to add, current wording first,
# then the wording before 2026-09-10, kept so historical runs still grade.
# Matched case-insensitively with any italic or bold markers stripped, since
# the skill shows the line in italics. At most one occurrence is stripped: a
# second copy of the line is commentary, and commentary fails the case.
TRIAGE_LINES = (
    "no changes needed for this request.",
    "this already reads as human-written; returned unchanged.",
)


TOOL_MARKUP = re.compile(
    r"<(?:invoke|parameter|invoke_response|function_calls)\b"   # XML-shaped
    r"|^\s*\*{0,2}Tool: ?\w+\*{0,2}\s*$",                      # **Tool: bash**
    re.M)


def strip_triage_line(text: str) -> str:
    for line in TRIAGE_LINES:
        pattern = r"[*_]*" + re.escape(line) + r"[*_]*"
        if re.search(pattern, text, flags=re.I):
            return re.sub(pattern, "", text, count=1, flags=re.I).strip()
    return text.strip()


def check(case: Case, output: str) -> list[str]:
    """Return the reasons this case failed. Empty means it held.

    Two asymmetries here are deliberate.

    must_survive is case-sensitive, because constraint 2 protects exact
    wording: gateway.pool.perrequest is not gateway.pool.perRequest, and a
    check that accepted it would be asserting the opposite of the rule. Use
    must_survive_any_case for ordinary vocabulary, which legitimately changes
    case when a rewrite moves it to the front of a sentence.

    must_go is case-insensitive, because a banned phrase is banned in any
    casing. Both directions therefore err towards failing.
    """
    failures: list[str] = []

    # Every case, whatever it asserts: a tool call written out as text is
    # never part of a rewrite. A model with no tool to call printed one on
    # 24 Sep 2026 and every asserted string survived around it.
    if TOOL_MARKUP.search(output):
        failures.append("a tool call written out as text")

    if case.unchanged:
        payload = normalise_ws(case.text)
        out_ws = normalise_ws(output)
        if payload not in out_ws:
            hint = (" (present in another casing)"
                    if payload.lower() in out_ws.lower() else "")
            failures.append(f"triage rewrote text that already reads as human{hint}")
        elif strip_triage_line(out_ws) != payload:
            # The input is in there, but so is something else: a second
            # version, a critique, a repeated preamble, a list of what it
            # would have changed. The skill permits exactly one line, and an
            # output that keeps the text while adding commentary has not
            # returned it unchanged.
            failures.append("triage returned the text but added more than the one permitted line")
    elif normalise(case.text) in normalise(output):
        # A rewrite case that returns its own input, with or without a
        # preamble wrapped round it, has done nothing. Without this, a case
        # asserting only must_survive passes on a verbatim no-op, because
        # every fact trivially survives text that was never touched.
        failures.append("no-op: the input came back whole, nothing was rewritten")

    for fact in case.must_survive:
        if fact not in output:
            hint = " (present in another casing)" if fact.lower() in output.lower() else ""
            failures.append(f"lost: {fact!r}{hint}")

    for fact in case.must_survive_any_case:
        if fact.lower() not in output.lower():
            failures.append(f"lost: {fact!r}")

    for banned in case.must_go:
        if banned.lower() in output.lower():
            failures.append(f"kept: {banned!r}")

    for pattern in case.must_match:
        # A smoke check for content whose wording legitimately varies (an
        # apology, a modality). Matching proves a shape is present, not that
        # the meaning is right: "we are not sorry" matches an apology
        # pattern. Do not treat a green must_match as the semantic criterion.
        if not re.search(pattern, output, flags=re.I):
            failures.append(f"no match: {pattern!r}")

    for pattern in case.must_not_match:
        # The mirror of must_match, for shapes that must be absent in any
        # wording: a probability score, an invented first person.
        found = re.search(pattern, output, flags=re.I)
        if found:
            failures.append(f"matched: {pattern!r} at {found.group(0)!r}")

    if case.max_loss is not None:
        before, after = words(case.text), words(output)
        if before and after < before * (1 - case.max_loss):
            lost = 1 - (after / before)
            failures.append(
                f"cut {lost:.0%} of the words, over the {case.max_loss:.0%} "
                f"this case allows ({before} -> {after})"
            )

    if case.max_gain is not None:
        # max_loss alone can be gamed: drop the unlisted claims, keep the
        # listed substrings, and pad the result back over the line. A ceiling
        # on growth closes that, and a faithful rewrite has no reason to be
        # half as long again as its source.
        before, after = words(case.text), words(output)
        if before and after > before * (1 + case.max_gain):
            gained = (after / before) - 1
            failures.append(
                f"grew by {gained:.0%}, over the {case.max_gain:.0%} "
                f"this case allows ({before} -> {after})"
            )

    return failures


# --------------------------------------------------------------------------
# Running
# --------------------------------------------------------------------------


def call_model(client, model: str, system: str, prompt: str) -> str:
    message = client.messages.create(
        model=model,
        max_tokens=MAX_TOKENS,
        system=system,
        messages=[{"role": "user", "content": prompt}],
    )
    return "".join(block.text for block in message.content if block.type == "text")


def call_cli(model: str, system_file: Path, prompt: str) -> str:
    """One fresh Claude Code session per call, isolated from the machine.

    --setting-sources "" and --strict-mcp-config keep the user's settings,
    hooks, MCP servers and CLAUDE.md out of the context, and running in an
    empty directory keeps a project's out too. --tools "" means the model can
    only answer, which is what the API path does. What remains is the CLI's
    own short preamble, which the API path does not have: a known difference,
    and small against a skill of this size.
    """
    command = ["claude", "-p", "--model", model,
               "--system-prompt-file", str(system_file),
               "--tools", "", "--setting-sources", "", "--strict-mcp-config",
               "--no-session-persistence"]
    # One retry on a timeout, because a CLI call occasionally stalls on the
    # network and a stall is the harness failing, not the skill.
    for attempt in (1, 2):
        try:
            with tempfile.TemporaryDirectory() as cwd:
                done = subprocess.run(command, input=prompt, capture_output=True,
                                      text=True, cwd=cwd, timeout=300)
            break
        except subprocess.TimeoutExpired:
            if attempt == 2:
                raise
    if done.returncode != 0:
        # The CLI reports some failures (a usage limit, an auth lapse) on
        # stdout with an empty stderr, so say whichever has something in it.
        detail = (done.stderr.strip() or done.stdout.strip())[:300]
        raise RuntimeError(f"claude -p exited {done.returncode}: {detail}")
    return done.stdout


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="no API calls")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--only", help="run one kind: triage, fidelity, variety, audience, "
                                       "overshare, tells, voice, detect, contact")
    parser.add_argument("--runs", type=int, default=1, help="repeats per case")
    parser.add_argument("--verbose", action="store_true", help="print every output")
    parser.add_argument("--via", choices=("api", "cli"), default="api",
                        help="api: the Anthropic SDK; cli: the claude CLI, no key needed")
    parser.add_argument("--jobs", type=int, default=4, help="parallel calls, --via cli only")
    parser.add_argument("--save", help="write each run's outputs as JSON for grade.py: "
                                       "PATH.json, or PATH-runN.json when --runs > 1")
    args = parser.parse_args()

    # Without this, --runs 0 makes no calls and reports every case as passing,
    # which is the most dangerous possible output from a test harness.
    if args.runs < 1:
        parser.error("--runs must be at least 1")

    system = build_system_prompt()
    cases = load_cases()
    if args.only:
        cases = [c for c in cases if c.kind == args.only]
        if not cases:
            sys.exit(f"No cases of kind {args.only!r}")

    print(f"skill prompt: {len(system):,} chars from SKILL.md and its references")
    print(f"corpus: {len(cases)} cases, {args.runs} run(s) each\n")

    if args.dry_run:
        for case in cases:
            print(f"  {case.kind:9} {case.id}")
            survive = len(case.must_survive) + len(case.must_survive_any_case)
            loss = "" if case.max_loss is None else f", max_loss={case.max_loss:.0%}"
            gain = "" if case.max_gain is None else f", max_gain={case.max_gain:.0%}"
            match = "" if not case.must_match else f", {len(case.must_match)} match"
            match += "" if not case.must_not_match else f", {len(case.must_not_match)} must not match"
            print(f"            asserts: {survive} survive, {len(case.must_go)} go{match}, "
                  f"unchanged={case.unchanged}{loss}{gain}")
        print("\nDry run. Nothing was sent anywhere and nothing was measured.")
        return 0

    if args.via == "api":
        try:
            import anthropic
        except ImportError:
            sys.exit("pip install anthropic")
        if not os.environ.get("ANTHROPIC_API_KEY"):
            sys.exit("ANTHROPIC_API_KEY is not set")
        client = anthropic.Anthropic()
        workers = 1

        def call(prompt: str) -> str:
            return call_model(client, args.model, system, prompt)
    else:
        if not shutil.which("claude"):
            sys.exit("claude is not on PATH")
        system_file = Path(tempfile.mkstemp(prefix="verve-system-", suffix=".md")[1])
        system_file.write_text(system, encoding="utf-8")
        workers = max(1, args.jobs)

        def call(prompt: str) -> str:
            return call_cli(args.model, system_file, prompt)

    # Every (case, run) pair is independent, so they run together and are
    # graded afterwards in corpus order.
    jobs = [(case, run) for run in range(args.runs) for case in cases]
    outputs: dict[tuple[str, int], str] = {}
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [(case, run, pool.submit(call, case.prompt())) for case, run in jobs]
        for done, (case, run, future) in enumerate(futures, 1):
            try:
                outputs[(case.id, run)] = future.result()
            except Exception as exc:  # a call that failed is a failed case, loudly
                outputs[(case.id, run)] = f"[harness error: {exc}]"
            print(f"  [{done}/{len(jobs)}] {case.id} run {run + 1}", file=sys.stderr, flush=True)

    if args.save:
        for run in range(args.runs):
            path = Path(f"{args.save}-run{run + 1}.json" if args.runs > 1 else f"{args.save}.json")
            path.write_text(json.dumps({c.id: outputs[(c.id, run)] for c in cases},
                                       indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
            print(f"saved {path}")

    results: list[tuple[Case, list[str]]] = []
    for case in cases:
        # Union the failures across runs rather than keeping whichever run
        # failed most. Two runs that each break one different rule are two
        # separate problems, and picking one by count hides the other.
        seen: list[str] = []
        for run in range(args.runs):
            output = outputs[(case.id, run)]
            if args.verbose:
                print(f"--- {case.id} run {run + 1} ---\n{output}\n")
            for reason in check(case, output):
                label = reason if args.runs == 1 else f"{reason}  [run {run + 1}]"
                if label not in seen:
                    seen.append(label)
        results.append((case, seen))
        mark = "pass" if not seen else "FAIL"
        print(f"  {mark}  {case.kind:9} {case.id}")
        for reason in seen:
            print(f"          {reason}")

    failed = [c for c, f in results if f]
    print(f"\n{len(results) - len(failed)}/{len(results)} passed on {args.model} via {args.via}")

    if failed:
        print("\nWhat each failure was protecting:\n")
        for case in failed:
            print(f"  {case.id}\n    {case.why}\n")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
