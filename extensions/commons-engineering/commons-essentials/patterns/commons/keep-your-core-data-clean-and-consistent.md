---
id: pat_d9feb7f0d33e44098e002d98
orbital_layer: 2
sector: Business
gravitational_hubs:
- hub_id: feedback-adaptive-cycles
  principle: Information Shapes Systems
  influence: 0.7
- hub_id: conservation-of-energy-matter
  principle: Nothing From Nothing
  influence: 0.7
- hub_id: carrying-capacity-ecological-limits
  principle: Every System Has Limits
  influence: 0.7
- hub_id: visibility-as-commons-act
  principle: Visibility as Commons Act
  influence: 0.7
- hub_id: truth-seeking-transparency
  principle: Truth-Seeking Sustains Systems
  influence: 0.7
slug: keep-your-core-data-clean-and-consistent
title: Keep Your Core Data Clean and Consistent
aliases: []
summary: Master data needs constant care, not just one-time fixes. Learn how to verify, deduplicate, and synchronize information
  across all your systems so everyone works with the same trusted facts.
context_labels: {}
ontology:
  domain: master-data-quality-synchronization
  cross_domains: []
  search_hints:
    primary_tension: Data entropy (drift, duplication, divergence across systems) vs. single source of truth (coherence, trustworthiness,
      actionability)
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
    vitality_reasoning: 'This pattern creates living value by embedding verification into the rhythms of the system itself
      — not as a corrective afterthought but as continuous stewardship. Data quality becomes a renewable practice, not a project.
      The pattern recognizes that data entropy is inevitable (Conservation of Energy) and designs cyclical reconciliation
      as the active work required to maintain coherence. By distributing verification authority across entry points, systems,
      and review intervals, it creates resilience and prevents single-source failure. Most importantly, it treats data governance
      as a commons act: accurate master records are shared infrastructure that all downstream processes depend on.'
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

> Master data needs constant care, not just one-time fixes. Learn how to verify, deduplicate, and synchronize information 

> [!NOTE] Confidence Rating: ★★☆ (Observed)
> This pattern was derived from GraphRAG analysis of the Business domain.

---

### Section 1: Context

Every organization accumulates data across multiple systems — ERP, CRM, procurement, fulfillment, finance. Customer records, product catalogs, supplier master files, and operational logs live in parallel silos, each with its own entry gates, update rhythms, and sources of truth. Over time, entropy compounds: duplicates accumulate from manual entry or system mergers; updates propagate unevenly; validation logic diverges. By the time the system is examined, no single record is fully authoritative — and every downstream process (pricing decisions, payment authorization, analytics, training) inherits the uncertainty. This reflects the Orbit 1 principle of Conservation of Energy: maintaining data coherence requires continuous work. It also invokes Information Shapes Systems — systems with no feedback about their own data quality degrade faster than systems that make verification visible and rhythmic.

---

### Section 2: Problem

> **The core conflict is Data entropy (drift, duplication, divergence across systems) vs. single source of truth (coherence, trustworthiness, actionability).**

The core tension is between entropy and coherence. Data naturally diverges: systems update at different intervals; manual entry introduces errors; mergers and integrations leave duplicate records; suppliers update their own information inconsistently. Organizations attempt to solve this through one-time data cleansing projects, but these create a false sense of resolution — within months, entropy returns. The real problem is deeper: data quality is treated as a state to achieve rather than a process to sustain. Simultaneously, organizations cannot afford to halt operations for data correction; the system must function while being repaired. This creates the working tension: How do you maintain authoritative records in motion, across multiple systems, without paralyzing operations? How do you distribute the work of verification so it doesn't concentrate in a single bottleneck? How do you make quality visible in time to prevent downstream harm?

---

### Section 3: Solution

Establish Master Data Stewardship through layered, continuous verification cycles that treat data accuracy as renewable infrastructure:

**1. Define Authoritative Source(s) by Domain**
For each master data domain (customers, vendors, products, accounts), explicitly name which system or process is authoritative for which attributes. This is not a static declaration but a living governance choice: it names who is responsible for entry quality, how often it updates, and what constitutes a valid record. Document the rule for deduplication (which version wins in a conflict, and why).

**2. Embed Entry-Point Validation**
At the moment data enters any system (manual entry, API import, form submission), implement validation checks: format conformity, required fields, duplicate detection, cross-reference integrity. Validation must be visible to the person entering data — immediate feedback, not a report discovered weeks later. This is early stewardship, preventing entropy at the source.

