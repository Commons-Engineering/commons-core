---
# ═══════════════════════════════════════════════════════════════════
# GROUP 0: ARCHITECTURAL POSITION (The Gravity Well)
# ═══════════════════════════════════════════════════════════════════
id: pat_01kkhc8hcz07b4ddvk6300twtj
orbital_layer: 2
sector: "Universal"
gravitational_hubs:
  - hub_id: "core_transparency"
    influence: 0.9
  - hub_id: "core_resilience"
    influence: 0.8
  - hub_id: "core_subsidiarity"
    influence: 0.75

# ═══════════════════════════════════════════════════════════════════
# GROUP 1: CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════
slug: intranet-extranet-publishing
title: "Intranet-Extranet Publishing"
aliases: ["Dual Visibility Architecture", "Private Workshop / Public Storefront", "Single Source, Two Audiences"]
summary: >-
  A single Git repository serves two visibility layers: the intranet
  (private, for the team — deliberation, drafts, governance records)
  and the extranet (public, for the world — polished patterns,
  specifications, offerings). Same source of truth, different build
  targets. This pattern dissolves the false choice between radical
  transparency and necessary privacy by making visibility a build
  configuration, not an organisational boundary.

# ═══════════════════════════════════════════════════════════════════
# GROUP 2: CONTEXTUAL TRANSLATION (The Navigator Engine)
# ═══════════════════════════════════════════════════════════════════
context_labels:
  corporate: "Intranet/Extranet Content Strategy"
  government: "Internal Working Papers vs. Public Records"
  activist: "Private Strategy vs. Public Campaign"
  tech: "Private Repo with Selective Open-Source Publishing"
  academic: "Working Papers vs. Published Research"

# ═══════════════════════════════════════════════════════════════════
# GROUP 3: ONTOLOGY & SEARCH OPTIMIZATION (The RAG Fuel)
# ═══════════════════════════════════════════════════════════════════
ontology:
  domain: commons-engineering
  cross_domains: [business, life, urban, ecology]
  commons_domain:
    - commons-engineering
  search_hints:
    primary_tension: "Privacy of Process vs. Transparency of Purpose"
    vector_keywords: ["intranet", "extranet", "publishing", "visibility",
                      "transparency", "privacy", "dual build", "Git subtree",
                      "selective publishing", "single source of truth",
                      "commons engineering", "private workshop", "public site"]
  commons_assessment:
    stakeholder_architecture: 5
    value_creation: 5
    resilience: 4
    ownership: 5
    autonomy: 5
    composability: 5
    fractal_value: 4
    vitality: 4.6
    vitality_reasoning: >-
      The dual visibility architecture directly serves the commons
      principle that process may be private while outcomes must be
      transparent. It prevents the false binary of "everything open"
      (which chills honest deliberation) and "everything closed"
      (which prevents accountability). By making visibility a build
      target rather than a repository boundary, it keeps the source
      of truth unified while honouring both the need for safe
      working space and the obligation of public transparency.
    overall_score: 4.6

# ═══════════════════════════════════════════════════════════════════
# GROUP 4: LIFECYCLE & CONFIDENCE
# ═══════════════════════════════════════════════════════════════════
lifecycle:
  usage_stage: design
  adoption_stage: early_adopters
  status: stable
  version: 1.0
  confidence: 3

# ═══════════════════════════════════════════════════════════════════
# GROUP 5: HARD RELATIONSHIPS (Human-Curated Graph)
# ═══════════════════════════════════════════════════════════════════
relationships:
  generalizes_from:
    - slug: visibility-as-commons-act
      weight: 0.9
    - slug: truth-seeking-and-transparency
      weight: 0.85
  specializes_to:
    - slug: ce-learning-in-public
      weight: 0.85
    - slug: authentic-visibility
      weight: 0.8
  enables:
    - slug: body-of-work-cultivation
      weight: 0.9
    - slug: pattern-sharing-practice
      weight: 0.85
    - slug: transparent-operations
      weight: 0.85
    - slug: reputation-compounding
      weight: 0.8
  requires:
    - slug: commons-boundary-definition
      weight: 0.9
    - slug: governance-design
      weight: 0.8
  alternatives: []
  complementary:
    - slug: locale-first-identity
      weight: 0.85
    - slug: fork-template-setup-chain
      weight: 0.85
    - slug: integrity-under-pressure
      weight: 0.75
  tools:
    - slug: git-subtree
      type: tool
    - slug: cloudflare-pages
      type: platform
    - slug: github-pages
      type: platform

