---
id: pat_64d6fdccb7ac449ba6938b1b
orbital_layer: 2
sector: Business
gravitational_hubs:
- hub_id: collective-action-governance
  principle: The Challenge of Cooperation
  influence: 0.7
- hub_id: polycentric-fractal-organisation
  principle: Power at Every Scale
  influence: 0.7
- hub_id: subsidiarity-local-empowerment
  principle: Decide at the Lowest Level
  influence: 0.7
- hub_id: incentives-self-interest
  principle: Channel Self-Interest
  influence: 0.7
- hub_id: adaptive-management-feedback
  principle: Governance as Experiment
  influence: 0.7
- hub_id: reciprocity-fairness
  principle: Reciprocity Sustains Cooperation
  influence: 0.7
slug: who-gets-to-say-yes-to-discounts
title: Who Gets to Say Yes to Discounts
aliases: []
summary: Set up clear rules about which people can approve discounts at different price levels, so teams can act fast without
  losing control over profits.
context_labels: {}
ontology:
  domain: approval-authority-discount-governance
  cross_domains: []
  search_hints:
    primary_tension: Centralized control vs. distributed empowerment
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
    vitality_reasoning: 'This pattern creates living value by embedding authority within the practitioners closest to decisions
      (sales, procurement, stewardship roles) while maintaining visibility and accountability through transparent thresholds.
      Rather than static rules that calcify, threshold-based governance adapts as conditions change: thresholds rise when
      trust is demonstrated, escalate when deviation patterns emerge. The system learns from each decision, feedback flows
      continuously, and authority becomes a form of stewardship—earned through sound judgment, exercised within clear bounds,
      and revoked when violated. This transforms approval from compliance friction into a commons act: each actor who exercises
      authority judiciously protects the shared resource (margin, budget, relationship integrity) for all future stewards.'
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

> Set up clear rules about which people can approve discounts at different price levels, so teams can act fast without los

> [!NOTE] Confidence Rating: ★★☆ (Observed)
> This pattern was derived from GraphRAG analysis of the Business domain.

---

### Section 1: Context

Every commons faces the same foundational tension: How do we distribute decision-making authority to those closest to conditions and consequences, while protecting the shared resource from depletion, drift, or capture by individual incentive? In sales, procurement, and pricing governance, this tension manifests acutely. Centralized approval protects margin and consistency but throttles response speed and demotivates the very stewards who sense market conditions first. Unrestricted delegation invites margin erosion, inconsistent treatment, and hidden variance. The Orbit 1 principles of Subsidiarity, Polycentric Organisation, and Incentives offer a third path: distribute authority along threshold-based lines, making each actor a governed steward rather than a gatekeeper or a free agent. This echoes how living systems—from ant colonies to forests—coordinate without central control.

---

### Section 2: Problem

> **The core conflict is Centralized control vs. distributed empowerment.**

Organizations conflate two distinct problems: (1) deciding *who* can make what decisions, and (2) ensuring *transparency* about what decisions are made and why. They respond with cascading approval matrices—role-based, amount-based, category-based—that multiply rules faster than they simplify them. The result: approvers become bottlenecks; stewards become frustrated; hidden variance (the real margin leakage) happens outside formal channels; and trust erodes because the system signals distrust in the first place. Meanwhile, true exceptions—the deals that violate thresholds for legitimate strategic reasons—drown in process. The deeper problem: authority is treated as a privilege to defend rather than a responsibility to exercise on behalf of the commons. Incentives are misaligned: approvers face no consequences for slowing decisions; practitioners face consequences for breaching thresholds but none for creative workarounds.

---

### Section 3: Solution

Design Threshold-Based Authority Stewardship as a three-layer system:

**Layer 1: Authority Thresholds as Fractal Hierarchy.** Define decision authority by *objective threshold*, not role title. A frontline practitioner (sales rep, procurement specialist) holds authority to approve decisions up to a defined threshold (deal size, discount depth, order value, contract term length). Authority increases predictably as practitioners demonstrate competence and local knowledge: rep → senior rep → manager → director. Crucially, thresholds are *published and transparent*—every actor knows their own authority and their peers', removing ambiguity and politics.

