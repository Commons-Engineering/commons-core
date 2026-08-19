# COMMONS ENGINEERING — BODY OF KNOWLEDGE
*The Canonical Index*

**Version:** 1.0
**Status:** Living Document
**Companion:** COMMONS_TAXONOMY_MANIFEST.md, PATTERN_SPEC.md (v8.2), COMMONS_ENGINEERING_ARCHITECTURE.md

---

## §1 What This Is

Commons Engineering is a discipline for designing living systems — individuals, organisations, cities, ecosystems — toward vitality rather than extraction. Its Body of Knowledge (BoK) is the complete set of documents, patterns, specifications, taxonomies, scripts, and data that constitute the intellectual infrastructure of that discipline.

This document is the map. It does not repeat what the other documents say. It tells you what exists, where it lives, how it relates, and in what order to read it.

The BoK is organised in six layers:

| Layer | What it contains | Where it lives |
|---|---|---|
| **Manifests** | The philosophy, architecture, and identity of the discipline | `_manifests/` |
| **Specifications** | The normative technical standards | `_specifications/` |
| **Pattern Library** | The knowledge commons — ~26,100 patterns across four domains | `_patterns/` |
| **Lighthouse Library** | The coastline — organisational briefings and account records | `_lighthouses/` |
| **Taxonomy** | The structural scaffolding — domain maps, spreadsheets, coverage reports | `_taxonomy/` |
| **Pipeline** | The scripts and processes that generate, enrich, and validate patterns | `_scripts/` |
| **Data & Registries** | TypeID registries, slug mappings, reference frameworks | `_scripts/*.json`, root `*.xlsx` |

---

## §2 The Architecture in One Page

```
                        ┌─────────────────────────────┐
                        │   COMMONS_ENGINEERING_BOK   │  ← YOU ARE HERE
                        │   (this document)           │
                        └──────────────┬──────────────┘
                                       │
              ┌────────────────────────┼────────────────────────┐
              │                        │                        │
    ┌─────────▼──────────┐  ┌─────────▼──────────┐  ┌─────────▼──────────┐
    │  THE FIELD         │  │  THE FORMAT        │  │  THE STRUCTURE     │
    │                    │  │                    │  │                    │
    │  Commons Eng.      │  │  PATTERN_SPEC v8.2 │  │  Taxonomy Manifest │
    │  Manifest          │  │ (definitive format)│  │  (gravitational    │
    │  (philosophy)      │  │                    │  │   architecture)    │
    └─────────┬──────────┘  └─────────┬──────────┘  └─────────┬──────────┘
              │                        │                        │
    ┌─────────▼──────────┐  ┌─────────▼──────────┐  ┌─────────▼──────────┐
    │  THE INSTRUMENTS   │  │  THE PIPELINE      │  │  THE DOMAINS       │
    │                    │  │                    │  │                    │
    │  Engine Manifest   │  │  Pipeline Spec     │  │  Business Manifest │
    │  Blueprint Manifest│  │  Scripts & Runners │  │  Urban Manifest    │
    │  Engineer Manifest │  │  Enrichment & RAG  │  │  Life Manifest     │
    │  Incubator Manifest│  │                    │  │  Ecology Manifest  │
    └────────────────────┘  └────────────────────┘  └────────────────────┘
```

**Three pillars hold the Body of Knowledge:**

1. **The Field** — what Commons Engineering is, why it exists, and who practises it
2. **The Format** — how every pattern is written, structured, and qualified
3. **The Structure** — how ~26,100 patterns are organised across six orbital layers and four domain scales

Everything else — the engines, the blueprint, the pipeline, the taxonomies, the domain manifests — is an instrument built on top of these three pillars.

---

## §3 The Document Constellation

### §3.1 Manifests — The Philosophy Layer

Manifests define *what* and *why*. They are the normative documents of the discipline — they describe what Commons Engineering is, what it values, and how it organises itself. They are written in natural language, in the voice of the discipline itself.

