---
id: pat_259c647ebb554b28bb3edad8
orbital_layer: 2
sector: Business
gravitational_hubs:
- hub_id: polycentric-fractal-organisation
  principle: Power at Every Scale
  influence: 0.7
- hub_id: reciprocity-fairness
  principle: Reciprocity Sustains Cooperation
  influence: 0.7
- hub_id: subsidiarity-local-empowerment
  principle: Decide at the Lowest Level
  influence: 0.7
- hub_id: conservation-of-energy-matter
  principle: Nothing From Nothing
  influence: 0.7
- hub_id: incentives-self-interest
  principle: Channel Self-Interest
  influence: 0.7
- hub_id: conflict-resolution-evolving-rules
  principle: Conflict Evolves Systems
  influence: 0.7
slug: keep-your-data-switch-your-service
title: Keep Your Data, Switch Your Service
aliases: []
summary: Own your data and move it freely between platforms. Standards and open formats prevent companies from trapping you
  in their system.
context_labels: {}
ontology:
  domain: data-portability-interoperability
  cross_domains: []
  search_hints:
    primary_tension: Data utility (shared access, integration, value) vs. data autonomy (sovereignty, portability, exit rights)
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
    vitality_reasoning: 'This pattern creates living value by treating data as a shared commons that must be stewarded—not
      owned or controlled—by distributed participants. Federated sovereignty ensures the system adapts to local legal, cultural,
      and operational contexts while maintaining interoperability. Portability and open formats prevent calcification; reversible
      participation (easy exit) keeps all actors honest and responsive. The pattern embodies fairness through structural reciprocity:
      you can only extract value proportional to what you contribute, and you cannot unilaterally trap others. This builds
      durable trust without requiring a central arbiter.'
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

> Own your data and move it freely between platforms. Standards and open formats prevent companies from trapping you in th

> [!NOTE] Confidence Rating: ★★☆ (Observed)
> This pattern was derived from GraphRAG analysis of the Business domain.

---

### Section 1: Context