**Layer 2: Escalation as Stewardship Act.** When a decision approaches or exceeds a threshold, escalation is not failure—it is the steward invoking collective judgment. The approver at the next level reviews not to gatekeep but to ensure the practitioner has done their due diligence: customer context, competitive pressure, margin impact, precedent. The question is never "Do I allow this?" but "Is this decision sound given what this steward knows that I don't?" Feedback from escalation flows back to the original practitioner, building judgment over time.

**Layer 3: Transparency as Commons Protection.** Every approval decision—at any threshold—is logged with: the threshold that applied, the deviation (if any), the business justification, and the outcome. This creates visibility without surveillance. Over time, patterns emerge: which practitioners consistently escalate? Which thresholds prove too high or too low? Where is hidden variance clustering? The commons engineer uses this data not to punish but to *recalibrate*—raising thresholds for stewards who demonstrate sound judgment, lowering them for thresholds that invite consistent circumvention, and identifying where training or market context has shifted.

**Adaptive Cycle Integration.** Thresholds are not static. At regular intervals (quarterly, semi-annually), the collective reviews decision data: variance patterns, escalation frequency, margin outcomes by threshold tier. If a steward's decisions consistently outperform expectations, their threshold rises—authority flows to competence. If variance clusters around a threshold, the threshold itself may be misplaced and requires adjustment. This creates a living commons: authority adapts as the system learns.

---

### Section 4: Implementation

Start by mapping your actual decisions, not your org chart. For one month, collect every discount, exception, or price adjustment that occurred—approved or blocked. Categorize by size, product line, customer segment, and outcome. You'll see patterns: which decisions recur, which truly need human judgment, which hide as exceptions.

Then define your thresholds collaboratively. Bring together frontline practitioners (the ones asking for approval), approvers (the ones granting it), and stakeholders who care about outcomes (finance, leadership, customers). The conversation isn't "who deserves authority?"—it's "at what point does the decision's complexity or consequence require a different eye?" A $500 discount on a known product to a loyal customer carries different risk than a $500 discount on new territory. Name that difference.

Encode thresholds as *conditions, not roles*. Instead of "account managers can approve up to $10K," write: "Any practitioner can approve discounts up to 15% off list price for existing customers with 2+ year history; up to 7% for new customers; steward approval required above those limits." Make the logic transparent. Include what *can't* be traded away (margin floors, contract term minimums, exclusivity provisions).

Build an approval workflow that captures decisions in real time—not retrospectively. Every approval (or delegation, or override) creates a visible record: who decided, what the thresholds were, what conditions applied, what the outcome was. This isn't surveillance. It's the commons keeping its own memory.

Train practitioners to *explain* their decisions using the threshold logic. Not to defend themselves, but to demonstrate their stewardship. Over time, you'll see which thresholds are calibrated well (decisions hold up) and which are brittle (constant workarounds).

Review quarterly. Bring the data back to the group that set thresholds. Do decisions at the margin surprise you? Are approvers overridden often? Is margin holding? Adjust thresholds, not attitude.

### Section 5: Consequences

**What flourishes:** Practitioners move with confidence. They know the boundaries and can act within them without waiting. Decisions cluster predictably. Approvers see signal instead of noise. You discover which decisions truly need human judgment (customer relationships, strategic moves, exceptions) and which can be delegated safely to clear rules. Speed and consistency coexist.

Trust deepens between layers. When a frontline practitioner knows exactly what authority they hold, and why, they steward it carefully. When approvers see transparent records of those decisions, they stop second-guessing and start mentoring. The system becomes educative rather than punitive.

**Risks if neglected:** If thresholds aren't revisited, they calcify. Market conditions change; what seemed safe at $50K discount becomes dangerous at quarter-end. Practitioners find workarounds—splitting deals, gaming categories—that fragment the commons more than centralization ever did. The record-keeping becomes theater if no one acts on the data. Worst: approvers treat thresholds as rules to break rather than boundaries to protect, and authority drifts back to politics.

