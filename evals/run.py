#!/usr/bin/env python3
"""Run the verve corpus and report what held.

The skill itself is prose and stays that way. This lives outside skills/ so the
CI check that keeps the skill free of executable code still passes.

Usage:
    python3 evals/run.py --dry-run     # assemble and validate, no API calls
    python3 evals/run.py               # run the corpus, costs money
    python3 evals/run.py --only triage
    python3 evals/run.py --runs 3      # repeat each case, report worst result

Needs ANTHROPIC_API_KEY unless --dry-run. Needs Python 3.11 or newer.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import tomllib
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
    must_go: list[str] = field(default_factory=list)

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
        if not (case.unchanged or case.must_survive or case.must_go):
            sys.exit(f"Case {case.id} asserts nothing")
        cases.append(case)

    if not cases:
        sys.exit("Corpus is empty")
    return cases


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------


def normalise(text: str) -> str:
    """Collapse whitespace so a reflowed line is not a false failure."""
    return re.sub(r"\s+", " ", text).strip().lower()


def check(case: Case, output: str) -> list[str]:
    """Return the reasons this case failed. Empty means it held."""
    failures: list[str] = []

    if case.unchanged:
        want = normalise(case.text)
        got = normalise(output)
        if want not in got:
            failures.append("triage rewrote text that already reads as human")

    for fact in case.must_survive:
        if fact.lower() not in output.lower():
            failures.append(f"lost: {fact!r}")

    for banned in case.must_go:
        if banned.lower() in output.lower():
            failures.append(f"kept: {banned!r}")

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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="no API calls")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--only", help="run one kind: triage, fidelity, variety, audience")
    parser.add_argument("--runs", type=int, default=1, help="repeats per case")
    parser.add_argument("--verbose", action="store_true", help="print every output")
    args = parser.parse_args()

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
            print(f"            asserts: {len(case.must_survive)} survive, "
                  f"{len(case.must_go)} go, unchanged={case.unchanged}")
        print("\nDry run. Nothing was sent anywhere and nothing was measured.")
        return 0

    try:
        import anthropic
    except ImportError:
        sys.exit("pip install anthropic")

    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY is not set")

    client = anthropic.Anthropic()
    results: list[tuple[Case, list[str]]] = []

    for case in cases:
        worst: list[str] = []
        for run in range(args.runs):
            output = call_model(client, args.model, system, case.prompt())
            if args.verbose:
                print(f"--- {case.id} run {run + 1} ---\n{output}\n")
            failures = check(case, output)
            if len(failures) > len(worst):
                worst = failures
        results.append((case, worst))
        mark = "pass" if not worst else "FAIL"
        print(f"  {mark}  {case.kind:9} {case.id}")
        for reason in worst:
            print(f"          {reason}")

    failed = [c for c, f in results if f]
    print(f"\n{len(results) - len(failed)}/{len(results)} passed on {args.model}")

    if failed:
        print("\nWhat each failure was protecting:\n")
        for case in failed:
            print(f"  {case.id}\n    {case.why}\n")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
