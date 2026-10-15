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

Usage:  python .commons/scripts/generate_deliverables.py [--manifest PATH]
Requires: pip install markdown pyyaml   (browser found by markdown_to_pdf.find_browser)
"""
import sys, os, re, subprocess, tempfile, argparse, hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from markdown_to_pdf import build   # canonical renderer (same dir)

def repo_root():
    # this script lives in .commons/scripts/ -> root is two up
    return HERE.parent.parent

def load_manifest(path):
    try:
        import yaml
    except ImportError:
        sys.exit("Missing dependency: pip install pyyaml")
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

SRC_STAMP = "commons-source-sha:"


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()[:16]


def translated_source(entry, lang, out_dir, src_path):
    """Path to the translated markdown for a non-source language, plus a freshness verdict.

    The instance's DOCUMENTS stay single-language — only the DELIVERABLES are
    multilingual (founder decision 2026-08-12). Machine-near documents need no
    translation: an agent reads any language, framework terms are English
    already, and the pattern links are English. What humans actually read are
    these PDFs.

    So a translation is an OUTPUT, and it lives in the output directory beside
    the PDF it feeds — never beside the source, where it would become a second
    truth. It carries the source hash, so a stale translation is detected rather
    than silently shipped: the drift class this whole pipeline is built to catch.
    """
    md = out_dir / lang / (os.path.splitext(entry["output"])[0] + ".md")
    if not md.exists():
        return None, "missing"
    head = md.read_text(encoding="utf-8", errors="replace")[:400]
    m = re.search(SRC_STAMP + r"\s*([0-9a-f]{6,})", head)
    if not m:
        return md, "unstamped"
    return md, ("current" if m.group(1) == sha(src_path) else "stale")


def parity_problems(src_path, trans_path):
    """Structural parity of a translation against its source.

    The hash stamp proves FRESHNESS, not COMPLETENESS: an abridged translation
    with a correct stamp reads as current forever and no drift check will ever
    catch it (found live 2026-08-13 — a 1.5 KB English summary against a
    5.2 KB German source, whole sections silently dropped, stamp green).
    Headings and table rows are language-invariant, so they must match
    exactly; the byte ratio catches thinning between them. A federation
    reader must get the same artefact, not a digest.
    """
    def sig(p):
        t = open(p, encoding="utf-8", errors="replace").read()
        heads = len(re.findall(r"(?m)^#{1,6}\s", t))
        rows = sum(1 for l in t.split("\n") if l.lstrip().startswith("|"))
        return heads, rows, len(t.encode("utf-8"))
    h1, r1, s1 = sig(src_path)
    h2, r2, s2 = sig(trans_path)
    probs = []
    if h2 != h1:
        probs.append(f"headings {h2}/{h1}")
    if r2 != r1:
        probs.append(f"table rows {r2}/{r1}")
    if s2 < 0.6 * s1:
        probs.append(f"bytes {s2}/{s1} — reads like a digest, not a translation")
    return probs


def expected_translation_path(entry, lang, root):
    """Where the author must write a missing translation — named, not guessed.

    A generator that reports "no translation yet" tells you a fact you already
    suspected; one that names the exact file turns the note into a task.
    """
    out_dir = Path(root) / "instance" / "workshop" / "_deliverables"
    return out_dir / lang / (os.path.splitext(entry["output"])[0] + ".md")


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
    # languages[0] is the source language — the subject's own voice, rendered
    # straight from the instance documents. Any further language is a rendering
    # for the federation: a Swedish twin nobody outside Sweden can read is a dead
    # node in a shared knowledge graph, and today no AMERICAS incubator can read
    # a single EUROPE instance.
    # No default language. A silent fallback to "de" was a German assumption
    # sitting in the middle of a federation: a Swedish or Spanish instance that
    # forgot to declare would have rendered in an assumed language and reported
    # success. The language of a deliverable is a statement about whose voice it
    # is — it must be declared, never guessed.
    langs = m.get("languages") or ([m["language"]] if m.get("language") else None)
    if not langs:
        sys.exit("No language declared. Add `languages: [<subject language>, en]` "
                 "to .commons/deliverables.yml — languages[0] is the subject's own "
                 "voice, further entries are renderings for the federation.")
    out_dir.mkdir(parents=True, exist_ok=True)
    tmp = tempfile.mkdtemp(prefix="deliv_")
    # `pending` holds documents a declared language owes but does not yet have.
    # Kept apart from `failed`: nothing broke, the bundle is simply incomplete —
    # but it must not be mistaken for done. Declaring a language is a promise for
    # EVERY document in the bundle, including one commissioned later from inside
    # the instance; the obligation travels with the entry, not with the gate.
    failed, notes, pending = [], [], []
    for lang in langs:
        ldir = out_dir / lang
        ldir.mkdir(parents=True, exist_ok=True)
        for entry in bundle:
            try:
                src_path = resolve_source(entry, root, tmp)
                if not os.path.exists(src_path):
                    print("SKIP (missing source):", entry.get("source"), entry.get("source_repo") or "")
                    failed.append(entry["output"]); continue
                render_from, note = src_path, ""
                if lang != langs[0]:
                    md, state = translated_source(entry, lang, out_dir, src_path)
                    if state == "missing":
                        want = expected_translation_path(entry, lang, root)
                        pending.append(f"{lang}/{entry['output']}  <- write {want}")
                        continue
                    if state == "stale":
                        notes.append(f"{lang}/{entry['output']}: TRANSLATION STALE — source changed")
                        failed.append(f"{lang}/{entry['output']}"); continue
                    if state == "unstamped":
                        notes.append(f"{lang}/{entry['output']}: translation carries no source stamp")
                    probs = parity_problems(src_path, str(md))
                    if probs:
                        notes.append(f"{lang}/{entry['output']}: TRANSLATION INCOMPLETE — "
                                     + ", ".join(probs))
                        failed.append(f"{lang}/{entry['output']}")
                        continue
                    render_from, note = str(md), f" · Übersetzung / translation ({lang})"
                build(render_from, str(ldir / entry["output"]),
                      kicker=entry.get("kicker", ""), subtitle=entry.get("subtitle", ""),
                      foot=foot + note)
            except Exception as e:
                print("FAIL:", entry.get("output"), "->", e); failed.append(entry.get("output"))
    for n in notes:
        print("  note:", n)
    if failed:
        sys.exit("Deliverables failed: " + ", ".join(str(x) for x in failed))
    if pending:
        print(f"\n  {len(pending)} translation(s) owed by a declared language:")
        for p in pending:
            print("    ·", p)
        sys.exit(
            f"\nBundle INCOMPLETE — {len(bundle) * len(langs) - len(pending)}"
            f"/{len(bundle) * len(langs)} rendered. Declaring {langs} promises every\n"
            "document in every language; a bundle that ships only a translated cover\n"
            "does not keep that promise. Write the translations above, or reduce\n"
            "`languages:` in .commons/deliverables.yml to what the bundle honours.")
    print(f"Bundle complete: {len(bundle)} x {len(langs)} language(s) -> {out_dir}")

if __name__ == "__main__":
    main()
