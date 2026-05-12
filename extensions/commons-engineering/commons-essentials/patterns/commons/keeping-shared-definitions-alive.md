---
id: pat_7440e0d9f2f5476f9b7f2975
orbital_layer: 2
sector: Business
gravitational_hubs:
- hub_id: collective-action-governance
  principle: The Challenge of Cooperation
  influence: 0.7
- hub_id: cultural-meaning-shared-purpose
  principle: Meaning Binds Systems
  influence: 0.7
- hub_id: visibility-as-commons-act
  principle: Visibility as Commons Act
  influence: 0.7
- hub_id: polycentric-fractal-organisation
  principle: Power at Every Scale
  influence: 0.7
- hub_id: the-system-is-the-self
  principle: The System Is the Self
  influence: 0.7
slug: keeping-shared-definitions-alive
title: Keeping Shared Definitions Alive
aliases: []
summary: Assign clear owners to definitions and maintain them over time so everyone stays on the same page as your business
  evolves.
context_labels: {}
ontology:
  domain: data-governance-stewardship
  cross_domains: []
  search_hints:
    primary_tension: Autonomy (each team's right to define concepts locally) vs. Coherence (shared meaning needed for collective
      action)
    vector_keywords: []
  commons_assessment:
    stakeholder_architecture: 4
    value_creation: 4
    resilience: 4
    ownership: 4
    autonomy: 4
    composability: 4
    fractal_value: 4
    vitality: 4.0
    vitality_reasoning: This pattern makes the commons alive by treating definitions as stewardship responsibilities — not
      locked documents but living agreements that evolve with the system. By assigning explicit owners, versioning definitions,
      and cycling them through periodic review, the pattern embeds accountability into the definition process itself. The
      shared glossary becomes a visible commons artifact that makes coherence itself visible. Teams retain local autonomy
      while contributing to and drawing from shared meaning. The cycle ensures definitions adapt as context changes, preventing
      ossification. This creates a continuously regenerating knowledge commons that stays aligned without centralizing authority.
    overall_score: 4.0
lifecycle:
  status: draft
  version: '0.1'
  confidence: 2
relationships:
  manifests_as: []
  enables: []
  requires: []
  alternatives: []
  complementary: []
  tools: []
graph_garden:
  last_pruned: null
  entities: []
  communities: []
  inferred_links: []
contributors:
- higgerix
- cloudsters
sources: []
license: CC-BY-SA-4.0
attribution: commons.engineering by cloudsters, https://cloudsters.net
---

> Assign clear owners to definitions and maintain them over time so everyone stays on the same page as your business evolv

> [!NOTE] Confidence Rating: ★★☆ (Observed)
> This pattern was derived from GraphRAG analysis of the Business domain.

---

### Section 1: Context

Every organisation that grows beyond a single team faces the problem of shared meaning: when 'Active Customer' means different things to Sales and Finance, when product definitions shift across business units, when legacy systems and new platforms speak different dialects. The Commons Engineer recognises that definitions are not technical metadata problems — they are governance acts. They encode what the organisation collectively believes is true about its world. In healthy commons, this meaning-making is distributed, cycled, versioned, and stewarded. This pattern draws from Reciprocity (shared definitions as a form of exchange), Polycentric Organisation (distributed ownership at multiple scales), and Cultural Meaning (definitions as the carrier of collective purpose). It also reflects the principle that Visibility as Commons Act — making definitions explicit and accessible is itself a contribution to the knowledge commons.

---

### Section 2: Problem

