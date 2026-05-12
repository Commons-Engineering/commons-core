# Commons MCP Architecture Specification (v1.0)

**Version:** 1.0
**Status:** Specification
**Companion:** PATTERN_SPEC.md (v8.2), ENGAGEMENT_GRAPH_SPEC.md (v1.0), COMMONS_AGENT_MANIFEST.md (v1.0), COMMONS_OS_SPEC.md

---

## §1 Vision & Principles

### 1.1 The Transformation

The Commons Engineering workshop contains 54,000+ patterns across four domains, 10+ lighthouses, an engagement graph specification, and a gravitational architecture that organises knowledge from singularity (Orbit 0) through principles (Orbit 1) to the raw edge (Orbit 5). Today this knowledge is a structured library — navigable by humans who know where to look, but silent to the rest of the world.

The MCP architecture transforms this library into a **living knowledge service** — the epistemological infrastructure for the resilient transformation of the economy. An AI partner — any AI partner — connected to the commons knowledge via the Model Context Protocol, enabling contextual navigation rather than document browsing. The commons stops being a collection of files and becomes an intelligence that meets people where they are: in their IDE, in their chat window, in their planning session, in their agent workflow.

A system of this scale — 100,000+ patterns, 10,000+ lighthouses — must not be built on short-term hacks. It must be fault-tolerant, asynchronous, highly scalable, and cryptographically traceable.

### 1.2 Why MCP

The Model Context Protocol (MCP) is an open standard for connecting AI models to external data sources and tools. It provides a structured way for any AI model to discover, invoke, and compose tools that operate on external knowledge. MCP is to AI tools what HTTP is to web services: a shared protocol that makes interoperability possible without vendor lock-in.

For Commons Engineering, MCP provides three critical properties:

1. **Model-agnostic.** The commons knowledge works with Claude, GPT, Gemini, Llama, Mistral, or any local model that speaks MCP. The protocol is the interface; the model is the client's choice.
2. **Tool-native.** MCP exposes structured tools, not just text retrieval. This means the AI can navigate the orbital architecture, traverse the pattern graph, route through value streams, and diagnose situations — not just search for keywords in documents.
3. **Composable.** MCP servers can connect to each other. A client's private Blueprint MCP can call the Commons MCP for shared knowledge enrichment. An agent can chain tools: diagnose a situation, find relevant patterns, load the lighthouse, and prescribe an implementation path — all in a single conversation.

### 1.3 Why Not Just RAG?

The workshop knowledge is **structured data** — YAML frontmatter with 8 functional groups, orbital layers, gravitational hubs, commons assessment scores, value stream routing, pattern relationships, lighthouse brightness. This structure is the intelligence. A RAG system would flatten it into text chunks and lose precisely what makes the knowledge navigable.

The MCP architecture preserves structure. RAG becomes one tool among many:

| Capability | RAG Alone | MCP Architecture |
|:---|:---|:---|
| "Find patterns about resilience" | Keyword/semantic search over body text | `find_patterns(query="resilience")` — searches frontmatter fields, ontology, graph topology, AND body text |
| "Show me Orbit 2 commons patterns" | Cannot query by orbital layer | `navigate_orbit(layer=2)` — direct structural query |
| "What patterns does Deutsche Bahn need?" | Might find relevant text | `load_lighthouse(slug="deutsche-bahn")` → reads `relationships.needs` array |
| "Walk the graph from operational-resilience" | Not possible | `traverse_graph(pattern_slug="operational-resilience", depth=2)` — returns typed, weighted edges |
| "All Urban lighthouses using Orbit 1 Resilience patterns" | Not possible | Graph traversal: Cypher query across lighthouse → pattern → hub edges |
| "Navigate Plan to Fulfill for Deutsche Bahn" | Cannot route through value streams | `navigate_value_stream(lighthouse_slug="deutsche-bahn", stream_name="plan-to-fulfill")` |
| "What are the systemic patterns across post-industrial cities?" | Generic text matching | GraphRAG: aggregate graph clusters, find emergent cross-lighthouse patterns |

### 1.4 Core Principles

| Principle | Description |
|:---|:---|
| **The commons IS the product** | The knowledge is freely navigable. The OPEN tier gives full access to all patterns, lighthouses, and the graph. Revenue comes from tools, not from gating knowledge. |
| **Model-agnostic** | Works with any AI that speaks MCP. No vendor lock-in. The client chooses their model. |
| **Structured navigation > document retrieval** | The orbital architecture, value stream routing, and pattern graph are first-class queryable structures, not just text to be searched. |
| **Graph + vectors > flat search** | Hard relations (exemplifies, needs, enables) combined with semantic similarity (vector distance) produce GraphRAG — intelligence that no single document contains. |
| **Client sovereignty** | Client data stays in the client's MCP server. The commons provides shared knowledge; the client owns their context. |
| **Remote-first** | The MCP server is a network service accessible by any AI agent worldwide. Local/offline operation is a bonus, not the primary mode. |
| **Carpenter's joint** | Every interface should be clean, honest, and load-bearing. No decorative API surfaces — every tool does real structural work. |

---

## §2 Architecture Overview

### 2.1 Two-Server Architecture

The system consists of two complementary MCP servers with distinct ownership models:

```
+------------------------------------------------------------------+
|                        AI MODEL (any)                             |
|              Claude / GPT / Gemini / Local LLM                   |
+------------------------------------------------------------------+
        |                                         |
        | MCP Protocol                            | MCP Protocol
        v                                         v
+-------------------+                   +---------------------+
| COMMONS MCP       |                   | BLUEPRINT MCP       |
| (operated by      | <--- enrichment-- | (owned by client)   |
|  cloudsters)      | ---shared know--> |                     |
|                   |     ledge         |                     |
| - Graph DB        |                   | - Private Lighthouse|
| - Vector Index    |                   | - Private Engagement|
| - Pattern Index   |                   | - Pattern Adoption  |
| - Lighthouse Index|                   | - Client Knowledge  |
| - Engagement Store|                   |                     |
+-------------------+                   +---------------------+
```

**Commons MCP** is the shared knowledge server, operated by cloudsters. It contains the full pattern library, all public lighthouses, the pattern graph, and the commons engagement tools. It is the commons — open by design, structured by specification.

**Blueprint MCP** is the client's sovereign server, built by cloudsters but owned and operated by the client (or hosted by cloudsters under a data processing agreement). It contains the client's private lighthouse data (version 2+), their private engagement graph, their pattern adoption map, and connects back to the Commons MCP for shared knowledge enrichment.

### 2.2 Data Flow

```
Public Knowledge (commons)          Private Knowledge (client)
==========================          ==========================

100,000+ Patterns ────────────┐
10,000+ Lighthouses (public) ─┤
Pattern Graph ────────────────┼──> COMMONS MCP ──> AI Model <── BLUEPRINT MCP
Value Stream Routing ─────────┤         ^                            |
Vector Embeddings ────────────┘         |                            |
                                        └── enrichment ──────────────┘
                                       (shared patterns inform
                                        private diagnostics)

                                      Private Lighthouse (v2+) ──────┐
                                      Private Engagement Graph ──────┤
                                      Pattern Adoption Map ──────────┼──> BLUEPRINT MCP
                                      Client Knowledge Graph ────────┘
```

### 2.3 Interaction Modes

The architecture supports all three interaction modes from the Engagement Graph Spec:

| Mode | How it works with MCP |
|:---|:---|
| **H2H** (Human-to-Human) | A Commons Engineer uses their AI assistant (connected to Commons MCP) to prepare for a meeting, navigate patterns, or build a briefing. The AI is the navigator; the human is the pilot. |
| **H2A** (Human-to-Agent) | A practitioner connects their AI assistant to Commons MCP and asks: "Diagnose my organisation's resilience." The AI invokes `diagnose`, `find_patterns`, `prescribe` — structured tools returning structured results. |
| **A2A** (Agent-to-Agent) | A client's autonomous agent connects to Commons MCP via Blueprint MCP and requests pattern recommendations for a detected tension. No human in the loop. Raw structured data, typed responses, machine-to-machine. |

