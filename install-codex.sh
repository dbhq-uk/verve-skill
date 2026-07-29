#!/bin/bash
# Install the verve skill into ~/.codex/skills/ for Codex.
#
# Codex does not substitute ${CLAUDE_SKILL_DIR}, so this script rewrites that
# variable to each skill's installed Codex path and symlinks the supporting
# directories (edits stay live). Re-run after editing a SKILL.md.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_ROOT="$HOME/.codex/skills"

echo "=== verve skill installer (Codex) ==="
echo

# See install.sh: python3 is needed only by the optional API engine, so its
# absence is a note rather than a failure.
if command -v python3 >/dev/null 2>&1; then
  echo "Dependencies OK ($(python3 -V 2>&1) present for the optional API engine)."
else
  echo "Note: python3 not found. The default Claude engine needs nothing, so"
  echo "  verve installs and works; only the optional API engine is unavailable."
fi
echo

mkdir -p "$SKILLS_ROOT"
for src in "$SCRIPT_DIR"/skills/*/; do
  src="${src%/}"
  name="$(basename "$src")"
  target="$SKILLS_ROOT/$name"
  echo "Installing '$name' -> $target"
  mkdir -p "$target"
  # Clear what a previous install left before linking what this one needs.
  # Without this, an entry that has since been renamed or deleted upstream
  # survives as a symlink to a path that no longer exists - and a dangling
  # link fails more confusingly than a missing file, because it looks
  # installed. Only symlinks are removed, so a real SKILL.md is never at risk.
  find "$target" -mindepth 1 -maxdepth 1 -type l -exec rm -f {} +
  # Every directory SKILL.md can reference, so each one exists under the
  # rewritten path too.
  for sub in scripts references tests; do
    [ -d "$src/$sub" ] && ln -sfn "$src/$sub" "$target/$sub"
  done
  # setup.sh provisions the venv beside the SOURCE, but SKILL.md paths are
  # rewritten to $target - so ${CLAUDE_SKILL_DIR}/.venv has to be reachable
  # from there too, or every API-engine command resolves to nothing. Linked
  # only when it exists: a symlink to a venv nobody has created yet is a
  # dangling link, which fails in a far more confusing way than an absent one.
  # Re-run this installer after setup.sh to pick it up.
  [ -d "$src/.venv" ] && ln -sfn "$src/.venv" "$target/.venv"
  [ -f "$src/requirements.txt" ] && ln -sfn "$src/requirements.txt" "$target/requirements.txt"
  chmod +x "$src"/scripts/*.sh "$src"/scripts/*.py 2>/dev/null || true
  sed "s#\${CLAUDE_SKILL_DIR}#$target#g" "$src/SKILL.md" > "$target/SKILL.md"
done

echo
echo "Installed for Codex. Re-run after editing a SKILL.md, and after running"
echo "scripts/setup.sh if you enable the optional API engine."
echo
echo "Done. Try: 'verve draft.md' or 'verve this: <text>'"
