# GATE 1 — Verified Foundation  ·  {SUBJECT}

**Instance:** `{slug}.d` · **Verified:** {YYYY-MM-DD} · **Verifier:** {agent/human}

Gate 1 is the firewall between the **verified foundation** (evidence · industry
analysis · `.d` blueprint v1 · scenarios) and the **speculative layer** (dark-horse
+ the three game poles). Nothing downstream is built until this card passes,
because every speculative artifact anchors to this foundation — an error here
compounds. The gate is a 2-minute human read of this card; most rows are
machine-checkable (the seed of the deterministic build program).

## Conformance card (first line of every phase audit note)

> `Templates read: industry-analysis.md ({n} lines), scenarios-2050.md ({n} lines), blueprint.md ({n} lines), evidence-schema/ (3 files). Reference read: {wieds|avamo}.d equivalents.`

## Criteria

| # | Criterion | How checked | Pass |
|---|---|---|---|
| **G1.1** | `.d` scaffold present + config surface (identity/config/README/AGENT pointer). *(Full commons-os fork is a post-Gate-1 mechanical step; Gate-1 scope = the workshop foundation.)* | file presence | ☐ |
| **G1.2** | Evidence graph present + parseable: `sources.yml` · `entities.yml` · `claims.yml` · `README.md` · `knowledge/` | `evidence-validate.py` parses | ☐ |
| **G1.3** | **Belegregel:** every `tier: headline` Claim has ≥2 distinct `asserted_by`/`corroborated_by`, OR `confidence: unbestätigt`. No estimate without a tag. | validator | ☐ |
| **G1.4** | **No unresolved contradictions:** every `contradicts` edge answered by a `supersedes`. | validator | ☐ |
| **G1.5** | Industry Analysis present, follows template (§0–§10 + Sources), IA-§ referenceable, sources cited. | structure grep | ☐ |
| **G1.6** | `.d` Blueprint v1: structure = business-essentials `blueprint.md` **exactly** (all 13 canonical families named; §-structure complete); **every headline figure traces to a Claim** (`used_in` back-edge); Kern-Befund **derived, not reflexive**; Wir/subject perspective. | grep + trace | ☐ |
| **G1.7** | Scenarios 2050: **60 = 6×10** (N/T/W/R/K/U), fixed 7-part block, 2 axes → 2×2 → 4 worlds, No-Regret matrix, Wildcards; references IA §x. | structure grep | ☐ |
| **G1.8** | Independent verify pass run (this card) + audit note recorded. | this file exists | ☐ |

## Result

**GATE 1: {PASS | FAIL}** — {one line}. On PASS, Phase 4b (dark-horse + `.g1/.g2/.g3`) is unlocked.

### Findings (if any drift caught)
- {…}