| Document | Version | Purpose | Read when... |
|---|---|---|---|
| **COMMONS_ENGINEERING_MANIFEST** | v1.0 | The founding document. Defines the field: four domains, the commons imperative, the philosophical foundations. | You want to understand what Commons Engineering is and why it exists. |
| **COMMONS_AGENT_MANIFEST** | v1.0 | The four-agent governance model: Purpose, Participation, Proposition, Production. Agents converse and govern; engines (production lines) operate under agents. | You want to understand how the commons is governed and how production lines work. |
| **COMMONS_BLUEPRINT_MANIFEST** | v1.0 | The 9-layer temporal architecture (Anatomy L1–L6, Physiology L7–L9). The primary design artefact for specifying any living system. | You want to understand the Blueprint — the tool that practitioners use to specify organisations, settlements, ecosystems, or lives. |
| **COMMONS_ENGINEER_MANIFEST** | v1.0 | The practitioner development framework: the 7Cs arc, practitioner identity, development paths. | You want to understand who the practitioner is and how they develop. |
| **COMMONS_INCUBATOR_MANIFEST** | v1.0 | The deployment network: how Commons Incubators take patterns into the field and return learning. | You want to understand how the knowledge reaches the world. |
| **COMMONS_TAXONOMY_MANIFEST** | v1.0 | The gravitational architecture: six orbital layers, two opposing forces, 4×4 cross-taxonomy matrix, value stream hierarchy, clean room principle. | You want to understand how patterns are organised, classified, and positioned. **If any script disagrees with this document, this document governs.** |
| **COMMONS_ENGINEERING_IMPACT_MANIFEST** | v1.0 | The impact model: how the discipline measures its own effectiveness. | You want to understand how Commons Engineering evaluates success. |
| **COMMONS_ENGINEERING_ARCHITECTURE** | v2.0 | CE's system architecture: tech stack, AI-driven development, repository architecture, production lines. | You are a **developer** working on the platform or want to understand CE's infrastructure. |
| **CLOUDSTERS_LIVING_BLUEPRINT** | v1.0 | The Blueprint of cloudsters itself — the Commons Incubator that is building the Body of Knowledge. | You want to understand the organisation behind the project. |

### §3.2 Domain Manifests — The Four Scales

Each domain manifest defines a scale of the commons — its imperative, its terrain, its Purpose Spiral, its Blueprint, its practitioner, and its pattern library. They follow an identical structure:

| Document | Scale | Unique Position |
|---|---|---|
| **LIFE_ENGINEERING_MANIFEST** v1.0 | The organism — the individual human life | "Life as the Interior" — the only domain where designer and designed are the same entity |
| **BUSINESS_ENGINEERING_MANIFEST** v1.0 | The enterprise — any value-creation system | "Value Creation as Organising Principle" — profit is a design parameter, not the purpose |
| **URBAN_ENGINEERING_MANIFEST** v1.0 | The settlement — cities, towns, neighbourhoods | "Urban as Melting Point" — where every other domain is simultaneously enacted |
| **ECOLOGY_ENGINEERING_MANIFEST** v1.0 | The biosphere — ecosystems, watersheds, bioregions | "Ecology as Foundation" — the substrate on which all other domains rest |

**Structural template** (all four follow this):
- Preamble → §1 The [Domain] Imperative (§1.1 Century/Threshold, §1.2 Failure of..., §1.3 Standing on Giants) → §2 What a [Domain] Commons Is (§2.1 Fractal Chain, §2.2 Living System, §2.3 Unique Position) → §3 Purpose Spiral (4 dimensions) → §4 Blueprint → §5 Discipline → §6 Practitioner → §7 Pattern Library → §8 Relationship to Other Manifests

### §3.3 Specifications — The Technical Standards

Specifications define *how*. They are normative: if a pattern or a script does not conform to the spec, the pattern or script is wrong.

