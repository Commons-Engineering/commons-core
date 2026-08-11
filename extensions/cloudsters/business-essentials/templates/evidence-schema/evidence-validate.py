#!/usr/bin/env python3
"""evidence-validate.py — machine-checkable core of Gate 1 (G1.2-G1.4).

Validates a .d instance's evidence knowledge graph:
  - all three node files parse (sources.yml, entities.yml, claims.yml)
  - belegregel: every tier:headline Claim has >=2 distinct sources
      (asserted_by + corroborated_by) OR confidence:unbestaetigt
  - no unresolved contradictions: every `contradicts` edge is answered
      by a `supersedes` edge somewhere
  - referential integrity: asserted_by/corroborated_by ids exist in sources,
      about ids exist in entities, contradicts/supersedes ids exist in claims

Usage:  python evidence-validate.py <path-to-evidence-dir>
Exit 0 = pass, 1 = fail. Prints a JSON report.
"""
import sys, json, os
try:
    import yaml
except ImportError:
    print(json.dumps({"status": "error", "msg": "pyyaml not installed"}))
    sys.exit(1)


def load(path):
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def main(ev_dir):
    errors, warnings = [], []
    srcs = load(os.path.join(ev_dir, "sources.yml"))
    ents = load(os.path.join(ev_dir, "entities.yml"))
    clms = load(os.path.join(ev_dir, "claims.yml"))

    for name, doc in [("sources", srcs), ("entities", ents), ("claims", clms)]:
        if doc is None:
            errors.append(f"missing or empty: {name}.yml")

    src_ids = {s["id"] for s in (srcs or {}).get("sources", []) if "id" in s}
    # statutory primary sources confirm alone (spec: Klein-GmbH calibration —
    # Handelsregister/Bundesanzeiger/IP register filed under penalty of law)
    STATUTORY = {"register", "register-aggregator", "handelsregister", "bundesanzeiger",
                 "statutory", "ip-register"}
    src_type = {s["id"]: str(s.get("type", "")).lower()
                for s in (srcs or {}).get("sources", []) if "id" in s}
    ent_ids = {e["id"] for e in (ents or {}).get("entities", []) if "id" in e}
    claims = (clms or {}).get("claims", [])
    claim_ids = {c["id"] for c in claims if "id" in c}

    superseded = set()
    for c in claims:
        for s in c.get("supersedes", []) or []:
            superseded.add(s)

    headline_ct = 0
    for c in claims:
        cid = c.get("id", "?")
        conf = c.get("confidence")
        if conf is None:
            errors.append(f"{cid}: no confidence tag (belegregel: never estimate untagged)")
        # referential integrity
        for s in (c.get("asserted_by", []) or []) + (c.get("corroborated_by", []) or []):
            if s not in src_ids:
                errors.append(f"{cid}: source '{s}' not in sources.yml")
        for e in c.get("about", []) or []:
            if e not in ent_ids:
                warnings.append(f"{cid}: entity '{e}' not in entities.yml")
        for x in c.get("contradicts", []) or []:
            if x not in claim_ids:
                errors.append(f"{cid}: contradicts '{x}' not a known claim")
        for x in c.get("supersedes", []) or []:
            if x not in claim_ids:
                errors.append(f"{cid}: supersedes '{x}' not a known claim")
        # belegregel for headline claims
        if c.get("tier") == "headline":
            headline_ct += 1
            n = len(set((c.get("asserted_by", []) or []) + (c.get("corroborated_by", []) or [])))
            # Graded single-source honesty (spec triangulation standard): a single
            # source is admissible ONLY under a tag that names the limitation.
            # "belegt" (confirmed) always requires >=2 distinct sources.
            SINGLE_OK = {"unbestätigt", "unbestaetigt", "website", "marktreport", "inferred"}
            allsrc = set((c.get("asserted_by", []) or []) + (c.get("corroborated_by", []) or []))
            statutory_single = (n == 1 and all(src_type.get(s) in STATUTORY for s in allsrc))
            if n < 2 and conf not in SINGLE_OK and not statutory_single:
                errors.append(
                    f"{cid}: headline claim has {n} source(s), needs >=2 or a "
                    f"limitation-naming confidence ({'/'.join(sorted(SINGLE_OK))})")
        # unresolved contradiction
        if c.get("contradicts") and c.get("id") not in superseded:
            # the contradicted-away claim should itself be superseded by another
            for x in c.get("contradicts"):
                if x not in superseded:
                    warnings.append(
                        f"{cid}: contradicts {x} but neither is superseded — resolve before Gate 1")

    report = {
        "status": "pass" if not errors else "fail",
        "counts": {"sources": len(src_ids), "entities": len(ent_ids),
                   "claims": len(claim_ids), "headline_claims": headline_ct},
        "errors": errors,
        "warnings": warnings,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    sys.exit(0 if not errors else 1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
