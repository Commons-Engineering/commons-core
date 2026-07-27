#!/usr/bin/env python3
"""gate1-verify.py — independent structural verifier for Gate 1.

Given a .d instance root, checks the STRUCTURE half of Gate 1 (G1.2 & G1.5-G1.7),
then shells out to evidence-validate.py for the DATA half (G1.2-G1.4).
Deterministic, reusable — the seed of the deterministic build program.

Usage:  python gate1-verify.py <path-to-{slug}.d>
Prints a per-criterion PASS/FAIL table + overall verdict. Exit 0 = pass.
"""
import sys, os, re, subprocess, json

FAMILIES = [  # the 13 canonical C|EN families (D0 seed + 3/dimension) per the canonical
    "Perception to Mandate",                                             # D0
    "Purpose to Portfolio", "Value to Sustainability", "Portfolio to System",           # D1
    "Participant to Community", "Collaboration to Automation", "Contributor to Succession",  # D2
    "Discovery to Usage", "Interest to Relationship", "Proposition to Audience",         # D3
    "Demand to Fulfillment", "Source to Alliance", "Acquire to Retire",                  # D4
]
IA_SECTIONS = [f"## §{i}" for i in range(0, 11)]  # §0..§10
PERSPECTIVES = ["N", "T", "W", "R", "K", "U"]
HERE = os.path.dirname(os.path.abspath(__file__))


def read(p):
    try:
        with open(p, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None


def main(root):
    ws = os.path.join(root, "instance", "workshop")
    ev = os.path.join(ws, "evidence")
    checks = []

    # G1.2 evidence files present + data validator
    ev_files = ["sources.yml", "entities.yml", "claims.yml", "README.md"]
    present = all(os.path.exists(os.path.join(ev, f)) for f in ev_files)
    know = os.path.isdir(os.path.join(ev, "knowledge"))
    checks.append(("G1.2 evidence files + knowledge/", present and know))
    val = None
    if present:
        r = subprocess.run([sys.executable, os.path.join(HERE, "evidence-schema", "evidence-validate.py"), ev],
                           capture_output=True, text=True)
        try:
            val = json.loads(r.stdout)
        except Exception:
            val = {"status": "error", "raw": r.stdout[-400:]}
    checks.append(("G1.3/G1.4 belegregel + no unresolved contradictions",
                   bool(val) and val.get("status") == "pass"))

    # G1.5 industry analysis §0..§10
    ia = read(os.path.join(ws, "analysis", "industry-analysis.md")) or ""
    ia_ok = all(s in ia for s in IA_SECTIONS) and "Source" in ia
    checks.append(("G1.5 industry-analysis §0-§10 + Sources", ia_ok))

    # G1.6 blueprint structure
    bp = read(os.path.join(root, "blueprint.md")) or ""
    fam_hits = sum(1 for f in FAMILIES if f in bp)
    has_d0 = "Perception to Mandate" in bp
    has_econ = ("§2.1b" in bp or "Economic Model" in bp)
    has_constituent = bp.count("Constituent Value Streams") >= 13
    bp_ok = ("§0" in bp and fam_hits == 13 and has_d0 and has_econ and has_constituent
             and ("§6" in bp or "§8" in bp)
             and re.search(r"\bwe\b|\bour\b", bp, re.I) is not None)
    checks.append((f"G1.6 blueprint §0 + {fam_hits}/13 families + D0={has_d0} + §2.1b={has_econ}"
                   f" + ConstituentVS={has_constituent} + 1st-person", bp_ok))
    # traceability: at least some C_ ids referenced in blueprint
    cids = len(set(re.findall(r"C_\d{3}", bp)))
    checks.append((f"G1.6 traceability (C_ids cited in blueprint: {cids})", cids >= 5))

    # G1.7 scenarios 60 = 6x10
    sc = read(os.path.join(ws, "analysis", "scenarios-2050.md")) or ""
    counts = {p: len(re.findall(rf"^###\s+{p}\d+\b", sc, re.M)) for p in PERSPECTIVES}
    total = sum(counts.values())
    scl = sc.lower()
    struct = (re.search(r"no.?regret", scl) is not None
              and "wildcard" in scl
              and ("axis" in scl or "world" in scl or "2×2" in sc or "2x2" in scl))
    checks.append((f"G1.7 scenarios {total}/60 {counts} + 2×2/No-Regret/Wildcards",
                   total == 60 and struct))

    # G1.8 gate card present
    checks.append(("G1.8 GATE1.md present", os.path.exists(os.path.join(ws, "GATE1.md"))))

    print(f"\n=== GATE 1 VERIFY — {os.path.basename(root)} ===")
    for name, ok in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if val:
        print(f"  evidence-validate: {val.get('status')} · counts={val.get('counts')}")
        for e in (val.get("errors") or [])[:8]:
            print(f"      ! {e}")
    verdict = all(ok for _, ok in checks)
    print(f"  --> GATE 1: {'PASS' if verdict else 'FAIL'}\n")
    sys.exit(0 if verdict else 1)


if __name__ == "__main__":
    main(sys.argv[1].rstrip("\\/") if len(sys.argv) > 1 else ".")