Data flows are the circulatory system of modern cooperation. Yet most platforms treat data as property to be captured and controlled, creating asymmetric power: once data enters a system, exit becomes costly, legal terms change unilaterally, and sovereignty is surrendered. This mirrors the commons tragedy—a shared resource (data's usefulness) is exploited by concentrating control (vendor lock-in). The tension is real: data becomes more valuable when shared across many participants, but sharing requires standards, trust, and protection. Orbit 1 principles guide us: Subsidiarity says decisions belong closest to the data's origin. Reciprocity demands fair exchange. Conservation of Energy reminds us that every lock-in imposes hidden costs—extracting reversibility later requires energy. Polycentric Organisation shows that durable systems distribute governance across scales and actors, not concentrate it.

---

### Section 2: Problem

> **The core conflict is Data utility (shared access, integration, value) vs. data autonomy (sovereignty, portability, exit rights).**

Three forces collide: First, data integration requires common formats and interoperability, pushing toward standardization and centralisation. Second, jurisdictional sovereignty demands that data respect local law, governance, and cultural norms—pushing toward fragmentation and local control. Third, individual participants fear lock-in: once data is uploaded, deleted terms of service, proprietary formats, and high switching costs make exit impossible and trust erodes. The deeper problem: current architectures treat these as binary choices. Data is locked into platforms to fund integration. Sovereignty is preserved by refusing to share. Exit rights are expensive because portability is afterthought, not design. The result: brittle commons. Participants comply out of necessity, not commitment. The system demands continuous enforcement (regulation, litigation, compliance overhead) rather than aligning incentives. No actor can leave without catastrophic cost, so everyone remains trapped together.

---

### Section 3: Solution

Design data stewardship through federated sovereignty: distributed governance across nested tiers, with portable formats and reversible participation as structural foundations.

Three interlocking mechanisms:

**1. Portable Formats as Commons Infrastructure.** Encode all data in open, standardized formats (RDF/Linked Data, schema.org, domain-specific open standards) from ingestion, not as afterthought conversion. This is not optional compatibility—it is constitutional design. Any participant can export their data and history in full, portable form, readable by any compliant system. This prevents lock-in at the format layer and makes switching cost transparent: if switching is expensive, it is because of genuine business logic, not artificial friction.

**2. Federated Sovereignty Through Data Sharing Agreements.** Establish written protocols that specify: where data is held, which jurisdiction's law governs it, who can access it, under what conditions, and for how long. Embed data sovereignty by design—data stays in the jurisdiction of origin unless explicit consent and legal clearance permits movement. Use decentralized architectures (federated nodes, distributed storage) so no single actor can unilaterally revoke access. Agreements are bilateral and symmetric: if a participant's terms can change, the other party can exit. Immutability is bounded: blockchain-style integrity logs prevent tampering but allow legitimate corrections through governance process (with audit trail).

**3. Reversibility as Design Principle.** Make exit rights structural, not legal. Any participant can withdraw participation, carrying portable data, without penalty after a defined notice period. This shifts incentive alignment: the platform must continuously earn participation, not trap it. Switching costs are minimised through standardised formats. Terms of service are frozen unless both parties consent to change; unilateral modification triggers exit rights. This prevents the asymmetric lock-in that corrodes trust.

The pattern creates a living commons: data flows across boundaries because format portability removes friction; sovereignty is preserved because governance remains distributed; reciprocity emerges because no actor can trap another. The system is built to last because it does not depend on enforcement—it aligns self-interest (stay if value exceeds alternatives) with collective interest (shared data utility).

---

### Section 4: Implementation

Start by auditing what data your organization actually holds and how it moves. Map the current flows: where does it enter, what formats does it take, where does it get trapped? This clarity is your first act of cultivation.

Adopt open, standardized formats *at the point of ingestion*, not as an afterthought. If you're building a service, choose formats like JSON-LD, CSV with documented schemas, or domain-specific standards (like BioBB for biomedical data) from day one. This isn't a technical choice alone—it's a political one. It signals that participants' data belongs to them.

Implement three concrete mechanisms:

**Export by default.** Build tools that let users download their complete data history in portable formats without friction—no waiting periods, no degraded formats, no fees. Make this a background feature, not buried in settings. Test it monthly; if export takes longer than five minutes, redesign the interface.

**API-first architecture.** Design your platform's internal systems to use the same open APIs that external partners access. When your engineers can't move data without going through the same open channels as outsiders, lock-in becomes visible and costly to maintain. It naturally creates pressure toward standardization.

**Federated identity and consent.** Let participants authenticate through multiple identity providers (OAuth, open protocols) rather than creating accounts locked to your system. Separate authentication from data ownership. Record consent decisions in portable, machine-readable formats (following ODRL or similar standards) that follow the data itself across systems.

Create governance structures—even if small—that steward the standards you adopt. A working group with representatives from users, competitors, and civil society builds legitimacy and prevents standards from drifting toward vendor interests. Document everything publicly.

The slowest but most essential act: build organizational culture that sees data portability as a feature, not a threat. Train teams to ask: "Could a user reasonably leave us tomorrow?" If the answer is no, you have debt to repay.

### Section 5: Consequences

When this pattern takes root, several flowers bloom. Users gain genuine choice—they can migrate to better services without losing history or relationships. Competition becomes real again; vendors must compete on features and experience, not switching costs. Innovation accelerates because new entrants aren't automatically disadvantaged by data lock-in. Communities can host their own instances of tools they depend on, adapting them to local needs.

Organizationally, you discover which parts of your service create real value and which relied on friction. Some teams initially fear this clarity. Over time, it clarifies purpose: you survive by being genuinely useful, not by making exit painful.

But tensions emerge if the pattern is half-implemented. If you export data in open formats but your interface makes it hard to understand what's being exported, you've created the *appearance* of portability without the substance. Users feel deceived. If standards exist but you ignore them—adopting open formats only for public data while keeping sensitive data proprietary—trust fractures.

Risks: Standards themselves can become battlegrounds. Organizations with resources can shape standards to their advantage, creating the illusion of openness while embedding capture mechanisms. Re-implementing services in new formats carries costs; smaller users and organizations may lack resources to migrate, creating a new form of inequality. And if portability becomes frictionless, malicious actors can more easily extract and weaponize data.

The deepest risk: if every platform truly becomes interchangeable, the incentive to invest in quality interfaces, reliability, and user support diminishes. Genuine community needs—the things that make a commons thrive—can wither if everything becomes transactional.

### Section 6: Known Uses

**Mastodon and the Fediverse.** The distributed social network lets users download their full post history and followers list in standard formats, then migrate to another instance—or host their own—without losing their social graph. The protocol (ActivityPub) is open and documented. Users can leave any single instance because the network itself is portable. This shifted power away from platform operators toward communities. Some instances have failed or been abandoned; users simply migrated. The pattern works at scale across thousands of independent operators.

**Solid (Social Linked Data).** Tim Berners-Lee's initiative lets individuals store their data in "pods"—personal data repositories using linked data standards—accessed by applications through standardized protocols. A user can switch apps while keeping their pod; apps compete on interface and features, not data capture. Early adoption is slow (indicating that users value other things too), but it demonstrates the technical feasibility. Used in small circles of health data, professional networks, and research communities.

**Brazil's Open Banking Standards.** Regulatory mandate requiring banks to share customer financial data (accounts, transactions, credit offers) via standardized APIs in open formats. Customers control which third-party services access their data. New fintech competitors emerged rapidly because they could build on portable data rather than starting from zero. Competition intensified; some traditional banks lost market share but the overall ecosystem became more innovative. Jurisdictional governance (through Brazil's central bank) enforced the standards; this avoided vendor dominance but created new regulatory dependency.

