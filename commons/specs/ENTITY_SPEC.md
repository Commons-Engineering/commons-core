# Entity Specification (v1.0)

**Version:** 1.0
**Status:** Draft Specification
**Companion:** PATTERN_SPEC.md (the pattern format), COMMONS_TAXONOMY_MANIFEST.md (the gravitational architecture)

---

## 1. Purpose: A Language for Business Objects

This specification defines the format for **entity definitions** in the Commons Engineering library. Where patterns describe reusable knowledge (how, why, when), entities describe **business objects** (what, who, structure, relationships). An entity is any noun that capabilities act upon: a Customer, a Journal Entry, a Strategy, a Work Order.

Entity definitions are **archetypes** — they describe what a class of business object IS, what capabilities act on it, and where it lives in the four-dimensional model. When an entity definition is **activated** in a fork's registry, it becomes a living instance with concrete data.

Following this spec ensures that every entity definition is:
- **Graph-compatible** with patterns (same Groups 0, 5, 6 — same GraphRAG emulation)
- **Dimensionally positioned** (every entity has a measurable gravitational pull toward D1–D4)
- **Activatable** (every definition can be instantiated in the fork's registry)

---

## 2. The Core Principle: Definition and Instance

Every entity has two lives:

| State | Where | Format | Purpose |
|---|---|---|---|
| **Definition** (archetype) | `extensions/{provider}/{pack}/entities/` | Markdown (this spec) | What this class of entity IS |
| **Instance** (activated) | `instance/registry/entities/{dimension}/` | YAML | What THIS entity is in OUR context |

The definition is upstream knowledge — it travels with the pack. The instance is sovereign — it belongs to the fork. The agent reads definitions to understand what entities exist; it reads instances to understand the current state of the commons.

---

## 3. Entity Types

Every entity belongs to one of four types. These types correlate with the four dimensions — not by rule, but by gravitational tendency:

| Type | Code | Description | Dimensional Gravity |
|---|---|---|---|
| **Master Data** | `master` | Long-lived reference objects. The nouns that other objects point to. | D3 Proposition + D4 Production |
| **Transactional** | `transactional` | Lifecycle objects with state transitions. The events that move the system. | D4 Production + D1 Purpose |
| **Governance** | `governance` | Rules and structures. The constraints that shape behaviour. | D1 Purpose |
| **Intelligence** | `intelligence` | Knowledge objects. The insights that inform decisions. | D2 Participation + D3 Proposition |

> **Why four types?** Because the correlation between entity type and dimension is architecturally significant. D1 owns governance entities (19 of 25). D4 owns transactional entities (12 of 30). D3 owns master data (7 of 25). D2 owns intelligence (5 of 15). This is not a coincidence — it is the structural signature of enterprise architecture.

---

## 4. The Definitive Frontmatter (v1.0)

The frontmatter is organised into 9 functional groups. Groups 0–7 mirror the PATTERN_SPEC to ensure graph compatibility. Group 8 is entity-specific.

```yaml
---
# ═══════════════════════════════════════════════════════════════════
# GROUP 0: ARCHITECTURAL POSITION (The Gravity Well)
# ═══════════════════════════════════════════════════════════════════
id: ent_01h8x4e1gq7r9d1z2x3c4v5b6n    # TypeID prefix: ent_ (not pat_)
orbital_layer: 2                         # Pack entities live at Orbit 2 (Commons)
sector: "Business"                       # Life, Ecology, Urban, Business, or Universal
gravitational_hubs:
  - hub_id: "core_resilience"
    influence: 0.6

# ═══════════════════════════════════════════════════════════════════
# GROUP 1: CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════
slug: customer
title: "Customer"
aliases: ["Client", "Buyer", "Account"]
entity_type: master                      # master | transactional | governance | intelligence
summary: >-
  The party who acquires goods, services, or value from the commons.
  A role of the universal Partner entity, not a separate master record.

# ═══════════════════════════════════════════════════════════════════
# GROUP 2: CONTEXTUAL TRANSLATION (The Navigator Engine)
# ═══════════════════════════════════════════════════════════════════
context_labels:
  corporate: "Customer Account"
  cooperative: "Member"
  commons: "Participant"
  tech: "User"

# ═══════════════════════════════════════════════════════════════════
# GROUP 3: ONTOLOGY & DIMENSIONAL DENSITY
# ═══════════════════════════════════════════════════════════════════
ontology:
  domain: proposition
  cross_domains: [purpose, production]
  search_hints:
    primary_tension: "Individual Need vs. Collective Value Creation"
    vector_keywords: ["customer", "buyer", "account", "relationship", "revenue"]
  dimensional_density:                   # Capability count per dimension
    d1: 2                                # Financial capabilities (credit, invoicing)
    d2: 0
    d3: 9                                # Primary home: proposition & exchange
    d4: 0
  primary_dimension: d3                  # Dimension with highest density
  concentration: 0.82                    # Primary density / total density

# ═══════════════════════════════════════════════════════════════════
# GROUP 4: LIFECYCLE & CONFIDENCE
# ═══════════════════════════════════════════════════════════════════
lifecycle:
  status: stable
  version: 1.0
  confidence: 3                          # 1: Experimental, 2: Observed, 3: Proven/Stable
states:                                  # State machine (required for transactional, optional for others)
  - name: prospect
    description: "Identified but not yet transacting"
  - name: active
    description: "Actively transacting"
  - name: dormant
    description: "No recent transactions"
  - name: churned
    description: "Formally ended relationship"
transitions:
  - from: prospect
    to: active
    trigger: "First order placed"
  - from: active
    to: dormant
    trigger: "No transaction for defined period"
  - from: dormant
    to: active
    trigger: "New transaction"
  - from: dormant
    to: churned
    trigger: "Formal exit or write-off"

# ═══════════════════════════════════════════════════════════════════
# GROUP 5: RELATIONSHIPS (Human-Curated Graph)
# ═══════════════════════════════════════════════════════════════════
relationships:
  # --- Entity-to-Entity relationships ---
  is_role_of:                            # This entity is a role/view of another entity
    - typeid: ent_partner
      slug: partner-party
      weight: 1.0
      source: curated
  composed_of:                           # Sub-entities or child records
    - typeid: ent_address
      slug: address-contact
      weight: 0.9
      source: curated
  depends_on: []                         # Entities that must exist first
  produces: []                           # Entities created by this entity's lifecycle

  # --- Entity-to-Pattern relationships ---
  participates_in:                       # Value Stream Families this entity appears in
    - typeid: pat_lead_to_user
      slug: lead-to-user
      weight: 0.9
      source: curated
    - typeid: pat_discover_to_usage
      slug: discover-to-usage
      weight: 0.7
      source: curated
  governed_by: []                        # Governance patterns that constrain this entity

  # --- Capabilities (Orbit 4 Patterns that act on this entity) ---
  acted_upon_by:                         # Hard graph edges to Capability Patterns
    - typeid: pat_01h9x1a2bc3d4e5f6g7h  # Links to the Capability Pattern definition
      slug: cap-survey-customer-needs    # Human-readable — the Pattern's own slug
      weight: 1.0
      source: curated
    - typeid: pat_01h9x2b3cd4e5f6g7h8
      slug: cap-segment-market
      weight: 0.9
      source: curated
    - typeid: pat_01h9x3c4de5f6g7h8i9
      slug: cap-manage-customer-accounts
      weight: 0.9
      source: curated
    - typeid: pat_01h9x4d5ef6g7h8i9j0
      slug: cap-invoice-customer
      weight: 0.8
      source: curated
    - typeid: pat_01h9x5e6fg7h8i9j0k1
      slug: cap-collect-receivables
      weight: 0.8
      source: curated
    # Value stream and dimension are NOT repeated here — they live in the
    # Capability Pattern itself. The agent resolves them by following the edge.
    # This keeps the YAML DRY and the graph authoritative.

# ═══════════════════════════════════════════════════════════════════
# GROUP 6: GRAPH GARDEN (Machine-Written Graph)
# ═══════════════════════════════════════════════════════════════════
graph_garden:
  last_pruned: null
  entities: []
  communities: []
  inferred_links: []                     # Populated by GraphRAG engine

# ═══════════════════════════════════════════════════════════════════
# GROUP 7: PROVENANCE
# ═══════════════════════════════════════════════════════════════════
contributors: ["higgerix", "cloudsters"]
sources:
  - "APQC PCF v7.4 (structural inspiration)"
  - "Odoo 17 ORM: res.partner"
  - "ERPNext v15: Customer"
license: CC-BY-SA-4.0
attribution: "commons.engineering by cloudsters, https://cloudsters.net"

# ═══════════════════════════════════════════════════════════════════
# GROUP 8: REGISTRY ACTIVATION (Entity-Specific)
# ═══════════════════════════════════════════════════════════════════
registry:
  activation_path: "instance/registry/entities/{primary_dimension}/{slug}.yml"
  instance_fields:
    required:
      - name                             # The local name (e.g., "Tchibo Endkunde")
      - status                           # Current state from the state machine
      - owner                            # Responsible steward or team
    optional:
      - systems                          # Systems that manage this entity (e.g., ["SAP-CRM", "Webshop"])
      - contacts                         # Key contacts for this entity class
      - custom_fields                    # Fork-specific extensions
      - notes                            # Free-form context
  default_state: "prospect"              # Initial state when activated
---
```

---

## 5. The Definitive Body Structure (v1.0)

The body follows the same 8-section structure as the PATTERN_SPEC. This ensures that entity definitions can be read, searched, and rendered by the same tooling as patterns. The prompts are adapted for entity description rather than solution narrative.

```markdown
> A one-sentence description of what this entity is and why it matters.

> [!NOTE] Confidence Rating: ★★★ (High)
> This rating reflects our confidence that this entity is correctly identified,
> well-bounded, and architecturally positioned.

---

### Section 1: Context

*(100–200 words)*

> **Lineage:** This entity orbits [Hub ID/Name] and primarily serves the [Dimension] dimension.

Describe the organisational context in which this entity exists. What role does it play in value creation? Which stakeholders interact with it? How does it relate to the value streams it participates in?

---

### Section 2: Problem

*(100–200 words)*

> **The core tension is [State the Primary Tension from the frontmatter].**

What happens when this entity is poorly defined, duplicated, or missing? What organisational dysfunction does unclear entity governance produce? Describe the forces that make this entity architecturally significant.

---

### Section 3: Structure

*(200–400 words)*

> **Therefore, [describe the essential structure of this entity in one sentence].**

Define the entity's key attributes, its identity (what makes two instances the same or different), its boundaries (what is inside and outside this entity), and its invariants (rules that must always hold). Include the state machine diagram for transactional entities.

---

### Section 4: Implementation

*(300–500 words)*

Describe how this entity is typically realised in systems. Where does it live — Fabric MCP, Blueprint MCP, or both? What are the common implementation patterns? What are the integration challenges when this entity spans multiple dimensions?

Include a table of known realisations:

| System | Class / DocType | Notes |
|---|---|---|
| Odoo | `res.partner` | Universal party model — customer is a flag |
| ERPNext | `Customer` | Separate DocType linked to Address, Contact |
| SAP | `BP` (Business Partner) | Central master since S/4HANA |

---

### Section 5: Consequences

*(200–300 words)*

What are the governance implications of this entity? What happens when it is well-managed versus neglected? What cross-dimensional tensions does it create? For cross-dimensional entities (those with significant density in 2+ dimensions), describe the integration seams and handoff challenges.

---

### Section 6: Known Uses

*(200–300 words)*

Provide at least two real-world examples of how this entity manifests in actual organisations. Tell the story of how this entity's governance created or destroyed value.

---

### Section 7: Cognitive Era

*(150–250 words)*

How does this entity change in the Cognitive Age? Can an agent manage its lifecycle autonomously? What new capabilities become possible when the entity is governed by an AI steward? What risks emerge?

---

### Section 8: Vitality

*(200–300 words)*

What does vitality look like for this entity? A vital Customer entity: clean, deduplicated, role-aware, connected to its value streams, governed by clear policies, measured by meaningful KPIs. A decaying Customer entity: duplicated across systems, role-confused, disconnected from the value streams it participates in, measured only by revenue.

Provide a diagnostic checklist for assessing entity health.
```

---

## 6. Validation Rules

To ensure graph integrity and registry compatibility, the following rules must be enforced:

1. **TypeID Rule:** Entity IDs must use the `ent_` prefix (not `pat_`). This distinguishes entities from patterns in the graph.
2. **Type Rule:** Every entity must declare exactly one `entity_type` from: `master`, `transactional`, `governance`, `intelligence`.
3. **Density Rule:** `dimensional_density` must be present with values for all four dimensions (d1–d4). Values are non-negative integers.
4. **Primary Dimension Rule:** `primary_dimension` must match the dimension with the highest density value. Ties are resolved by the author.
5. **State Machine Rule:** Entities of type `transactional` must define at least two `states` and at least one `transition`. Other types may optionally define states.
6. **Anchor Rule:** Every entity at Orbit 2+ must link to at least one `gravitational_hub` in Orbit 0 or 1.
7. **Capability Rule:** Every entity must declare at least one hard edge in `relationships.acted_upon_by`, linking to existing Capability Pattern TypeIDs.
8. **Registry Rule:** Every entity must define `registry.activation_path` and `registry.instance_fields.required`.
9. **Sector Consistency:** Entities in a specific `sector` must provide a `context_label` for that sector.

---

## 7. Registry Instance Format

When an entity definition is **activated** in a fork, the agent creates a YAML instance file at the path specified in `registry.activation_path`. This instance file has a minimal, fork-specific format:

```yaml
# instance/registry/entities/proposition/customer.yml
---
entity_ref: ent_01h8x4e1gq7r9d1z2x3c4v5b6n   # Points back to the definition
name: "Tchibo Endkunde"                          # Local name for this entity
status: active                                   # Current state from state machine
owner: "Proposition Agent"                       # Responsible steward
activated: 2026-03-15                            # When this entity was activated
systems:                                         # Systems that manage this entity
  - name: "SAP-CRM"
    role: "System of Record"
    status: "retiring"
  - name: "Hunter-Webshop"
    role: "Primary Touchpoint"
    status: "active"
contacts:                                        # Key contacts
  - name: "Hannah (Persona)"
    role: "Primary Persona"
custom_fields:                                   # Fork-specific extensions
  segment: "B2C"
  loyalty_program: true
notes: >-
  Zukünftig kundensegment/profil-spezifische Merkmale berücksichtigen.
---
```

The instance file is intentionally minimal. It captures what is **specific to this fork** — not what is universally true about the entity class (which lives in the definition).

---

## 8. Relationship to Other Specifications

| Specification | Relationship |
|---|---|
| **PATTERN_SPEC** | Sibling specification. Entities share Groups 0–7 with patterns for graph compatibility. Entities add Group 8 (Registry Activation) and replace `commons_assessment` with `dimensional_density`. |
| **PACK_SPEC** | Entity definitions are delivered inside extension packs alongside patterns and collections. |
| **COMMONS_OS_SPEC** | The OS spec defines the three-layer architecture (commons/extensions/instance) in which entity definitions and instances live. |
| **COMMONS_MCP_ARCHITECTURE_SPEC** | MCP tools navigate entities alongside patterns. Future tools: `find_entities`, `get_entity`, `activate_entity`. |
| **COMMONS_TAXONOMY_MANIFEST** | The gravitational architecture (orbits, sectors) applies equally to entities and patterns. |

---

## 9. Design Decisions

| Decision | Rationale |
|---|---|
| **Entities are not patterns** | Patterns describe reusable knowledge (how, why, when). Entities describe business objects (what, who, structure). Different species, same habitat. |
| **Same Groups 0–7 as patterns** | Graph compatibility. The same tools (find, traverse, lineage) work for both. The same GraphRAG emulation includes both. |
| **Four entity types** | The correlation between entity type and dimension is architecturally significant and too valuable to lose in a binary (Registry/Ledger) classification. |
| **Dimensional density over commons assessment** | Patterns are assessed for commons alignment (stakeholder architecture, resilience, etc.). Entities are assessed for dimensional gravity — where they live in the four-dimensional model. |
| **State machine for transactional entities** | Transactional entities have lifecycles. A Sales Order moves from draft to confirmed to fulfilled to closed. This state machine is the entity's most defining characteristic. |
| **Registry activation as Group 8** | The bridge between definition (knowledge) and instance (operations). No other knowledge object has this duality — it is what makes entities unique. |
| **Capabilities as hard graph edges, not strings** | Capabilities are Orbit 4 Patterns with their own TypeIDs. The entity links to them via `acted_upon_by` with TypeID references, creating unbreakable graph edges. Value stream and dimension are NOT repeated in the entity — the agent resolves them by following the edge to the Capability Pattern. This keeps the YAML DRY and the graph authoritative. |
| **Orbit 2 for pack entities** | Pack entities are archetypes — they describe universal business object classes. Orbit 2 (Commons) is the attractor state for archetypes. Instance-specific entity variations would be Orbit 4-5. |
| **Definition in Markdown, instance in YAML** | Definitions are rich documents (8 sections of narrative). Instances are structured data (name, status, systems). Different purposes, different formats. |

---

*ENTITY SPECIFICATION v1.0*
*Commons Engineering is licensed under CC-BY-SA-4.0*
*Distributed by cloudsters*