**3. Establish Reconciliation Cycles by Frequency**
Not all master data requires daily verification; different domains have different carrying capacity. Create a seasonal rhythm: daily reconciliation for high-velocity, high-risk data (supplier payments, product pricing); weekly for transaction-level records; monthly for reference data (product catalogs, customer hierarchies); quarterly for slow-moving reference (certifications, tax IDs). Each cycle compares authoritative source against dependent systems, flags discrepancies, and triggers resolution protocols.

**4. Create Transparent Resolution Protocols**
When reconciliation discovers a discrepancy, the protocol specifies: Who decides the truth? What data do they consult? What is the resolution timeline? How is the decision recorded? The protocol should distribute decision-making close to the source (the team that created the record knows its context) while escalating genuinely ambiguous cases. Make each resolution visible — not hidden in a database, but logged and reviewable.

**5. Design Deduplication as Continuous Tending**
Duplicates don't arrive all at once; they accumulate over time. Rather than periodic mass deduplication (disruptive, error-prone), establish a lightweight detection system that surfaces probable duplicates in real time. Assign responsibility for review and merge to the domain steward, supported by tools that merge records without data loss. This is gardening, not demolition.

**6. Measure & Make Visible**
Track data quality metrics at the domain level: percentage of complete records, duplicate density, time-to-resolution for discrepancies, reconciliation pass rates. Report these publicly (internally) so all downstream teams see the health of their dependencies. Visibility creates feedback; feedback drives continuous improvement. Use these metrics to adjust cycle frequency — if discrepancies are rising, tighten the cycle; if quality is stable, maintain the rhythm.

---

### Section 4: Implementation

Data cleanliness lives or dies in routine. Think of it as tending a garden rather than renovating a house—you're not trying to fix everything at once, but establishing rhythms of care.

**Start with a data audit.** Pick one master domain (customers, products, vendors—whatever causes the most friction in your operations). Map how it flows: where it's created, who touches it, which systems consume it, where it diverges. This isn't theoretical. Walk the actual workflows. Watch how a new customer entry gets typed into CRM by sales, then re-entered into ERP by finance because they need slightly different fields. That friction point is where entropy accumulates.

**Assign a steward.** Not a committee. One person (or small team) owns the ongoing health of each domain. They're not responsible for knowing everything—they're responsible for knowing *who* knows and for orchestrating the verification cycles. This person becomes the living memory of why certain rules exist.

**Establish verification cycles.** Don't clean data once; verify it regularly on a predictable schedule. Monthly for high-churn domains like customer contact info. Quarterly for product catalogs. Annual for less-volatile master files. Each cycle involves: sampling records against source documents or system logs, flagging discrepancies, correcting them at the source (not just the symptom), and documenting what went wrong.

**Implement single-entry points where possible.** If the CRM is authoritative for customer contact information, remove the ability to edit that field in the ERP. Lock it. Route any updates back through the CRM. This isn't about control; it's about physics—if data can be updated in seven places, it *will* diverge in seven ways.

**Use matching and deduplication tools, but keep humans in the loop.** Algorithms can flag probable duplicates or inconsistencies quickly. But a customer named "J. Smith" matched to "John Smith" to "J. Smith Inc." might be one person, three people, or one person with a business. The tool surfaces the candidate; a human decides. This hybrid approach scales faster than pure manual work while avoiding the confidence trap of pure automation.

**Document exceptions explicitly.** Sometimes a customer record needs to differ across systems for legitimate business reasons (different billing vs. shipping addresses, different tax treatments). Don't hide these. Maintain a registry: "Why is this record in state X?" Exceptions should be rare and explained. If you find dozens, your authoritative source definition is wrong.

**Measure what matters.** Track completeness (what percentage of required fields are filled?), accuracy (how many records match their source documents?), and consistency (how many records appear duplicated across systems?). These metrics should trend upward over quarters, not spike and collapse. Spikes mean you've found a new source of entropy; that's data quality working.

### Section 5: Consequences

**What flourishes:** When your core data is clean and consistent, trust in your systems compounds. Finance can reconcile without wrestling with duplicate invoices. Sales can see the true customer picture—not a fragmented view across systems—and spot cross-selling opportunities. Operations can route orders without delays caused by address disputes or SKU confusion. Mergers and integrations move faster because you're not discovering during migration that the same vendor exists under 47 different names. Decision-making speeds up because people stop debating which version of the data is real.

Beyond efficiency, clean data unlocks analytics. You can't build reliable dashboards, AI models, or forecasts on dirty data. The more you depend on intelligent systems, the more your data quality determines whether those systems help or mislead.

