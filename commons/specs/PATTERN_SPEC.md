# Pattern Specification (v8.2)

**Version:** 8.2
**Status:** Definitive Specification
**Companion:** COMMONS_TAXONOMY_MANIFEST.md (the gravitational architecture)

---

## 1. Purpose: A Language for Stewards

This specification defines the format for patterns in the Commons Engineering library. Its purpose is to provide a shared language for **Cognitive Systems Builders**—the intrapreneurs, entrepreneurs, and systems thinkers designing the resilient, living systems of the Cognitive Age.

Following this spec ensures that every pattern is not just a document, but a tool: a legible, repeatable, and machine-readable artifact that helps you make your systems thinking visible, influential, and effective.

---

## 2. The Core Principle: Write Once, Render Richly

The source of truth (the Markdown file) is optimized for the **author**, while the rendered web page is optimized for the **reader**. We achieve this by keeping the author-written body focused on the core narrative, and then programmatically injecting machine-readable data from the frontmatter into the page at build time.

-   **Author Focus:** Write the story (Context, Problem, Solution, etc.) in a clear, narrative flow that makes the reader feel the life of the system.
-   **Machine Focus:** Structure all graph data, metadata, and relationships in the YAML frontmatter.
-   **Build Process:** A build script reads the frontmatter and renders it as rich, human-readable components on the page (e.g., a visual score card for the Commons Alignment, a dynamic list of Related Patterns).

This eliminates content duplication, ensures data consistency, and keeps the authoring experience clean and focused.

---

## 3. The Architectural Logic: Gravity & Orbit

To manage a library of 100,000+ patterns, we move from a simple hierarchical graph to a physics-based **Orbital Model**. Every pattern exists at a specific **Orbital Layer** (its distance from first principles) and is pulled toward one or more **Gravitational Hubs** (its centers of gravity).

-   **Inward Flow (Centripetal):** As patterns move toward the core (from Orbit 4 to Orbit 0), specific solutions **distill** into universal principles.
-   **Outward Flow (Centrifugal):** As principles move toward the periphery (from Orbit 0 to Orbit 4), they **manifest** as specific, contextualized solutions.

This architecture allows for a more nuanced, scalable, and queryable graph that reflects the complex, multi-faceted nature of real-world systems.

| Orbital Layer | Name | Character | Example |
|:---|:---|:---|:---|
| 0 | **SINGULARITY** | Compressed potential. The centre of gravity. One point from which all patterns emerge. | `the-singularity` |
| 1 | **PRINCIPLES** | First Principles & Practices. The bones. Forces the structure. <100 patterns. | `the-commons` |
| 2 | **COMMONS** | The attractor state. Resilient, collaborative, just, systematic value creation. | `commons-blueprint` |
| 3 | **TRANSVERSALS** | Universal cross-domain patterns. Knowledge, communication, governance. Living tissue woven through multiple domains simultaneously. | `polycentric_governance` |
| 4 | **DOMAINS** | Mechanical substrate. Dry, process-oriented operating patterns. Clean room generated. | `transparent-ledger` |
| 5 | **EDGE** | Raw frontier. Unvalidated signals, historic substrate, emerging anomalies. | `new-experimental-idea` |

> **The gravitational dynamic:** Orbit 0 (SINGULARITY) creates the force. Orbit 1 (PRINCIPLES) forces the structure. Orbit 2 (COMMONS) is the attractor state. Orbit 3 (TRANSVERSALS) weaves across domains. Orbit 4 (DOMAINS) is the mechanical baseline. Orbit 5 (EDGE) is the raw frontier. Centripetal force (Orbit 0) pulls inward toward unity. Centrifugal force (Orbits 4–5) pulls outward toward extraction and specialisation. Every pattern lives in this tension.

---

## 4. The Definitive Frontmatter (v8.2)

The frontmatter is organized into 8 functional groups, including the new **Group 0** for architectural positioning.