| Document | Version | Purpose |
|---|---|---|
| **PATTERN_SPEC** | v8.2 | The definitive pattern format. Seven frontmatter groups, eight body sections, orbital layer definitions, clean room compliance rules. Every pattern in the library must conform to this spec. |
| **LIGHTHOUSE_BUSINESS_SPEC** | v1.2 | The lighthouse briefing format for Business domain. Eight frontmatter groups (paralleling PATTERN_SPEC), eight body sections following the Business Purpose Spiral (13 value streams). Includes account management fields for CRM integration. |
| **LIGHTHOUSE_URBAN_SPEC** | v1.2 | The lighthouse briefing format for Urban domain. Eight frontmatter groups (paralleling LIGHTHOUSE_BUSINESS_SPEC), eight body sections following the Urban Purpose Spiral (21 value streams). Includes settlement identity, regional context, and business lighthouse nesting. |
| **PATTERN_PIPELINE_SPEC** | — | How patterns move through the pipeline: stub generation → body enrichment → GraphRAG enrichment → validation. Defines the async enrichment process, prompt templates, and quality gates. |
| **COMMONS_MCP_ARCHITECTURE_SPEC** | v1.0 | The MCP knowledge service architecture. Five layers (GitHub → ETL → Neo4j → MCP Server → GraphRAG), tool catalogue, tier model, data sovereignty. |
| **COMMONS_OS_SPEC** | v1.0 | The forkable OS template: fork mechanics, AGENT.md, ALIGN.md, curated collections, intranet/extranet publishing. |

---

## §4 The Pattern Library

### §4.1 Scale and Structure

The pattern library is the knowledge commons — the core intellectual asset of the discipline. As of March 2026:

| Location | Content | Count |
|---|---|---|
| `_patterns/_core/` | **Orbit 0 — Singularity.** The irreducible principles from which all pattern knowledge derives. | 7 |
| `_patterns/business/` | **Business domain** — enterprise-scale patterns across the four dimensions (Definition & Purpose, Participation & Relationship, Proposition & Exchange, Production & Resilience). Organised in ~63 functional domain subfolders. | ~9,425 |
| `_patterns/urban/` | **Urban domain** — settlement-scale patterns. Flat structure (awaiting subfolder organisation). | ~14,593 |
| `_patterns/life/` | **Life domain** — organism-scale patterns. Flat structure. | ~2,050 |
| `_patterns/ecology/` | **Ecology domain** — biosphere-scale patterns. Early stage. | 2 |
| `_patterns/_emerge/` | **Edge frontier** — patterns without existing governance frameworks. Staging area. | 0 |
| `_patterns/collections/` | **Curated collections** — hand-assembled pattern sets for specific purposes. | 2 |
| `_patterns/Commons Engineer Collection 01/` | **Practitioner curriculum** — patterns selected for the Commons Engineer development arc. | 22 |
| **Total** | | **~26,100** |

### §4.2 Orbital Layers

Every pattern occupies an orbital layer (see COMMONS_TAXONOMY_MANIFEST §2 for full definitions):

| Orbit | Name | Character | Current Status |
|---|---|---|---|
| 0 | **Singularity** | Infinite density. The source. | 7 patterns in `_core/` |
| 1 | **Principle** | First Principles & Practices. Universal truths. | ~19 candidates identified (see §4.3); not yet written to spec |
| 2 | **Commons** | Cross-domain patterns. Shared across all four scales. | Emerging via GraphRAG; not yet formally separated |
| 3 | **Bridge** | Domain-anchored but reaching across. Visible from other domains. | Emerging via GraphRAG |
| 4 | **Domain** | The mechanical substrate. Domain-specific, clean room. | Bulk of the library (~26,000) |
| 5 | **Edge** | Incoming. Unvalidated. The frontier. | `_emerge/` staging area |

