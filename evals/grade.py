#!/usr/bin/env python3
"""Grade rewrites that were produced somewhere else.

`run.py` calls the API and grades what comes back. This grades outputs that
already exist, so a run done by hand, in an agent session, or against a model
this harness cannot reach, is still checked by the same assertions rather than
by eye.

    python3 evals/grade.py evals/runs/2026-09-08-claude-opus-5.json

The file is a JSON object mapping case id to the output that case produced.
Every case in the corpus must be present, because a run that quietly skipped
the cases it would have failed is worse than no run.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from run import check, load_cases  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("outputs", help="JSON file: {case_id: output}")
    parser.add_argument("--only", help="grade one kind")
    args = parser.parse_args()

    outputs = json.loads(Path(args.outputs).read_text(encoding="utf-8"))
    cases = load_cases()
    if args.only:
        cases = [c for c in cases if c.kind == args.only]
        if not cases:
            sys.exit(f"No cases of kind {args.only!r}")

    missing = [c.id for c in cases if c.id not in outputs]
    if missing:
        sys.exit("No output for: " + ", ".join(missing))

    unknown = set(outputs) - {c.id for c in load_cases()}
    if unknown:
        sys.exit("Outputs for cases not in the corpus: " + ", ".join(sorted(unknown)))

    results = []
    for case in cases:
        failures = check(case, outputs[case.id])
        results.append((case, failures))
        print(f"  {'pass' if not failures else 'FAIL'}  {case.kind:9} {case.id}")
        for reason in failures:
            print(f"          {reason}")

    failed = [c for c, f in results if f]
    print(f"\n{len(results) - len(failed)}/{len(results)} passed")

    if failed:
        print("\nWhat each failure was protecting:\n")
        for case in failed:
            print(f"  {case.id}\n    {case.why}\n")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
