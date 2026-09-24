#!/usr/bin/env python3
"""Judge whether a rewrite kept its source's meaning, claim by claim.

The substring grader in run.py catches deletion: a figure that is gone, a
phrase that stayed. It cannot catch distortion, where every string survives
and the meaning moves - a figure attached to the wrong subject, a condition
turned into a consequence, evidence turned into a purpose. This is the
reading pass that catches those.

Each corpus case carries `claims`: the atomic claims its rewrite must keep. A
second model, shown only the source, the rewrite and the claims - never the
skill, never which model wrote the rewrite - rules on each claim and lists
anything the rewrite added. One claim not kept, or one addition, fails the
case.

    python3 evals/judge.py evals/runs/FILE.json            # judge a recorded run
    python3 evals/judge.py FILE.json --judge claude:claude-sonnet-5
    python3 evals/judge.py --selftest --reps 3             # judge the judge

--judge codex (the default) uses the Codex CLI with its configured model, so
the judge is a different model family from the Claude models verve is run on.
Use a judge that did not write the rewrite: the point is a second reader, and
a model shares its own blind spots. --selftest runs judge_fixtures.toml, rewrites
known to keep or break their meaning, and fails if any verdict disagrees.

Needs a model, so it is not in CI. Needs Python 3.11 or newer.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from run import Case, call_cli, load_cases  # noqa: E402

HERE = Path(__file__).resolve().parent
FIXTURES = HERE / "judge_fixtures.toml"

VERDICTS = ("kept", "weakened", "strengthened", "changed", "missing")

JUDGE_SYSTEM = """\
You check whether a rewrite kept the meaning of its source. You get the \
SOURCE, the REWRITE, and a numbered list of CLAIMS the source makes that the \
rewrite was required to keep. Other content in the source may have been cut \
on purpose: judge only the listed claims, and anything the rewrite adds.

For each claim give exactly one verdict:
- "kept": the rewrite asserts it with the same subject, the same polarity, \
the same strength (should is not will, may is not is, only is not one of \
several), the same conditions and order, and the same attribution. Different \
wording is fine.
- "weakened": it is there but hedged, softened or narrowed.
- "strengthened": it is there but asserted more firmly or more broadly.
- "changed": it is there but altered - a different subject, a figure attached \
to the wrong thing, a condition turned into a consequence, an order or a cause \
reversed, evidence turned into a purpose, the attribution moved.
- "missing": the rewrite does not assert it, even by plain implication.

Then list ADDITIONS: facts, opinions, reasons, comparisons, experiences, \
narrators or instructions in the rewrite that the source neither states nor \
plainly implies. Do not list courtesy (a greeting, thanks, a sign-off, an \
apology or acknowledgement offered to the reader), rewording, or a plainer \
restatement of something the source says.

Be strict about meaning and relaxed about wording. Near-synonyms of about \
the same force are kept; only a real change of force counts, such as should to \
will, may to is, some to all, or one of several to the only. A claim's own text \
may say what must not change about it; hold the rewrite to that.

