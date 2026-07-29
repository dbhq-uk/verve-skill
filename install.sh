#!/bin/bash
# Install the verve skill into ~/.claude/skills/ as a live symlink install.
#
# SKILL.md references scripts via ${CLAUDE_SKILL_DIR}, which Claude Code
# substitutes to the skill's own directory for personal, project, and plugin
# installs alike. So this script symlinks the whole skill directory into
# ~/.claude/skills/ - every edit (scripts AND SKILL.md) is immediately live,
# with no per-file rewrite. Re-run only when you add a new skill directory.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_ROOT="$HOME/.claude/skills"

echo "=== verve skill installer (Claude Code) ==="
echo

# --- Dependencies ---
# There are none, and there is no check here because there is nothing to check.
# The skill is instructions and reference material: no scripts, no packages, no
# interpreter, no credentials, no network. If a dependency check ever needs to
# appear in this file, something has been added that should not have been.
echo "No dependencies - this skill is instructions, not tooling."
echo

# --- Install each skill in this repo as a full-directory symlink ---
mkdir -p "$SKILLS_ROOT"
for src in "$SCRIPT_DIR"/skills/*/; do
  src="${src%/}"
  name="$(basename "$src")"
  target="$SKILLS_ROOT/$name"
  echo "Installing '$name' -> $target"
  rm -rf "$target"            # replace any prior copy or partial-symlink install
  ln -sfn "$src" "$target"    # whole-directory symlink; ${CLAUDE_SKILL_DIR} resolves it
done

echo
echo "Installed as directory symlinks - all edits (SKILL.md and references) are live. Re-run only when adding a new skill."
echo
echo "No setup step, no API key, nothing further to configure."
echo
echo "Done. Try: 'verve draft.md' or 'verve this: <text>'"