### §4.3 Orbit 1 — First Principles & Practices (Seed Catalogue)

The following Orbit 1 candidates were identified in the cloudsters *First Principles & First Practices* document (March 2025). This is a starting collection, not a complete catalogue. Additional Orbit 1 patterns will be surfaced by the enrichment pipeline and GraphRAG analysis as the library matures.

**First Principles** (from physics, ecology, systems science — relatively immutable):

| # | Principle | Domain of Origin |
|---|---|---|
| 1 | Conservation of Energy & Matter (1st Law of Thermodynamics) | Physics |
| 2 | Entropy & Irreversibility (2nd Law of Thermodynamics) | Physics |
| 3 | Carrying Capacity & Ecological Limits | Ecology |
| 4 | Evolutionary Adaptation (Variation & Selection) | Biology |
| 5 | Emergence & Complexity | Systems Science |
| 6 | Feedback & Adaptive Cycles (Cybernetic Control) | Cybernetics |

**First Practices** (from social, economic, governance traditions — evolving):

| # | Practice | Domain of Origin |
|---|---|---|
| 7 | Reciprocity & Fairness | Social |
| 8 | Subsidiarity & Local Empowerment | Governance |
| 9 | Cultural Meaning & Shared Purpose | Cultural |
| 10 | Truth-Seeking & Transparency | Cultural |
| 11 | Economic Constraint (Scarcity & Opportunity Cost) | Economic |
| 12 | Incentives & Self-Interest | Economic |
| 13 | Cooperative Surplus & Alignment | Economic |
| 14 | Time-Sliced (Iterative) Planning | Economic |
| 15 | Network Effects & Multi-Sided Platforms | Economic |
| 16 | Collective Action & Governance | Governance |
| 17 | Polycentric / Fractal Organisation | Governance |
| 18 | Adaptive Management & Feedback | Governance |
| 19 | Conflict Resolution & Evolving Rules | Governance |

**Status:** These 19 candidates need to be written as full v8.2 patterns and placed in `_patterns/` at Orbit 1. The existing 7 Orbit 0 (Singularity) patterns in `_core/` provide the layer above; the ~26,000 Orbit 4 patterns provide the layer below. Orbit 1 is the structural bridge between them — the bones of the system.

### §4.4 Pattern Format

Every pattern in the library conforms to **PATTERN_SPEC v8.2** — the Orbital Edition. The spec defines:

- **Seven frontmatter groups:** identity, classification, commons assessment, relationships, graph garden, content metadata, section summaries
- **Eight body sections:** Context, Forces & Tensions, Solution, Implementation, Related Patterns, Commons Alignment, Sources, Changelog
- **Clean Room Principle:** Sections 1–5 are original, IP-free work. Section 6 may contain fair-use references with proper attribution.
- **Orbital classification:** Every pattern declares its `universality_class` (Orbit 0–5), `gravitational_hubs`, `primary_tension`, and `vector_keywords`

For full detail: read `_specifications/PATTERN_SPEC.md`.

---

## §5 The Pipeline

### §5.1 How Patterns Are Made

The pattern pipeline has four stages. Each stage has its own scripts and processes:

```
  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
  │ 1. GENERATE  │ ──▶ │ 2. ENRICH    │ ──▶ │ 3. GRAPH     │ ──▶ │ 4. VALIDATE  │
  │   (stubs)    │     │   (body)     │     │   (GraphRAG) │     │   (QA)       │
  └──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
```

**Stage 1 — Stub Generation:** Create v8.2 frontmatter stubs from domain taxonomy. Scripts: `generate_balanced_patterns.py`, `pattern_stub_generator_business.py` (referenced by migration scripts).

**Stage 2 — Body Enrichment:** Async Claude API calls to fill body sections (Context, Forces, Solution, Implementation, etc.). Scripts: `enrich_business_async.py`, `enrich_urban_async.py`, `enrich_async.py`. Batch runner: `run_enrich_business_overnight.bat`.