If thresholds are set without practitioner input, they'll be too tight. Practitioners lose faith and stop using the system. They approve via shadow channels (informal handshakes, verbal agreements) that leave no record. The commons becomes invisible.

If consequences aren't connected to decisions, stewardship dies. A practitioner who approves a bad discount needs to see and learn from that decision's outcome—not punishment, but reflection.

### Section 6: Known Uses

**Patagonia's Employee Discount Stewardship.** Patagonia empowers store employees to approve customer refunds and exchanges up to defined thresholds without manager approval, grounded in the company's commitment to standing behind products. The thresholds (based on item cost, time owned, condition) are widely known. Employees feel trusted; the commons (both financial sustainability and customer trust) is protected because the thresholds reflect Patagonia's actual values, not distrust.

**Grameen Bank's Loan Officer Authority.** In Bangladesh, Grameen pioneered threshold-based lending authority for loan officers in the field. Officers could approve microloans up to specific amounts without waiting for central review, because the bank built in accountability mechanisms: group lending (peer co-signers created mutual stewardship), regular repayment cycles (fast feedback), and transparent record-keeping. Speed + margin protection emerged from clear thresholds and transparency, not from centralizing every decision.

**Haier's Micro-Enterprise Model.** The Chinese appliance manufacturer reorganized into thousands of small decision-making units, each with clear authority over pricing, production, and customer relationships within their segment. Each unit knows its thresholds; the parent company monitors outcomes and system health, not individual approvals. The result: rapid response to customer need without losing coherence across the company. Thresholds are conditional on business context, not universal.

### Section 7: Cognitive Era

Threshold-based authority becomes more valuable as organizations integrate AI and distributed intelligence. An AI system can now *propose* discounts in real time—analyzing customer lifetime value, inventory position, margin targets, competitive pressure—and present those proposals to the human decision-maker with full reasoning visible. The threshold system changes from a constraint on human speed to a *scaffold* for human judgment.

The threshold itself can become dynamic. Instead of static rules, you set *parameters*: "margins must stay above this floor; this customer segment is worth this much churn risk; this product line has this inventory sensitivity." An AI learns patterns from past decisions, flags anomalies, and suggests which decisions should escalate to human review. The human keeps authority and purpose; the AI handles the information work.

But this works only if the thresholds themselves are transparent and regularly examined. An opaque AI system saying "this discount is approved" replaces one kind of bottleneck with another—one you can't see or audit. The commons erodes. The pattern demands that threshold-setting remain human and collective, even as the information infrastructure becomes more intelligent.

Distributed teams benefit most. When practitioners span geographies and time zones, threshold-based authority (plus transparent record-keeping) allows genuine decentralization. Each region can calibrate thresholds to local markets while the transparency ensures the whole organization learns from those variations.

### Section 8: Vitality

**Signs of life:** Practitioners can describe their authority in plain language and explain their recent decisions using that language. Approver calendars have fewer interruptions; meetings focus on exceptions and learning, not routine approvals. The ratio of decisions made at threshold to decisions escalated stays stable (or improves). Frontline team members stay longer—they feel trusted, not watched. When someone steps outside their threshold, they know it and can articulate why. Data gets reviewed; thresholds change in response.

**Signs of decay:** "Everyone knows the thresholds" but they're unwritten or live in email. Decisions disappear—no record of what was approved or why. Practitioners game the system: splitting deals, creating phantom categories, asking three people the same question until one says yes. Approvers feel burdened despite the system. Senior leaders complain about margin while the thresholds stay unchanged. The pattern becomes a formality that nobody trusts.

**Diagnostic question:** If you asked a frontline practitioner "What's the biggest discount you can approve to a new customer for this product, and why is that the limit?"—could they answer clearly? And could an approver reviewing their recent decisions see a coherent logic, or just a collection of exceptions?
