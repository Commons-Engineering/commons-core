#!/usr/bin/env bash
#
# sync-upstream.sh — pull Commons OS substrate updates into this instance,
# while guaranteeing that instance-owned files (blueprint.md, AGENT.md,
# README.md, .commons/identity.yml, .commons/config.yml, instance/, docs/)
# are bit-identical before and after the sync.
#
# Reads the upstream relationship from .commons/identity.yml (commons_os_upstream
# block). Falls back to the `upstream` git remote if the declarative block is absent.
#
# Usage:
#   commons/scripts/sync-upstream.sh                  # fetch, merge, push
#   commons/scripts/sync-upstream.sh --dry-run        # show what would happen
#   commons/scripts/sync-upstream.sh --no-push        # merge locally, don't push
#   commons/scripts/sync-upstream.sh --rebase         # rebase instead of merge
#
# Safety design — three concentric layers that protect instance-owned content:
#   1. Rename detection is disabled (`merge.renames=false`). An upstream rename
#      of, say, blueprint.md → blueprint.md.template arrives as DELETE + ADD,
#      so `-X ours` correctly preserves the instance file.
#   2. After the merge, every path in INSTANCE_OWNED is forcibly restored from
#      the pre-merge HEAD tree. Even if a strategy quirk modified one of them,
#      this layer reverts it.
#   3. A final assertion verifies that every pre-merge instance file still exists
#      with non-empty content. Any mismatch aborts the push and surfaces a clear
#      error pointing at the saved pre-merge SHA for manual recovery.
#
# The instance can never lose its blueprint.md (or any other instance-owned file)
# through this script. The worst case is "sync aborted, pre-merge state preserved
# at SHA X — investigate and re-run".
#
# Exit codes:
#   0  success (or nothing to update)
#   1  merge/rebase conflict — resolve manually, commit, then push
#   2  configuration error (no upstream declared, not a git repo, etc.)
#   3  safety assertion failed — instance file would have been lost; sync aborted

set -e

# --- Instance-owned protection list ---------------------------------------
# These files and directories are owned by the instance. After every merge,
# they are forcibly restored to their pre-merge state — no exceptions.
INSTANCE_OWNED_FILES=(
  blueprint.md
  AGENT.md
  README.md
  .commons/identity.yml
  .commons/config.yml
)
INSTANCE_OWNED_DIRS=(
  instance
  docs
)

# --- Argument parsing ------------------------------------------------------
DRY_RUN=0; NO_PUSH=0; REBASE=0
for arg in "$@"; do
  case "$arg" in
    --dry-run)  DRY_RUN=1 ;;
    --no-push)  NO_PUSH=1 ;;
    --rebase)   REBASE=1 ;;
    -h|--help)
      sed -n '2,/^$/p' "$0" | sed 's/^# \{0,1\}//'
      exit 0
      ;;
    *) echo "Unknown argument: $arg" >&2; exit 2 ;;
  esac
done

if ! git rev-parse --git-dir >/dev/null 2>&1; then
  echo "✗ Not inside a git repository." >&2; exit 2
fi