Reply with JSON only, and nothing else:
{"claims": [{"n": 1, "verdict": "kept", "quote": "the rewrite's words you \
relied on, empty if missing", "why": "one short sentence, required unless \
kept"}], "additions": [{"quote": "...", "why": "..."}]}
"""

# Notes verve prints under the text. They are written for the writer, and a
# claim found only in a note has not survived in the text.
NOTE_LINE = re.compile(
    r"^\s*[*_`]*\s*(?:Overshare \((?:not )?cut\)|First contact \(not cut\)|Set:)")


def strip_notes(output: str) -> str:
    lines = output.strip().splitlines()
    for i, line in enumerate(lines):
        if NOTE_LINE.match(line):
            kept = lines[:i]
            while kept and kept[-1].strip() in ("", "```", "---"):
                kept.pop()
            return "\n".join(kept)
    return output.strip()


def build_prompt(case: Case, rewrite: str) -> str:
    claims = "\n".join(f"{n}. {c}" for n, c in enumerate(case.claims, 1))
    return (f"SOURCE:\n<<<\n{case.text.strip()}\n>>>\n\n"
            f"REWRITE:\n<<<\n{strip_notes(rewrite)}\n>>>\n\n"
            f"CLAIMS the rewrite must keep:\n{claims}\n")


# --------------------------------------------------------------------------
# Judges
# --------------------------------------------------------------------------


def call_codex(model: str | None, prompt: str) -> str:
    """One `codex exec`, read-only, in an empty directory."""
    command = ["codex", "exec", "--skip-git-repo-check", "--sandbox", "read-only"]
    if model:
        command += ["-c", f"model={model}"]
    with tempfile.TemporaryDirectory() as cwd:
        out = Path(cwd) / "verdict.txt"
        for attempt in (1, 2):
            try:
                done = subprocess.run(command + ["-o", str(out), "-"],
                                      input=f"{JUDGE_SYSTEM}\n\n{prompt}",
                                      capture_output=True, text=True, cwd=cwd,
                                      timeout=300)
                break
            except subprocess.TimeoutExpired:
                if attempt == 2:
                    raise
        if done.returncode != 0 or not out.exists():
            detail = (done.stderr.strip() or done.stdout.strip())[-300:]
            raise RuntimeError(f"codex exec exited {done.returncode}: {detail}")
        return out.read_text(encoding="utf-8")


def make_judge(spec: str):
    """codex, codex:MODEL or claude:MODEL -> a function prompt -> reply."""
    provider, _, model = spec.partition(":")
    if provider == "codex":
        if not shutil.which("codex"):
            sys.exit("codex is not on PATH")
        return lambda prompt: call_codex(model or None, prompt)
    if provider == "claude":
        if not model:
            sys.exit("--judge claude needs a model: claude:claude-sonnet-5")
        if not shutil.which("claude"):
            sys.exit("claude is not on PATH")
        system_file = Path(tempfile.mkstemp(prefix="verve-judge-", suffix=".md")[1])
        system_file.write_text(JUDGE_SYSTEM, encoding="utf-8")
        return lambda prompt: call_cli(model, system_file, prompt)
    sys.exit(f"unknown judge {spec!r}: use codex, codex:MODEL or claude:MODEL")


def parse(reply: str, n_claims: int) -> dict:
    start, end = reply.find("{"), reply.rfind("}")
    if start < 0 or end < start:
        raise ValueError(f"no JSON in the judge's reply: {reply[:200]!r}")
    data = json.loads(reply[start:end + 1])
    by_n = {int(c["n"]): c for c in data.get("claims", [])}
    if sorted(by_n) != list(range(1, n_claims + 1)):
        raise ValueError(f"judge ruled on claims {sorted(by_n)}, expected 1..{n_claims}")
    for c in by_n.values():
        if c.get("verdict") not in VERDICTS:
            raise ValueError(f"unknown verdict {c.get('verdict')!r}")
    return {"claims": [by_n[n] for n in range(1, n_claims + 1)],
            "additions": data.get("additions") or []}


def judge_one(judge, case: Case, output: str) -> dict:
    """Return {'pass': bool, 'problems': [...], 'raw': {...}}."""
    try:
        verdict = parse(judge(build_prompt(case, output)), len(case.claims))
    except Exception as exc:  # a judge that cannot answer is not a pass
        return {"pass": False, "problems": [f"judge error: {exc}"], "raw": None}
    problems = [
        f"claim {n} {c['verdict']}: {case.claims[n - 1]}  -  {c.get('why', '')}".rstrip(" -")
        for n, c in enumerate(verdict["claims"], 1) if c["verdict"] != "kept"
    ]
    problems += [f"added: {a.get('quote', '')!r}  -  {a.get('why', '')}"
                 for a in verdict["additions"]]
    return {"pass": not problems, "problems": problems, "raw": verdict}


# --------------------------------------------------------------------------
# Modes
# --------------------------------------------------------------------------


def judge_run(args, judge) -> int:
    outputs = json.loads(Path(args.outputs).read_text(encoding="utf-8"))
    cases = [c for c in load_cases() if c.claims and c.id in outputs]
    if args.only:
        cases = [c for c in cases if c.kind == args.only]
    if not cases:
        sys.exit("No case in that file has claims to judge")

    with ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        futures = [(c, pool.submit(judge_one, judge, c, outputs[c.id])) for c in cases]
        results = [(c, f.result()) for c, f in futures]

    for case, r in results:
        print(f"  {'pass' if r['pass'] else 'FAIL'}  {case.kind:9} {case.id}")
        for p in r["problems"]:
            print(f"          {p}")
    failed = [c for c, r in results if not r["pass"]]
    print(f"\n{len(results) - len(failed)}/{len(results)} kept their meaning "
          f"(judge: {args.judge})")

    if args.save:
        Path(args.save).write_text(json.dumps(
            {"judge": args.judge, "outputs": args.outputs,
             "verdicts": {c.id: r for c, r in results}},
            indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"saved {args.save}")
    return 1 if failed else 0


def selftest(args, judge) -> int:
    with FIXTURES.open("rb") as fh:
        fixtures = tomllib.load(fh)["fixture"]
    cases = {c.id: c for c in load_cases()}

    jobs = []
    for fx in fixtures:
        case = cases[fx["case"]]
        if "output" in fx:
            output = fx["output"]
        else:
            output = json.loads((HERE / fx["run"]).read_text(encoding="utf-8"))[fx["case"]]
        for rep in range(args.reps):
            jobs.append((fx, case, output, rep))

    with ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        futures = [(fx, rep, pool.submit(judge_one, judge, case, output))
                   for fx, case, output, rep in jobs]
        results = [(fx, rep, f.result()) for fx, rep, f in futures]

    wrong = 0
    for fx in fixtures:
        mine = [r for f, _, r in results if f["id"] == fx["id"]]
        agree = sum((r["pass"]) == (fx["expect"] == "pass") for r in mine)
        ok = agree == len(mine)
        wrong += not ok
        print(f"  {'ok  ' if ok else 'WRONG'}  expect {fx['expect']:4}  "
              f"{agree}/{len(mine)} agree  {fx['id']}")
        for r in mine:
            if (r["pass"]) != (fx["expect"] == "pass"):
                for p in r["problems"] or ["<passed>"]:
                    print(f"          {p}")
    print(f"\n{len(fixtures) - wrong}/{len(fixtures)} fixtures judged right "
          f"on every rep (judge: {args.judge}, reps: {args.reps})")
    return 1 if wrong else 0


def dry_run() -> int:
    """What CI can check without a model: every fixture names a case that has
    claims, every pass fixture's run holds that case, every prompt builds."""
    cases = {c.id: c for c in load_cases()}
    with FIXTURES.open("rb") as fh:
        fixtures = tomllib.load(fh)["fixture"]
    problems = []
    seen = set()
    for fx in fixtures:
        if fx["id"] in seen:
            problems.append(f"{fx['id']}: duplicate id")
        seen.add(fx["id"])
        case = cases.get(fx["case"])
        if case is None or not case.claims:
            problems.append(f"{fx['id']}: case {fx['case']!r} has no claims")
            continue
        if fx.get("expect") not in ("pass", "fail"):
            problems.append(f"{fx['id']}: expect must be pass or fail")
        if "output" in fx:
            output = fx["output"]
        else:
            run = HERE / fx.get("run", "")
            outputs = json.loads(run.read_text(encoding="utf-8")) if run.is_file() else {}
            if fx["case"] not in outputs:
                problems.append(f"{fx['id']}: {fx.get('run')} has no output for {fx['case']}")
                continue
            output = outputs[fx["case"]]
        build_prompt(case, output)
    with_claims = [c for c in cases.values() if c.claims]
    print(f"claims: {sum(len(c.claims) for c in with_claims)} across {len(with_claims)} cases")
    print(f"fixtures: {len(fixtures)} "
          f"({sum(f.get('expect') == 'pass' for f in fixtures)} pass, "
          f"{sum(f.get('expect') == 'fail' for f in fixtures)} fail)")
    for p in problems:
        print(f"  {p}")
    print("Dry run. No model was called." if not problems else "Dry run failed.")
    return 1 if problems else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("outputs", nargs="?", help="JSON file: {case_id: output}")
    parser.add_argument("--judge", default="codex",
                        help="codex, codex:MODEL or claude:MODEL (default codex)")
    parser.add_argument("--only", help="judge one kind")
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("--save", help="write the verdicts as JSON")
    parser.add_argument("--selftest", action="store_true",
                        help="judge judge_fixtures.toml and check every verdict")
    parser.add_argument("--reps", type=int, default=1, help="repeats per fixture, --selftest")
    parser.add_argument("--dry-run", action="store_true",
                        help="check the claims and fixtures load, and build every prompt; no model")
    args = parser.parse_args()

    if args.dry_run:
        return dry_run()
    if args.selftest == bool(args.outputs):
        parser.error("give an outputs file, or --selftest, not both")
    judge = make_judge(args.judge)
    return selftest(args, judge) if args.selftest else judge_run(args, judge)


if __name__ == "__main__":
    raise SystemExit(main())