**Stage 3 — GraphRAG Enrichment:** Infer cross-pattern relationships, entities, gravitational hubs, and community assignments. Script: `graphrag_enrich.py`. Batch runner: `run_graphrag.bat`.

**Stage 4 — Validation:** Check patterns against PATTERN_SPEC v8.2 for structural conformance. Script: `validate_pattern.py`. Normalisation: `normalize_patterns.py`, `run_normalize.bat`.

### §5.2 Supporting Scripts

| Script | Purpose |
|---|---|
| `generate_typeid.py` | Generate Crockford-base32 TypeIDs for patterns |
| `build_combined_excel.py` | Build combined Excel tracking spreadsheet |
| `canonicalize_business.py` | Canonical slug normalisation for business patterns |
| `crossref_territory_map.py` | Cross-reference patterns against domain taxonomy |
| `map_patterns_to_new_domains.py` | Reclassify patterns after taxonomy changes |
| `variant_families.py` | Detect variant families across patterns |
| `rebuild_territory_map.py` | Rebuild the territory coverage map |

### §5.3 Registries

| File | Purpose |
|---|---|
| `_scripts/typeid_registry.json` | Master TypeID → slug mapping |
| `_scripts/business_typeid_registry.json` | Business domain TypeIDs |
| `_scripts/urban_typeid_registry.json` | Urban domain TypeIDs |
| `_scripts/commons_os_typeid_registry.json` | Migrated Commons-OS TypeIDs |
| `_scripts/business_slug_mapping.json` | Business slug normalisation mapping |

---

## §6 The Taxonomy

### §6.1 Domain Taxonomies

Each domain has a taxonomy spreadsheet that maps the functional structure of the domain — the sub-domains, value stream families, and pattern territories:

| File | Domain | Structure |
|---|---|---|
| `_taxonomy/business-engineering-domain-taxonomy-v2.xlsx` | Business | ~63 functional domains across the four dimensions |
| `_taxonomy/urban-engineering-domain-taxonomy.xlsx` | Urban | Functional domains for settlement-scale commons |
| `_taxonomy/life-engineering-domain-taxonomy.xlsx` | Life | Functional domains for organism-scale commons |
| `_taxonomy/ecology-engineering-domain-taxonomy.xlsx` | Ecology | Functional domains for biosphere-scale commons |

### §6.2 Pattern Tracking

| File | Purpose |
|---|---|
| `_taxonomy/business-engineering-patterns-combined.xlsx` | Combined business patterns (mapped + generated) |
| `_taxonomy/business-engineering-patterns-orbit4.xlsx` | Clean-room Orbit 4 business patterns |
| `_taxonomy/urban-engineering-patterns.xlsx` | Urban pattern tracking |
| `_taxonomy/territory-coverage-report.xlsx` | Coverage analysis: which domains have patterns, which need generation |
| `_taxonomy/cull_manifest.xlsx` | Record of culled/removed patterns and reasons |

### §6.3 Reference Frameworks

| File | Purpose |
|---|---|
| `K014749_APQC PCF...xlsx` | APQC Process Classification Framework v7.4 — the reference framework used to build the Business domain taxonomy. The PCF was studied and abstracted, not copied — patterns are clean-room original work. |

---

## §7 Reading Paths

Not everyone needs to read everything. Here are the recommended reading paths for different roles:

### §7.1 The Newcomer — "What is this?"

1. **This document** (you are here) — the map
2. **COMMONS_ENGINEERING_MANIFEST** — the philosophy
3. **One domain manifest** (whichever domain interests you most) — the application
4. **PATTERN_SPEC §1–§3** — what a pattern looks like

### §7.2 The AI Agent — "I'm starting a session"

