# Contributing

Thanks for your interest - contributions are welcome.

## Ways to help

- Report a bug or request a feature via [issues](https://github.com/dbhq-uk/verve-skill/issues)
- Add a tell to the catalogue, sharpen a tone preset, or improve the skill instructions via a pull request

## Local development

```bash
git clone https://github.com/dbhq-uk/verve-skill.git
cd verve-skill
./install.sh          # symlinks into ~/.claude/skills (edits are live)
```

The whole skill directory is symlinked, so edits - including to `SKILL.md` and `references/` - are live immediately. For Codex, re-run `./install-codex.sh` after editing a `SKILL.md`, since that file is copied at install time rather than symlinked. Full walkthrough in [`docs/dev-setup.md`](docs/dev-setup.md).

## Before opening a PR

- `bash -n install.sh install-codex.sh` - the installers parse
- `claude plugin validate .` - the plugin validates
- `python3 evals/run.py --dry-run` - the corpus loads and every reference resolves
- `python3 evals/run.py` - the corpus actually passes. This one needs an `ANTHROPIC_API_KEY` and costs a few pence, and it is the only check that tests the skill rather than describing it. If you changed anything under `skills/`, run it. What it asserts, and what it cannot, is in [`evals/README.md`](evals/README.md)
- `python3 evals/grade.py evals/runs/<file>.json` - grades outputs produced somewhere else against the same assertions. Use it when the rewrites came from an agent session rather than the API, and commit the outputs under `evals/runs/` so the grading can be repeated
- British English, plain hyphens, no trailing full stops on headings

Nothing under `skills/` is executable, and CI asserts it. Please keep it that way - see below. `evals/` is the one place code is allowed, because there is no offline way to check that a fact survived a rewrite.

## The bar for a new tell

A tell earns its place in `references/patterns.md` only if it comes with a **before and after**. A named pattern with no worked example is unactionable - the model has to guess what the fix looks like, and guessing is how a de-slopping pass turns into a rewrite.

Two related rules, and they are the ones that matter:

**A tell may never cost meaning.** If removing it plausibly drops a claim, a figure or a qualifier, it is not a tell - it is content you find stylistically annoying. The hard constraints in `SKILL.md` outrank everything in `references/`, and a pattern that fights them is a bug in the pattern.

**Subtraction is not the whole job.** Anything added to the catalogue should leave the prose more human, not merely less florid. A change that makes writing blander has moved it from one kind of machine-made to another.

**A group F tell has to name its reader.** Group F covers condescension and overreach, and nothing in it is a tell in the abstract: a gloss on a term is helpful for one reader and insulting to another. So a group F before-and-after states who the text is addressed to, the way the existing entries do. Without that the example cannot be judged, and the rule will be applied to readers it was never meant for.

## What we will not accept

**Code under `skills/`.** What ships is instructions and reference material - no scripts, no packages, no interpreter, no network call. Anyone can verify that in one glance at the tree, and that is worth more than any feature a script would buy. CI enforces it. If you are convinced something genuinely cannot be done in prose, open an issue first.

`evals/` is outside `skills/` and is the exception, because checking that a fact survived a rewrite requires doing the rewrite, and no amount of prose does that. It is not installed, not shipped, and not part of the skill. Adding code there is fine; adding it anywhere else is not.

**A paid path.** An optional commercial detector-evasion API shipped until July 2026 and was removed. Please do not propose reinstating it, adding a hosted service, or gating anything behind a key or a tier.

**A number that did not come from a measured run.** If a claim in the README or the skill carries a figure - a word count, a percentage, a score, a comparison against anything else - it has to come from a run somebody actually did, with the method stated next to it. An estimate that reads as a measurement is worse than no figure at all, because a reader cannot tell the two apart.

The second is not really about money. Verve aims at prose a person would put their name to; a detector aims at a classifier score. Those two come apart the moment you optimise for the score, and when they do the score wins and the writing loses. A pull request that helps text evade detection rather than deserve to pass will be declined.

## Code of conduct

By taking part you agree to the [code of conduct](CODE_OF_CONDUCT.md).

## Licence

By contributing you agree your work is licensed under the [MIT licence](LICENSE).
