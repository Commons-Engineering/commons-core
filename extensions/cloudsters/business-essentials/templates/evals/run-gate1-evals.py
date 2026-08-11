#!/usr/bin/env python3
"""run-gate1-evals.py — manifest-driven Gate-1 eval runner.

Executes the deterministic evals of gate1-evals.yml against a .d instance,
reports llm-judged evals as PENDING-JUDGE, and can write the gate card
(GATE1.md) from the verdict — the card IS the eval report.

Only status:active deterministic evals bear the verdict; probation evals run
and report but never gate. Supersedes gate1-verify.py as the entry point
(evidence-validate.py stays the data-half workhorse underneath).

Usage:
  python run-gate1-evals.py <path-to-{slug}.d> [--json] [--write-card]
Exit 0 = all active deterministic evals pass.
"""
import sys, os, re, json, subprocess, datetime

try:
    import yaml
except ImportError:
    print(json.dumps({"status": "error", "msg": "pyyaml not installed"})); sys.exit(1)

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(HERE, "gate1-evals.yml")
EVIDENCE_VALIDATE = os.path.join(HERE, "..", "evidence-schema", "evidence-validate.py")

FAMILIES = [
    "Perception to Mandate",
    "Purpose to Portfolio", "Value to Sustainability", "Portfolio to System",
    "Participant to Community", "Collaboration to Automation", "Contributor to Succession",
    "Discovery to Usage", "Interest to Relationship", "Proposition to Audience",
    "Demand to Fulfillment", "Source to Alliance", "Acquire to Retire",
]
STRIP_MARKER = "<!-- pipeline-annotation:end -->"
CORPUS_DIRS = ("knowledge", "scans", "public", "external", "internal", "dossiers")
REGISTRY_LEVELS = ["1_journeys", "2_touchpoints", "3_valuestreams",
                   "4_capabilities", "5_entities", "value-propositions"]


def read(p):
    try:
        with open(p, encoding="utf-8") as f:
            return f.read()
    except (FileNotFoundError, NotADirectoryError):
        return None


def load_yaml(p):
    t = read(p)
    if t is None:
        return None
    try:
        return yaml.safe_load(t)
    except yaml.YAMLError:
        return None


def md_count(d, recursive=True):
    if not os.path.isdir(d):
        return 0
    n = 0
    for base, _, files in os.walk(d):
        n += sum(1 for f in files if f.endswith(".md"))
        if not recursive:
            break
    return n