# ═══════════════════════════════════════════════════════════════════
# GROUP 6: GRAPH GARDEN (Machine-Written Graph)
# ═══════════════════════════════════════════════════════════════════
graph_garden:
  last_pruned: 2026-03-12
  entities:
    - id: dual-visibility
      type: concept
      label: "Dual Visibility Architecture"
      relevance: 1.0
    - id: single-source-of-truth
      type: practice
      label: "Single Source of Truth"
      relevance: 0.95
    - id: selective-publishing
      type: practice
      label: "Selective Publishing via Build Targets"
      relevance: 0.95
    - id: workshop-storefront-split
      type: systemic-pattern
      label: "Workshop/Storefront Split"
      relevance: 0.9
    - id: privacy-gradient
      type: concept
      label: "Privacy Gradient"
      relevance: 0.85
  communities:
    - commons-os-foundations
    - commons-engineering-foundations
    - publishing-practice
  inferred_links:
    - target: visibility-as-commons-act
      reason: "Shared entities: Dual Visibility, Selective Publishing"
      strength: 5
    - target: transparent-operations
      reason: "Shared entities: Single Source of Truth, Privacy Gradient"
      strength: 4
    - target: fork-template-setup-chain
      reason: "Shared entities: Build targets configured during setup"
      strength: 4
    - target: body-of-work-cultivation
      reason: "Shared entities: Workshop/Storefront Split enables curation"
      strength: 4

# ═══════════════════════════════════════════════════════════════════
# GROUP 7: PROVENANCE
# ═══════════════════════════════════════════════════════════════════
contributors: ["higgerix", "cloudsters"]
sources:
  - "Commons Engineering Framework"
  - "Commons OS Specification v0.1"
  - "Git subtree documentation — selective cross-repo publishing"
  - "Corporate intranet/extranet architecture (1990s–present)"
  - "Open source dual-licensing and selective disclosure practices"
license: CC-BY-SA-4.0
attribution: "commons.engineering by cloudsters, https://cloudsters.net"
collection: commons-os
collection_ring: operating-patterns
7cs_arc: [clarity, credibility, commons]
---

> The workshop is private because honest work requires safe space. The storefront is public because a commons owes its purpose to the world. The craft is keeping one source of truth that serves both.

> [!NOTE] Confidence Rating: ★★★ (High)
> The intranet/extranet split has been standard practice in enterprise content management since the 1990s. The specific innovation here — implementing it as build targets from a single Git repository rather than as separate systems — is validated by Commons Engineering's own architecture (private `workshop` repo, public `commons.engineering` site) and by hundreds of open-source projects that maintain private development branches and public release branches from a single codebase.

---

### Section 1: Context

Every organisation, every commons, every living system operates with two kinds of information: the information that belongs to the internal process and the information that belongs to the external world. The internal process includes deliberation — the messy, honest, sometimes contradictory work of figuring things out. Drafts that are not yet ready. Governance debates that are candid precisely because they are not public. Financial projections that are uncertain. Strategic options that are being evaluated but not yet committed.

The external world includes everything the commons has decided to share: its purpose, its patterns, its specifications, its offerings. These are polished — not in the sense of dishonest or sanitised, but in the sense of considered. They represent the commons' best understanding, its current commitments, its public face.

The traditional approach to managing this split is to maintain separate systems: an intranet for internal content, an extranet or public website for external content. This works, but it creates a fundamental problem: content must be manually moved from one system to the other. This creates duplication, synchronisation failures, and — most importantly — a friction that discourages publishing. The easier it is to keep things internal, the less gets shared. The commons becomes opaque by default rather than transparent by design.

