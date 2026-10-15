#!/usr/bin/env python3
"""lint_flagged_claims.py — deterministic pre-pass for E28/E37.

THE LEAK THIS CATCHES, proven three times in one day (2026-08-13): a value the
evidence graph marks as divergent, teil-belegt, website-only or otherwise
non-confirmed is declared once with its qualification — and then HARDENS into a
flat fact as it travels outward into blueprint, summary, registry and the
shipped translations. Trixie's customer count, Ammerländer's investments,
Westküste's refinancing rate: same mechanism every time, and the judge missed
all three because judging is sampling. Finding must be deterministic; only the
verdict needs judgement.

So: read claims.yml, take every claim that is NOT cleanly confirmed (confidence
other than `belegt`, or carrying a `flag:` / `contradicts*`), extract its
numeric anchors, and hunt the derived artefacts for lines that state those
numbers WITHOUT any qualification. The output is the judge's worklist — and
usually the author's fix list.

Heuristics, stated openly rather than hidden (calibrated against the live
fleet on day one — the first cut produced 26-296 hits per instance, a haystack,
for two reasons now fixed: digit strings matched as SUBSTRINGS ("500" inside
"8.500"), and a clean `belegt` claim carrying a soft precision-flag poisoned
its own headline number):
  * numbers are compared token-against-token with separators stripped
    ("8.500" == "8,500" == 8500), never by substring; tokens shorter than 3
    digits and year-like tokens (19xx/20xx) are skipped.
  * two severities. HARD (gates): anchors of claims whose confidence is
    unbestaetigt/divergent/teil-belegt, and anchors named in a contradicts*
    entry — these are KNOWN disputes, and stating one side flat is the proven
    leak. SOFT (reported, not gating): anchors of website/marktreport/inferred
    claims asserted without their tag — a calibration question for the
    founder, not a red build. A `flag:` on an otherwise belegt claim is a
    precision note, not a dispute — skipped.
  * a line counts as QUALIFIED if it carries a hedge word (unbestätigt,
    divergent, Band, Spanne, website, Selbstauskunft, G_<gap>, …) or if it
    shows the SPREAD itself (two distinct anchors of the same claim in one
    line — ">8.500 … >30.000" is the honest form, not a leak).
  * evidence/ is never scanned (it is the source of the flags), and lines that
    are themselves the §0 declaration carry their hedge and pass.

Usage:
  python lint_flagged_claims.py <instance-root> [--json]

Exit 0 = clean, 1 = findings, 2 = cannot lint (no claims.yml — fail closed).
"""
import os, re, sys, json

try:
    import yaml
except ImportError:
    print("pyyaml not installed"); sys.exit(2)
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

