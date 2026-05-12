#!/usr/bin/env bash
#
# sync-upstream.sh — pull Commons OS substrate updates into this instance
#
# Reads the upstream relationship from .commons/identity.yml (commons_os_upstream block).
# Falls back to the `upstream` git remote if the declarative block is absent.
#
# Usage:
#   commons/scripts/sync-upstream.sh                  # fetch, merge, push
#   commons/scripts/sync-upstream.sh --dry-run        # show what would happen
#   commons/scripts/sync-upstream.sh --no-push        # merge locally, don't push
#   commons/scripts/sync-upstream.sh --rebase         # rebase instead of merge
#
# Exit codes:
#   0  success (or nothing to update)
#   1  merge/rebase conflict — resolve manually, commit, then push
#   2  configuration error (no upstream declared, not a git repo, etc.)

set -e

DRY_RUN=0
NO_PUSH=0
REBASE=0
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
  echo "✗ Not inside a git repository." >&2
  exit 2
fi

# Discover upstream URL — declarative block wins, git remote is fallback.
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
  # Make sure the `upstream` git remote matches the declaration.
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
    echo "  git rebase upstream/$BRANCH"
  else
    echo "  git merge --no-edit upstream/$BRANCH"
  fi
  [ $NO_PUSH -eq 0 ] && echo "  git push"
  exit 0
fi

echo "→ Fetching upstream..."
git fetch upstream

BEHIND=$(git rev-list --count "HEAD..upstream/$BRANCH" 2>/dev/null || echo 0)
if [ "$BEHIND" = "0" ]; then
  echo "✓ Already up to date."
  exit 0
fi
echo "→ $BEHIND new commit(s) on upstream/$BRANCH"

if [ $REBASE -eq 1 ]; then
  git rebase "upstream/$BRANCH" || {
    echo ""
    echo "✗ Rebase conflict. Resolve, then run:" >&2
    echo "    git add <files> && git rebase --continue" >&2
    exit 1
  }
else
  git merge --no-edit "upstream/$BRANCH" || {
    echo ""
    echo "✗ Merge conflict. Resolve, then commit." >&2
    exit 1
  }
fi

if [ $NO_PUSH -eq 0 ]; then
  echo "→ Pushing to origin/$BRANCH..."
  git push
fi

echo "✓ Substrate sync complete."