The modern infrastructure of Git, static site generators, and deployment platforms makes a different architecture possible: a single repository that serves both audiences through different build configurations. The same Markdown file can be rendered on the private intranet and the public extranet — or only on one, depending on its metadata. The decision of what to publish is a property of the content, not a property of the system.

Commons Engineering operates exactly this architecture today. The `workshop` repository is private — it is the Werkstatt, the craftsman's workshop where patterns are forged, deliberated, and matured. The `commons.engineering` public site is the storefront — it shows the world what the commons has produced. The content flows from workshop to storefront through a selective publishing mechanism, not through manual copying.

---

### Section 2: Problem

> **The core conflict is Privacy of Process vs. Transparency of Purpose.**

A commons must be transparent about its purpose, its decisions, and its outputs — this is a foundational requirement of legitimacy. But a commons also needs private space for honest deliberation — this is a foundational requirement of good governance. The tension between these two requirements is real, and most organisations resolve it badly.

**Force 1: The chilling effect of premature transparency.** When every draft, every debate, every half-formed idea is immediately public, people self-censor. They write defensively rather than honestly. They avoid raising uncomfortable questions because the record is permanent and public. The quality of deliberation drops because the cost of candour rises. This is well-documented in governance research: public bodies that conduct all business in public session produce worse decisions than those that combine public accountability with private deliberation.

**Force 2: The opacity trap.** When everything is private by default and publishing requires effort, the default state is opacity. Internal wikis accumulate knowledge that never reaches the people who need it. Governance decisions are made but not communicated. Patterns are developed but not shared. The commons hoards rather than contributes — which is the opposite of its purpose.

**Force 3: The synchronisation problem.** When internal and external content live in separate systems, they drift. The internal version evolves while the public version stagnates. The public version is updated but the internal deliberation record is not linked. Contradictions accumulate. The person who reads the public site and the person who reads the internal wiki have different understandings of the same topic — and neither knows it.

**Force 4: The publishing friction problem.** In a separate-systems architecture, publishing requires a conscious act of migration: copy the content from the internal system, adapt it for the external audience, publish it, and maintain the mapping between the two versions. This friction means that only content deemed "important enough" gets published. But the threshold of importance is set by the person doing the work, not by the audience who might benefit. Valuable content stays internal because nobody got around to publishing it.

**Force 5: The four-dimensional visibility question.** A commons operates across four dimensions — Purpose, Participation, Proposition, Production. Each dimension has different visibility requirements. Purpose and governance decisions (D1) should generally be public. Participant details and community dynamics (D2) require privacy. Propositions and offerings (D3) are public by nature. Production processes and infrastructure (D4) may be a mix. A single visibility toggle (public/private) is too coarse; the system needs visibility control at the dimension level.

---

### Section 3: Solution

> **Therefore, maintain a single Git repository as the source of truth for all content, and use build configurations to render different visibility layers — the intranet (private, for the team) and the extranet (public, for the world) — from the same source.**

The solution has three structural components:

**Component 1: Visibility metadata on every content unit.** Every Markdown file, every pattern, every specification carries a `visibility` field in its frontmatter: `internal`, `public`, or `selective`. Internal content renders only on the intranet. Public content renders on both. Selective content renders on both but with different detail levels — a summary on the extranet, the full content on the intranet.

**Component 2: Two build targets from one repository.** The static site generator (e.g., Cloudflare Pages, GitHub Pages, or equivalent) runs two builds from the same repository. The intranet build includes all content. The extranet build filters to `visibility: public` and `visibility: selective` content, rendering the selective content in its summary form. The build configuration is the only difference — the source is shared.

**Component 3: The publishing workflow as governance act.** Changing a document's visibility from `internal` to `public` is a pull request — a reviewable, auditable governance decision. The PR diff shows exactly what is being made public. The review process ensures that the team has consented to the publication. The Git history records who decided, when, and why. Publishing becomes a first-class governance act rather than an administrative task.

