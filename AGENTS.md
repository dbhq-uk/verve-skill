# AGENTS.md

Guidance for AI agents (and people) working in this repository.

## What this is

The **verve** skill for AI coding agents - strip AI tells from prose and put a human voice back, in British English. It follows the [Agent Skills](https://agentskills.io) layout (`skills/<name>/SKILL.md`) and ships as a [Claude Code plugin](https://code.claude.com/docs/en/plugins).

## Layout

```
.claude-plugin/plugin.json      # plugin manifest
skills/verve/SKILL.md           # the skill (agent-facing instructions)
skills/verve/references/        # the tell catalogue, wordlists, tone presets, worked examples
skills/verve/scripts/           # optional Undetectable AI engine + its setup
skills/verve/tests/             # offline unit tests for the API script
install.sh / install-codex.sh   # local symlink installers (Claude / Codex)
```

## The three constraints that must not be broken

Everything else here is a preference. These are not.

**1. Meaning is a veto.** The skill's hard constraints - every fact, number, name, date and citation survives; technical terms keep their exact wording; nothing is invented; the argument keeps its claims - outrank every other instruction in `SKILL.md`, and they outrank anything you add to `references/`. A rewrite that reads beautifully and drops a figure has failed. If you are editing a pattern and cannot tell whether it costs meaning, it does; leave it out.

**2. Triage stays.** The skill must be able to decide to do nothing. Text that already reads as human-written is returned unchanged. Removing or weakening that step turns a tool you can safely run on anything into one that degrades good writing, and the damage is invisible because the output still looks like work.

**3. The default engine stays free and dependency-free.** The Claude engine runs in the conversation - no packages, no venv, no credentials, no network. The Undetectable AI engine is optional, commercial, and must remain so. Never move a required step behind the paid path, and never let the installers demand a key.

## Conventions

- `SKILL.md` references scripts via `${CLAUDE_SKILL_DIR}` (the skill's own directory), which Claude Code substitutes for personal, project and plugin installs alike. `install.sh` therefore symlinks the whole skill directory into `~/.claude/skills/` with no rewrite. `install-codex.sh` rewrites the variable, since Codex does not substitute it. **Never hardcode a `~/.claude/skills/verve` path** - it is wrong under a Codex install and wrong under a plugin install.
- `SKILL.md` is the short half on purpose. Workflow, constraints, checks and scoring live there; the catalogue, wordlists, tone presets and worked examples live in `references/` and are read on demand.
- Shell scripts use `set -e`; errors go to stderr, output to stdout.
- No secrets in the repo - the API key lives at `~/.verve/config.json`.
- House style: British English, plain hyphens, no em dashes. The skill removes em dashes from other people's writing; shipping them in its own source is not a good look.

## Validating a change

```bash
cd skills/verve && python3 -m pytest tests/ -v   # offline; requests and sleep are patched
bash -n install.sh install-codex.sh skills/verve/scripts/*.sh
claude plugin validate .
```

The tests only cover `verve-api.py`, which is the optional engine - so a green suite says nothing about the part of the skill that does the actual work. After editing `references/` or `SKILL.md`, verify by hand: give it a plainly human passage and confirm triage returns it unchanged, then give it a passage dense with figures and names and confirm every one survives. Those two behaviours are what the constraints above are protecting, and no test asserts them.