---

## §3 The Five-Layer Infrastructure

To scale from 54,000 to 100,000+ patterns and from 10 to 10,000+ lighthouses, read and write operations must be fully decoupled (CQRS pattern: Command Query Responsibility Segregation).

### 3.1 Layer 1 — Source of Truth (GitHub)

GitHub is the immutable long-term memory. Every commit is a cryptographically secured knowledge snapshot.

| Aspect | Detail |
|:---|:---|
| **Data** | Markdown files with validated YAML frontmatter (per PATTERN_SPEC, LIGHTHOUSE_SPEC) |
| **Rule** | No system writes data past GitHub. All AI-generated syntheses flow back as Pull Requests. |
| **Cost** | €0 (Free tier sufficient for private repos with GitHub Actions) |

The workshop repository (`commons-engineering/workshop`) is the single source of truth. All downstream systems are derived, rebuildable, and disposable.

### 3.2 Layer 2 — Ingestion & ETL Pipeline

An event-driven pipeline transforms Markdown into computable knowledge.

**Trigger:** GitHub Actions on push to `main`. The pipeline runs for the duration of the build (~10 minutes for a full index), not as a permanent server.

**Process:**
1. Clone or pull the workshop repository (or receive the delta of changed files)
2. Parse YAML frontmatter (deterministic extraction) and separate body text (semantic content)
3. Validate frontmatter against PATTERN_SPEC / LIGHTHOUSE_SPEC schemas
4. Generate vector embeddings for body text via embedding API
5. Write graph nodes, edges, properties, and vectors to the database
6. Report validation errors and coverage statistics

**Technology:** Python. The existing `build_indices.py` pipeline has proven the parsing at scale (54,266 patterns indexed in 639 seconds). It will be extended to write to Neo4j instead of SQLite, and to generate embeddings.

**Cost:** €0 (GitHub Actions free tier: 2,000 CI/CD minutes/month)

### 3.3 Layer 3 — The Brain (Graph + Vector Database)

This is the most important infrastructure decision. We need a system that combines hard relations (`(:Lighthouse)-[:EXEMPLIFIES]->(:Pattern)`) with semantic similarity (vector distance).

**Decision: Neo4j Community Edition on a managed VPS.**

| Why Neo4j | Why not alternatives |
|:---|:---|
| Native graph traversal — Cypher is designed for exactly our orbital model | PostgreSQL + pgvector + Apache AGE: graph traversal over multiple levels is slow and complex in SQL |
| Native vector index (since Neo4j 5.11) — KNN search integrated into graph queries | Separate vector DB (Qdrant, Pinecone): another service to operate, no graph integration |
| Open source Community Edition is free, handles millions of nodes | SQLite: proven as stepping stone (our prototype), but lacks graph traversal and vector search |
| 8 GB RAM VPS handles our entire dataset comfortably | Cloud-managed Neo4j (Aura): hundreds of €/month, unnecessary at this stage |

**Data model in Neo4j:**

```cypher
// Nodes
(:Pattern {slug, title, sector, orbital_layer, domain, vitality, summary, ...})
(:Lighthouse {slug, name, sector, orbital_layer, overall_score, summary, ...})
(:Hub {slug, title, orbital_layer})  // Gravitational hubs (Orbit 0-2)
(:ValueStream {name, dimension, agent})

// Edges (from pattern frontmatter Group 5 + 6)
(:Pattern)-[:MANIFESTS_AS {weight}]->(:Pattern)
(:Pattern)-[:ENABLES {weight}]->(:Pattern)
(:Pattern)-[:REQUIRES {weight}]->(:Pattern)
(:Pattern)-[:ALTERNATIVE_TO {weight}]->(:Pattern)
(:Pattern)-[:COMPLEMENTARY_TO {weight}]->(:Pattern)
(:Pattern)-[:ATTRACTED_BY]->(:Hub)

// Lighthouse edges
(:Lighthouse)-[:EXEMPLIFIES {weight, evidence}]->(:Pattern)
(:Lighthouse)-[:NEEDS {weight, note}]->(:Pattern)
(:Lighthouse)-[:RELATED_TO {relationship}]->(:Lighthouse)
(:Lighthouse)-[:OPERATES]->(:ValueStream)

// Vectors stored as node properties
(:Pattern {embedding: [float]})  // Body text vector
(:Lighthouse {embedding: [float]})
```

**Hosting options (in priority order):**

| Option | Cost | Fit |
|:---|:---|:---|
| **Hetzner VPS** (CPX21: 4 vCPU, 8 GB RAM) | ~€8/month | Best price/performance ratio for EU-hosted data |
| **Azure VM** (B2s or similar) | ~€15-30/month | If cloudsters' existing Azure instances have capacity |
| **DigitalOcean/Vultr** | ~€10-15/month | Alternatives if Hetzner is unavailable |

cloudsters has two Azure instances available. If either has 8 GB RAM free, Neo4j can run alongside existing services — saving the cost of a separate VPS entirely.

**Cost:** €0-10/month (depending on whether Azure capacity is available)

### 3.4 Layer 4 — The MCP Server (API)

The MCP server is a Python or TypeScript application that implements the Model Context Protocol, connects to Neo4j, and exposes tools to AI agents.

**Technology:** Python with the MCP Python SDK (FastMCP). The existing `server.py` provides the tool signatures and business logic — it will be adapted to query Neo4j instead of SQLite.

**Hosting:** Railway.app or Render.com. Both scale to zero when nobody is asking, and are developer-friendly for single-person operations.

| Platform | Cost | Fit |
|:---|:---|:---|
| **Railway** | ~€5/month (usage-based, scales to zero) | Best DX, easy deploys from GitHub |
| **Render** | ~€5/month (free tier available) | Good alternative, slightly less flexible |
| **Same VPS as Neo4j** | €0 incremental | Simplest — one server runs everything |
| **Cloudflare Workers** | €0-5/month | Only if using D1/SQLite path (no Neo4j access) |

**Recommendation:** Run the MCP server on the same VPS as Neo4j for Phase 1. One server, one deployment, minimal ops. Move to separate hosting when scale demands it.

**Transport:** Streamable HTTP at `/mcp` endpoint. This is the production MCP transport with full authentication support. The existing Cloudflare Worker at `mcp.commons.engineering` proves this works.

**Cost:** €0-5/month

### 3.5 Layer 5 — GraphRAG & Synthesis (The Weaver)

An asynchronous batch process that runs periodically (nightly or weekly) over the Neo4j graph. It uses Graph Data Science algorithms to discover emergent knowledge that exists in no single Markdown file.

**What the Weaver does:**

1. **Community Detection** (Leiden algorithm): Find clusters of lighthouses that share similar needs, or clusters of patterns that co-occur across domains
2. **Orbit 2 Pattern Generation:** When cross-domain clusters emerge, propose new Orbit 2 (commons attractor) patterns as Pull Requests to GitHub
3. **Gap Analysis:** Identify lighthouses that need patterns no lighthouse yet exemplifies — these are market opportunities
4. **Relationship Inference:** Discover implicit pattern relationships from co-occurrence, similarity, and structural position

**Output:** The Weaver writes its findings back to GitHub as Pull Requests. Humans review and curate. The cycle closes: GitHub → Pipeline → Neo4j → Weaver → GitHub.

**Cost:** Runs as a GitHub Action or a scheduled job on the VPS. The only external cost is the LLM API for synthesis (~€5-15/month usage-based).

### 3.6 Total Bootstrapper Stack Cost

| Layer | Component | Monthly Cost |
|:---|:---|:---|
| 1. Source of Truth | GitHub (private repo, Actions) | €0 |
| 2. ETL Pipeline | GitHub Actions | €0 |
| 3. Graph + Vector DB | VPS + Neo4j Community Edition | €0-10 |
| 4. MCP Server | Same VPS or Railway | €0-5 |
| 5. Embeddings + Synthesis | OpenAI `text-embedding-3-small` + Claude Haiku | €5-15 |
| **Total** | | **~€10-30/month** |

