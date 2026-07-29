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
# There are none. The default Claude engine runs entirely in the conversation:
# no scripts, no packages, no credentials. python3 is checked only because the
# OPTIONAL Undetectable AI engine needs it, and a missing python3 must never
# block an install of the half that everybody actually uses.
if command -v python3 >/dev/null 2>&1; then
  echo "Dependencies OK ($(python3 -V 2>&1) present for the optional API engine)."
else
  echo "Note: python3 not found. The Claude engine - the default, and the one"
  echo "  this skill is really about - needs nothing at all, so verve installs"
  echo "  and works regardless. Only the optional Undetectable AI engine is"
  echo "  unavailable until python3 is installed."
fi
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
  chmod +x "$src"/scripts/*.sh "$src"/scripts/*.py 2>/dev/null || true
done

echo
echo "Installed as directory symlinks - all edits (scripts and SKILL.md) are live. Re-run only when adding a new skill."
echo

# --- Optional commercial engine ---
# Deliberately NOT run automatically. setup.sh prompts for a paid API key, and
# the default engine needs no setup at all - so running it on every install
# would demand a credit card for a feature most people never turn on.
if [ -f "$HOME/.verve/config.json" ] || [ -f "$HOME/.humanize/config.json" ]; then
  echo "Undetectable AI key found - the optional commercial engine is available."
else
  echo "Note: the optional Undetectable AI engine is not configured. verve works"
  echo "  without it; the Claude engine is the default and costs nothing. To add"
  echo "  it later: $SKILLS_ROOT/verve/scripts/setup.sh"
fi

echo
echo "Done. Try: 'verve draft.md' or 'verve this: <text>'"