```yaml
---
# ═══════════════════════════════════════════════════════════════════
# GROUP 0: ARCHITECTURAL POSITION (The Gravity Well)
# ═══════════════════════════════════════════════════════════════════
id: pat_01h8x4e1gq7r9d1z2x3c4v5b6n
orbital_layer: 4
sector: "Urban"                   # Life, Ecology, Urban, Business, or Universal
gravitational_hubs:               # The "Centers of Gravity" this pattern orbits
  - hub_id: "core_resilience"     # ID of an Orbit 0-2 Principle
    influence: 0.8                # Strength of connection (0.0 - 1.0)
  - hub_id: "urb_metabolism"      # ID of an Orbit 3 Domain Archetype
    influence: 0.5

# ═══════════════════════════════════════════════════════════════════
# GROUP 1: CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════
slug: transparent-ledger
title: "Transparent Ledger"
aliases: ["Open Book Management", "Public Audit"]
summary: >-
  A pattern for establishing collective trust by making operational data
  and financial records accessible and auditable by all relevant stakeholders.

# ═══════════════════════════════════════════════════════════════════
# GROUP 2: CONTEXTUAL TRANSLATION (The Navigator Engine)
# ═══════════════════════════════════════════════════════════════════
context_labels:
  corporate: "Open Book Management"
  government: "Public Account Auditing"
  activist: "Radical Transparency"
  tech: "Public Blockchain Ledger"

# ═══════════════════════════════════════════════════════════════════
# GROUP 3: ONTOLOGY & VITALITY (The RAG Fuel)
# ═══════════════════════════════════════════════════════════════════
ontology:
  domain: finance
  cross_domains: [governance, technology]
  search_hints:
    primary_tension: "Information Asymmetry vs. Collective Trust"
    vector_keywords: ["accountability", "ledger", "auditability", "commons"]
  commons_assessment:
    stakeholder_architecture: 5
    value_creation: 4
    resilience: 5
    ownership: 5
    autonomy: 4
    composability: 3
    fractal_value: 5
    vitality: 4.5
    vitality_reasoning: >-
      Scores highly because it directly enables feedback loops and
      adaptation, which are the core mechanisms of any living system.
    overall_score: 4.4

# ═══════════════════════════════════════════════════════════════════
# GROUP 4: LIFECYCLE & CONFIDENCE
# ═══════════════════════════════════════════════════════════════════
lifecycle:
  status: stable
  version: 1.2
  confidence: 3 # 1: Experimental, 2: Observed, 3: Proven/Stable

# ═══════════════════════════════════════════════════════════════════
# GROUP 5: RELATIONSHIPS (Human-Curated Graph)
# ═══════════════════════════════════════════════════════════════════
relationships:
  manifests_as:                     # Centrifugal (Moving toward Specifics)
    - typeid: pat_01h9y5f2hr8s0e2z3x4c5v6b7m  # Stable reference (survives renames)
      slug: subscription-model                   # Human-readable label
      weight: 0.9                                # Relationship strength (0.0-1.0)
      source: curated                            # curated | migration | graphrag
  enables: []
  requires: []
  alternatives: []
  complementary: []
  tools: []

# ═══════════════════════════════════════════════════════════════════
# GROUP 6: GRAPH GARDEN (Machine-Written Graph)
# ═══════════════════════════════════════════════════════════════════
graph_garden:
  last_pruned: 2026-02-25
  entities: []
  communities: []
  inferred_links: [] # Populated by GraphRAG engine

# ═══════════════════════════════════════════════════════════════════
# GROUP 7: PROVENANCE
# ═══════════════════════════════════════════════════════════════════
contributors: ["higgerix", "cloudsters"]
sources: []
license: CC-BY-SA-4.0
attribution: "commons.engineering by cloudsters, https://cloudsters.net"
---
```

---

## 5. The Definitive Body Structure (v8.2)

The body is the author's canvas. It contains **8 author-written sections**. The only change from v7.1 is the addition of a "Lineage" prompt in Section 1 to connect the narrative to the orbital model.

```markdown
> A one-sentence summary of the pattern's core idea.

> [!NOTE] Confidence Rating: ★★★ (High)
> This rating reflects our confidence that this pattern is a good and correct
> solution to the stated problem.

---

### Section 1: Context

*(100–200 words)*

> **Lineage:** This pattern is a specialized manifestation of [Hub ID/Name], primarily serving the [Sector] domain.

Describes the situation or environment in which the problem arises. It should be a concise, narrative paragraph that helps the reader feel the living energy of the context — is this a system that is growing, stagnating, fragmenting, or decaying?

---

### Section 2: Problem

*(100–200 words)*

> **The core conflict is [State the Primary Tension from the frontmatter].**

After the bold problem statement, describe the **forces** at play. Forces are not abstract concepts; they are living tensions experienced by real people in real systems.

---

### Section 3: Solution

*(200–400 words)*

> **Therefore, [State the core instruction of the solution in one bold sentence].**

After the bold solution statement, provide a detailed explanation of the mechanism. Include a diagram if it helps clarify the structure.

---

### Section 4: Implementation

*(300–500 words)*

Provide concrete, actionable steps for implementing the solution. This section should feel like a practical guide, not a theoretical treatise. Frame the steps as acts of cultivation — tending, protecting, and growing the living system.

---

### Section 5: Consequences

*(200–300 words)*

Describe the trade-offs and implications. What new capacities for life does it create? What forms of decay does it make possible if not tended carefully?

---

### Section 6: Known Uses

*(200–300 words)*

Provide at least two real-world examples of this pattern in action. Tell the stories of these living systems — don't just state facts.

---

### Section 7: Cognitive Era

*(150–250 words)*

How does this pattern change in the Cognitive Age? How does it interact with AI, autonomous agents, and distributed intelligence?

---

### Section 8: Vitality

*(200–300 words)*

This is the explicit diagnostic section. What does vitality look like in a system that uses this pattern? What are the signs of life? Conversely, what does decay look like? This section should provide a clear, actionable diagnostic for assessing the health of the pattern in practice.
```

---

## 6. Validation Rules

To ensure the long-term integrity of the graph, the following rules must be enforced by a validation script (`scripts/validate_entity.py`) in the CI/CD pipeline:

1.  **Anchor Rule:** Every pattern in Orbit 3 or 4 must link to at least one `gravitational_hub` in Orbit 0, 1, or 2.
2.  **Sector Consistency:** Patterns in a specific `sector` (e.g., Urban) must provide a `context_label` for that same sector.
3.  **Vitality Minimum:** Patterns with a `vitality` score below 2.0 are automatically flagged for "Decomposition Review" (a process for archival or refactoring).
4.  **Hub Existence:** All `hub_id` values must correspond to an existing pattern ID in the library.

---

## 7. Workflow

1.  **Generate ID:** `python3 scripts/generate_typeid.py`
2.  **Create File:** `cp _templates/pattern_v8.md _patterns/{slug}.md`
3.  **Fill Content:** Complete all YAML fields and the 8 body sections.
4.  **Validate:** `python3 scripts/validate_entity.py _patterns/{slug}.md`
5.  **Commit:** `git add _patterns/{slug}.md && git commit -m "feat(patterns): Add pattern {title}"`

---

*PATTERN SPECIFICATION v8.2*
*Commons Engineering is licensed under CC-BY-SA-4.0*
*Distributed by cloudsters*
