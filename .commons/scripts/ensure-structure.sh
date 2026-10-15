#!/usr/bin/env bash
#
# ensure-structure.sh — guarantee the canonical Commons Core hull structure.
#
# The canonical empty hull skeleton (per COMMONS_CORE_SPEC §2.1) must exist in
# EVERY instance — chain repo, fork, or customer instance — at any scale.
# This script is the SINGLE SOURCE OF TRUTH for that skeleton. It is:
#   * ADDITIVE        — only creates missing directories and .keep markers
#   * IDEMPOTENT      — safe to run any number of times
#   * NON-DESTRUCTIVE — never deletes or overwrites any file or content
#
# It separates three things:
#   1. STRUCTURE — the empty hull skeleton. Guaranteed here, for everyone.
#   2. CONTENT — commons/, extensions/, the guides and templates: delivered by
#      .commons/scripts/install.py from commons-library, never created here.
#   3. SOVEREIGN CONTENT — blueprint.md, .commons/ settings, instance/. Never touched.
#
# A directory receives a .keep marker only when it is otherwise EMPTY. A
# directory that already holds content (e.g. extensions/ with installed packs,
# or instance/registry/5_entities/purpose/ with registered entities) is left
# exactly as it is — the skeleton is guaranteed, the content is sovereign.
#
# Modes:
#   .commons/scripts/ensure-structure.sh            # create missing dirs + .keep
#   .commons/scripts/ensure-structure.sh --check    # report-only; exit 1 if any missing
#
# Wired into: .github/workflows/sync.yml, .github/workflows/validate.yml (--check).
# Also safe to run by hand.
#
# Exit codes:  0 ok   1 (--check) one or more canonical directories missing

set -e

# --- The canonical hull skeleton (COMMONS_CORE_SPEC §2.1) --------------------
# Layer roots and every delivery folder that Git would otherwise drop when
# empty. Content-bearing directories appear here too: they are created if
# absent and left untouched (no .keep) when they already hold files.
HULL_DIRS=(
  # commons/ and extensions/ are not created here: install.py delivers them from commons-library.
  # The instance — the house's own workspace
  "instance"
  "instance/patterns"
  "instance/manifests"
  "instance/specs"
  "instance/templates"
  "instance/scripts"
  "instance/operations"
  "instance/portals/intranet"
  "instance/portals/extranet"
  # Registry — the nine positions of the scaffold, flat; the dimension is derived (COMMONS_MODEL_SPEC §2.3)
  "instance/registry/1_stakeholders"
  "instance/registry/2_journeys"
  "instance/registry/3_touchpoints"
  "instance/registry/4_value-exchanges"
  "instance/registry/5_value-streams"
  "instance/registry/6_capabilities"
  "instance/registry/7_entities"
  "instance/registry/8_solutions"
  "instance/registry/9_seats"
  "instance/workshop"
  # Boot configuration & GitHub conventions
  ".commons"
  ".commons/scripts"
  ".github/ISSUE_TEMPLATE"
  ".github/workflows"
)

CHECK_ONLY=0
[ "${1:-}" = "--check" ] && CHECK_ONLY=1

# Resolve repo root (this script lives in .commons/scripts/)
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

missing=0
added=0

# An instance still on the retired registry names is left to its migration run (§2.3: migration
# is a run, not an edit). Creating the nine folders beside populated retired ones would let a
# tool that reads the new names first see an empty registry. This script never moves records.
UNMIGRATED=0
for r in 1_journeys 2_touchpoints 3_valuestreams 4_capabilities 5_entities providers stakeholders value-propositions solutions seats; do
  [ -e "instance/registry/$r" ] && UNMIGRATED=1
done
[ $UNMIGRATED -eq 1 ] && echo "notice  : instance/registry is on retired names — left to the migration run (COMMONS_MODEL_SPEC §2.3)"
for d in "${HULL_DIRS[@]}"; do
  case "$d" in instance/registry/*) [ $UNMIGRATED -eq 1 ] && continue ;; esac
  if [ ! -d "$d" ]; then
    if [ $CHECK_ONLY -eq 1 ]; then
      echo "MISSING directory: $d"
      missing=$((missing + 1))
    else
      mkdir -p "$d"
      touch "$d/.keep"
      echo "created : $d/.keep"
      added=$((added + 1))
    fi
  elif [ $CHECK_ONLY -eq 0 ]; then
    # Directory exists — add a .keep only if it is empty (no content at all).
    if [ -z "$(ls -A "$d" 2>/dev/null)" ]; then
      touch "$d/.keep"
      echo "marked  : $d/.keep (was empty)"
      added=$((added + 1))
    fi
  fi
done

if [ $CHECK_ONLY -eq 1 ]; then
  if [ $missing -gt 0 ]; then
    echo "FAIL: $missing canonical directory(ies) missing."
    echo "      Run: .commons/scripts/ensure-structure.sh"
    exit 1
  fi
  echo "OK: canonical hull structure complete (${#HULL_DIRS[@]} directories)."
  exit 0
fi

echo "OK: hull structure ensured (${added} addition(s) across ${#HULL_DIRS[@]} canonical directories)."