**One-time embedding cost:** 100,000 patterns × ~1,000 tokens = 100M tokens. At OpenAI's `text-embedding-3-small` rate of $0.02/1M tokens: **~€2 total** to embed the entire knowledge base.

---

## §4 Commons MCP Server

### 4.1 Purpose

The Commons MCP Server is the public-facing knowledge service for the entire Commons Engineering body of knowledge. It transforms the static workshop repository into a queryable, navigable, composable knowledge system accessible to any AI agent worldwide.

### 4.2 Server Metadata

```json
{
  "name": "commons-engineering",
  "version": "1.0.0",
  "description": "Commons Engineering knowledge service — 100,000+ patterns, 10,000+ lighthouses, pattern graph, value stream routing, orbital navigation, GraphRAG synthesis.",
  "protocol_version": "2025-03-26"
}
```

### 4.3 Resources (MCP Resources)

MCP Resources are read-only data that the server exposes for context.

| Resource URI | Description | Content |
|:---|:---|:---|
| `commons://specs/pattern` | Pattern specification | PATTERN_SPEC v8.2 schema summary |
| `commons://specs/lighthouse-business` | Business lighthouse spec | LIGHTHOUSE_BUSINESS_SPEC v1.2 schema summary |
| `commons://specs/lighthouse-urban` | Urban lighthouse spec | LIGHTHOUSE_URBAN_SPEC v1.0 schema summary |
| `commons://specs/engagement-graph` | Engagement graph spec | ENGAGEMENT_GRAPH_SPEC v0.1 schema summary |
| `commons://taxonomy/orbits` | Orbital layer definitions | The 6 orbital layers with descriptions |
| `commons://taxonomy/dimensions` | Universal Dimensions | The 4 dimensions with their value streams |
| `commons://taxonomy/sectors` | Domain definitions | Life, Business, Urban, Ecology, Cross-Domain |
| `commons://stats` | Library statistics | Pattern counts by domain/orbit, lighthouse counts, graph density |

### 4.4 Tool Catalogue

Tools are organised into five categories, gated by access tier (see §8).

---

#### 4.4.1 Navigation Tools (Tier 0 — OPEN)

**`get_framework_context`** — Return the commons definition, four dimensions, orbital layers.

```typescript
get_framework_context() → {
  definition: string,          // What is Commons Engineering
  dimensions: [{
    id: string,                // "D1" | "D2" | "D3" | "D4"
    name: string,
    paired_name: string,       // "Definition & Purpose" etc.
    agent: string,             // "Purpose Agent" etc.
    perspective: string
  }],
  orbits: [{
    layer: int,                // 0-5
    name: string,
    description: string,
    pattern_count: int
  }]
}
```

**`navigate_orbit`** — List patterns at a given orbital layer.

```typescript
navigate_orbit(
  layer: int,            // 0-5, required
  sector?: string,       // "Life" | "Business" | "Urban" | "Ecology" | "Cross-Domain"
  limit?: int,           // default 50, max 500
  offset?: int           // pagination offset, default 0
) → {
  total: int,
  patterns: [{
    slug: string,
    title: string,
    sector: string,
    orbital_layer: int,
    vitality: float,
    summary: string
  }]
}
```

**`find_patterns`** — Topological vector search: combines semantic meaning with structural orbital position.

```typescript
find_patterns(
  query: string,              // natural language query, required
  target_orbit?: int[],       // filter by orbital layers (e.g., [2,3] for commons + domain patterns)
  sector?: string,            // filter by domain
  domain?: string,            // filter by ontology.domain
  vitality_min?: float,       // filter by minimum vitality score
  confidence_min?: int,       // filter by minimum confidence (1-3)
  limit?: int                 // default 20, max 100
) → {
  total: int,
  patterns: [{
    slug: string,
    title: string,
    sector: string,
    orbital_layer: int,
    vitality: float,
    summary: string,
    relevance_score: float,   // combined semantic + structural relevance
    match_source: string      // "graph" | "vector" | "frontmatter" | "combined"
  }]
}
```

**Search strategy:** The MCP server converts the `query` into a vector, performs KNN search in Neo4j's vector index, then hard-filters results by the specified orbits, sectors, and domains via Cypher. Results are ranked by combined relevance (vector distance + structural position + vitality).

**`traverse_graph`** — Walk the pattern relationship graph.

```typescript
traverse_graph(
  pattern_slug: string,            // starting pattern, required
  relationship_type?: string,      // "manifests_as" | "enables" | "requires" |
                                   // "alternatives" | "complementary" | "tools" |
                                   // "inferred" | "all" (default: "all")
  direction?: string,              // "outgoing" | "incoming" | "both" (default: "both")
  depth?: int,                     // traversal depth, default 1, max 3
  min_weight?: float               // minimum edge weight, default 0.0
) → {
  root: { slug: string, title: string, orbital_layer: int },
  edges: [{
    source_slug: string,
    target_slug: string,
    relationship: string,
    weight: float,
    source_type: string,           // "curated" | "migration" | "graphrag"
    depth: int
  }],
  nodes: [{
    slug: string,
    title: string,
    sector: string,
    orbital_layer: int,
    vitality: float
  }]
}
```

**`get_pattern`** — Full pattern content (frontmatter + body text).

```typescript
get_pattern(
  slug: string               // required
) → {
  frontmatter: { ... },      // all frontmatter fields
  body: string               // full narrative body (Sections 1-8)
}
```

**`get_pattern_lineage`** — Traverse the gravity well of a pattern.

```typescript
get_pattern_lineage(
  pattern_slug: string,            // required
  direction: string                // "inward" (centripetal: towards Orbit 0/1 hubs)
                                   // | "outward" (centrifugal: towards Orbit 4/5 implementations)
) → {
  origin: { slug: string, title: string, orbital_layer: int },
  lineage: [{
    slug: string,
    title: string,
    orbital_layer: int,
    sector: string,
    relationship: string,          // how it connects to the previous step
    depth: int                     // hops from origin
  }]
}
```

**`navigate_value_stream`** — Navigate value streams within a lighthouse.

```typescript
navigate_value_stream(
  lighthouse_slug: string,         // required
  stream_name: string              // one of the value stream family names, required
) → {
  lighthouse: { slug: string, name: string, sector: string },
  stream: {
    name: string,
    dimension: string,
    relevance: string,
    body_excerpt: string
  },
  patterns_exemplified: [{
    slug: string, title: string, weight: float
  }],
  patterns_needed: [{
    slug: string, title: string, weight: float, note: string
  }]
}
```

---

#### 4.4.2 Lighthouse Tools (Tier 0 — OPEN)

**`load_lighthouse`** — Full lighthouse briefing with structured frontmatter.

```typescript
load_lighthouse(
  slug: string,                    // required
  include_body?: boolean,          // include narrative body, default false
  include_engagement?: boolean     // include engagement summary, default false (Tier 1+)
) → {
  identity: { ... },               // Group 1
  position: { ... },               // Group 0
  market: { ... },                 // Group 2
  commons_vitality: { ... },       // Group 3
  relationships: {
    exemplifies: [{ slug, weight, orbit, evidence }],
    needs: [{ slug, weight, note }],
    related_lighthouses: [{ slug, weight, relationship }],
    value_streams: [{ stream, relevance }]
  },
  body?: string,
  engagement_summary?: { ... }     // Tier 1+ only
}
```

**`list_lighthouses`** — Browse the lighthouse gallery.

```typescript
list_lighthouses(
  sector?: string,
  orbit_min?: int,
  orbit_max?: int,
  urban_lighthouse?: string,       // filter by parent urban lighthouse
  limit?: int,                     // default 20, max 100
  sort_by?: string                 // "brightness" | "vitality" | "name"
) → {
  total: int,
  lighthouses: [{ slug, name, sector, orbital_layer, overall_score, summary, industry?, headquarters? }]
}
```