**Risks if neglected:** Data entropy accelerates. Cleaning becomes exponentially harder as duplicates and divergence compound. Eventually, nobody trusts the data—reports contradict each other, decisions get made on spreadsheets copied from emails, and you maintain a shadow system of "real" facts outside your official systems. This hidden complexity becomes your technical debt.

There's also a subtler risk: over-governance. If you lock down data too rigidly or require too many sign-offs for updates, your systems become slow and people work around them. The stewardship role matters more than the rules—good stewardship makes structure feel like help, not bureaucracy.

### Section 6: Known Uses

**Procter & Gamble's Product Master Data Initiative:** P&G operates across dozens of businesses, regions, and supply chains. In the early 2000s, product data was fragmented—the same item coded differently in different countries, making supply chain optimization nearly impossible. They established a global product stewardship function, defined authoritative sources by product attribute (formulation from R&D, regulatory compliance from legal, supply chain specifics from operations), and implemented quarterly verification cycles. The result: years of supply chain efficiency gains because product data finally moved as a single entity through their network.

**Kenya's M-Pesa Customer Registry (Safaricom):** As a fintech serving millions of users with varying identity documentation and low digital infrastructure, Safaricom faced massive challenges in customer deduplication. They implemented a continuous verification model: every transaction passes through a matching algorithm that flags probable duplicates, and stewards (trained field agents and back-office teams) resolve them in near-real time. This hybrid approach prevented the kind of fraud and regulatory failures that plague high-entropy financial systems in similar markets.

**Hospital Systems in the National Health Service (UK):** The NHS struggled for years with patient records fragmented across different hospital trusts and GP systems. They established data stewardship by clinical domain (patient identity, medication history, allergy records) and implemented interoperability standards requiring systems to synchronize at defined intervals. While not perfect, this approach reduced dangerous errors from duplicate or missing records—a life-or-death consequence that made the stewardship investment unambiguous.

### Section 7: Cognitive Era

AI and distributed systems both amplify the importance of clean core data and change how stewardship works.

Large language models and analytics engines are sensitive to data quality in ways that traditional systems weren't. A duplicate customer record might confuse a human looking at a CRM; it actively misleads an AI model training on your data, producing systematic bias in its outputs. If your model learns from poisoned data, you don't get slightly wrong predictions—you get confidently wrong ones. Clean data becomes a prerequisite, not a nice-to-have.

Simultaneously, AI tools can accelerate data stewardship itself. Machine learning can run matching algorithms faster than humans, flag anomalies in real time rather than monthly, and predict where data will drift before it does. A steward's job shifts from manual checking to exception handling and pattern learning: "Here's where data quality is breaking down. Why? What's changed in our processes?"

Distributed systems (microservices, decentralized networks, edge computing) mean data lives in more places and updates less synchronously. This increases entropy risk but also creates opportunities for new stewardship patterns: event-driven verification, where systems publish data changes and automated monitors validate consistency across the network in near-real time. The steward's role becomes less about maintaining a central repository and more about orchestrating consensus across distributed sources.

The trap: assuming AI can solve data quality without governance. It can't. AI amplifies clean data and amplifies dirty data equally. The most important shift is recognizing that stewardship becomes *more* central in a cognitive era, not less.

### Section 8: Vitality

**Signs of life in your data stewardship:**

- Stewards can explain *why* a record is in its current state, not just what state it's in.
- Your verification cycle catches new sources of entropy before they compound (changes are small and frequent, not massive and infrequent).
- When someone finds a data error, they report it to the steward, not to their friend in IT. The system feels designed for that feedback.
- Your duplicate-record rate trends downward over months, not up.
- Merges, integrations, or system migrations move faster than expected because data is already coherent.
- People actually use your authoritative sources. They're not maintaining shadow systems.

**Signs of decay:**

- You can't explain why a record looks the way it does. "It's just always been that way."
- Verification cycles are sporadic or skipped. Cleansing projects happen episodically, not rhythmically.
- Duplicates cluster in specific areas (certain customer segments, product lines, time periods). This signals a process broke and wasn't fixed.
- People don't trust the data enough to act on it. Reports get questioned; decisions wait for manual verification.
- Your steward role is unfilled, invisible, or treated as a punishment assignment rather than a craft.

**The diagnostic question:** If you merged with another company tomorrow, could your team quickly identify which records are duplicates because you have clean data, or would you discover the mess during the integration? That answer tells you how much stewardship work remains.
