---
# ═══════════════════════════════════════════════════════════════════
# GROUP 0: ARCHITECTURAL POSITION (The Gravity Well)
# ═══════════════════════════════════════════════════════════════════
id: pat_XXXXXXXXXXXXXXXXXXXXXXXXXX    # Generate via scripts/generate_typeid.py
orbital_layer: 4                       # 0=Singularity, 1=Principles, 2=Commons, 3=Transversals, 4=Domains, 5=Edge
sector: "Business"                     # Life | Ecology | Urban | Business | Universal
gravitational_hubs:                    # Orbit 0-2 patterns this pattern orbits
  - hub_id: ""                         # TypeID of an Orbit 0-2 pattern
    influence: 0.5                     # Strength of connection (0.0 - 1.0)

# ═══════════════════════════════════════════════════════════════════
# GROUP 1: CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════
slug: pattern-slug-here
title: "Pattern Title Here"
aliases: []
summary: >-
  One to three sentence description of what this pattern is and what
  it achieves for the practitioner.

# ═══════════════════════════════════════════════════════════════════
# GROUP 2: CONTEXTUAL TRANSLATION (The Navigator Engine)
# ═══════════════════════════════════════════════════════════════════
context_labels:
  corporate: "Corporate Context Label"
  government: "Government Context Label"
  activist: "Activist Context Label"
  tech: "Tech Context Label"

# ═══════════════════════════════════════════════════════════════════
# GROUP 3: ONTOLOGY & VITALITY (The RAG Fuel)
# ═══════════════════════════════════════════════════════════════════
ontology:
  domain: domain-slug
  cross_domains: []
  commons_domain:
    - commons-engineering
  search_hints:
    primary_tension: "Force A vs. Force B"
    vector_keywords: ["keyword1", "keyword2", "keyword3", "keyword4", "keyword5"]
  commons_vitality:
    stakeholder_architecture: 3.0
    reciprocity: 3.0
    regenerative_capacity: 3.0
    emergent_potential: 3.0
    vitality_score: 3.0
    vitality_reasoning: >-
      Explanation of vitality score in 2-3 sentences. What mechanisms
      create or sustain life? What risks of decay exist?

# ═══════════════════════════════════════════════════════════════════
# GROUP 4: LIFECYCLE & CONFIDENCE
# ═══════════════════════════════════════════════════════════════════
lifecycle:
  status: draft                        # draft | stable | mature | deprecated
  version: 1.0
  confidence: 1                        # 1: Experimental, 2: Observed, 3: Proven/Stable

# ═══════════════════════════════════════════════════════════════════
# GROUP 5: RELATIONSHIPS (Human-Curated Graph)
# ═══════════════════════════════════════════════════════════════════
relationships:
  generalizes_from: []
  specializes_to: []
  enables: []
  requires: []
  alternatives: []
  complementary: []

# ═══════════════════════════════════════════════════════════════════
# GROUP 6: GRAPH GARDEN (Machine-Written Graph)
# ═══════════════════════════════════════════════════════════════════
graph_garden:
  entities: []
  communities: []
  inferred_links: []                   # Populated by GraphRAG engine

# ═══════════════════════════════════════════════════════════════════
# GROUP 7: PROVENANCE
# ═══════════════════════════════════════════════════════════════════
contributors: []
sources: []
license: CC-BY-SA-4.0
attribution: "commons.engineering by cloudsters"
---

> One memorable sentence that captures the essential insight of this pattern.

> [!NOTE] Confidence Rating: ★★ (Medium)
> This rating reflects our confidence that this pattern is a good and correct
> solution to the stated problem.

---

### Section 1: Context

*(100–200 words)*

> **Lineage:** This pattern is a specialized manifestation of [Hub ID/Name], primarily serving the [Sector] domain.

Describe the situation or environment in which this problem arises. Make the
reader feel the living energy of the context — is this a system that is growing,
stagnating, fragmenting, or decaying?

---

### Section 2: Problem

*(100–200 words)*

> **The core conflict is [Primary Tension from frontmatter].**

Describe the forces at play. These are not abstract concepts but lived tensions
experienced by real people in real systems.

---

### Section 3: Solution

*(200–400 words)*

> **Therefore, [core instruction of the solution].**

Explain the mechanism. Include a diagram if it helps clarify the structure.

---

### Section 4: Implementation

*(300–500 words)*

Provide concrete, actionable steps for implementing the solution. Frame the
steps as acts of cultivation — tending, protecting, and growing the living system.

---

### Section 5: Consequences

*(200–300 words)*

Describe the trade-offs and implications. What new capacities for life does it
create? What forms of decay does it make possible if not tended carefully?

---

### Section 6: Known Uses

*(200–300 words)*

Provide at least two real-world examples of this pattern in action. Tell the
stories of these living systems — don't just state facts.

---

### Section 7: Cognitive Era

*(150–250 words)*

How does this pattern change in the Cognitive Age? How does it interact with
AI, autonomous agents, and distributed intelligence?

---

### Section 8: Vitality

*(200–300 words)*

What does vitality look like in a system that uses this pattern? What are the
signs of life? Conversely, what does decay look like? Provide an actionable
diagnostic for assessing the health of the pattern in practice.