**`compare_lighthouses`** — Compare multiple lighthouses across dimensions.

```typescript
compare_lighthouses(
  slugs: string[],                 // 2-5 lighthouse slugs, required
  dimension?: string               // "purpose" | "participation" | "proposition" | "production" | "all"
) → {
  lighthouses: [{ slug, name, orbital_layer }],
  comparison: {
    commons_vitality: { [slug]: { d1, d2, d3, d4, vitality_signal } },
    shared_patterns: [{ slug, title, present_in: string[] }],
    unique_needs: [{ slug, title, needed_by, exemplified_by }]
  }
}
```

**`analyze_lighthouse_ecosystem`** — 360-degree view of an organisation in its context.

```typescript
analyze_lighthouse_ecosystem(
  lighthouse_slug: string,         // required
  include_nested?: boolean         // if urban lighthouse, include nested business lighthouses
) → {
  lighthouse: { ... },
  ecosystem: {
    nested_lighthouses?: [{ slug, name, sector }],           // business lighthouses within an urban lighthouse
    shared_patterns: [{ slug, title, shared_with: string[] }],
    pattern_gaps: [{ slug, title, needed_by, available_from }],
    common_needs: [{ slug, title, needed_by: string[] }]
  }
}
```

---

#### 4.4.3 Diagnostic Tools (Tier 1 — PEER)

**`diagnose`** — Given a situation description, identify relevant patterns and dimensions.

```typescript
diagnose(
  context: string,                 // situation description, required (500-5000 chars)
  sector?: string,
  dimension?: string,
  depth?: string                   // "quick" | "standard" | "deep"
) → {
  analysis: {
    dimensions_affected: [{ dimension, relevance: float, tension_identified }],
    orbital_mapping: {
      principles_relevant: [{ slug, title, influence: float }],
      commons_patterns: [{ slug, title, fit }],
      domain_patterns: [{ slug, title, fit }]
    },
    value_streams_affected: [{ stream, dimension, severity }]
  },
  recommended_next: string[]
}
```

**`prescribe`** — Generate implementation guidance for specific patterns in a specific context.

```typescript
prescribe(
  pattern_slugs: string[],        // 1-10 pattern slugs, required
  context: string,                // situation context, required
  lighthouse_slug?: string,       // prescribe for a specific organisation
  depth?: string                  // "overview" | "detailed"
) → {
  prescription: [{
    pattern: { slug, title, orbital_layer },
    context_fit: float,
    implementation_guidance: string,
    dependencies: [{ slug, title, relationship }],
    value_streams_affected: string[],
    estimated_effort: string,
    cognitive_era_notes: string
  }],
  implementation_sequence: string[],
  standard_offers_relevant: [{ offer, scope }]
}
```

---

#### 4.4.4 Engagement Tools (Tier 1 — PEER)

**`start_engagement`** — Begin a new engagement graph for a lighthouse.

```typescript
start_engagement(
  lighthouse_slug: string,
  engineer_slug?: string,
  dimension?: string,
  notes?: string
) → {
  engagement_id: string,
  lighthouse: { slug, name },
  status: "planned",
  created: string
}
```

**`log_signal`** — Log a market signal or touchpoint to an engagement.

```typescript
log_signal(
  engagement_id: string,
  signal: {
    signal_source: string,
    dimension_triggered: string,
    urgency: string,
    summary: string,
    patterns_relevant?: [{ slug, relevance }],
    expires?: string
  }
) → {
  signal_id: string,
  engagement_id: string,
  status: "logged",
  created: string
}
```

**`engagement_status`** — Current state of an engagement.

```typescript
engagement_status(
  engagement_id: string
) → {
  engagement: { id, lighthouse, status, created, last_activity },
  signals: int,
  explorations: int,
  blueprints: int,
  pulses: int,
  patterns_explored: [{ slug, title, fit }],
  next_action?: string,
  timeline: [{ date, type, summary }]
}
```

---

#### 4.4.5 Meta Tools (Tier 0 — OPEN)

**`get_schema`** — Return the full schema definition for any entity type.

```typescript
get_schema(
  entity_type: string              // "pattern" | "lighthouse_business" | "lighthouse_urban" |
                                   // "steward" | "signal" | "exploration" | "blueprint" |
                                   // "engagement" | "pulse"
) → {
  entity_type: string,
  spec_version: string,
  frontmatter_groups: [{ group_number, group_name, fields: [{ name, type, required, description }] }],
  body_sections: [{ section_number, section_name, word_range }]
}
```

**`library_stats`** — Return current library statistics.

```typescript
library_stats() → {
  patterns: {
    total: int,
    by_sector: { [sector]: int },
    by_orbit: { [orbit]: int },
    avg_vitality: float
  },
  lighthouses: {
    total: int,
    by_sector: { [sector]: int },
    avg_overall_score: float
  },
  graph: {
    total_edges: int,
    curated_edges: int,
    inferred_edges: int,
    avg_edges_per_pattern: float
  },
  last_updated: string
}
```

**`get_manifest`** — Return a commons manifest document.

```typescript
get_manifest(
  name: string                     // manifest file name without extension
) → {
  title: string,
  content: string                  // full text of the manifest
}
```

**`get_spec`** — Return a commons specification document.

```typescript
get_spec(
  name: string                     // spec file name without extension
) → {
  title: string,
  content: string
}
```

#### 4.4.6 Extension Pack Tools (Tier 0 — OPEN for browse, Tier 1 — PEER for install)

> The extension pack architecture — pack structure, manifest.yml format, provider registry, and loading flow — is defined in COMMONS_OS_SPEC §2.5. This section defines the MCP tools that expose the pack ecosystem to AI agents.

**`list_packs`** — Browse available extension packs in the registry. *(Tier 0 — OPEN)*

```typescript
list_packs(
  provider?: string,        // filter by provider
  domain?: string,          // filter by domain
  status?: string           // filter: "active" | "beta" | "deprecated" (default: "active")
) → {
  packs: [{
    provider: string,
    pack: string,
    version: string,
    title: string,
    description: string,
    domains: string[],
    patterns: int,
    status: string
  }]
}
```

**`get_pack_manifest`** — Return the full manifest for a specific extension pack. *(Tier 0 — OPEN)*

```typescript
get_pack_manifest(
  provider: string,         // required
  pack: string              // required
) → {
  manifest: { ... }         // Full manifest.yml content
}
```

**`list_providers`** — Browse registered extension pack providers. *(Tier 0 — OPEN)*

```typescript
list_providers() → {
  providers: [{
    provider: string,
    name: string,
    url: string,
    verified: boolean,
    pack_count: int,
    total_patterns: int
  }]
}
```

**`get_provider`** — Return full provider profile and all packs from that provider. *(Tier 0 — OPEN)*

```typescript
get_provider(
  provider: string          // required
) → {
  profile: { ... },         // Full provider.yml content
  packs: [{ ... }]          // All packs from this provider
}
```

**`download_pack`** — Download an extension pack payload from the registry. *(Tier 1 — PEER)*

The Commons MCP is a **remote server** — it cannot write files to the local instance. This tool returns the pack contents as a structured payload. The **local agent** is responsible for writing the files to `extensions/{provider}/{pack}/` and validating the manifest. This separation mirrors the npm/apt model: the registry serves packages, the local client installs them.

```typescript
download_pack(
  provider: string,         // required
  pack: string,             // required
  version?: string,         // optional, defaults to latest
  include_dependencies?: bool // optional, defaults to true — include dependency manifests in response
) → {
  provider: string,
  pack: string,
  version: string,
  manifest: { ... },        // Full manifest.yml content
  files: [{                 // Pack contents as file tree
    path: string,           // Relative path within the pack (e.g., "patterns/purpose-spiral.md")
    content: string         // File content (text) or base64 (binary)
  }],
  dependencies: [{          // Dependency manifests (if include_dependencies=true)
    provider: string,
    pack: string,
    version: string,
    installed: boolean       // Whether this dependency exists in the caller's known installs
  }]
}
```

