#!/usr/bin/env bash
#
# ensure-structure.sh — guarantee the canonical Commons OS hull structure.
#
# The canonical empty hull skeleton (per COMMONS_OS_SPEC §2.1) must exist in
# EVERY instance — chain repo, fork, or customer instance — at any scale.
# This script is the SINGLE SOURCE OF TRUTH for that skeleton. It is:
#   * ADDITIVE        — only creates missing directories and .keep markers
#   * IDEMPOTENT      — safe to run any number of times
#   * NON-DESTRUCTIVE — never deletes or overwrites any file or content
#
# It separates the three things the sync logic used to conflate:
#   1. STRUCTURE — the empty hull skeleton. Guaranteed here, for everyone.
#   2. OS CONTENT — files under commons/ etc., synced from upstream.
#   3. SOVEREIGN CONTENT — blueprint.md, .commons/, instance/ content, and
#      installed extension PACKS under extensions/. Never touched.
#
# A directory receives a .keep marker only when it is otherwise EMPTY. A
# directory that already holds content (e.g. extensions/ with installed packs,
# or instance/registry/5_entities/purpose/ with registered entities) is left
# exactly as it is — the skeleton is guaranteed, the content is sovereign.
#
# Modes:
#   commons/scripts/ensure-structure.sh            # create missing dirs + .keep
#   commons/scripts/ensure-structure.sh --check    # report-only; exit 1 if any missing
#
# Wired into: commons/scripts/sync-upstream.sh, .github/workflows/sync-upstream.yml,
# .github/workflows/validate.yml (--check). Also safe to run by hand after a fork.
#
# Exit codes:  0 ok   1 (--check) one or more canonical directories missing

set -e

# --- The canonical hull skeleton (COMMONS_OS_SPEC §2.1) --------------------
# Layer roots and every delivery folder that Git would otherwise drop when
# empty. Content-bearing directories appear here too: they are created if
# absent and left untouched (no .keep) when they already hold files.
HULL_DIRS=(
  # Layer 1 — commons (OS substrate, upstream-owned)
  "commons"
  "commons/manifests"
  "commons/specs"
  "commons/patterns"
  "commons/templates"
  "commons/scripts"
  # Layer 2 — extensions (provider packs: skeleton guaranteed, packs sovereign)
  "extensions"
  # Layer 3 — instance (sovereign workspace)
  "instance"
  "instance/patterns"
  "instance/manifests"
  "instance/specs"
  "instance/templates"
  "instance/scripts"
  "instance/operations"
  "instance/portals/intranet"
  "instance/portals/extranet"
  "instance/registry/1_journeys"
  "instance/registry/2_touchpoints"
  "instance/registry/3_valuestreams"
  "instance/registry/4_capabilities/purpose"
  "instance/registry/4_capabilities/participation"
  "instance/registry/4_capabilities/proposition"
  "instance/registry/4_capabilities/production"
  "instance/registry/5_entities/purpose"
  "instance/registry/5_entities/participation"
  "instance/registry/5_entities/proposition"
  "instance/registry/5_entities/production"
  "instance/registry/providers"
  "instance/workshop"
  # Boot configuration & GitHub conventions
  ".commons"
  ".github/ISSUE_TEMPLATE"
  ".github/workflows"
)

CHECK_ONLY=0
[ "${1:-}" = "--check" ] && CHECK_ONLY=1

# Resolve repo root (this script lives in commons/scripts/)
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

missing=0
added=0
for d in "${HULL_DIRS[@]}"; do
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
    echo "      Run: commons/scripts/ensure-structure.sh"
    exit 1
  fi
  echo "OK: canonical hull structure complete (${#HULL_DIRS[@]} directories)."
  exit 0
fi

echo "OK: hull structure ensured (${added} addition(s) across ${#HULL_DIRS[@]} canonical directories)."
