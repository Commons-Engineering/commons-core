#!/usr/bin/env python3
"""sync.py — bring this house's hull up to date with commons-core (target architecture §3).

The hull is small and rarely changes; content arrives through install.py, never through here.

First run in a house made with "Use this template": the house has a root commit of its own, so git
sees no shared history with commons-core. sync.py then connects it once. It finds the commons-core
commit whose tree equals the house's first commit — the commit the template was taken from — and
records it as an ancestor in a merge that changes no file. Every later sync is an ordinary merge.

What a sync never changes — the house's own surface, restored after every merge:
    .commons/identity.yml  .commons/config.yml  .commons/library.yml  .commons/library.lock
    instance/  blueprint.md  README.md  AGENT.md  LICENSE
and every path the library owns (commons/ except commons/setup/, extensions/, the guides and templates) — content
arrives only through install.py, so a sync never adds, changes or deletes it.

Usage:
    python .commons/scripts/sync.py            # merge on the current branch; never pushes
    python .commons/scripts/sync.py --check    # report only: connected? how far behind?

The `Sync` workflow runs it on a branch and opens a pull request — adoption is always a merge
someone chose.
"""
import argparse
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
RECORD = os.path.join(ROOT, ".commons", "library.yml")
OWN = [".commons/identity.yml", ".commons/config.yml", ".commons/library.yml", ".commons/library.lock",
       "instance", "blueprint.md", "README.md", "AGENT.md", "LICENSE"]
# Content is install's business, never the hull's: whatever lies at the library's paths is left alone,
# even where an older commons-core still carried it. A sync can therefore never delete content.
# commons/setup/ is the hull's (the person doors) and is synced; the rest of commons/ is the library's.
LIBRARY = ["commons/manifests", "commons/specs", "commons/patterns", "commons/templates", "commons/scripts",
           "extensions", "docs", "ALIGN.md", "CONTRIBUTING.md",
           "AGENT.md.template", "README.md.template", "blueprint.md.template"]


def git(*args, check=True):
    r = subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True)
    if check and r.returncode:
        raise SystemExit(f"sync: git {' '.join(args)} failed\n{r.stderr.strip()}")
    return r.stdout.strip()


def hull_source():
    cfg = os.path.join(ROOT, ".commons", "config.yml")
    inside = False
    if os.path.isfile(cfg):
        for line in open(cfg, encoding="utf-8", errors="replace"):
            if re.match(r"^sources:\s*$", line):
                inside = True
                continue
            if inside and re.match(r"^\S", line):
                break
            m = inside and re.match(r'^\s+hull:\s*"?([^"#\s]+)"?', line)
            if m:
                return m.group(1)
    return "Commons-Engineering/commons-core"


def record_connection(commit):
    text = open(RECORD, encoding="utf-8").read() if os.path.isfile(RECORD) else \
        "# Where this house comes from — written by install.py and sync.py, never by hand.\n" \
        "hull:\n  source: Commons-Engineering/commons-core\n  connected_at: null\n"
    text = re.sub(r"(?m)^(  connected_at:).*$", rf"\1 {commit}", text)
    open(RECORD, "w", encoding="utf-8", newline="\n").write(text)


def connect(upstream):
    """Find the commons-core commit this house was taken from, by tree; record it as an ancestor."""
    root = git("rev-list", "--max-parents=0", "HEAD").splitlines()[0]
    tree = git("rev-parse", f"{root}^{{tree}}")
    for line in git("log", "--format=%H %T", upstream).splitlines():
        commit, t = line.split()
        if t == tree:
            git("merge", "-s", "ours", "--allow-unrelated-histories", "--no-edit",
                "-m", f"Connect this house to commons-core at {commit[:10]}", commit)
            record_connection(commit)
            git("add", RECORD)
            git("commit", "--amend", "--no-edit")
            return commit
    raise SystemExit(
        "sync: this house shares no history with commons-core, and its first commit matches no "
        "commons-core commit (it was changed before its first push, or it comes from elsewhere).\n"
        "It has to be connected once by hand — see COMMONS_CORE_SPEC, 'Connecting a house'.")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if git("status", "--porcelain"):
        raise SystemExit("sync: the working tree has uncommitted changes — commit or stash them first")

    src = hull_source()
    url = src if re.match(r"^(https?://|git@|file://|/|[A-Za-z]:)", src) else f"https://github.com/{src}.git"
    git("fetch", "--quiet", url, "main:refs/remotes/commons-core/main", "--force")
    upstream = "refs/remotes/commons-core/main"
    base = git("merge-base", "HEAD", upstream, check=False)
    behind = git("rev-list", "--count", f"HEAD..{upstream}") if base else "?"
    if a.check:
        print(f"hull source {src} · {'connected' if base else 'not connected'} · {behind} commit(s) behind")
        return 0
    if not base:
        print(f"connected at {connect(upstream)[:10]}")
    if git("rev-list", "--count", f"HEAD..{upstream}") == "0":
        print("The hull is current.")
        return 0

    before = git("rev-parse", "HEAD")
    lock = os.path.join(ROOT, ".commons", "library.lock")
    delivered = [l.split("  ", 1)[1].strip() for l in open(lock, encoding="utf-8")
                 if l.strip() and not l.startswith("#")] if os.path.isfile(lock) else []
    r = subprocess.run(["git", "-C", ROOT, "-c", "merge.renames=false", "merge", "--no-commit", "--no-ff", upstream],
                       capture_output=True, text=True)
    protected = OWN + LIBRARY + delivered
    for p in protected:
        if subprocess.run(["git", "-C", ROOT, "cat-file", "-e", f"{before}:{p}"], capture_output=True).returncode == 0:
            git("checkout", before, "--", p)
        elif os.path.exists(os.path.join(ROOT, p)):
            git("rm", "-r", "--quiet", "--cached", "--ignore-unmatch", p)
    still = [f for f in git("diff", "--name-only", "--diff-filter=U").splitlines() if f]
    if still:
        git("merge", "--abort", check=False)
        raise SystemExit("sync: the hull update conflicts in files the house changed:\n  " + "\n  ".join(still) +
                         "\nNothing was changed. Resolve by hand, or keep the house's version and propose the change upstream.")
    git("commit", "--no-edit", "-m", f"Sync the hull from {src}")
    print(f"Synced the hull from {src}; {len(protected)} house-owned paths left as they were.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
