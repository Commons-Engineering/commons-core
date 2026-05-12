---
id: pat_193ac87519884d12af2acd7d
orbital_layer: 2
sector: Business
gravitational_hubs:
- hub_id: collective-action-governance
  principle: The Challenge of Cooperation
  influence: 0.7
- hub_id: polycentric-fractal-organisation
  principle: Power at Every Scale
  influence: 0.7
- hub_id: reciprocity-fairness
  principle: Reciprocity Sustains Cooperation
  influence: 0.7
- hub_id: subsidiarity-local-empowerment
  principle: Decide at the Lowest Level
  influence: 0.7
- hub_id: conflict-resolution-evolving-rules
  principle: Conflict Evolves Systems
  influence: 0.7
- hub_id: time-sliced-iterative-planning
  principle: Plan in Short Cycles
  influence: 0.7
- hub_id: truth-seeking-transparency
  principle: Truth-Seeking Sustains Systems
  influence: 0.7
slug: getting-approval-before-you-commit
title: Getting Approval Before You Commit
aliases: []
summary: Set up clear checkpoints so offers and requests get the right approvals, everyone knows who decided what, and you
  can track the whole thing from start to finish.
context_labels: {}
ontology:
  domain: offer-requisition-approval-workflows
  cross_domains: []
  search_hints:
    primary_tension: Authority distribution vs. commitment clarity — how to disperse decision-making while ensuring every
      commitment is binding, auditable, and adaptive
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
    vitality_reasoning: This pattern creates living adaptive value by making commitment visible and contestable at every threshold.
      Rather than treating approval as a compliance burden, it positions each gate as a moment of genuine stewardship — where
      the organization confirms readiness, the candidate confirms intent, and both parties remain empowered to surface conflicts
      before they harden into broken agreements. The pattern evolves through decline tracking and negotiation escalation,
      learning what thresholds actually work. It persists because it distributes authority to those closest to the decision
      (hiring managers, budget stewards) while maintaining transparency about what was promised and when.
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

> Set up clear checkpoints so offers and requests get the right approvals, everyone knows who decided what, and you can tr

> [!NOTE] Confidence Rating: ★★☆ (Observed)
> This pattern was derived from GraphRAG analysis of the Business domain.

---

### Section 1: Context

Every organization that brings new members into relationship must move through a sequence of commitments: from budgeted need to authorized requisition, from candidate screening to formal offer, from verbal agreement to binding documentation, from acceptance to coordinated start. These commitments span multiple actors (hiring managers, finance, legal, executives, the candidate themselves), involve irreversible decisions (headcount is allocated; the candidate may decline other offers), and carry asymmetric risk. The Commons Engineer inherits from two lineages: the governance principle that authority should be subsidiarily distributed, and the reciprocity principle that binding agreements require genuine consent from both parties. The tension is acute: early gates (requisition approval, verbal offer authorization) protect shared resources; late gates (acceptance confirmation, start date verification) protect the candidate from bad faith. Without nested gates, resources are wasted on non-viable offers. Without documented transitions, commitments dissolve into confusion and broken expectations.

---

### Section 2: Problem

> **The core conflict is Authority distribution vs. commitment clarity — how to disperse decision-making while ensuring every commitment is binding, auditable, and adaptive.**

Requisition-to-start workflows typically suffer from three interlocking failures. First, authority remains unclear or concentrated: who can approve a requisition? Can the hiring manager authorize a verbal offer, or must finance sign first? Second, consent is treated as event rather than process: the candidate's "yes" to a verbal offer is not the same as acceptance of a formal letter, which is not the same as confirmation of start date three months later. Organizations often discover at the last moment that a candidate has changed circumstances. Third, the workflow lacks adaptive capacity: when negotiation stalls, escalation paths are unclear; when offers decline, the organization learns nothing from the pattern of refusals; when start dates slip, there is no early warning gate. The result is either rigid bureaucracy (every offer must wait seven days for legal review, killing urgency) or chaos (verbal offers made without authorization, leading to budget overruns or legal exposure). The deeper tension: approval chains exist to protect shared resources and fair process, but they often destroy the very consent they aim to secure, because they introduce delay, opacity, and the sense that the decision is no longer in the candidate's hands.

---

### Section 3: Solution

Build a Nested Consent Stewardship workflow structured as a cascade of transparent, reversible gates, each with clear authority, explicit deadlines, and documented evidence of genuine agreement.

**Gate 1: Requisition Authorization.** The hiring manager submits a requisition with: role scope, budget line, business justification, and reporting structure. Authority is subsidiarily distributed by department and role level (a team lead can approve up to 3 requisitions/year; a director approves without limit; VP requisitions require CFO sign). Each approval is time-stamped and traceable. This gate confirms: do we have budget? Does this role align with strategy? Is the hiring manager ready to steward the process?