CONFIRMED = {"belegt"}
HARD_CONF = {"unbestaetigt", "unbestätigt", "divergent", "teil-belegt", "obekräftad"}
SOFT_CONF = {"website", "marktreport", "inferred", "webbplats", "marknadsrapport"}
HEDGES = [
    "unbestätigt", "unbestaetigt", "unconfirmed", "obekräftad",
    "diverg",                                  # divergent/-enz/-ieren/diverge
    "teil-belegt", "teilbelegt",
    "inferred", "abgeleitet", "härledd",
    # a figure the publisher itself marks as an estimate travels qualified by that word
    "schätzung", "schaetzung", "geschätzt", "geschaetzt", "estimate", "estimated", "uppskatt",
    "website", "webbplats", "marktreport", "market report", "marknadsrapport",
    "selbstauskunft", "selbstbeschreibung", "self-descri", "self-report",
    "egen uppgift", "operatörens egen",
    "bandbreite", "spanne", "band ", "range", "spann",
    "einzelquellig", "single source", "single-source", "en källa",
    "deal pr", "deal-pr", "laut ", "according to", "enligt ",
    "nicht sichtbar", "not visible", "inte synlig", "unbestimmt", "undetermined",
    "vs.", "gegen ", "kursiert", "circulat",
    # the federation rendering says in English what the source says in German:
    # a contradiction shown as "A against B" is the honest form there too
    "against", "versus", "conflicting", "discarded", "encyclopaedic", "encyclopedic",
    "company statement", "per company", "own statement", "not verified",
    "firmenangabe", "aggregator",
    # naming the counting frame IS the qualification: "drei Quellen, drei
    # Abgrenzungen; eine Rankingdatenbank führt 748" is the honest form
    "abgrenzung", "rankingdatenbank", "ranking database", "kopfzahl", "zählweise", "zaehlweise",
    "sekundärkäll", "sekundärquell", "secondary source",
    "huvudmannanivå", "regional nivå",         # sv scope qualifiers (level, not subject)
    # The English forms our own authors actually write. The list grew on German
    # instances and did not know them, so honest English sentences — "by our own
    # account", "no source we hold reconciles the two" — were charged as flat
    # assertions (found 2026-08-26 across five English twins).
    "by our own", "our own account", "our own count", "our own figures",
    "our own current", "our own reading", "on our own reading",
    "count differently", "counts differently", "counted differently",
    "no source we hold", "does not reconcile", "do not reconcile", "reconciles the two",
    "the readings differ", "two readings", "both readings",
    "cautions travel", "caution travels",
    "statutory annual average", "as filed", "audited consolidated",
    "not established", "could not be established", "remains open", "unresolved",
    "the company states", "the company puts", "the house states", "the group states",
    "without naming", "does not name", "no number", "nearest published",
    "own projection", "sector's own", "issuer's own",
    "false precision", "currencies and financial years", "would be a false",
    # NOT hedges, deliberately: "around", "about", "more than", "approximately".
    # They round a figure; they say nothing about a reading being contested. Adding
    # them (tried and reverted 2026-08-26) would have made the instrument blind to
    # exactly the sentences it exists to catch.
]
GAP_REF = re.compile(r"G_[a-z0-9_]+|G\d+", re.I)  # G_customers AND bare G4 (sv twin)
CLAIM_REF = re.compile(r"C_[a-z0-9_]+", re.I)
# Numbers that are IDENTIFIERS, not quantities: norm/register/issue/paragraph
# references. Left in, they anchor on ISO 15378 or europe.o#155 and flood the
# report (observed live: bk 68 "hard" hits, most of them the ISO number of a
# cleanroom cert quoted in a contradicts note).
# A claim or gap id is an IDENTIFIER, not a quantity — "C_042" carries no 42.
# Until 2026-08-26 the ids were left in the number stream and collided with the
# anchors of real claims, so evidence footers ("- Evidence: C_019, C_015, …")
# were charged as unqualified statements. The defect stayed invisible because
# the same line was then excused for citing a claim id at all: one bug hid the
# other. Both are fixed — ids are not numbers, and citing an id is not a hedge.
IDENT = re.compile(r"([CG]_[a-z0-9_]+|#\d+|(?:ISO|IEC|EN|DIN|HRB|HRA|WZ|SGB|COM)\s*[-(]?\s*\d[\d-]*|§\s*\d+[a-z]?"
                   # EU legal acts are cited as year/number — "VO (EU) 2025/2650",
                   # "Richtlinie 2014/24/EU". Left in, the act NUMBER anchors on any
                   # claim that happens to share those digits (niederegger.d: the EUDR
                   # amending regulation collided with a flagged quantity, twice).
                   r"|\(EU\)\s*\d{4}/\d+|\b\d{4}/\d+/(?:EU|EG|EWG)\b|\b\d{4}/\d{1,5}\b(?=\s*\)|\s*(?:vom|of)\b)"
                   r"|(?:per|je|pro)\s+1[.,]?000)", re.I)   # rate denominators are units, not quantities
NUM = re.compile(r"\d[\d.,  ]*\d|\d")
YEARLIKE = re.compile(r"^(19|20)\d{2}$")
# Two claims may legitimately carry the SAME digits in different currencies —
# oldendorff.d had 600 Mio. AED (a freight contract, unbestaetigt) beside
# 600 Mio. USD (cumulative transhipment investment, website). The lint blamed
# the AED claim for every line about the USD one, and a "fix" would have hedged
# a correct sentence. Where a line names a currency, it may only be charged to a
# claim of that currency.
CURRENCY = re.compile(r"(?<![A-Za-z])(AED|USD|EUR|CHF|GBP|SEK|DKK|NOK|JPY|CNY|RMB)(?![A-Za-z])|[€$£]")