> **Why not `install_pack`?** A remote MCP server cannot write to a local filesystem. The agent calls `download_pack`, receives the payload, and writes the files locally using its native file access. For commons with a Blueprint MCP, the Blueprint MCP can expose a local `install_pack` tool that wraps this flow. See PACK_SPEC §4.4 for the full local installation sequence.

**`check_pack_updates`** — Compare installed pack versions against the registry. *(Tier 1 — PEER)*

The agent passes its locally known pack versions; the Commons MCP compares them against the registry and returns available updates. No local filesystem access needed — purely informational.

```typescript
check_pack_updates(
  installed: [{             // required — agent reads local manifest.yml files
    provider: string,
    pack: string,
    version: string
  }]
) → {
  updates_available: [{
    provider: string,
    pack: string,
    installed_version: string,
    latest_version: string,
    changelog_summary?: string
  }]
}
```

---

### 4.5 Tool Composition Patterns

The tools are designed to be composed in natural conversational flows:

**Discovery flow:**
```
library_stats()
  → navigate_orbit(layer=2)
  → traverse_graph("mutual-accountability", depth=2)
  → find_patterns("stakeholder governance in rail", target_orbit=[2,3])
```

**Diagnostic flow:**
```
diagnose(context="Our infrastructure maintenance backlog...", sector="Business")
  → find_patterns(query, target_orbit=[1,2])
  → prescribe(["operational-resilience", "subsidiarity-governance"], context)
```

**Lighthouse flow:**
```
list_lighthouses(sector="Business")
  → load_lighthouse("deutsche-bahn")
  → analyze_lighthouse_ecosystem("luebeck", include_nested=true)
  → compare_lighthouses(["deutsche-bahn", "sncf"], dimension="production")
```

**Lineage flow:**
```
get_pattern("just-in-time-production")
  → get_pattern_lineage("just-in-time-production", direction="inward")
  → get_pattern_lineage("operational-resilience", direction="outward")
```

---

## §5 Blueprint MCP Server

### 5.1 Purpose

The Blueprint MCP Server is the client's sovereign knowledge service. It contains their private organisational knowledge — the lighthouse briefing enriched with insider data (version 2+), the private engagement graph, the pattern adoption map, and any client-specific knowledge structures.

The Blueprint MCP is built by cloudsters but **owned by the client**. The client controls where it runs, who has access, and what data it contains.

### 5.2 Deployment Models

| Model | Description | Client Profile |
|:---|:---|:---|
| **cloudsters-hosted** | cloudsters operates the Blueprint MCP on the client's behalf under a DPA. Client data encrypted at rest, logically isolated. | Smaller organisations, initial engagements |
| **client-hosted** | Blueprint MCP runs on client infrastructure. cloudsters provides software and setup. | Enterprises with data sovereignty requirements |
| **hybrid** | Shared knowledge from Commons MCP; private data on client infrastructure. | Regulated industries |

### 5.3 Blueprint MCP Tools

The Blueprint MCP mirrors the Commons MCP tool catalogue but operates on private data. Additional tools:

**Private Navigation:** `find_patterns` searches commons AND client-specific annotations. `traverse_graph` includes client's private adoption edges.

**Private Lighthouse:** `load_lighthouse` returns full lighthouse including private sections. `load_engagement_graph` returns full engagement graph.

**Adoption Tools:** `adoption_status`, `adoption_map`, `adoption_progress` — track pattern adoption across the organisation.

**Enrichment Tools:** `enrich_diagnosis`, `enrich_prescription`, `compare_with_commons` — call Commons MCP and overlay client context.

### 5.4 Data Flow

```
Commons MCP ──────────────────> Blueprint MCP
(public patterns,                (used for enrichment,
 public lighthouses,              never stored beyond
 shared diagnostics)              session context)

Blueprint MCP ─────────────X──> Commons MCP
(private data NEVER                (no private data
 flows to commons)                  crosses this boundary)
```

The only data that flows from private to commons is **anonymised structural insight** — through the Clean Room process (ENGAGEMENT_GRAPH_SPEC §6.4), not through the MCP protocol.

---

## §6 Data Layer

### 6.1 Neo4j Data Model

All frontmatter from patterns and lighthouses maps to Neo4j node properties. All relationships (Group 5 + 6) map to typed, weighted edges.

**Pattern nodes:**

```cypher
CREATE (p:Pattern {
  // Group 0: Architectural Position
  id: "pat_...",
  orbital_layer: 2,
  sector: "Business",

  // Group 1: Core Identity
  slug: "operational-resilience",
  title: "Operational Resilience",
  aliases: ["ops resilience", "business continuity"],
  summary: "...",

  // Group 2: Contextual Translation
  context_labels: {business: "...", urban: "...", ecology: "...", life: "..."},

  // Group 3: Ontology & Vitality
  domain: "governance",
  primary_tension: "...",
  vitality: 0.78,
  overall_score: 0.72,

  // Group 4: Lifecycle
  status: "stable",
  confidence: 2,

  // Vector embedding (body text)
  embedding: [0.012, -0.034, ...],  // 1536-dim float array

  // Metadata
  indexed_at: "2026-03-12T14:00:00Z"
})
```

**Edge types:**

| Relationship | Source | From Group | Direction |
|:---|:---|:---|:---|
| `MANIFESTS_AS` | Pattern → Pattern | Group 5 (manifests_as) | Outward (centrifugal) |
| `ENABLES` | Pattern → Pattern | Group 5 (enables) | Outward |
| `REQUIRES` | Pattern → Pattern | Group 5 (requires) | Inward (centripetal) |
| `ALTERNATIVE_TO` | Pattern → Pattern | Group 5 (alternatives) | Bidirectional |
| `COMPLEMENTARY_TO` | Pattern → Pattern | Group 5 (complementary) | Bidirectional |
| `ATTRACTED_BY` | Pattern → Hub | Group 0 (gravitational_hubs) | Inward |
| `EXEMPLIFIES` | Lighthouse → Pattern | Lighthouse Group 5 | Cross-entity |
| `NEEDS` | Lighthouse → Pattern | Lighthouse Group 5 | Cross-entity |
| `RELATED_TO` | Lighthouse → Lighthouse | Lighthouse Group 5 | Bidirectional |
| `INFERRED` | Pattern → Pattern | Group 6 (inferred) | Directional |

### 6.2 Vector Index

Neo4j 5.11+ supports native vector indices:

```cypher
CREATE VECTOR INDEX pattern_embeddings
FOR (p:Pattern) ON (p.embedding)
OPTIONS {indexConfig: {
  `vector.dimensions`: 1536,
  `vector.similarity_function`: 'cosine'
}}
```

**Embedding model:** OpenAI `text-embedding-3-small` (1536 dimensions). Cost: $0.02 per 1M tokens. One-time full embed: ~€2. Incremental re-embed on content change: negligible.

**Why not model-agnostic embeddings?** The embedding index is used for server-side semantic search, not client-side. The MCP client never sees the vectors — it sends a natural language query, the server embeds it and runs KNN. The choice of embedding model is an internal implementation detail.

### 6.3 Content Store

Pattern and lighthouse body text is stored as a node property in Neo4j (`body_text`). This enables:
- Full-text search via Neo4j's built-in text indices
- Body excerpt extraction for `navigate_value_stream`
- Direct retrieval for `get_pattern` without filesystem access

At 100,000 patterns with ~1,000 words each, the body text adds ~500 MB to the database. Within Neo4j's capacity on an 8 GB VPS.

### 6.4 Engagement Store

The Engagement Store follows the entity architecture from ENGAGEMENT_GRAPH_SPEC v0.1. Engagement entities (stewards, signals, explorations, blueprints, engagements, pulses) are stored as Neo4j nodes with typed edges to lighthouses and patterns.

This is a Tier 1+ feature. Engagement data is logically isolated per subscriber.

### 6.5 Index Build Pipeline

