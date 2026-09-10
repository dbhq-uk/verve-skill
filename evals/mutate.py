#!/usr/bin/env python3
"""Assert that the grader fails what it was built to fail.

`run.py` checks outputs against the corpus. This checks the checker: it takes
recorded outputs that pass, damages each one in a way the corpus claims to
care about, and asserts `check()` fails the damaged version with the expected
failure. Every mutation class here passed the harness on 2026-09-10, before
the assertions it now exercises existed, which is the reason this file exists.

    python3 evals/mutate.py

Three outcomes per automated mutation, and all must be the first one:
  ok      control passes, mutation fails with the expected failure
  MISSED  the grader accepted the mutated output, or failed it for an
          unrelated reason
  BROKEN  the control itself fails - the corpus and the recorded run have
          diverged, which must be fixed before mutations mean anything

Semantic mutations are listed, not checked. A substring harness cannot see
them by design; they are recorded so a reading pass knows what to look for.
"""

from __future__ import annotations

import sys
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from run import check, load_cases  # noqa: E402

HERE = Path(__file__).resolve().parent
MUTATIONS = HERE / "mutations.toml"


def load_output(run_rel: str, case_id: str) -> str:
    import json

    path = HERE / run_rel
    outputs = json.loads(path.read_text(encoding="utf-8"))
    if case_id not in outputs:
        sys.exit(f"{run_rel} has no output for {case_id}")
    return outputs[case_id]


def apply_mutation(base: str, m: dict) -> str:
    mutated = base
    if "replace" in m:
        old, new = m["replace"]
        if old not in mutated:
            sys.exit(f"{m['id']}: replace target not in base output: {old!r}")
        mutated = mutated.replace(old, new, 1)
    if m.get("append"):
        mutated = mutated + m["append"]
    if m.get("uppercase"):
        mutated = mutated.upper()
    if mutated == base:
        sys.exit(f"{m['id']}: mutation changed nothing")
    return mutated


def main() -> int:
    with MUTATIONS.open("rb") as fh:
        raw = tomllib.load(fh)

    cases = {c.id: c for c in load_cases()}
    failed = 0
    semantic: list[dict] = []

    for m in raw.get("mutation", []):
        if m.get("kind") == "semantic":
            semantic.append(m)
            continue

        case = cases.get(m["case"])
        if case is None:
            sys.exit(f"{m['id']}: no corpus case {m['case']!r}")

        base = load_output(m["run"], m["case"])
        control = check(case, base)
        if control:
            failed += 1
            print(f"  BROKEN  {m['id']}: control fails: {control}")
            continue

        mutated = apply_mutation(base, m)
        failures = check(case, mutated)
        hits = [f for f in failures if m["expect_failure"].lower() in f.lower()]
        if hits:
            print(f"  ok      {m['id']}: {hits[0]}")
        else:
            failed += 1
            got = failures or ["<accepted - no failures at all>"]
            print(f"  MISSED  {m['id']}: expected a failure containing "
                  f"{m['expect_failure']!r}, got {got}")

    if semantic:
        print("\nSemantic mutations - not checkable by substrings, read for these:")
        for m in semantic:
            print(f"  {m['id']} ({m['case']})")
            print(f"      {m['violated_claim']}")

    total = len(raw.get("mutation", [])) - len(semantic)
    print(f"\n{total - failed}/{total} automated mutations caught")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
