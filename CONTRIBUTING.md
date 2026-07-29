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

The whole skill directory is symlinked, so edits - including to `SKILL.md` and `references/` - are live immediately. For Codex, re-run `./install-codex.sh` after editing a `SKILL.md`, since that path is rewritten at install time. Full walkthrough in [`docs/dev-setup.md`](docs/dev-setup.md).

## Before opening a PR

- `cd skills/verve && python3 -m pytest tests/ -v` - the suite passes, no network needed
- `bash -n install.sh install-codex.sh skills/verve/scripts/*.sh` - shell scripts parse
- `claude plugin validate .` - the plugin validates
- Keep credentials out of the repo and out of commits
- British English, plain hyphens, no trailing full stops on headings

## The bar for a new tell

A tell earns its place in `references/patterns.md` only if it comes with a **before and after**. A named pattern with no worked example is unactionable - the model has to guess what the fix looks like, and guessing is how a de-slopping pass turns into a rewrite.

Two related rules, and they are the ones that matter:

**A tell may never cost meaning.** If removing it plausibly drops a claim, a figure or a qualifier, it is not a tell - it is content you find stylistically annoying. The hard constraints in `SKILL.md` outrank everything in `references/`, and a pattern that fights them is a bug in the pattern.

**Subtraction is not the whole job.** Anything added to the catalogue should leave the prose more human, not merely less florid. A change that makes writing blander has moved it from one kind of machine-made to another.

## Licence

By contributing you agree your work is licensed under the [MIT licence](LICENSE).
