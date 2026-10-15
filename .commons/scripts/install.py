#!/usr/bin/env python3
"""install.py — bring this house the content it declares (target architecture §4, §4a).

What the house is stands in .commons/identity.yml; what that means stands in the library's
library.json. This script joins the two and touches nothing else:

    every house                  the lean profile: canon, guides, templates, Orbits 0–1
    instance_type os | incubator in addition Orbits 2–3 (the sovereign profile)
    domain: <d>                  in addition the released essentials pack of that domain
    instance_type incubator      incubator-essentials instead of a domain pack

Rules — what install may touch:
  * It manages exactly the files a release delivered. Their list, with hashes, is kept in
    .commons/library.lock.
  * It never removes a file it did not deliver.
  * Before it overwrites or removes anything that differs from what it delivered, it stops and
    shows the difference. --adopt takes the library's version anyway, and says so file by file.
  * It writes .commons/library.yml: which library, which tag, which profile, which packs.

Usage (from the house's root, or by the `Install` workflow):
    python .commons/scripts/install.py                  # newest release, from the source in config.yml
    python .commons/scripts/install.py --tag v2026.10.1
    python .commons/scripts/install.py --from PATH      # a library checkout or unpacked archive (offline)
    python .commons/scripts/install.py --dry-run        # show the plan, change nothing
    python .commons/scripts/install.py --adopt          # take the library's version where the house differs

Standard library only, so it runs wherever Python 3.8+ runs.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
LOCK = os.path.join(ROOT, ".commons", "library.lock")
RECORD = os.path.join(ROOT, ".commons", "library.yml")
DEFAULT_SOURCE = "Commons-Engineering/commons-library"
SOVEREIGN = {"os", "incubator"}


def scalar(path, key):
    """A top-level `key: value` from a simple YAML file; None for null, empty or absent."""
    if not os.path.isfile(path):
        return None
    for line in open(path, encoding="utf-8", errors="replace"):
        m = re.match(rf"^{re.escape(key)}:\s*(.*?)\s*(?:#.*)?$", line)
        if m:
            v = m.group(1).strip().strip('"').strip("'")
            return None if v in ("", "null", "~") else v
    return None


def nested(path, block, key):
    """`key` inside a top-level `block:` of a simple YAML file."""
    if not os.path.isfile(path):
        return None
    inside = False
    for line in open(path, encoding="utf-8", errors="replace"):
        if re.match(rf"^{re.escape(block)}:\s*$", line):
            inside = True
            continue
        if inside and re.match(r"^\S", line):
            break
        m = inside and re.match(rf"^\s+{re.escape(key)}:\s*(.*?)\s*(?:#.*)?$", line)
        if m:
            v = m.group(1).strip().strip('"').strip("'")
            return None if v in ("", "null", "~") else v
    return None


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def read_lock():
    lock = {}
    if os.path.isfile(LOCK):
        for line in open(LOCK, encoding="utf-8"):
            if line.strip() and not line.startswith("#"):
                h, rel = line.rstrip("\n").split("  ", 1)
                lock[rel] = h
    return lock


def fetch(source, tag, into):
    url = source if re.match(r"^(https?://|git@|file://)", source) else f"https://github.com/{source}.git"
    cmd = ["git", "clone", "--quiet", "--depth", "1"] + (["--branch", tag] if tag else []) + [url, into]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"install: cannot fetch {url}{' at ' + tag if tag else ''}\n{r.stderr.strip()}")


def plan(lib):
    index = json.load(open(os.path.join(lib, "library.json"), encoding="utf-8"))
    ident = os.path.join(ROOT, ".commons", "identity.yml")
    itype, domain = scalar(ident, "instance_type"), scalar(ident, "domain")
    profile = "sovereign" if itype in SOVEREIGN else "lean"
    prefixes = list(index["profiles"]["lean"])
    if profile == "sovereign":
        prefixes += index["profiles"]["sovereign"]
    wanted, notes = [], []
    pack = "incubator" if itype == "incubator" else (domain.lower() if domain else None)
    if pack and itype in SOVEREIGN:
        key = f"cloudsters/{pack}-essentials"
        if key in index["packs"]:
            prefixes.append(index["packs"][key]["path"].rstrip("/") + "/")
            wanted.append(f"{key}@{index['packs'][key]['version']}")
        else:
            notes.append(f"{key} is not released in {index['tag']} yet — the house runs on the canon "
                         f"until it is; a pilot house receives the candidate from commons-graph")
    files = {}
    for line in open(os.path.join(lib, "library.files"), encoding="utf-8"):
        h, rel = line.rstrip("\n").split("  ", 1)
        if any(rel == p or rel.startswith(p) for p in prefixes):
            files[rel] = h
    return index, profile, wanted, files, notes


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Install what this house declares.")
    ap.add_argument("--from", dest="src")
    ap.add_argument("--tag")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adopt", action="store_true")
    a = ap.parse_args()

    tmp = None
    if a.src and os.path.isdir(a.src):
        lib = os.path.abspath(a.src)
        source = lib
    else:
        source = a.src or nested(os.path.join(ROOT, ".commons", "config.yml"), "sources", "library") or DEFAULT_SOURCE
        tmp = tempfile.mkdtemp(prefix="commons-library-")
        lib = os.path.join(tmp, "lib")
        fetch(source, a.tag, lib)
    try:
        index, profile, packs, files, notes = plan(lib)
        lock = read_lock()

        write, keep, conflicts, remove = [], [], [], []
        for rel, h in files.items():
            dst = os.path.join(ROOT, rel)
            if not os.path.exists(dst):
                write.append(rel)
                continue
            have = sha(dst)
            if have == h:
                keep.append(rel)
            elif rel in lock and have == lock[rel]:
                write.append(rel)                                 # unchanged since we delivered it
            else:
                conflicts.append((rel, "changed in the house" if rel in lock else "present, not delivered by install"))
        for rel, h in lock.items():
            if rel in files:
                continue
            dst = os.path.join(ROOT, rel)
            if not os.path.exists(dst):
                continue
            if sha(dst) == h:
                remove.append(rel)
            else:
                conflicts.append((rel, "changed in the house, no longer in the release"))

        print(f"install {index['tag']} · profile {profile}" + (f" · {', '.join(packs)}" if packs else ""))
        print(f"  {len(write)} to write · {len(keep)} already current · {len(remove)} to remove · {len(conflicts)} differ")
        for n in notes:
            print(f"  note: {n}")
        by_reason = {}
        for rel, why in conflicts:
            by_reason.setdefault(why, []).append(rel)
        for why, rels in by_reason.items():
            print(f"  ≠ {len(rels)} {why}:")
            for rel in rels[:15]:
                print(f"      {rel}")
            if len(rels) > 15:
                print(f"      … and {len(rels) - 15} more")
        if "present, not delivered by install" in by_reason:
            print("  A house that is installing for the first time carries content from before install existed. "
                  "--adopt replaces it with the library's version.")
        if conflicts and not a.adopt:
            print("Stopped: the files above differ from what install delivers. Nothing was changed.\n"
                  "Look at them; to keep a change, propose it upstream. Run again with --adopt to take the library's version.")
            return 2
        if a.dry_run:
            print("Dry run: nothing changed.")
            return 0

        adopt = [rel for rel, _ in conflicts]
        for rel in write + [r for r in adopt if r in files]:
            dst = os.path.join(ROOT, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copyfile(os.path.join(lib, rel), dst)
        for rel in remove + [r for r in adopt if r not in files]:
            os.remove(os.path.join(ROOT, rel))
        for rel in adopt:
            print(f"  adopted: {rel}")

        with open(LOCK, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(f"# Written by install.py — every file delivered from {index['tag']}. Do not edit.\n")
            for rel in sorted(files):
                fh.write(f"{files[rel]}  {rel}\n")
        hull_source = nested(RECORD, "hull", "source") or "Commons-Engineering/commons-core"
        connected = nested(RECORD, "hull", "connected_at") or "null"
        with open(RECORD, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("# Where this house comes from — written by install.py and sync.py, never by hand.\n")
            fh.write(f"hull:\n  source: {hull_source}\n  connected_at: {connected}\n")
            fh.write(f"library:\n  source: {source if not os.path.isdir(source) else DEFAULT_SOURCE}\n"
                     f"  tag: {index['tag']}\n  profile: {profile}\n  packs: [{', '.join(packs)}]\n")
        print("Done.")
        return 0
    finally:
        if tmp:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
