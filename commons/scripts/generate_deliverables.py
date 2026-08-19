#!/usr/bin/env python3
"""
generate_deliverables.py — the CANONICAL Commons OS deliverable generator.

Reads a DECLARATIVE bundle from `.commons/deliverables.yml` and renders each entry
to PDF via markdown_to_pdf.py. This is the anti-wildwuchs mechanism: an instance's
sendable document set is *declared* (versioned, reviewable) instead of produced by
ad-hoc per-user scripts. Inherited by every fork; only the manifest is per-instance.

Manifest (`.commons/deliverables.yml`):
    output_dir: instance/workshop/_deliverables      # where PDFs are written
    foot: "cloudsters · Commons Engineering"          # optional page footer
    bundle:
      - source: blueprint.md                          # path relative to repo root
        output: 01_Blueprint.pdf
        kicker: "Optional eyebrow"
        subtitle: "Optional subtitle"
      - source: blueprint.md                          # a sibling instance's document
        source_repo: https://github.com/ORG/slug.g1   # optional: shallow-cloned first
        output: 05_Game_Specialist.pdf

Usage:  python commons/scripts/generate_deliverables.py [--manifest PATH]
Requires: pip install markdown pyyaml   (browser found by markdown_to_pdf.find_browser)
"""
import sys, os, subprocess, tempfile, argparse
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from markdown_to_pdf import build   # canonical renderer (same dir)

def repo_root():
    # this script lives in commons/scripts/ -> root is two up
    return HERE.parent.parent

def load_manifest(path):
    try:
        import yaml
    except ImportError:
        sys.exit("Missing dependency: pip install pyyaml")
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def resolve_source(entry, root, tmpdir):
    """Return a filesystem path to the source markdown, cloning a sibling repo if declared."""
    src = entry["source"]
    repo = entry.get("source_repo")
    if repo:
        dest = os.path.join(tmpdir, entry["output"] + ".src")
        if not os.path.isdir(dest):
            subprocess.run(["git", "clone", "--depth", "1", repo, dest],
                           capture_output=True, text=True, check=True)
        return os.path.join(dest, src)
    return str(root / src)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default=None)
    a = ap.parse_args()
    root = repo_root()
    manifest_path = a.manifest or (root / ".commons" / "deliverables.yml")
    if not os.path.exists(manifest_path):
        sys.exit("No deliverables manifest at %s (nothing declared)." % manifest_path)
    m = load_manifest(manifest_path)
    out_dir = root / m.get("output_dir", "instance/workshop/_deliverables")
    foot = m.get("foot", "cloudsters · Commons Engineering")
    bundle = m.get("bundle", [])
    if not bundle:
        sys.exit("Manifest has an empty bundle.")
    out_dir.mkdir(parents=True, exist_ok=True)
    tmp = tempfile.mkdtemp(prefix="deliv_")
    failed = []
    for entry in bundle:
        try:
            src_path = resolve_source(entry, root, tmp)
            if not os.path.exists(src_path):
                print("SKIP (missing source):", entry.get("source"), entry.get("source_repo") or ""); failed.append(entry["output"]); continue
            build(src_path, str(out_dir / entry["output"]),
                  kicker=entry.get("kicker", ""), subtitle=entry.get("subtitle", ""), foot=foot)
        except Exception as e:
            print("FAIL:", entry.get("output"), "->", e); failed.append(entry.get("output"))
    if failed:
        sys.exit("Deliverables failed: " + ", ".join(str(x) for x in failed))
    print("Bundle complete:", len(bundle), "PDFs ->", out_dir)

if __name__ == "__main__":
    main()