```
GitHub (push to main)
  |
  v
GitHub Action triggers pipeline
  |
  v
build_indices.py (Python)
  |
  +---> Parse YAML frontmatter → validate against spec
  +---> Extract body text → generate embeddings via OpenAI API
  +---> Write Pattern nodes + properties to Neo4j
  +---> Write Lighthouse nodes + properties to Neo4j
  +---> Write edges (relationships) to Neo4j
  +---> Write vectors to Neo4j vector index
  +---> Report statistics + validation errors
```

The pipeline is **idempotent** — running it twice produces the same result. It uses `MERGE` (upsert) operations in Neo4j to handle incremental updates.

### 6.6 SQLite as Stepping Stone

The existing SQLite index (`commons.db`, 126 MB, 54,266 patterns indexed) remains as:
- **Local/offline fallback:** The Python MCP server can run against SQLite for offline use
- **Development tool:** Fast iteration without Neo4j dependency
- **Migration source:** The SQLite schema validates the data model before Neo4j migration
- **CI artifact:** The pipeline produces SQLite as a portable artifact alongside Neo4j writes

---

## §7 Tool Catalogue Summary

### 7.1 Complete Tool Registry

| Tool | Category | Tier | Description |
|:---|:---|:---|:---|
| `get_framework_context` | Meta | 0 (OPEN) | Commons definition, dimensions, orbits |
| `navigate_orbit` | Navigation | 0 (OPEN) | List patterns at orbital layer |
| `find_patterns` | Navigation | 0 (OPEN) | Topological vector search (semantic + structural) |
| `traverse_graph` | Navigation | 0 (OPEN) | Walk the pattern relationship graph |
| `get_pattern` | Navigation | 0 (OPEN) | Full pattern content |
| `get_pattern_lineage` | Navigation | 0 (OPEN) | Traverse the gravity well inward/outward |
| `navigate_value_stream` | Navigation | 0 (OPEN) | Value stream detail + patterns |
| `load_lighthouse` | Lighthouse | 0 (OPEN) | Full lighthouse record |
| `list_lighthouses` | Lighthouse | 0 (OPEN) | Browse lighthouse gallery |
| `compare_lighthouses` | Lighthouse | 0 (OPEN) | Side-by-side comparison |
| `analyze_lighthouse_ecosystem` | Lighthouse | 0 (OPEN) | 360-degree ecosystem view |
| `diagnose` | Diagnostic | 1 (PEER) | Structured situation diagnosis |
| `prescribe` | Diagnostic | 1 (PEER) | Implementation guidance |
| `start_engagement` | Engagement | 1 (PEER) | New engagement record |
| `log_signal` | Engagement | 1 (PEER) | Log market signal |
| `engagement_status` | Engagement | 1 (PEER) | Engagement state + timeline |
| `get_schema` | Meta | 0 (OPEN) | Schema definition for any entity type |
| `library_stats` | Meta | 0 (OPEN) | Library statistics |
| `get_manifest` | Meta | 0 (OPEN) | Commons manifest document |
| `get_spec` | Meta | 0 (OPEN) | Commons specification document |
| `list_packs` | Extension | 0 (OPEN) | Browse available and installed extension packs |
| `get_pack_manifest` | Extension | 0 (OPEN) | Full manifest for a specific extension pack |
| `list_providers` | Extension | 0 (OPEN) | Browse registered extension pack providers |
| `get_provider` | Extension | 0 (OPEN) | Provider profile and all packs |
| `download_pack` | Extension | 1 (PEER) | Download extension pack payload for local installation |
| `check_pack_updates` | Extension | 1 (PEER) | Compare installed versions against registry |

---

## §8 Access Tiers & Revenue

### 8.1 Tier Architecture

| Tier | Name | Audience | Price Model | Key Capabilities |
|:---|:---|:---|:---|:---|
| **0** | **COMMONS OPEN** | Anyone | Free | Full pattern library, full lighthouse gallery, all navigation tools, graph traversal, lineage, ecosystem analysis, schema access, extension pack browsing |
| **1** | **PEER** | Individual practitioner | ~€29-49/month | + Diagnostic tools (diagnose, prescribe), + Engagement tools (personal workspace), + Extension pack download and version checking, + API access |
| **2** | **TEAM** | Team of practitioners | ~€99-199/month per team | + Shared engagement workspace, + Team analytics, + Collaborative diagnostics |
| **3** | **ENTERPRISE** | Organisations | Custom pricing | + Blueprint MCP integration, + A2A agent integration, + Custom enrichment, + Dedicated support |

### 8.2 The Free Tier Is Not a Teaser

The COMMONS OPEN tier gives full access to all knowledge. Every pattern. Every lighthouse. Every relationship. The full graph. The full lineage. The ecosystem analysis. This is not a marketing strategy — it is the commons principle made operational.

What the free tier does not include is **tools that require computation and state**: diagnostics (which synthesise across multiple knowledge sources), engagement management (which requires persistent storage), and integration capabilities (which require infrastructure).

### 8.3 Revenue Model

```
Tier 0 (OPEN)       → Free — the commons grows through use and contribution
Tier 1 (PEER)       → ~EUR 29-49/month individual subscription
Tier 2 (TEAM)       → ~EUR 99-199/month per team (up to 10 seats)
Tier 3 (ENTERPRISE) → Custom pricing — Blueprint MCP setup + ongoing enrichment
```

### 8.4 Mapping to Standard Offers

| Standard Offer | MCP Tier | Delivery |
|:---|:---|:---|
| #1 Baseline Blueprint | Tier 1-2 | Commons MCP diagnostic tools produce the blueprint diagnostic |
| #2 Pattern Injection | Tier 2-3 | Commons MCP prescribe tools guide the injection; Blueprint MCP tracks adoption |
| #3 Governance Shift | Tier 3 | Blueprint MCP as the ongoing governance intelligence layer |
| #4 Context Engine Deployment | Tier 3 | The Blueprint MCP IS the context engine — deployed for the client |
| #5 Graph-to-Graph Handshake | Tier 3 | Blueprint MCP ↔ Commons MCP connection is the handshake |
| #6 Agentic Governance Alignment | Tier 3 | A2A integration through Blueprint MCP |

---

## §9 Security, Sovereignty & Tier Enforcement

### 9.1 How Tier Gating Works (Technical)

The MCP server must technically differentiate between tiers. This is the mechanism:

#### 9.1.1 The Request Flow

```
AI Agent (Claude, GPT, etc.)
  |
  | HTTP request to mcp.commons.engineering/mcp
  | Header: Authorization: Bearer <api_key>   (or no header for Tier 0)
  |
  v
MCP Server (Python/FastMCP)
  |
  +---> Auth Middleware
  |       |
  |       +---> No key?           → caller_tier = 0 (OPEN)
  |       +---> Valid key found?  → look up subscriber in Subscribers table
  |       |                         → caller_tier = subscriber.tier (1, 2, or 3)
  |       +---> Invalid key?      → 401 Unauthorized
  |       +---> Expired key?      → 403 Forbidden ("Subscription expired")
  |
  +---> Tool Router
          |
          +---> tool.required_tier <= caller_tier?  → Execute tool
          +---> tool.required_tier > caller_tier?   → 403 with upgrade message:
                  "This tool requires PEER tier (€29-49/month).
                   Your current tier: OPEN.
                   Subscribe at commons.engineering/subscribe"
```

#### 9.1.2 The Subscribers Table

A lightweight subscribers table — stored in Neo4j alongside the knowledge graph, or in a separate SQLite file on the same VPS:

```sql
CREATE TABLE subscribers (
  api_key         TEXT PRIMARY KEY,      -- UUID, issued on subscription
  subscriber_id   TEXT UNIQUE NOT NULL,  -- TypeID with sub_ prefix
  email           TEXT NOT NULL,
  name            TEXT,
  tier            INTEGER NOT NULL,      -- 0, 1, 2, 3
  team_id         TEXT,                  -- NULL for individual, team UUID for TEAM tier
  stripe_id       TEXT,                  -- Stripe customer ID (for subscription management)
  created_at      TEXT NOT NULL,         -- ISO timestamp
  expires_at      TEXT,                  -- NULL = active subscription, date = expiry
  rate_limit      INTEGER DEFAULT 60,   -- requests/minute (overridable per subscriber)
  is_active       INTEGER DEFAULT 1     -- 0 = suspended/cancelled
);

CREATE TABLE teams (
  team_id         TEXT PRIMARY KEY,
  name            TEXT NOT NULL,
  tier            INTEGER NOT NULL,      -- 2 or 3
  max_seats       INTEGER DEFAULT 10,
  stripe_id       TEXT,
  created_at      TEXT NOT NULL
);
```

#### 9.1.3 Tool Registry with Tier Annotations

Every tool is registered with its minimum required tier. The server enforces this before execution:

```python
TOOL_REGISTRY = {
    # Navigation — OPEN (Tier 0)
    "get_framework_context":        {"tier": 0, "category": "navigation"},
    "navigate_orbit":               {"tier": 0, "category": "navigation"},
    "find_patterns":                {"tier": 0, "category": "navigation"},
    "traverse_graph":               {"tier": 0, "category": "navigation"},
    "get_pattern":                  {"tier": 0, "category": "navigation"},
    "get_pattern_lineage":          {"tier": 0, "category": "navigation"},
    "navigate_value_stream":        {"tier": 0, "category": "navigation"},

    # Lighthouse — OPEN (Tier 0)
    "load_lighthouse":              {"tier": 0, "category": "lighthouse"},
    "list_lighthouses":             {"tier": 0, "category": "lighthouse"},
    "compare_lighthouses":          {"tier": 0, "category": "lighthouse"},
    "analyze_lighthouse_ecosystem": {"tier": 0, "category": "lighthouse"},

    # Diagnostic — PEER (Tier 1)
    "diagnose":                     {"tier": 1, "category": "diagnostic"},
    "prescribe":                    {"tier": 1, "category": "diagnostic"},

    # Engagement — PEER (Tier 1)
    "start_engagement":             {"tier": 1, "category": "engagement"},
    "log_signal":                   {"tier": 1, "category": "engagement"},
    "engagement_status":            {"tier": 1, "category": "engagement"},

    # Meta — OPEN (Tier 0)
    "get_schema":                   {"tier": 0, "category": "meta"},
    "library_stats":                {"tier": 0, "category": "meta"},
    "get_manifest":                 {"tier": 0, "category": "meta"},
    "get_spec":                     {"tier": 0, "category": "meta"},

    # Extension — OPEN (Tier 0) for browsing, PEER (Tier 1) for download
    "list_packs":                   {"tier": 0, "category": "extension"},
    "get_pack_manifest":            {"tier": 0, "category": "extension"},
    "list_providers":               {"tier": 0, "category": "extension"},
    "get_provider":                 {"tier": 0, "category": "extension"},
    "download_pack":                {"tier": 1, "category": "extension"},
    "check_pack_updates":           {"tier": 1, "category": "extension"},
}
```

#### 9.1.4 Data-Level Tier Gating

Some tools are available at Tier 0 but return *more data* at higher tiers. This is data-level gating, not tool-level gating:

| Tool | Tier 0 (OPEN) | Tier 1+ (PEER) |
|:---|:---|:---|
| `load_lighthouse` | Groups 0-3, 5-7 (public sections) | + Group 4 (Account Lifecycle), + Section 8 (Business Potential) |
| `find_patterns` | Results from public data only | + results weighted by engagement context |
| `list_lighthouses` | Public fields only | + `account_status`, `engagement_level` |

Implementation: The tool checks the caller's tier and adjusts the Cypher query accordingly — either excluding private node properties or including them.

```python
def load_lighthouse(slug: str, caller_tier: int):
    if caller_tier >= 1:
        # Return full lighthouse including Group 4
        query = "MATCH (l:Lighthouse {slug: $slug}) RETURN l"
    else:
        # Exclude private fields
        query = """
        MATCH (l:Lighthouse {slug: $slug})
        RETURN l { .slug, .name, .sector, .orbital_layer, .summary,
                   .vitality, .overall_score, .industry,
                   .headquarters_city, .headquarters_country }
        """
```

#### 9.1.5 Subscription Management

**Stripe** handles payments and subscription lifecycle. The flow:

```
User visits commons.engineering/subscribe
  → Selects PEER or TEAM plan
  → Stripe Checkout session
  → On payment success: Stripe webhook → MCP server creates subscriber record + API key
  → API key returned to user
  → User configures AI agent with API key

Subscription renewal:
  → Stripe handles automatic billing
  → On failure: Stripe webhook → MCP server sets expires_at
  → On expiry: caller_tier falls back to 0 (OPEN)
  → All OPEN tools still work — no cliff edge
```

**Key design decision:** When a subscription lapses, the user doesn't lose access — they fall back to Tier 0 (OPEN). All navigation, lighthouse, and meta tools still work. They lose diagnostic and engagement tools. This is the commons principle: knowledge is never gated.

#### 9.1.6 MCP Protocol Auth

The MCP Streamable HTTP transport supports standard HTTP headers. The API key is passed as a Bearer token:

```
POST /mcp HTTP/1.1
Host: mcp.commons.engineering
Authorization: Bearer ce_pk_a1b2c3d4e5f6...
Content-Type: application/json

{"jsonrpc": "2.0", "method": "tools/call", "params": {"name": "diagnose", ...}}
```

For Claude Desktop configuration:

```json
{
  "mcpServers": {
    "commons-engineering": {
      "url": "https://mcp.commons.engineering/mcp",
      "headers": {
        "Authorization": "Bearer ce_pk_a1b2c3d4e5f6..."
      }
    }
  }
}
```

Without the `headers` field, the connection works at Tier 0 — all OPEN tools are available, no API key needed.

### 9.2 Authentication Summary

| Tier | Auth Method | What happens technically |
|:---|:---|:---|
| **Tier 0 (OPEN)** | No key required. Rate-limited by IP. | `caller_tier = 0`, all OPEN tools work |
| **Tier 1 (PEER)** | API key (`ce_pk_...`) in Bearer header | Key → subscriber lookup → `caller_tier = 1` |
| **Tier 2 (TEAM)** | API key per member + team_id in subscriber record | Key → subscriber → team lookup → `caller_tier = 2` |
| **Tier 3 (ENTERPRISE)** | OAuth 2.0 / mutual TLS for A2A. API keys for humans. | Service credentials or key → `caller_tier = 3` |

### 9.4 Data Classification

| Data Class | Examples | Storage | Access |
|:---|:---|:---|:---|
| **Public Commons** | Patterns, public lighthouse sections, pattern graph, value streams | Neo4j (derived from public git repo) | Tier 0+ |
| **Gated Commons** | Lighthouse Section 8 (Business Potential), diagnostic syntheses | Neo4j (access-controlled) | Tier 1+ |
| **Private Guild** | Lighthouse Group 4 (Account Lifecycle), engagement graph | Neo4j engagement store (per-subscriber isolation) | Tier 1+ (own data only) |
| **Sovereign Client** | Private lighthouse data, private engagement graph, pattern adoption map | Blueprint MCP (client infrastructure) | Tier 3 (client only) |

### 9.5 Data Sovereignty Principles

1. **Public knowledge stays public.** All patterns and public lighthouse sections are freely accessible.
2. **Private data stays private.** Subscriber engagement data is logically isolated.
3. **Client data is sovereign.** Blueprint MCP data never flows to Commons MCP.
4. **No model training on private data.**

### 9.6 Rate Limiting

| Tier | Rate Limit |
|:---|:---|
| **Tier 0** | 60 requests/minute, 1,000 requests/day |
| **Tier 1** | 300 requests/minute, no daily limit |
| **Tier 2** | 300 requests/minute per seat, no daily limit |
| **Tier 3** | Custom |

---

## §10 Implementation Roadmap