### Section 7: Cognitive Era

AI and distributed intelligence reshape this pattern in three ways. First, *data becomes more valuable and more dangerous simultaneously*. LLMs thrive on scale and diversity; the incentive to concentrate data increases. But the pattern gains urgency: if your training data is locked in proprietary systems, your models inherit those constraints and biases. Open, federated data sources become crucial infrastructure for creating AI that isn't shaped by any single entity's commercial interests.

Second, *verification becomes harder and more necessary*. When data moves between systems, provenance matters—where did this come from, has it been altered, who trained on it? Distributed intelligence systems need portable *metadata* about data's history and usage rights, not just the data itself. Standards must include cryptographic signatures and consent logs that travel with data.

Third, *agency becomes distributed but less transparent*. In a federated system where users move between AI-mediated services, it becomes unclear who's responsible for outcomes. Did the service cause harm, or the data source, or the model? The pattern needs to evolve to include responsibility frameworks and liability trails that stay portable and auditable.

Emergently: systems that truly implement this pattern may become *less* centralizing even as AI drives toward concentration elsewhere. A user with portable data and portable AI models becomes harder to trap. But this only works if the ecosystem actively resists re-concentration—an ongoing political act, not a technical solution.

### Section 8: Vitality

**Signs of life:** Users regularly export their data without surprise or friction. New services launch and grow despite incumbent competitors (the churn you see signals a healthy commons). Documentation about data formats is public and kept current; the community actively maintains it, not just the vendor. Competitors use compatible formats; you find data flowing across organizational boundaries. Users can articulate what data they own and where it lives. When a service shuts down, users don't lose access to their histories.

**Signs of decay:** Export features exist but are slow, incomplete, or generate corrupted files. Users discover—only when trying to leave—that critical data wasn't portable. Standards become stale; vendors adopt them superficially while building proprietary layers on top. Network effects cause lock-in despite open formats: "everyone else is here, so I can't leave." Documentation disappears or becomes inconsistent. A single organization begins to control the "reference implementation" of the standard, making it de facto closed.

**The diagnostic question:** *Could someone I dislike—a competitor, a government I distrust, or someone with values antithetical to mine—competently take my role tomorrow and serve my users using the same data, without my cooperation?*

If the answer is no, you've created a person-shaped lock-in. If yes, the pattern is doing its work. The discomfort you feel is the point; it's the cost of genuine Commons engineering.
