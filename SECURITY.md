# Security

## Reporting a vulnerability

Email <dan@dbhq.uk> rather than opening a public issue. Include what you found,
how to reproduce it, and what an attacker could do with it. You will get a first
response within 48 hours.

## What this skill does

Verve rewrites prose. That is the whole of it, and the sections below are the
complete account of what it touches.

### Network

**None.** The skill makes no network requests of any kind. There is no API to
call, no key to supply, no telemetry, and no external service behind it. If you
run it with the network off, it behaves identically.

This is worth stating plainly because the category is full of tools that post
your text to a remote endpoint. Verve does not.

### On disk

- Installs into `~/.claude/skills/verve` or `~/.codex`, depending on the agent
- Reads and rewrites only the files you point it at
- Writes no cache, no history, no log

### Credentials

None. The skill has no concept of an account.

### Third-party code

No packages are installed and no dependencies are pulled at runtime. The skill
is instructions and reference material - markdown, not executable tooling.

The repository contains one directory of code, `evals/`, which is the test
corpus and its runner. It is not installed, not shipped with the plugin, and
never executed by the skill. It is the only thing here that uses an API key, it
uses one you supply yourself when you choose to run it, and nothing in the skill
can reach it.

## What it deliberately is not

Verve is not a detector-evasion tool. It does not tune text to score against an
AI classifier, and it says so if asked to. Anyone evaluating it for that purpose
should know that up front.