**The Four-Dimensional View.** On request, both the intranet and extranet can be structured by the four dimensions — showing Purpose content, Participation content, Proposition content, and Production content as separate navigational areas. This allows stakeholders to find information through the lens of their relationship to the commons: a governance stakeholder navigates via D1, a community member via D2, a customer via D3, a contributor via D4.

---

### Section 4: Implementation

**Step 1: Add visibility metadata to all content.** Establish a frontmatter convention for all Markdown files in the repository:

```yaml
visibility: internal    # Only on intranet
visibility: public      # On both intranet and extranet
visibility: selective   # Summary on extranet, full on intranet
```

For selective content, add a `public_summary` field that contains the extranet-appropriate summary. If absent, the build process uses the `summary` field from the standard frontmatter.

**Step 2: Configure the dual build pipeline.** Set up two deployment targets:

| Target | Domain | Access | Content Filter |
|---|---|---|---|
| Intranet | `internal.[purpose]-os.commons.engineering` | Authenticated (team) | All content |
| Extranet | `[purpose]-os.commons.engineering` | Public | `visibility: public` + selective summaries |

The build script reads each file's frontmatter and includes or excludes it based on the visibility field. For selective content on the extranet, it renders the `public_summary` instead of the full body.

**Step 3: Establish the publishing governance workflow.** Define a pull request template for visibility changes:

- Title: `[PUBLISH] <content title>`
- Checklist: Content reviewed for accuracy. No private deliberation leaked. External links verified. Locale rendering checked.
- Required reviewer: At least one board member (any dimension).

This makes publishing a deliberate governance decision with an audit trail.

**Step 4: Implement the selective publishing mechanism.** For repositories that publish to separate public repos (as Commons Engineering does with `workshop` → `commons.engineering`), use Git subtree or a custom sync script that respects visibility metadata. The script reads each file's visibility, copies `public` and `selective` (summary-only) files to the public repo, and ignores `internal` files.

**Step 5: Build the four-dimensional navigation.** On both intranet and extranet, provide navigational views organised by the four dimensions. Content is tagged with its primary dimension in frontmatter (`dimension: purpose | participation | proposition | production`). The build generates dimension-specific index pages that collect all content for that dimension, filtered by the target's visibility rules.

**Step 6: Establish the default visibility policy.** New content defaults to `internal`. This is safety-first — nothing is accidentally published. The act of making content public is always deliberate. The policy should be documented in the commons governance documents and reviewed periodically to ensure that valuable content is not trapped in internal-only status indefinitely.

---

### Section 5: Consequences

**What this pattern creates:**

A commons with clear, governed visibility boundaries. The team has safe space for honest deliberation — drafts, debates, financial projections, strategic options — knowing that this content is visible only to the team unless deliberately published. The public has access to the commons' outputs — patterns, specifications, offerings, governance decisions — knowing that this content has been reviewed and approved for publication.

The single-source-of-truth architecture eliminates synchronisation problems. There is one version of every document, with visibility as a metadata property rather than a system boundary. When the internal version evolves, the public version evolves with it (if the visibility is set to public). When a selective document is updated, both the full and summary versions are rebuilt from the same source.

The publishing-as-governance pattern creates accountability and intentionality around what the commons shares. Every publication is a PR, every PR has a reviewer, every review is recorded. The commons cannot accidentally publish sensitive content, and it cannot hide behind "we haven't gotten around to publishing that" — the visibility decisions are visible themselves.

**What this pattern risks:**

Over-classification — the tendency to mark everything as internal because it is safer. If the default is internal and the act of publishing requires a PR, the friction favours privacy. The mitigation is a periodic visibility audit: a scheduled review (quarterly or per cadence cycle) that asks "what internal content should be public by now?" This audit is a governance activity, owned by the Purpose Agent (D1).

Build complexity — maintaining two build targets, filtering by visibility, rendering selective summaries, and optionally structuring by dimension adds engineering overhead. The mitigation is to start simple: two targets, one visibility field, no selective rendering. Add complexity only as the content volume justifies it.

The illusion of privacy — the intranet is private from the public, but it is visible to all team members. Content that is sensitive even within the team (personnel matters, individual performance, confidential negotiations) needs a third layer — truly private content that is not in the shared repository at all. The visibility metadata should not become a substitute for genuine confidentiality practices.