> **The core conflict is Autonomy (each team's right to define concepts locally) vs. Coherence (shared meaning needed for collective action).**

Organisations accumulate data assets, systems, and teams faster than they accumulate shared understanding of what those assets mean. Without explicit stewardship, definitions drift: the same term means different things in different contexts; definitions become outdated as business rules change; metadata becomes scattered across systems, disconnected from its source; accountability for accuracy and change disperses into silence. Teams either fragment into isolated islands of meaning (losing coherence) or centralise definition-making into a slow, bureaucratic gatekeeping function (losing adaptation and local legitimacy). The deeper problem: definitions are treated as static documentation rather than living stewardship responsibilities that evolve with the system. No one is explicitly accountable for keeping them current. No one cycles them through review. No one makes the evolution visible.

---

### Section 3: Solution

Create a Stewardship Registry — a distributed governance structure that assigns explicit accountability for definition and maintenance across three nested cycles:

**ASSIGNMENT: Definition Steward Ownership.** For every critical data element, concept, or reference dataset, designate a steward — typically the team closest to the source of truth. The steward is accountable for: maintaining the current definition in a shared glossary; communicating changes to downstream users; versioning the definition and its rationale; ensuring the definition stays aligned with how the concept is actually used. The steward is not a gatekeeper but a custodian and communicator. Stewardship can be rotated or shared (polycentric) — multiple teams can co-steward if they jointly own the concept.

**REGISTRY: Living Glossary & Lineage.** Maintain a centralised, version-controlled registry of all shared definitions. Each entry includes: the current definition and its rationale; the steward name and contact; change history with timestamps and reasons; links to where the concept is used (systems, reports, processes); any aliases or synonyms; governance status (active, deprecated, in-review). The registry is searchable, accessible, and visible — making shared meaning itself discoverable.

**CYCLE: Periodic Definition Review.** Establish a governance cadence (quarterly or semi-annual, depending on system volatility) in which stewards review their definitions against actual usage. Is the definition still accurate? Have business rules changed? Are there new synonyms emerging? Are downstream users still interpreting it correctly? Document the review outcome and any changes, making the evolution visible to the organisation. This cycle embeds learning into definition stewardship — definitions improve as the system learns.

**POLYCENTRIC STRUCTURE:** The registry is maintained centrally but stewardship is distributed. Governance decisions escalate only when conflicts arise (e.g., two teams use the same concept differently). Lower-level stewards have autonomy; higher-level governance intervenes only when local autonomy threatens coherence.

---

### Section 4: Implementation

Start small, with the definitions that hurt most when they're wrong. Convene the teams that clash over meaning — Sales and Finance arguing about "Active Customer," Product and Engineering disagreeing on what constitutes a "release," Operations and Support with different thresholds for "critical incident." Ask them: *When did this term last cause us real friction?* That's your first steward assignment.

The steward's job has three rhythms:

**Weekly tending.** The steward monitors their definition in live use. They scan logs, watch Slack conversations, attend standup meetings where the term appears. They notice drift — when someone uses it differently, when a system change affects its scope. This isn't bureaucratic surveillance; it's gardening. You're watching for weeds.

**Monthly sync.** Once a month, stewards from adjacent domains meet for 45 minutes. A Sales steward meets with the Finance steward. A Product steward connects with Engineering. Not to argue, but to surface the small divergences that accumulate into contradictions. "We've been flagging churned customers differently since the platform migration. Should we document that, or align?" These conversations prevent definitions from calcifying into silos.

**Quarterly refresh.** Every three months, the full definition registry gets a health check. Stewards review their definitions against current business logic. Have rule changes happened? Did a system integration shift how we calculate something? Has the term taken on informal uses that should be formalized? The registry entry updates — not as a chore, but as an act of keeping the organisation honest about what it actually means.

Make the registry visible. A shared spreadsheet, a wiki, a living document — whatever your culture already maintains. Include: the term, who stewards it, the current definition, when it was last reviewed, known variations, and a link to where it lives in systems. Make it mundane and findable, not rarified.

Crucially: protect stewards from ownership bloat. One person stewarding three critical definitions is sustainable. Seven is a warning sign that you need to redistribute or hire.

---

### Section 5: Consequences

When definitions are actively kept, remarkable things become possible. Teams move faster because they don't have to re-solve alignment problems. Cross-functional projects don't stall on semantic tangles. New hires onboard faster because the organisation has articulated what it actually means by its own terms — not just how systems work, but *why*. Data governance stops being a compliance burden and becomes a clarity asset.

The definition registry becomes institutional memory. When someone asks, "Why do we calculate NRR this way?" the answer lives somewhere, documented, with context. You preserve the reasoning, not just the rule. That matters when senior leaders change, when acquisitions happen, when you're explaining your model to partners.

But attend to what can go wrong. Stewardship without real authority becomes theatre. If a steward maintains a definition that no one actually uses — because the "real" version lives in someone's script or a downstream system — the registry becomes a beautiful lie. Stewardship only works if teams actually defer to the steward and treat the definition as authoritative.

There's also the risk of definition creep. A term that starts precise (Active Customer: paid subscription + login in last 30 days) gradually accumulates exceptions and caveats until it's meaningless. The steward must have permission to say no, to refuse edge cases, to keep definitions bounded. This requires visible backing from leadership.

And there's the subtle risk of false consensus. A definition can appear agreed-upon in the registry while teams continue to use it differently in practice. Regular spot-checks help — stewards should occasionally audit their terms in actual use, checking that reality matches documentation.

---

### Section 6: Known Uses

**Spotify, definition stewardship across music and platform.** Spotify's early growth created the problem that every team had a different idea of what "a play" meant for licensing, analytics, and payment purposes. Was skipping a play? A 30-second threshold? Counting in a playlist shuffle? They assigned stewardship of core metrics to specific squads, who became accountable for keeping definitions current as the platform evolved. This allowed their data analytics and finance teams to trust the same numbers.

**Twende, a Nairobi-based fintech cooperative.** In East Africa, where informal financial instruments and mobile money create definitions that Western banking doesn't have, Twende built a stewardship practice around local financial concepts. They assigned stewards from their community finance teams to maintain definitions of "active member," "trustworthy borrower," and "seasonal liquidity need" — terms that carry cultural meaning beyond accounting categories. This kept their systems aligned with how people actually behaved, rather than imposing foreign definitions.

**The UK National Health Service (NHS), clinical definitions across regions.** The NHS faced chaos when "hospital admission" meant different things in different trusts, making nationwide resource planning impossible. They created a stewardship model where each major clinical concept had a regional steward who met quarterly with peers. This allowed local variation where it mattered (how different regions managed triage) while maintaining coherence on definitions that crossed trust boundaries (what counts as a "completed treatment"). The stewards weren't central authorities; they were guardians of alignment.

---

### Section 7: Cognitive Era

AI changes what it means to "keep definitions alive." When large language models can infer patterns from data and generate plausible definitions autonomously, the human steward's role shifts from *creator* to *validator and integrator*.

An AI system can scan your codebase, your data schemas, your business documents, and surface where the same concept is being used inconsistently. It can flag when a definition has drifted from documented intent. It can even suggest unified definitions based on usage patterns. But it will miss something crucial: *Why does this organisation care about this concept?* What business problem does it solve? What does this definition protect or enable?

The steward becomes a bridge between machine-generated coherence and human intentionality. You might ask an LLM, "What definitions are most critical for our annual planning cycle?" and it surfaces terms. But only a human steward asks, "Which definitions, if wrong, would break our ability to serve our customers?"

There's also opportunity. Distributed intelligence — teams operating semi-autonomously with AI-assisted coordination — can maintain more granular, context-specific definitions if there's a clear registry that allows LLMs to reconcile local variation with global coherence. Instead of forcing one definition of "customer satisfaction," you might allow regional or product-line variations *within a documented framework*. The steward doesn't eliminate variation; they make it legible.

The risk: if stewardship becomes purely algorithmic, optimized for consistency at the cost of nuance, you lose the governance act. Definitions are only alive if humans are still choosing what they mean.

---

### Section 8: Vitality

**Signs of life:** Stewards can answer questions about their definitions without hunting for documents. Teams cite the definition registry casually, the way you'd reference a dictionary. New projects check definitions before they begin work. When disagreement arises, people ask, "What does the steward say?" not "What's in the system?" — because they trust the steward more than the artifact. Definitions get updated visibly; you can see when and why a term changed. Stewards sometimes *refuse* requests to broaden or complicate a definition, and that refusal is respected because it's protecting coherence.

**Signs of decay:** The registry becomes outdated, with "last reviewed" dates months old. Stewards don't exist or don't know they're stewards. Teams maintain shadow definitions — informal spreadsheets, Slack pinned messages, person-dependent knowledge — that diverge from the "official" registry. New team members learn terms from whoever's sitting next to them, not from the stewardship structure. Definitions are written in jargon that only specialists understand. Stewards spend more time defending definitions than tending them, a sign they lack real authority.

**The diagnostic question:** If you asked a random engineer, a random finance person, and a random product manager to each write down what "Active User" means in your organisation, how much would they agree? If they substantially agreed, your definitions are alive. If they diverged significantly, stewardship is absent or invisible. If they all deferred to a specific person or document, you have stewardship working.
