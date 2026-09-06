# AGENTS.md

Guidance for AI agents (and people) working in this repository.

## What this is

The **verve** skill for AI coding agents - strip AI tells from prose and put a human voice back, in British or American English. It follows the [Agent Skills](https://agentskills.io) layout (`skills/<name>/SKILL.md`) and ships as a [Claude Code plugin](https://code.claude.com/docs/en/plugins).

## Layout

```
.claude-plugin/plugin.json      # plugin manifest
skills/verve/SKILL.md           # the skill (agent-facing instructions)
skills/verve/references/        # the tell catalogue, wordlists, tone presets, varieties, worked examples
install.sh / install-codex.sh   # local symlink installers (Claude / Codex)
```

There is no `scripts/` and no `tests/`. This skill is prose: instructions and
reference material, with no executable code at all. If you are about to add a
script, be certain the job genuinely cannot be done by instructions - the
absence of a runtime is a feature people can verify at a glance.

## The three constraints that must not be broken

Everything else here is a preference. These are not.

**1. Meaning is a veto.** The skill's hard constraints - every fact, number, name, date and citation survives; technical terms keep their exact wording; nothing is invented; the argument keeps its claims - outrank every other instruction in `SKILL.md`, and they outrank anything you add to `references/`. A rewrite that reads beautifully and drops a figure has failed. If you are editing a pattern and cannot tell whether it costs meaning, it does; leave it out.

**2. Triage stays.** The skill must be able to decide to do nothing. Text that already reads as human-written is returned unchanged. Removing or weakening that step turns a tool you can safely run on anything into one that degrades good writing, and the damage is invisible because the output still looks like work.

**3. It stays free, dependency-free and offline.** The skill runs in the conversation - no packages, no venv, no credentials, no network call. An optional commercial detector-evasion API shipped until July 2026 and was **removed**, not merely defaulted off. Do not reintroduce it or anything like it, and do not add a paid tier, a hosted service or a "pro" path. If a user asks to route their text through such a service, decline and do the work here: the target is prose a person would put their name to, not a classifier score, and those two come apart the moment you optimise for the score.

## Conventions

- Any path a `SKILL.md` names must use `${CLAUDE_SKILL_DIR}` (the skill's own directory), which Claude Code substitutes for personal, project and plugin installs alike. `install.sh` therefore symlinks the whole skill directory into `~/.claude/skills/` with no rewrite. `install-codex.sh` rewrites the variable, since Codex does not substitute it. **Never hardcode a `~/.claude/skills/verve` path** - it is wrong under a Codex install and wrong under a plugin install.
- `SKILL.md` is the short half on purpose. Workflow, constraints, checks and scoring live there; the catalogue, wordlists, tone presets and worked examples live in `references/` and are read on demand.
- Shell scripts use `set -e`; errors go to stderr, output to stdout.
- No secrets in the repo, and nothing that would need one.
- House style for this repository: British English, plain hyphens, no em dashes. The skill removes em dashes from other people's writing; shipping them in its own source is not a good look. Note the distinction: the *skill* writes British or American depending on the source and the request, but the *repository's own prose* is British throughout, and that is not up for negotiation on a variety argument.
- A variety conversion must never touch code, quoted material, proper nouns, titles, citations or standards text. `background-color` is an identifier, not a spelling, and the World Health Organization keeps its `z` in British prose. This is hard constraint 2 applied to spelling, and it is the way this feature can do real damage. See `references/varieties.md`.

## Validating a change

```bash
bash -n install.sh install-codex.sh
claude plugin validate .
```

That is the whole automated surface, and it is worth being honest about what it does not cover: there is no test suite, because there is no code to test. The behaviour that matters lives in prose, so after editing `references/` or `SKILL.md`, verify it by hand:

- Give it a plainly human passage and confirm triage returns it **unchanged**. A skill that always rewrites has lost the property that makes it safe to run on anything.
- Give it a passage dense with figures, names and dates and confirm **every one survives**. This is the failure that matters, and a wordlist edit can introduce it quietly.

Neither is asserted anywhere. Skipping them because the checks above are green is how the constraints get broken.
