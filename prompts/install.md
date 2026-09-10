Install the verve skill for me. Do all of it yourself, and tell me at the end what changed.

Verve is prose: a `SKILL.md` and seven reference files, with no code, no packages and no credentials. Installing it means putting eight markdown files where this agent looks for skills.

First, work out where that is. Check which of these directories exist, and use every one you find:

- `~/.claude/skills/` for Claude Code
- `~/.codex/skills/` for Codex
- `~/.cursor/skills/`, `~/.config/opencode/skills/`, or whatever this agent uses if it is neither of those

If none exists and you know where this agent keeps its skills, create that directory. If you genuinely do not know, stop and tell me rather than guessing.

Then fetch these eight files:

- https://raw.githubusercontent.com/dbhq-uk/verve-skill/main/skills/verve/SKILL.md
- https://raw.githubusercontent.com/dbhq-uk/verve-skill/main/skills/verve/references/patterns.md
- https://raw.githubusercontent.com/dbhq-uk/verve-skill/main/skills/verve/references/wordlist.md
- https://raw.githubusercontent.com/dbhq-uk/verve-skill/main/skills/verve/references/voice.md
- https://raw.githubusercontent.com/dbhq-uk/verve-skill/main/skills/verve/references/varieties.md
- https://raw.githubusercontent.com/dbhq-uk/verve-skill/main/skills/verve/references/audience.md
- https://raw.githubusercontent.com/dbhq-uk/verve-skill/main/skills/verve/references/preferences.md
- https://raw.githubusercontent.com/dbhq-uk/verve-skill/main/skills/verve/references/examples.md

Write them to `verve/SKILL.md` and `verve/references/` under each skills directory you found, keeping that layout exactly. The seven reference files must sit in a `references/` subdirectory, because `SKILL.md` names them by that relative path and nothing rewrites it. Check afterwards that every `references/` path `SKILL.md` names exists on disk next to it.

If a `verve` skill is already installed, do not overwrite it. Show me the version that is there and the version you fetched, say what differs, and ask.

Then tell me, in one short message: which directories you wrote to, how many files each got, whether anything was already there, and the one sentence I need to start using it, which is that I can now say "verve this: [text]" or "verve draft.md" in any session.

Change nothing else. No config, no settings files, no edits to anything in my projects.

---

If you would rather not paste a prompt, verve installs in one command:

```
/plugin marketplace add dbhq-uk/marketplace     # then: /plugin install verve@dbhq
```

```bash
npx skills add dbhq-uk/verve-skill              # any agent that skills.sh supports
```

This prompt exists for the agents those two do not cover.