1. **COMMONS_ENGINEERING_ARCHITECTURE §0** — the Boot Protocol (read first, always)
2. **This document** — the full BoK map
3. **COMMONS_TAXONOMY_MANIFEST** — the gravitational architecture (governs all classification decisions)
4. **PATTERN_SPEC v8.2** — the format standard (governs all pattern writing)
5. **PATTERN_PIPELINE_SPEC** — the enrichment process (if doing pipeline work)
6. **Relevant domain manifest** — if doing domain-specific work

### §7.3 The Practitioner — "I want to use patterns"

1. **This document** — the map
2. **COMMONS_ENGINEERING_MANIFEST** — the field you are entering
3. **Your domain manifest** (Life, Business, Urban, or Ecology) — your terrain
4. **COMMONS_BLUEPRINT_MANIFEST** — the design tool (the 9-layer Blueprint)
5. **COMMONS_ENGINEER_MANIFEST** — your development path
6. **The pattern library** — browse `_patterns/{your domain}/`

### §7.4 The Developer — "I want to build"

1. **COMMONS_ENGINEERING_ARCHITECTURE** — the platform architecture (start with §0, read fully)
2. **This document** — the BoK map
3. **PATTERN_SPEC v8.2** — the format you are building for
4. **PATTERN_PIPELINE_SPEC** — the pipeline you are extending
5. **COMMONS_TAXONOMY_MANIFEST** — the classification system your code must respect

### §7.5 The Consultant — "I want to deploy patterns with clients"

1. **This document** — the map
2. **COMMONS_ENGINEERING_MANIFEST** — the field
3. **COMMONS_INCUBATOR_MANIFEST** — the deployment model
4. **Your domain manifest** — your terrain
5. **COMMONS_BLUEPRINT_MANIFEST** — the design artefact you will use with clients
6. **COMMONS_ENGINEER_MANIFEST** — the practitioner arc (you are walking it)
7. **COMMONS_ENGINEERING_IMPACT_MANIFEST** — how to measure what you do

### §7.6 The Lighthouse Builder — "I want to produce briefings"

1. **This document** — the map
2. **LIGHTHOUSE_BUSINESS_SPEC v1.0** — the briefing format (non-negotiable)
3. **BUSINESS_ENGINEERING_MANIFEST** — the domain context
4. **COMMONS_TAXONOMY_MANIFEST §3** — the 13 Business value streams
5. **PATTERN_SPEC v8.2 §4** — the commons assessment scoring (shared between patterns and lighthouses)
6. Browse `_lighthouses/business/` for existing briefings as reference

### §7.7 The Contributor — "I want to add patterns"

1. **This document** — the map
2. **PATTERN_SPEC v8.2** — the format (non-negotiable)
3. **COMMONS_TAXONOMY_MANIFEST** — the classification system (where does your pattern sit?)
4. **PATTERN_PIPELINE_SPEC** — the process your pattern will go through
5. **Your domain manifest** — the terrain your pattern serves

---

## §8 The Gravitational Model — A Primer

For the full treatment, read `COMMONS_TAXONOMY_MANIFEST.md`. Here is the essential mental model:

The pattern library is not a filing cabinet. It is a **gravitational field**.

**Two forces:**
- **Centripetal** (Orbit 0 pulls inward) — toward unity, first principles, universality
- **Centrifugal** (Orbits 4–5 pull outward) — toward specificity, domain expertise, the gravity of extraction

**Six orbits:**
- **0 Singularity** — the source (7 patterns)
- **1 Principle** — first principles & practices (~19 candidates, growing)
- **2 Commons** — cross-domain patterns visible from every scale
- **3 Bridge** — domain-anchored but reaching across domains
- **4 Domain** — the mechanical substrate, domain-specific, clean room (~26,000 patterns)
- **5 Edge** — incoming, unvalidated, the frontier

**Four domain scales:**
- **Life** — the organism (the self as living system)
- **Business** — the enterprise (any value-creation system)
- **Urban** — the settlement (cities, towns, neighbourhoods)
- **Ecology** — the biosphere (ecosystems, watersheds, bioregions)