### Phase 1: Full OPEN Tier — Remote-First (Target: Q2 2026)

**Goal:** The Commons MCP Server runs remotely at `mcp.commons.engineering`, accessible by any AI agent, serving 54,000+ patterns and all lighthouses with graph traversal and vector search.

**Infrastructure:**
- VPS (Hetzner or Azure) with Neo4j Community Edition
- MCP server (Python/FastMCP) on the same VPS
- Streamable HTTP transport at `mcp.commons.engineering`
- GitHub Action for index rebuilds on push

**Tools shipped:**
- All Navigation tools (get_framework_context, navigate_orbit, find_patterns with vector search, traverse_graph, get_pattern, get_pattern_lineage, navigate_value_stream)
- All Lighthouse tools (load_lighthouse, list_lighthouses, compare_lighthouses, analyze_lighthouse_ecosystem)
- All Meta tools (get_schema, library_stats, get_manifest, get_spec)

**Milestone:** Any AI agent worldwide can connect to `mcp.commons.engineering` and navigate the full commons knowledge — 54,000+ patterns, all lighthouses, full graph, vector search, orbital lineage.

---

### Phase 2: Semantic Search + Diagnostics (Target: Q2-Q3 2026)

**Goal:** Add diagnostic tools and first revenue (PEER tier).

**Scope:**
- Diagnostic tools: `diagnose`, `prescribe`
- Tier 1 (PEER) authentication with API keys
- Engagement tools: `start_engagement`, `log_signal`, `engagement_status`
- Subscription management

**Milestone:** A practitioner can describe a situation, receive a structured diagnosis, and get contextualised implementation guidance. First paying subscribers.

---

### Phase 3: GraphRAG & The Weaver (Target: Q3 2026)

**Goal:** The Weaver runs nightly, discovering emergent patterns and generating Orbit 2 candidates.

**Scope:**
- Graph Data Science algorithms (community detection, centrality, similarity)
- Orbit 2 pattern generation as Pull Requests
- Gap analysis across lighthouses
- Relationship inference from structural position

**Milestone:** The knowledge base grows autonomously. New commons patterns emerge from cross-domain synthesis.

---

### Phase 4: Blueprint MCP & Enterprise (Target: Q4 2026)

**Goal:** Launch the Blueprint MCP for enterprise clients.

**Scope:**
- Blueprint MCP server (mirrors Commons MCP on private data)
- Blueprint ↔ Commons enrichment connection
- A2A integration framework
- First enterprise pilot

**Milestone:** An enterprise client has their own Blueprint MCP running, connected to Commons MCP, with private lighthouse data and engagement graph.

---

### Phase Summary

| Phase | Focus | Tier | Timeline | Monthly Cost |
|:---|:---|:---|:---|:---|
| **1** | Full OPEN tier, remote-first, graph + vectors | 0 (OPEN) | Q2 2026 | ~€10-30 |
| **2** | Diagnostics + engagement + first revenue | 0-1 | Q2-Q3 2026 | ~€20-40 |
| **3** | GraphRAG synthesis (The Weaver) | 0-1 | Q3 2026 | ~€30-50 |
| **4** | Blueprint MCP, enterprise pilot | 0-3 | Q4 2026 | Offset by revenue |

---

## §11 Open Questions

| # | Question | Phase | Status |
|:---|:---|:---|:---|
| 1 | **VPS choice:** Hetzner vs. cloudsters' existing Azure instances? Depends on available capacity. | 1 | Open |
| 2 | **Neo4j version:** Community 5.x is free. Which exact release to pin? | 1 | Open |
| 3 | **Embedding model:** OpenAI `text-embedding-3-small` is the default. Should we also support open-source embeddings (Nomic, BGE) for vendor independence? | 1 | Open |
| 4 | **Domain routing for MCP:** `mcp.commons.engineering` currently points to Cloudflare Worker. Reroute to VPS, or keep CF as reverse proxy? | 1 | Open |
| 5 | **Diagnostic tool implementation:** Pure structured matching (let the AI model synthesise) vs. LLM-assisted synthesis inside the tool? Recommendation: structured matching. | 2 | Open |
| 6 | **Engagement data persistence:** Neo4j for hot data + git sync for cold persistence? Or Neo4j only? | 2 | Open |
| 7 | **Pricing validation:** EUR 29-49 PEER, EUR 99-199 TEAM — viable? | 2 | Open |
| 8 | **Offline mode:** SQLite index as portable offline artifact? | 1 | Decided — yes, SQLite stays as fallback |
| 9 | **The Weaver:** Which LLM for synthesis? Claude Haiku for speed/cost, or a stronger model for quality? | 3 | Open |
| 10 | **Multi-tenant isolation:** Neo4j RBAC for engagement data isolation, or separate databases per subscriber? | 2 | Open |

---

## Appendix A: Lineage

This specification descends from:

- **v0.1 (06 March 2026)** — "The Navigator Edition." Established the two-server architecture, tool catalogue, tier model, data sovereignty principles. These remain unchanged in v1.0.
- **Prototype (11-12 March 2026)** — SQLite-based pipeline indexing 54,266 patterns in 639s. Python MCP server with 11 tools. Cloudflare Worker at mcp.commons.engineering. Proved the data model and parsing at scale.
- **Gemini architectural review (12 March 2026)** — Five-layer architecture, Neo4j recommendation, bootstrapper stack (~€30/month), GraphRAG synthesis ("The Weaver"), topological vector search. Validated the strategic direction and filled the infrastructure gap.
- **BEN Ecosystem Framework** — Holger's IP from 9 years at MHP/Porsche (~200 enterprise briefings). The Purpose Spiral, value stream families, outside-in methodology. What took 3 years + consultants → Commons OS makes accessible to any organisation.

## Appendix B: Glossary

| Term | Definition |
|:---|:---|
| **MCP** | Model Context Protocol — open standard for connecting AI models to external tools and data |
| **Commons MCP** | The shared knowledge server operated by cloudsters |
| **Blueprint MCP** | The client's sovereign knowledge server |
| **The Weaver** | Asynchronous GraphRAG synthesis engine that discovers emergent patterns |
| **Pattern** | A reusable solution to a recurring problem, structured per PATTERN_SPEC v8.2 |
| **Lighthouse** | A structured briefing about an organisation (business) or settlement (urban) |
| **Engagement Graph** | The lifecycle graph of a relationship — from signal to delivery |
| **Orbital Layer** | A pattern's distance from first principles (0=Singularity to 5=Edge) |
| **Gravitational Hub** | An Orbit 0-2 principle that attracts higher-orbit patterns |
| **GraphRAG** | Graph-enhanced Retrieval Augmented Generation — combines graph structure with vector similarity for emergent synthesis |
| **CQRS** | Command Query Responsibility Segregation — separating read and write operations for scalability |
| **TypeID** | Unique identifier with entity-type prefix (pat_, lh_, sig_, etc.) |
| **Clean Room** | The process of anonymising private engagement knowledge for public commons return |

## Appendix C: Related Specifications

| Spec | Version | Role in MCP Architecture |
|:---|:---|:---|
| PATTERN_SPEC.md | v8.2 | Defines the schema for pattern nodes — all frontmatter groups become node properties |
| LIGHTHOUSE_BUSINESS_SPEC.md | v1.2 | Defines the schema for business lighthouse nodes and value stream routing |
| LIGHTHOUSE_URBAN_SPEC.md | v1.0 | Defines the schema for urban lighthouse nodes |
| ENGAGEMENT_GRAPH_SPEC.md | v0.1 | Defines the entity architecture for the engagement store |
| COMMONS_AGENT_MANIFEST.md | v0.1 | Defines the four-agent governance model |
| COMMONS_TAXONOMY_MANIFEST.md | current | Defines the gravitational architecture and orbital model |

---

*COMMONS MCP ARCHITECTURE SPECIFICATION v1.0*
*Commons Engineering is licensed under CC-BY-SA-4.0*
*Distributed by cloudsters*