def currencies(text):
    return set(m.group(0).upper() for m in CURRENCY.finditer(text or ""))

SCAN = ["blueprint.md", "lighthouse.md",
        "instance/workshop/management-summary.md",
        "instance/workshop/pitch.md"]
SCAN_GLOB_DIRS = ["instance/workshop/analysis", "instance/registry",
                  "instance/workshop/_deliverables"]


def norm_tokens(text):
    """Numeric anchors of a statement, separator-free, noise filtered."""
    out = set()
    text = IDENT.sub(" ", text or "")   # identifiers are not quantities
    for m in NUM.finditer(text):
        t = re.sub(r"[.,  ]", "", m.group(0))
        if len(t) < 3 or YEARLIKE.match(t):
            continue
        if re.match(r"^\d{1,4}(19|20)\d{2}$", t):
            continue                      # a DATE (13.05.2025 -> 13052025), not a quantity
        out.add(t)
    return out


def flagged_claims(root):
    """{claim_id: (anchors, severity)} — severity 'hard' gates, 'soft' informs."""
    p = os.path.join(root, "instance", "workshop", "evidence", "claims.yml")
    if not os.path.exists(p):
        return None
    doc = yaml.safe_load(open(p, encoding="utf-8")) or {}
    # Anchors of cleanly confirmed claims are EXEMPT everywhere: a number that
    # a belegt claim carries (">400 Servicekraefte", an ISO capability) must not
    # alarm just because an unrelated unbestaetigt claim happens to contain the
    # same digits. Observed live: auma's revenue-trajectory claim (unbestaetigt
    # for the GAP YEARS) shares "400" with the belegt service network and put 32
    # false hits on it. Only claims with neither contradicts nor flag donate
    # exemptions — a disputed claim must never exempt its own dispute.
    confirmed_anchors = set()
    for c in doc.get("claims") or []:
        conf = str(c.get("confidence", "")).lower()
        # a flag on a belegt claim is a precision note, not a dispute — it may
        # still exempt (auma: revenue 580.7 belegt-with-note; the unbestaetigt
        # TRAJECTORY claim quoting the same figure must not alarm on it)
        if conf in CONFIRMED and not any(k.startswith("contradicts") for k in c):
            confirmed_anchors |= norm_tokens(c.get("statement", ""))
    # anchor -> {claim_id: its currencies} across ALL claims, so a collision on
    # the same digits can be resolved by the currency the line actually names
    owners = {}
    for c in doc.get("claims") or []:
        cur = currencies(f"{c.get('unit', '')} {c.get('statement', '')}")
        for a in norm_tokens(c.get("statement", "")):
            owners.setdefault(a, {})[c.get("id", "?")] = cur
    flagged = {}
    for c in doc.get("claims") or []:
        conf = str(c.get("confidence", "")).lower()
        contra = " ".join(str(v) for k, v in c.items() if k.startswith("contradicts"))
        if conf in HARD_CONF:
            anchors, sev = norm_tokens(c.get("statement", "")) | norm_tokens(contra), "hard"
        elif contra:
            # claim is belegt but a named dispute exists: only the DISPUTED
            # numbers gate, the rest of the statement is confirmed
            anchors, sev = norm_tokens(contra), "hard"
        elif conf in SOFT_CONF:
            anchors, sev = norm_tokens(c.get("statement", "")), "soft"
        else:
            continue
        # The exemption decides what may TRIGGER, never what counts as a spread:
        # "20.000 USD/Tag nach zuvor 14.000" is the honest form, and it stayed
        # honest when another belegt claim happened to donate 14.000 (oldendorff.d,
        # three false hits). Keep the full anchor set for the spread test.
        trigger = anchors - confirmed_anchors
        if trigger:
            flagged[c.get("id", "?")] = (trigger, sev,
                                         currencies(f"{c.get('unit', '')} {c.get('statement', '')}"),
                                         anchors)
    return flagged, owners


