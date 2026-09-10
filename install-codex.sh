#!/bin/bash
# Install the verve skill into ~/.codex/skills/ for Codex.
#
# SKILL.md names its references by relative path, so nothing in it needs
# rewriting. This script copies SKILL.md into ~/.codex/skills/<name>/ and
# symlinks references/ beside it, so reference edits stay live and SKILL.md
# edits need a re-run. Copying rather than symlinking the whole directory is
# deliberate: it gives Codex a real file at the path it discovers.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_ROOT="$HOME/.codex/skills"

echo "=== verve skill installer (Codex) ==="
echo

# No dependency check: the skill is instructions and reference material, with
# no scripts, packages, interpreter or credentials. See install.sh.
echo "No dependencies - this skill is instructions, not tooling."
echo

mkdir -p "$SKILLS_ROOT"
for src in "$SCRIPT_DIR"/skills/*/; do
  src="${src%/}"
  name="$(basename "$src")"
  target="$SKILLS_ROOT/$name"
  echo "Installing '$name' -> $target"

  # Every refusal happens before anything is touched, so "Nothing was
  # changed" is true when it prints.
  #
  # A non-empty target this script did not create belongs to somebody else's
  # skill of the same name, and touching it would destroy their work.
  # Ownership test: any install of this skill leaves $target/references as a
  # symlink to a path ending in /<name>/references - true from this checkout,
  # and still true after the checkout has moved.
  if [ -d "$target" ] && [ -n "$(ls -A "$target" 2>/dev/null)" ]; then
    ref_link="$(readlink "$target/references" 2>/dev/null || true)"
    case "$ref_link" in
      */"$name"/references) : ;;  # a previous install of this skill
      *)
        echo "error: $target exists, is not empty, and was not created by this script." >&2
        echo "       Move or remove it first, then re-run. Nothing was changed." >&2
        exit 1
        ;;
    esac
  fi
  # ln -sfn into an existing real directory creates a link *inside* it and
  # leaves the stale directory in place, so a user who once had a copied
  # install would keep running old reference files while this script
  # reported success. Refuse instead.
  for sub in references scripts; do
    [ -d "$src/$sub" ] || continue
    if [ -e "$target/$sub" ] && [ ! -L "$target/$sub" ]; then
      echo "error: $target/$sub is a real directory, not a symlink, so it was not created by this script." >&2
      echo "       Move or remove it first, then re-run. Nothing was changed." >&2
      exit 1
    fi
  done

  mkdir -p "$target"
  # Clear what a previous install left before linking what this one needs.
  # Without this, an entry that has since been renamed or deleted upstream
  # survives as a symlink to a path that no longer exists - and a dangling
  # link fails more confusingly than a missing file, because it looks
  # installed. Only symlinks this installer would have created are removed:
  # the canonical names, and anything pointing into this checkout. A real
  # SKILL.md, and a symlink somebody else put here, are never at risk.
  for link in "$target"/*; do
    [ -L "$link" ] || continue
    case "$(basename "$link")" in
      references|scripts) rm -f "$link"; continue ;;
    esac
    case "$(readlink "$link")" in
      "$SCRIPT_DIR"/*) rm -f "$link" ;;
    esac
  done
  # Every directory SKILL.md can reference, so each one exists under the
  # rewritten path too. `references` is the only one this skill has; `scripts`
  # is kept in the list deliberately, so that if one is ever added it is linked
  # rather than silently missing from the Codex install.
  for sub in references scripts; do
    [ -d "$src/$sub" ] || continue
    ln -sfn "$src/$sub" "$target/$sub"
  done
  cp "$src/SKILL.md" "$target/SKILL.md"
done

echo
echo "Installed for Codex. Re-run after editing a SKILL.md - that file is
copied at install time rather than symlinked, so its edits are not live."
echo
echo "Done. Try: 'verve draft.md' or 'verve this: <text>'"
