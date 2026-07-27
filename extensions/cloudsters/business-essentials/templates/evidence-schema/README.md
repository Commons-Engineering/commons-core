# Evidence Knowledge Graph — Schema (business-essentials)

The evidence layer of a `.d` instance is a **git-diffable knowledge graph**, not a
pile of prose. Three node files plus typed edges expressed as id-reference fields.
No graph database — the yml *is* the adjacency list. A small validator
(`evidence-validate.py`) turns the belegregel into a machine check and is the
core of **Gate 1**.

## Why a graph and not two flat lists

A flat `metrics.yml` lets a stale number sit silently next to a corrected one and
propagate into the blueprint (this is exactly the −97 vs −140,7 failure on UKSH).
A graph makes three things first-class:

| Property | Flat list | Graph |
|---|---|---|
| **Belegregel** (headline figure ≥ 2 sources) | prose promise | query over `asserted_by` / `corroborated_by` edges |
| **Contradictions** | silent overwrite | explicit `contradicts` edge that **must** be resolved (`supersedes`) before Gate 1 |
| **Traceability** (every blueprint number traces to evidence) | manual | `used_in` back-edge, grep-checkable |

## Node kinds

| File | Node | Key fields |
|---|---|---|
| `sources.yml` | **Source** — a document/page you read | `id · title · type · year · url · retrieved · trust_tier` |
| `entities.yml` | **Entity** — the subject and its world (company, unit, competitor, person, programme, market) | `id · type · name` *(types come from the pack vocabulary)* |
| `claims.yml` | **Claim** — one assertion (a metric OR a qualitative fact) | `id · statement · value · unit · year · scope · confidence` + **edges** |

## Edge kinds (fields inside a Claim)

| Edge | Means | Used by |
|---|---|---|
| `asserted_by: [S1, S3]` | belegt durch diese Quelle(n), mit Locator | belegregel |
| `about: [E_ACME]` | handelt von dieser Entity | grouping |
| `corroborated_by: [S4]` | zusätzlich bestätigt durch | belegregel (≥2) |
| `contradicts: [C_042]` | widerspricht diesem Claim | **must resolve** |
| `supersedes: [C_042]` | ersetzt (neuer/geprüfter Wert) | freshness |
| `used_in: [d§2.1, scn:R2]` | wird verwendet in Blueprint-§ / Szenario | traceability |

## Confidence convention (belegregel — never estimate silently)

| Tag | Meaning |
|---|---|
| `belegt` | official / association / company report / regulatory filing |
| `marktreport` | commercial market research — read as an **order-of-magnitude band** (vendors differ ±30 %) |
| `unbestätigt` | weak / single-source — flagged, never asserted as fact |

**Rule:** every Claim carries a `confidence` tag. Every `tier: headline` Claim must
have **≥ 2 distinct** `asserted_by`/`corroborated_by` sources **or** be tagged
`unbestätigt`. Nothing is estimated without a tag. See
`../../../../workshop/_specifications/INSTANCE_PIPELINE_SPEC.md` Data Triangulation Standard.

## Layout produced per instance

```
{slug}.d/instance/workshop/evidence/
  sources.yml          # Source nodes
  entities.yml         # Entity nodes
  claims.yml           # Claim nodes + edges
  README.md            # 1-paragraph orientation for this subject
  knowledge/*.md       # human-readable dossiers; every hard figure cites a C_id
```

The dossiers in `knowledge/` are context for a human reader. **Every hard figure
they cite must exist as a Claim node** and be referenced by its `C_id` — the prose
never introduces an un-noded number.