---

### Section 6: Known Uses

**Corporate intranet/extranet architecture (1990s-present).** The split between internal and external content management has been standard enterprise practice for three decades. Intranets (SharePoint, Confluence, internal wikis) serve the team; extranets (corporate websites, partner portals) serve the world. The pattern here is proven. The innovation is implementing it as build targets from a single Git repository rather than as separate systems.

**Open-source documentation practices.** Many open-source projects maintain public documentation (user guides, API references) alongside private documentation (contributor guidelines, architectural decisions, roadmaps). Projects like Kubernetes, React, and Linux kernel maintain this split through repository structure (public docs in the main repo, private docs in contributor-only channels). The build-target approach formalises what these projects do informally.

**Commons Engineering workshop/storefront.** Commons Engineering operates this exact architecture: the `workshop` repository is private (the Werkstatt), the `commons.engineering` site is public (the storefront). Patterns, specifications, and manifests are authored in the workshop and selectively published to the public site. This is not theoretical — it is the lived practice of the commons that authored this pattern.

**Academic working papers vs. published research.** The academic publication cycle follows this pattern: working papers circulate privately among collaborators, evolving through feedback and revision. Published papers are the polished, peer-reviewed outputs that reach the public. The same content moves from private to public through a governed review process. The dual-build approach applies this logic to the continuous content of a commons rather than the discrete outputs of a research programme.

---

### Section 7: Cognitive Era

The Cognitive Age adds two dimensions to the intranet/extranet pattern. First, AI agents that operate the commons need access to the full internal content — deliberation records, governance debates, draft specifications — to provide contextually rich responses. The intranet build target serves as the knowledge base for the commons' MCP (Model Context Protocol) layer, giving agents access to the full picture while the public MCP endpoint serves only the extranet content.

Second, AI makes the selective publishing mechanism more powerful. An agent can generate public summaries of internal content, draft publication PRs, and flag internal content that has been stable long enough to consider for publication. The Purpose Agent (D1) can run a periodic visibility review by scanning internal content for documents whose last substantive edit was more than a cadence cycle ago and whose topic is of public interest.

The risk in the Cognitive Age is the leakage vector: an AI agent that has access to internal content might inadvertently include internal details in public-facing responses. The mitigation is the same privacy gradient architecture described in the Commons MCP specification — the agent's public persona has access only to the extranet content layer, while the internal persona has access to both layers. The boundary is enforced at the MCP endpoint level, not at the agent's discretion.

---

### Section 8: Vitality

**Signs of life:**

A healthy intranet/extranet split has a distinctive rhythm: content flows from internal to public at a steady cadence. Every cadence cycle, some content is promoted from internal to public through publishing PRs. The team actively debates what should be public — not because they disagree about transparency, but because they care about the quality of what they share.

The strongest vitality signal is the ratio of public to internal content. A healthy commons publishes a significant fraction of its work — not everything (that would chill deliberation), but enough that the extranet feels like a living, growing resource. If the ratio of internal to public content grows over time without corresponding growth in overall content, the commons is becoming opaque.

Another signal is the quality of selective summaries. When the team takes care to write good public summaries of internal content — summaries that are informative and honest without revealing premature deliberation — it means they understand the dual obligation: safe process and transparent purpose.

**Signs of decay:**

Decay looks like one of two failure modes. The first is total opacity: everything stays internal, the extranet stagnates, the publishing PR template gathers dust. The commons is doing work but the world cannot see it. This is a failure of courage — the team is protecting process at the expense of purpose.

The second failure mode is premature transparency: everything is published immediately, the intranet is empty, deliberation happens in public. This looks like radical openness but it is actually governance failure — the team has no safe space for honest debate, and the public-facing content includes half-formed ideas and unresolved contradictions that confuse rather than inform.

The recovery for both modes is the same: return to the publishing cadence. At each cycle, the team reviews internal content and asks: "What is ready for the world?" The answer should always include something — and should always leave something private. If neither condition holds, the balance is wrong.