def scan_files(root):
    files = [os.path.join(root, f) for f in SCAN]
    for d in SCAN_GLOB_DIRS:
        base = os.path.join(root, d)
        for dirpath, _, names in os.walk(base):
            files += [os.path.join(dirpath, n) for n in names if n.endswith(".md")]
    return [f for f in files if os.path.exists(f)]


def lint(root):
    loaded = flagged_claims(root)
    if loaded is None:
        return None
    claims, owners = loaded
    findings = []
    for f in scan_files(root):
        rel = os.path.relpath(f, root).replace("\\", "/")
        for ln, line in enumerate(open(f, encoding="utf-8", errors="replace"), 1):
            low = line.lower()
            line_tokens = norm_tokens(line)      # token vs token, no substrings
            if not line_tokens:
                continue
            # A line that cites its claim id is TRACEABLE — not qualified. The two
            # were conflated until 2026-08-26, when an independent judge found both
            # E28 failures of an instance sitting in exactly this shape: a disputed
            # figure stated flat with "(C_059)" after it, counted as honest because
            # the id was there. Traceability says where a number comes from;
            # qualification says that the reading is contested. A gap id (G_x) IS a
            # qualification — "not visible to us (G9)" names the limit.
            # The strict reading drops the claim-id exemption; `hedged` keeps it so
            # the standing gate (E37) does not move under the fleet's feet.
            hedged_words = any(h in low for h in HEDGES) or bool(GAP_REF.search(line))
            hedged = hedged_words or bool(CLAIM_REF.search(line))
            line_cur = currencies(line)
            for cid, (anchors, sev, cur, all_anchors) in claims.items():
                hit = sorted(anchors & line_tokens)
                if not hit:
                    continue
                spread_shown = len(all_anchors & line_tokens) >= 2  # both readings = honest form
                if hedged or spread_shown:
                    # still record it for the strict reading, where a bare claim id
                    # does not excuse an unqualified disputed figure
                    if not (hedged_words or spread_shown):
                        findings.append({"file": rel, "line": ln, "claim": cid,
                                         "severity": "strict", "anchor": hit[0],
                                         "text": line.strip()[:160]})
                    continue
                # the line names a currency, and it is not this claim's but
                # another claim's for the same digits — the number is not ours
                if line_cur and cur and not (line_cur & cur):
                    rivals = set()
                    for other, ocur in owners.get(hit[0], {}).items():
                        if other != cid:
                            rivals |= ocur
                    if line_cur & rivals:
                        continue
                findings.append({"file": rel, "line": ln, "claim": cid,
                                 "severity": sev, "anchor": hit[0],
                                 "text": line.strip()[:160]})
    return findings


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    root = sys.argv[1]
    findings = lint(root)
    if findings is None:
        print("FAIL-CLOSED: no claims.yml — nothing to lint against."); sys.exit(2)
    hard = [x for x in findings if x["severity"] == "hard"]
    soft = [x for x in findings if x["severity"] == "soft"]
    strict = [x for x in findings if x["severity"] == "strict"]
    if "--json" in sys.argv:
        print(json.dumps(findings, ensure_ascii=False, indent=2))
    else:
        for x in hard:
            print(f"  HARD  {x['file']}:{x['line']}  [{x['claim']} · {x['anchor']}]  {x['text']}")
        if "--soft" in sys.argv:
            for x in soft:
                print(f"  soft  {x['file']}:{x['line']}  [{x['claim']} · {x['anchor']}]  {x['text']}")
        if "--strict" in sys.argv:
            for x in strict:
                print(f"  strict {x['file']}:{x['line']}  [{x['claim']} · {x['anchor']}]  {x['text']}")
        print(f"\n  hard={len(hard)} (gates)  soft={len(soft)} (reported)  "
              f"strict={len(strict)} (claim id cited, reading not qualified)")
    sys.exit(1 if hard else 0)


if __name__ == "__main__":
    main()