def build_checks(root):
    """Return {eval_id: (ok, detail)} for all deterministic evals."""
    C = {}
    dc = os.path.join(root, ".commons")
    ws = os.path.join(root, "instance", "workshop")
    ev = os.path.join(ws, "evidence")

    ident = load_yaml(os.path.join(dc, "identity.yml")) or {}
    up = ident.get("commons_core_upstream") or {}
    C["E01"] = (bool(ident) and ident.get("instance_type") == "domain"
                and bool(ident.get("slug")) and bool(ident.get("purpose"))
                and all(up.get(k) for k in ("repository", "editorial_source", "forked_at")),
                f"type={ident.get('instance_type')} upstream_keys={sorted(k for k in up)}")

    cfg = load_yaml(os.path.join(dc, "config.yml")) or {}
    exts = cfg.get("extensions") or []
    C["E02"] = (bool(cfg.get("language")) and bool(exts) and bool(cfg.get("value_streams")),
                f"lang={cfg.get('language')} ext={exts[:1]}")

    cl = read(os.path.join(root, "CLAUDE.md")) or ""
    lines = [l for l in cl.splitlines() if l.strip()]
    C["E03"] = (0 < len(lines) <= 3 and "Read and follow AGENT.md" in cl,
                f"lines={len(lines)}")

    ag = read(os.path.join(root, "AGENT.md")) or ""
    slug = str(ident.get("slug") or "")
    name = str(ident.get("name") or "")
    C["E04"] = (bool(ag) and (bool(slug) and slug.lower() in ag.lower()
                or bool(name) and name.lower() in ag.lower()),
                f"len={len(ag)}")

    a2a = load_yaml(os.path.join(dc, "a2a.yml")) or {}
    C["E05"] = (bool((a2a.get("identity") or {}).get("slug")), "")

    acct = load_yaml(os.path.join(dc, "account.yml")) or {}
    a = acct.get("account") or acct
    C["E06"] = (bool(a.get("steward")) and bool(a.get("stage")),
                f"steward={a.get('steward')} stage={a.get('stage')}")

    node_files = ["sources.yml", "entities.yml", "claims.yml", "README.md"]
    nodes_ok = all(os.path.exists(os.path.join(ev, f)) for f in node_files)
    corpus = [d for d in CORPUS_DIRS if os.path.isdir(os.path.join(ev, d))]
    C["E07"] = (nodes_ok and bool(corpus), f"corpus={corpus}")

    val = None
    if nodes_ok:
        r = subprocess.run([sys.executable, EVIDENCE_VALIDATE, ev],
                           capture_output=True, text=True)
        try:
            val = json.loads(r.stdout)
        except Exception:
            val = {"status": "error", "raw": (r.stdout or r.stderr)[-300:]}
    C["E08"] = (bool(val) and val.get("status") == "pass",
                f"validate={val.get('status') if val else 'skipped'}"
                + (f" errors={len(val.get('errors') or [])}" if val else ""))

    C["E09"] = (load_yaml(os.path.join(ev, "metrics.yml")) is not None, "")

    ia = read(os.path.join(ws, "analysis", "industry-analysis.md")) or ""
    n_sec = len(re.findall(r"^##+\s+§\d+", ia, re.M))
    sem = (all(w in ia for w in ("Global", "Regional")) and ("Lokal" in ia or "Local" in ia)
           and all(f"D{i}" in ia for i in range(5)) and "ICP" in ia
           and ("Value Proposition" in ia or "Value-Proposition" in ia)
           and ("Quellen" in ia or "Source" in ia))
    C["E10"] = (n_sec >= 8 and sem, f"sections={n_sec} semantics={sem}")

    bp = read(os.path.join(root, "blueprint.md")) or ""
    fam = sum(1 for f in FAMILIES if f in bp)
    C["E11"] = (fam == 13, f"{fam}/13")
    cvs = bp.count("Constituent Value Streams")
    C["E12"] = (cvs >= 13, f"tables={cvs}")
    C["E13"] = (STRIP_MARKER in bp, "")
    body = bp.split(STRIP_MARKER, 1)[1] if STRIP_MARKER in bp else bp
    fp = len(re.findall(r"\b(wir|unser\w*|we|our)\b", body, re.I))
    C["E14"] = (fp >= 60, f"first-person tokens={fp}")
    trip = {w: bp.count(f"**{w}.**") for w in ("Beobachtung", "Potentiale", "Risiken")}
    C["E15"] = (all(v >= 13 for v in trip.values()), str(trip))
    C["E16"] = (("§2.1b" in bp or "konomie-Modell" in bp) and "Impact-KPI" in bp, "")
    # claim ids may be numeric (C_001, AMERICAS) or named (C_identity, EUROPE)
    cids = len(set(re.findall(r"\bC_[A-Za-z0-9_]{3,}\b", bp)))
    C["E23"] = (cids >= 5, f"C_ids={cids}")

    sc = read(os.path.join(ws, "analysis", "scenarios-2050.md")) or ""
    heads = re.findall(r"^###\s+([A-Z])(\d+)\b", sc, re.M)
    groups = {}
    for L, _ in heads:
        groups[L] = groups.get(L, 0) + 1
    scl = sc.lower()
    struct = (re.search(r"no.?regret", scl) is not None and "wildcard" in scl
              and any(w in scl for w in ("axis", "achse", "world", "welt", "2x2", "2×2")))
    C["E17"] = (len(heads) == 60 and len(groups) == 6 and all(v == 10 for v in groups.values())
                and struct, f"{len(heads)}/60 groups={groups}")

    reg = os.path.join(root, "instance", "registry")
    per = {lv: md_count(os.path.join(reg, lv)) for lv in REGISTRY_LEVELS}
    C["E18"] = (all(v >= 1 for v in per.values())
                and md_count(os.path.join(reg, "3_valuestreams"), recursive=False) == 13,
                str(per))

    lp = os.path.join(root, "instance", "operations", "loops")
    C["E19"] = (os.path.isdir(lp) and os.path.exists(os.path.join(lp, "README.md"))
                and os.path.isdir(os.path.join(lp, "_state")), "")

    dl = os.path.join(ws, "_deliverables")
    pdfs = sorted(f for f in os.listdir(dl) if f.endswith(".pdf")) if os.path.isdir(dl) else []
    cover = any(f.startswith("00_") and "Management_Summary" in f for f in pdfs)
    C["E20"] = (os.path.exists(os.path.join(dc, "deliverables.yml")) and cover and len(pdfs) >= 4,
                f"pdfs={len(pdfs)} cover={cover}")

    ms = read(os.path.join(ws, "management-summary.md")) or ""
    C["E21"] = (bool(ms) and "blueprint" in ms.lower()
                and any(w in ms for w in ("industry", "Industrie", "analysis", "Szenarien", "scenarios")),
                "")

    C["E22"] = (os.path.exists(os.path.join(ws, "GATE1.md")), "")
    return C


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    root = (args[0] if args else ".").rstrip("\\/")

    # FAIL CLOSED (lesson 2026-08-11): an unloadable manifest or an empty eval
    # set is a hard error, never a pass. A verifier that passes vacuously is
    # worse than no verifier.
    man_text = read(MANIFEST)
    if man_text is None:
        print(f"ERROR: manifest not found: {MANIFEST}"); sys.exit(2)
    try:
        man = yaml.safe_load(man_text)
    except yaml.YAMLError as e:
        print(f"ERROR: manifest unparseable (fail closed): {str(e)[:200]}"); sys.exit(2)
    evals = (man or {}).get("evals") or []
    n_det_active = sum(1 for e in evals
                       if e.get("method") == "deterministic" and e.get("status") == "active")
    if n_det_active < 15:
        print(f"ERROR: only {n_det_active} active deterministic evals in manifest "
              "(minimum 15) — refusing a vacuous verdict (fail closed)"); sys.exit(2)

    # applicability: pipeline-domain-twin only
    bp_head = (read(os.path.join(root, "blueprint.md")) or "")[:800]
    m = re.search(r"instance_class:\s*(\S+)", bp_head)
    iclass = m.group(1) if m else "unknown"
    if iclass == "business_public_self_presentation":
        print(f"{os.path.basename(root)}: instance_class={iclass} -> Gate-1 suite "
              "not applicable (self-presentation twin; config-surface advisory only)")
        sys.exit(0)

    checks = build_checks(root)
    rows, verdict_ok, pending = [], True, []
    for e in evals:
        eid, st, method = e.get("id"), e.get("status"), e.get("method")
        if st in ("deferred", "retired"):
            continue
        if method == "llm-judged":
            if st == "active":
                pending.append((eid, e.get("title")))
            continue
        ok, detail = checks.get(eid, (None, "not implemented"))
        rows.append((eid, e.get("title"), st, ok, detail))
        if st == "active" and ok is not True:
            verdict_ok = False

    stamp = datetime.date.today().isoformat()
    slug = os.path.basename(root)
    if "--json" in flags:
        print(json.dumps({"instance": slug, "date": stamp, "verdict": verdict_ok,
                          "evals": [{"id": r[0], "status": r[2], "pass": r[3], "detail": r[4]}
                                    for r in rows],
                          "pending_judge": [p[0] for p in pending]}, ensure_ascii=False))
    else:
        print(f"\n=== GATE-1 EVALS v{man.get('version')} — {slug} ({stamp}) ===")
        for eid, title, st, ok, detail in rows:
            tag = "PASS" if ok else "FAIL"
            probe = " (probation)" if st == "probation" else ""
            print(f"  [{tag}] {eid} {title}{probe}" + (f"  · {detail}" if detail else ""))
        for eid, title in pending:
            print(f"  [JUDGE] {eid} {title}  · pending llm judge")
        print(f"  --> GATE 1 (deterministic, active): {'PASS' if verdict_ok else 'FAIL'}\n")

    if "--write-card" in flags:
        ws = os.path.join(root, "instance", "workshop")
        lines = [f"# Gate 1 — Verified Foundation · Eval Card",
                 f"",
                 f"**Instance:** `{slug}` · **Suite:** gate1-evals v{man.get('version')} · "
                 f"**Run:** {stamp} · **Verdict (deterministic, active):** "
                 f"{'PASS' if verdict_ok else 'FAIL'}",
                 f"", "| Eval | Title | Status | Result | Detail |", "|---|---|---|---|---|"]
        for eid, title, st, ok, detail in rows:
            res = "PASS" if ok else "FAIL"
            if eid == "E22":
                res, detail = "PASS", "card generated by this run"
            lines.append(f"| {eid} | {title} | {st} | {res} | {detail} |")
        for eid, title in pending:
            lines.append(f"| {eid} | {title} | active | PENDING-JUDGE | llm rubric |")
        lines += ["", "*Card generated by `run-gate1-evals.py --write-card` — the card is "
                  "the eval report. Judge results are merged on completion.*", ""]
        with open(os.path.join(ws, "GATE1.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"  card written: {os.path.join(ws, 'GATE1.md')}")

    sys.exit(0 if verdict_ok else 1)


if __name__ == "__main__":
    main()
