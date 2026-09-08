#!/bin/bash
# Install the verve skill into ~/.claude/skills/ as a live symlink install.
#
# SKILL.md names its references by relative path (references/patterns.md), and
# Claude Code resolves those against the skill's own directory for personal,
# project and plugin installs alike. So this script symlinks the whole skill
# directory into ~/.claude/skills/ - every edit to SKILL.md or references/ is
# immediately live, with no per-file rewrite. Re-run only when you add a new
# skill directory.
#
# It replaces a symlink it finds at the target, because that is what a previous
# run of this script leaves. It will not delete a real directory: that is
# somebody's install, possibly edited, and removing it without asking is the
# kind of unrequested change this skill exists to avoid. Remove it yourself
# first if that is what you want.

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
  if [ -e "$target" ] && [ ! -L "$target" ]; then
    echo "error: $target exists and is not a symlink, so it was not created by this script." >&2
    echo "       Move or remove it first, then re-run. Nothing was changed." >&2
    exit 1
  fi
  rm -f "$target"             # a symlink from a previous run, if any
  ln -sfn "$src" "$target"    # whole-directory symlink; relative paths resolve inside it
done

echo
echo "Installed as directory symlinks - all edits (SKILL.md and references) are live. Re-run only when adding a new skill."
echo
echo "No setup step, no API key, nothing further to configure."
echo
echo "Done. Try: 'verve draft.md' or 'verve this: <text>'"