# --- Discover upstream -----------------------------------------------------
UPSTREAM_REPO=""
if [ -f .commons/identity.yml ]; then
  UPSTREAM_REPO=$(awk '
    /^commons_os_upstream:/ { in_block=1; next }
    in_block && /^[a-zA-Z]/ { in_block=0 }
    in_block && /^  *repository:/ { sub(/^  *repository: *"?/, ""); sub(/"? *$/, ""); print; exit }
  ' .commons/identity.yml)
fi

if [ -n "$UPSTREAM_REPO" ]; then
  UPSTREAM_URL="https://github.com/${UPSTREAM_REPO}.git"
  if git remote get-url upstream >/dev/null 2>&1; then
    CURRENT=$(git remote get-url upstream)
    if [ "$CURRENT" != "$UPSTREAM_URL" ]; then
      echo "⚠ git remote 'upstream' = $CURRENT  but identity.yml declares $UPSTREAM_URL"
      echo "   Updating remote to match declaration."
      [ $DRY_RUN -eq 0 ] && git remote set-url upstream "$UPSTREAM_URL"
    fi
  else
    echo "→ Adding git remote 'upstream' = $UPSTREAM_URL"
    [ $DRY_RUN -eq 0 ] && git remote add upstream "$UPSTREAM_URL"
  fi
elif git remote get-url upstream >/dev/null 2>&1; then
  UPSTREAM_URL=$(git remote get-url upstream)
  echo "→ Using git remote 'upstream' = $UPSTREAM_URL (no declaration in identity.yml)"
else
  echo "✗ No upstream declared. Set commons_os_upstream.repository in .commons/identity.yml" >&2
  echo "   or add a git remote: git remote add upstream <url>" >&2
  exit 2
fi

BRANCH=$(git symbolic-ref --short HEAD)
echo "→ Branch: $BRANCH"
echo "→ Upstream: $UPSTREAM_URL"

if [ $DRY_RUN -eq 1 ]; then
  echo ""
  echo "Dry-run — would run:"
  echo "  git fetch upstream"
  if [ $REBASE -eq 1 ]; then
    echo "  git -c merge.renames=false rebase upstream/$BRANCH"
  else
    echo "  git -c merge.renames=false merge --no-edit -X ours upstream/$BRANCH"
  fi
  echo "  (then: restore instance-owned files from pre-merge HEAD; assert all preserved)"
  [ $NO_PUSH -eq 0 ] && echo "  git push"
  exit 0
fi

# --- Refuse to run with a dirty working tree -------------------------------
if [ -n "$(git status --porcelain)" ]; then
  echo "✗ Working tree has uncommitted changes. Commit or stash before syncing." >&2
  git status --short >&2
  exit 2
fi

# --- Snapshot pre-merge HEAD for restoration & forensics -------------------
PRE_SHA=$(git rev-parse HEAD)
echo "→ Pre-merge HEAD: $PRE_SHA"

# --- Build the list of instance-owned paths that exist pre-merge -----------
# We track the exact paths (under instance/ and docs/, recursively) so we can
# restore them precisely from the pre-merge tree.
PROTECTED_PATHS=()
for f in "${INSTANCE_OWNED_FILES[@]}"; do
  if git cat-file -e "${PRE_SHA}:${f}" 2>/dev/null; then
    PROTECTED_PATHS+=("$f")
  fi
done
for d in "${INSTANCE_OWNED_DIRS[@]}"; do
  if git cat-file -e "${PRE_SHA}:${d}" 2>/dev/null; then
    # Expand the directory to the list of files it contained at PRE_SHA
    while IFS= read -r path; do
      PROTECTED_PATHS+=("$path")
    done < <(git ls-tree -r --name-only "$PRE_SHA" -- "$d")
  fi
done
echo "→ Protected paths: ${#PROTECTED_PATHS[@]}"

# --- Fetch & check whether we have anything to do --------------------------
echo "→ Fetching upstream..."
git fetch upstream

BEHIND=$(git rev-list --count "HEAD..upstream/$BRANCH" 2>/dev/null || echo 0)
if [ "$BEHIND" = "0" ]; then
  echo "✓ Already up to date."
  exit 0
fi
echo "→ $BEHIND new commit(s) on upstream/$BRANCH"

# --- Merge with rename detection OFF and -X ours ---------------------------
# Layer 1: disabling renames means an upstream rename of an instance-owned
# file arrives as DELETE+ADD, and -X ours blocks the delete on a modified file.
MERGE_FLAGS=( -c merge.renames=false )
if [ $REBASE -eq 1 ]; then
  "${MERGE_FLAGS[@]/#/git }" rebase "upstream/$BRANCH" || {
    echo "" >&2
    echo "✗ Rebase conflict. Resolve, then run:" >&2
    echo "    git add <files> && git rebase --continue" >&2
    echo "   Pre-merge HEAD is preserved at: $PRE_SHA" >&2
    exit 1
  }
else
  git -c merge.renames=false merge --no-edit -X ours "upstream/$BRANCH" || {
    echo "" >&2
    echo "✗ Merge conflict. Resolve, then commit." >&2
    echo "   Pre-merge HEAD is preserved at: $PRE_SHA" >&2
    exit 1
  }
fi

# --- Layer 2: forcibly restore every protected path from pre-merge ---------
# This is the belt-and-braces guarantee: regardless of what the merge did,
# every instance-owned file ends up exactly as it was before the merge.
if [ "${#PROTECTED_PATHS[@]}" -gt 0 ]; then
  echo "→ Restoring ${#PROTECTED_PATHS[@]} instance-owned path(s) from pre-merge HEAD"
  # checkout each path individually; ignore paths that no longer exist in the
  # merged tree (we'll re-create them from PRE_SHA)
  for path in "${PROTECTED_PATHS[@]}"; do
    git checkout "$PRE_SHA" -- "$path" 2>/dev/null || true
  done
  # If anything got restored, fold it into the merge commit
  if [ -n "$(git status --porcelain)" ]; then
    git add -A
    git -c user.email="$(git config user.email || echo sync@commons-os)" \
        -c user.name="$(git config user.name || echo sync-upstream)" \
        commit --amend --no-edit >/dev/null
    echo "  (instance-owned paths restored; merge commit amended)"
  else
    echo "  (no instance-owned changes from merge — nothing to restore)"
  fi
fi

# --- Layer 3: post-merge safety assertion ----------------------------------
# Every path that existed pre-merge must still exist and have identical content.
LOSS=0
for path in "${PROTECTED_PATHS[@]}"; do
  if [ ! -e "$path" ]; then
    echo "✗ SAFETY VIOLATION: instance-owned path missing after sync: $path" >&2
    LOSS=1
    continue
  fi
  # Compare blob SHA pre vs post
  PRE_BLOB=$(git rev-parse "${PRE_SHA}:${path}" 2>/dev/null || echo "")
  POST_BLOB=$(git rev-parse "HEAD:${path}" 2>/dev/null || echo "")
  if [ -n "$PRE_BLOB" ] && [ "$PRE_BLOB" != "$POST_BLOB" ]; then
    echo "✗ SAFETY VIOLATION: $path was modified by sync (pre=$PRE_BLOB post=$POST_BLOB)" >&2
    LOSS=1
  fi
done

if [ $LOSS -eq 1 ]; then
  echo "" >&2
  echo "✗ Sync aborted — instance-owned content would have been altered or lost." >&2
  echo "   Resetting to pre-merge HEAD: $PRE_SHA" >&2
  git reset --hard "$PRE_SHA"
  exit 3
fi

echo "✓ All ${#PROTECTED_PATHS[@]} protected path(s) preserved exactly."

# --- Push ------------------------------------------------------------------
if [ $NO_PUSH -eq 0 ]; then
  echo "→ Pushing to origin/$BRANCH..."
  git push
fi

echo "✓ Substrate sync complete."
