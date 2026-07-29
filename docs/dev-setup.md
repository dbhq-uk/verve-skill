# Developer setup - verve

Set the skill up from source with a **live symlink install**, so your edits are active immediately in Claude Code (and Codex). End users don't need this - they install via the [DBHQ marketplace](../README.md#install).

## Prerequisites

- `git` (and the GitHub CLI `gh` if you'll push changes)
- Nothing else for the default Claude engine - it runs in the conversation, with no scripts, no packages and no credentials
- `python3` and `pytest` only if you'll work on the optional Undetectable AI engine or run its test suite

## 1. Clone

```bash
git clone https://github.com/dbhq-uk/verve-skill.git ~/dbhq-verve
cd ~/dbhq-verve
```

## 2. Install (symlink)

```bash
./install.sh          # Claude Code: symlinks into ~/.claude/skills (edits are live)
./install-codex.sh    # Codex: installs into ~/.codex/skills
```

The committed skill references its scripts via `${CLAUDE_SKILL_DIR}` (the skill's own directory), which Claude Code substitutes for personal, project and plugin installs alike. So `install.sh` symlinks the **whole skill directory** into `~/.claude/skills/` - `SKILL.md`, `scripts/`, `references/` and `tests/` are all live, and every edit takes effect with no re-run. Codex does not substitute `${CLAUDE_SKILL_DIR}`, so `install-codex.sh` rewrites it to the install path - **re-run `./install-codex.sh` after editing a `SKILL.md`** for Codex.

Neither installer runs `setup.sh`. That is deliberate: setup prompts for a paid API key, and the engine most people use needs no setup at all, so running it on every install would ask for a credit card to enable something optional.

## 3. Verify

```bash
cd skills/verve && python3 -m pytest tests/ -v
```

Then, in Claude Code, try *"verve this: The implications of this paradigm shift cannot be overstated."* - a passage with enough tells that a working install is obvious from the output.

Most of the skill is prose rather than code, so the real verification is behavioural. Two things worth checking by hand after editing `references/`:

- **Triage still refuses to work.** Hand it something plainly human-written and confirm it comes back unchanged. A skill that always rewrites has lost the property that makes it safe to run on anything.
- **Fidelity still vetoes.** Hand it a passage dense with figures and names, and confirm every one survives. This is the failure mode that matters, and it is the one a wordlist edit can quietly introduce.

## 4. Optional - the commercial engine

```bash
skills/verve/scripts/setup.sh
```

Provisions a virtualenv for `requests` and stores an [Undetectable AI](https://undetectable.ai/develop) key in `~/.verve/config.json` (permissions `600`), never in the repo. If you set the skill up under its old `humanize` name, setup offers to copy the existing key across, and `verve-api.py` reads the old path either way.

For Codex, re-run `./install-codex.sh` afterwards - the venv link into `~/.codex/skills/verve/` is only created once the venv exists.

## Where the content lives

The skill is mostly prose, and `SKILL.md` is deliberately the short half.

| File | Contents |
|---|---|
| `skills/verve/SKILL.md` | Workflow, hard constraints, quick checks, scoring |
| `skills/verve/references/patterns.md` | The tell catalogue, before/after for each |
| `skills/verve/references/wordlist.md` | Flat scannable word and phrase lists |
| `skills/verve/references/voice.md` | Tone presets, and restoring voice without inventing content |
| `skills/verve/references/examples.md` | Worked passages, before and after |

Adding a tell means adding it to `patterns.md` with a before/after, and to `wordlist.md` if it is scannable as a literal string. Keep the hard constraints in `SKILL.md` - they outrank everything in `references/`, and burying them one level down is how they stop being obeyed.

## Working across machines

Editing anything under `~/dbhq-verve` (scripts, `SKILL.md` or `references/`) is live immediately in Claude Code - the skill directory is symlinked whole. For Codex, re-run `./install-codex.sh` after a `SKILL.md` edit. If you develop on more than one machine, `git pull` before you start and `git push` when done to keep them in sync.