**Gate 2: Verbal Offer Authorization.** Before any offer—verbal or written—can be extended, a budget and hiring authority (usually the hiring manager's manager) must sign an explicit authorization form naming: the candidate, the proposed terms (salary, benefits, start date), and contingencies. This gate creates a paper trail and surfaces conflicts early. If the candidate later disputes what was promised, there is written evidence.

**Gate 3: Verbal Offer Validation.** If a verbal offer is given (common in high-velocity hiring), it must be followed within a defined window (usually 48 hours) by a formal offer letter that mirrors the verbal terms exactly. The candidate confirms: "This matches what was promised." Any discrepancy triggers renegotiation. This gate prevents the verbal-offer-creep where the written letter introduces surprise terms.

**Gate 4: Offer Acceptance Confirmation.** The candidate has a defined response window (typically 5-10 business days, extensible by mutual agreement). Acceptance must be documented: signed offer letter, email confirmation, or system-recorded click. The organization tracks acceptance deadline, decline reason (if declined), and any negotiation requests. This gate creates binding consent and gives the organization visibility into conversion rates and friction points.

**Gate 5: Contingency Clearance.** If the offer carries contingencies (background check, reference verification, skills assessment), these are tracked explicitly. The organization confirms: contingency met? Any new conditions arose? Both parties confirm clearance before the offer becomes fully binding. This prevents late surprises.

**Gate 6: Start Date Coordination.** As the start date approaches (typically 2-4 weeks before), the organization initiates a confirmation cadence: is the candidate still committed? Have circumstances changed? Is onboarding readiness confirmed (equipment ordered, access provisioned, workspace ready)? The candidate confirms: start date still viable? Any accommodation requests? This gate catches last-minute attrition and ensures both parties are genuinely ready.

**Adaptive Mechanisms:**
- **Decline Tracking & Learning**: Every declined offer is captured with reason category (compensation, role fit, timing, better offer, personal). The organization reviews patterns quarterly: are offers declining in certain departments? Are verbal offers declining more than written? This data feeds back into requisition approval thresholds and offer structuring.
- **Escalation Path for Impasse**: If negotiation stalls (candidate requests exceed authorization ceiling), there is an explicit escalation to the next authority level with a defined decision deadline (48 hours). This prevents offers from dying in ambiguity.
- **Reversibility & Transparency**: Every gate is visible to both parties. The candidate knows where in the workflow their offer sits, what approvals are pending, and what deadlines apply. This visibility creates psychological safety and reduces anxiety-driven withdrawals.
- **Documentation Chain**: Each transition (requisition approved → verbal offer authorized → acceptance confirmed → start date verified) generates a timestamped record. This serves both parties: the organization has evidence of authorization; the candidate has evidence of what was promised.

**Polycentric Authority Distribution:**
Authority is nested by organizational level: individual contributors' hiring is approved by team leads; manager positions by directors; executive positions by C-suite. Each level applies the same gate sequence but with different review intensity. This respects subsidiarity (decisions made at the level closest to the work) while maintaining coherence (the same values—authorization clarity, consent documentation, adaptive learning—apply everywhere).

The pattern succeeds because it treats approval not as a control mechanism but as stewardship: each gate asks "Are we ready to make this commitment, and is the candidate genuinely able to consent to ours?" It creates living value by evolving through feedback (decline data, escalation patterns) rather than remaining static. It shares governance by distributing authority subsidiarily while maintaining transparency. It serves justice by ensuring both parties have equal access to information about what was promised and when. And it is built to last because the sequence and the documentation become organizational memory, reducing reinvention and protecting future hiring from the mistakes of the past.

---

### Section 4: Implementation

Build your approval sequence as a series of cultivated moments, not hurdles.

**Start with a decision map.** Before you automate anything, sit with the people who actually make decisions: hiring managers, finance leads, legal, whoever touches your commitments. Map out: What must be decided? In what order? Who has authority at each gate? What information does each decision-maker need? Write it down. Messy is honest; perfect is fictional.

**Establish clear gate ownership.** Don't say "finance approves." Say "the finance lead for this department approves requisitions under $X; the CFO approves above that." Name the actual humans, or establish the role explicitly. Authority distributed vaguely is authority no one feels responsible for.

**Make reversibility explicit.** At each gate, document not just the yes, but under what conditions it could become a no. Can a requisition be paused if budget changes? Can a verbal offer be withdrawn if background check surfaces something material? State this clearly upfront. It builds trust because it's honest about what commitment actually means at each stage.

**Create documentation that serves, not just records.** Your requisition form, your offer letter template, your acceptance confirmation—these should tell a story someone could read six months later and understand why this person was hired, who approved it, and what was promised. Include: decision date, approver name and title, explicit scope (what is included, what is not), and the deadline for the next gate.

**Install a notification rhythm.** Don't let approvals languish in email inboxes. Set up a cadence where pending decisions are surfaced weekly. Use a simple tool—spreadsheet, Airtable, even a shared document—that everyone can see. Transparency reduces bottlenecks; bottlenecks breed informal workarounds.

**Practice small before scaling.** Test the full sequence with one hire. Let the awkwardness surface. Fix it. Then expand. You'll learn where the real friction lives—it's rarely where you thought.

### Section 5: Consequences

**What flourishes:** When approval is clear and auditable, trust grows in specific ways. Candidates feel respected—they know who decided to hire them and why. Finance can account for commitments without detective work. Legal has a chain of custody if disputes arise. Hiring managers learn to think upstream (what does finance need to know?) and downstream (what does the new hire need to feel real about this offer?). The organization develops institutional memory: you can see patterns in who approves what, where delays happen, and where authority actually lives (versus where the org chart says it lives).

**Risks if neglected:** Without clear gates, approval becomes a shadow process. Managers make verbal offers before requisitions are funded, then scramble to retrofit authorization. Finance approves money after candidates have already been promised it. Legal discovers contractual problems weeks into employment. This creates a second, invisible workflow—the workaround—where real decisions happen offline, and the formal process becomes theater. Candidates sense the dissonance and lose confidence. When something goes wrong (candidate doesn't show up, role gets defunded mid-hiring), no one can point to where the commitment broke, because the commitment was never made clearly in the first place. Cumulative effect: your approval process teaches people that process doesn't matter.

### Section 6: Known Uses

**Healthcare hiring (Kaiser Permanente model).** Large health systems with union contracts and strict licensing requirements have long used tiered approval: department request → HR screening → finance → credentialing → executive sign-off. Each gate has a documented owner and a hard deadline (sometimes contractually mandated). This slows things down slightly, but ensures that when a clinician starts, all compliance is done and the role is genuinely funded—critical in an environment where errors ripple to patient safety.

**Indian IT services (Infosys-style process).** Global IT service companies operating across multiple countries discovered early that approval delays were costing them top talent. They moved to a "parallel gate" model: finance and HR approve simultaneously rather than sequentially, with clear escalation rules if gates disagree. They also built in explicit candidate communication at each gate—the candidate knows requisition is approved, knows offer is pending background check, knows exact start date—reducing ghosting and uncertainty.

**Cooperative lending circles (Kenyan SACCO model).** In rotating savings and credit associations (SACCOs) common across East Africa, loan approval happens through social consent: members must hear the request, members can voice concerns, the group decides together. Documentation is often minimal, but authority and decision-making are radically transparent because they happen in a room together. The pattern shows that approval clarity doesn't require bureaucracy—it requires visibility and named responsibility.

### Section 7: Cognitive Era

AI and distributed intelligence reshape approval workflows in three ways.

First, **bots can handle gate traffic without replacing judgment.** An LLM can watch a requisition submission, check it against your decision map, flag missing information, and route it to the right approver—all before a human touches it. This surfaces bottlenecks without creating new ones. But the authority to approve remains human and local; the AI is a traffic controller, not a decision-maker.

Second, **distributed teams need async-first approval.** When your hiring manager is in Singapore and your finance lead is in São Paulo, sequential gates become time-zone death marches. Parallel gates—where multiple approvers work simultaneously, surfacing conflicts only if they exist—become essential. AI can orchestrate this: "Finance approved at 2am UTC; waiting on legal; here's what they'll need to decide." The pattern itself stays the same; the rhythm changes.

Third, **approval becomes more adaptive and less binary.** Instead of yes/no at each gate, you can have "yes, with conditions" or "approved for 3 months, then reassess." An LLM trained on your organization's hiring data can flag: "This requisition matches roles that usually get defunded by month 6—flag for finance to commit to full-year funding upfront." Approval becomes diagnostic rather than just permissive.

The deeper shift: as more decisions are automated or AI-assisted, approval workflows matter *more*, not less. They become the human layer that keeps AI recommendations grounded in accountability. Who approved this hire? becomes as important as Did the ML model suggest this hire?

### Section 8: Vitality

**Signs of life:**
- Candidates can tell you, weeks after joining, who approved their hire and roughly when each decision happened. (They felt seen, not processed.)
- Finance can pull a report of approved requisitions and map them to actual hires, with few orphans or mysteries.
- When a hiring delay happens, the teams can point to which gate is stuck and why—and can make a deliberate choice to escalate or wait.
- Hiring managers use the approval sequence to think better (not just faster): "What does finance need from me?" surfaces real questions about scope and budget.
- Your approval process is actually used, not bypassed. People aren't making informal verbal offers because they don't trust the formal process.

**Signs of decay:**
- Candidates say, "I'm still not sure who actually hired me or when it's official."
- Finance has a growing portfolio of "mysterious" expenses that don't map to headcount.
- Hiring is slow, with no clear explanation for where the delays live.
- Managers circumvent the approval process because it feels like bureaucracy, not decision-making.
- Your documentation is thorough but no one reads it; it's filed away, not used.

**The diagnostic question:**
*If a candidate asked you, "Walk me through exactly who decided to hire me, in what order, and why," could you do it clearly, or would you fumble?*

If you'd fumble, your approval workflow isn't serving clarity yet. Not every organization needs a complex process, but every organization needs one where someone can retrace the path.