**The 4×4 matrix:** Four Universal Dimensions × Four Domain Scales = the complete taxonomy. Every pattern can be located in this matrix.

| # | Technical Field | Human Display (Overlay) |
|---|---|---|
| 1 | `purpose` | Definition & Purpose |
| 2 | `agents` | Participation & Relationship |
| 3 | `offers` | Proposition & Exchange |
| 4 | `operations` | Production & Resilience |

Technical field names remain in pattern YAML, scripts, and schemas. Paired overlay names appear in education, website, and human-facing materials.

**The clean room principle:** All patterns are original, IP-free work. Sections 1–5 are clean room. Section 6 (Sources) may contain fair-use references with proper attribution.

---

## §9 Governance

### §9.1 Canonical Hierarchy

When documents disagree, resolution follows this hierarchy:

1. **COMMONS_TAXONOMY_MANIFEST** — governs all classification and structural decisions
2. **PATTERN_SPEC v8.2** — governs all pattern format decisions
3. **LIGHTHOUSE_BUSINESS_SPEC v1.0** / **LIGHTHOUSE_URBAN_SPEC** — govern lighthouse briefing format decisions
4. **Domain Manifests** — govern domain-specific interpretation
5. **PATTERN_PIPELINE_SPEC** — governs pipeline process
6. **COMMONS_ENGINEERING_ARCHITECTURE** — governs platform decisions
7. **Scripts** — implement the above; if a script contradicts a spec, the spec wins

### §9.2 Versioning

- Manifests carry version numbers in their headers (minimum v1.0 for all shipped documents)
- PATTERN_SPEC is at **v8.2** (the long-running pattern format standard)
- Architecture doc is at **v2.0**
- All documents are living documents — subject to eternal iteration
- Major version changes require explicit documentation in changelogs

### §9.3 Working Model

All content is licensed under **CC-BY-SA-4.0**. No content enters the Body of Knowledge without human review and explicit approval. The knowledge commons is a collaboration, not a delegation.

---

## §10 What Is Not Yet Here

The BoK is incomplete. The following are known gaps as of March 2026:

| Gap | Status | Priority |
|---|---|---|
| **Lighthouse library** — the coastline of organisational briefings that connect patterns to real-world enterprises, cities, and ecosystems | LIGHTHOUSE_BUSINESS_SPEC v1.0 drafted; first briefings in production | Critical |
| **Orbit 1 patterns** — the 19 First Principles & Practices need to be written as full v8.2 patterns | Candidates identified; not yet written | High |
| **Ecology domain patterns** — only 2 patterns exist; the domain needs stub generation and enrichment at scale | Taxonomy spreadsheet exists; generation not yet run | High |
| **Cross-domain taxonomy** — Urban, Life, and Ecology do not yet have the detailed functional domain mapping that Business has | Domain taxonomy spreadsheets exist but are less mature | Medium |
| **Orbit 2–3 formal separation** — GraphRAG is surfacing cross-domain and bridge patterns, but they are not yet formally classified at Orbit 2 or 3 | Emerging from GraphRAG analysis | Medium |
| **Commons-OS migration** — ~1,598 unique legacy patterns from the Commons-OS GitHub repository need migration to v8.2 format | Migration plan exists; script not yet written | Medium |
| **Value Stream Family naming** — the value stream hierarchy (Stakeholder → Value Proposition → Journey → Touchpoint → Valuestream → Capability → Solution → Organisation) needs formal domain-to-family mapping beyond Business | Described in Taxonomy Manifest; not yet operationalised | Low |
| **Hugo site** — the public-facing site for pattern browsing and search | Architecture described; not yet deployed | Low |

---

*COMMONS ENGINEERING — BODY OF KNOWLEDGE v1.0*
*Commons Engineering is licensed under CC-BY-SA-4.0*
*Distributed by cloudsters*
