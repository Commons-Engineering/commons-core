---
id: pat_1a3419cc8b084844a4b364b2
orbital_layer: 2
sector: Business
gravitational_hubs:
- hub_id: cooperative-surplus-alignment
  principle: Cooperation Creates Surplus
  influence: 0.7
- hub_id: visibility-as-commons-act
  principle: Visibility as Commons Act
  influence: 0.7
- hub_id: incentives-self-interest
  principle: Channel Self-Interest
  influence: 0.7
- hub_id: polycentric-fractal-organisation
  principle: Power at Every Scale
  influence: 0.7
- hub_id: truth-seeking-transparency
  principle: Truth-Seeking Sustains Systems
  influence: 0.7
slug: selling-what-actually-fits
title: Selling What Actually Fits
aliases: []
summary: Help customers find products that genuinely solve their problems instead of pushing whatever generates the most profit.
  Make opportunities visible and governed so growth feels earned, not forced.
context_labels: {}
ontology:
  domain: cross-sell-upsell-operations
  cross_domains: []
  search_hints:
    primary_tension: Extractive growth (maximizing revenue per customer) vs. Reciprocal growth (deepening customer value and
      loyalty)
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
    vitality_reasoning: This pattern creates living value by making the relationship ecosystem visible and collectively stewarded.
      Rather than treating cross-sell as a unidirectional extraction mechanism, it distributes knowledge of customer needs,
      product fit, and pricing fairness across the organization. Teams see the whole product relationship map, constraints
      are explicit (margin thresholds, cannibalization limits, brand integrity), and feedback loops adjust what gets recommended
      based on real customer outcomes—not just conversion metrics. The pattern evolves as customer needs and product offerings
      change, stays just by aligning incentives with genuine complementarity, and persists because it builds trust rather
      than transactional friction.
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

> Help customers find products that genuinely solve their problems instead of pushing whatever generates the most profit. 

> [!NOTE] Confidence Rating: ★★☆ (Observed)
> This pattern was derived from GraphRAG analysis of the Business domain.

---

### Section 1: Context

Organizations selling multiple products or services to existing customers face a design challenge: how to identify and execute growth opportunities without damaging the relationship or extracting value faster than the customer receives it. This happens across sectors—software platforms, retail, marketplace sellers, account-based businesses. The gravitational centre is recognition that every customer carries latent needs, and every product relationship exists in a network (some products complement, some substitute, some are independent). This network is not visible by default. The organization must make it collectively visible—naming standards, substitutability maps, pricing logic, governance boundaries—so that frontline teams, sales, and customer success can navigate the landscape together. Lineage: Channel Self-Interest (align what we measure with what serves customers), Visibility as Commons Act (make the product graph and decision rules transparent), Cooperation Creates Surplus (identify where additional products genuinely create more value for customer and company together).

---

### Section 2: Problem

> **The core conflict is Extractive growth (maximizing revenue per customer) vs. Reciprocal growth (deepening customer value and loyalty).**

Three forces collide: (1) Organizations measure and incentivize revenue velocity and attachment rates, creating pressure to recommend broadly and quickly. (2) Sales and support teams lack visibility into which products actually fit which customers, and lack shared rules for pricing and naming—so recommendations feel arbitrary or aggressive. (3) Customers experience cannibalization (sold substitute products), margin-hostile pricing (low-margin recommendations that look like growth but aren't), and compliance violations (marketplace brand misalignment). The underlying tension: if the organization optimizes for recommendation volume or conversion rate alone, it extracts short-term revenue at the cost of long-term customer fit and trust. If it optimizes for customer value alone, it leaves genuine opportunities unrecognized. The system becomes opaque, fragmented, and misaligned.

---

### Section 3: Solution

Build a visible, governed, evolving Product Relationship Stewardship system with these interlocking elements:

**STRUCTURE THE KNOWLEDGE (Make It Visible):** Create a Product Relationship Matrix that maps every product or service against every other—showing substitutability (can this replace that?), complementarity (do they work together?), independence, and cannibalization risk. Document pricing logic for each relationship: what margin threshold triggers approval? When does pricing favor customer value perception over revenue extraction? Document brand and compliance constraints (marketplace requirements, regulatory limits). Make this matrix live and transparent across all teams. Every frontline practitioner sees the same map.

**DISTRIBUTE OPPORTUNITY IDENTIFICATION (Localize Authority):** Enable every team that touches customers—sales, support, account management—to flag cross-sell opportunities using the matrix as a guide. Create a lightweight flagging rule: if customer has Product A, and the matrix shows Product B as complementary with margin >threshold and no cannibalization risk, flag for consideration. This is subsidiarity: the person closest to the customer makes the initial nomination. Do not centralize opportunity identification in a separate engine.

**DESIGN APPROVAL AS LEARNING, NOT GATEKEEPING:** When an opportunity is flagged, route it through a lightweight approval workflow that asks: Does this genuinely serve the customer? Does it fit the product relationship logic? Is the pricing fair by our standards? Does it comply? If yes, approve and execute. If no, return with reasoning. Measure not conversion rate but *approval rate, execution speed, and customer outcome*—did the customer renew? Expand? Stay loyal? This reverses the incentive: teams are rewarded for recommendations that stick and deepen the relationship.

**MAKE PRICING A SHARED CONSTRAINT, NOT A VARIABLE:** Establish pricing nomenclature and logic rules that all teams follow. Example: "Complementary products to existing customers receive a 15% bundle discount; substitute products are not recommended; pricing never undercuts margin thresholds for this customer segment." Write it down. Make it visible. When a salesperson proposes a price, they check the rule first. This prevents margin-hostile recommendations and builds trust with customers (pricing feels consistent and fair).

**CLOSE THE FEEDBACK LOOP:** Track attachment rate, yes—but *also* track customer renewal, expansion velocity (speed of moving customers to higher-value products), and relationship health scores. If attachment rate rises but renewal falls, the system is recommending too aggressively or wrongly. Adjust the matrix, the approval rules, or the flagging criteria. This is adaptive management: treat the cross-sell system as an experiment with hypotheses about what recommendations create cooperative surplus.

**STEWARD THE ECOSYSTEM:** Appoint a small governance body (product, sales, customer success, compliance) that owns the Product Relationship Matrix, pricing logic, and approval rules. Meet monthly. Review flagged opportunities that were declined; review customer feedback about recommendations; evolve the rules. This is polycentric governance: no single function owns the decision, but all are represented in evolving it.

The result: Cross-sell becomes a visible, fair, collectively stewarded growth mechanism. Teams have clear maps and constraints. Customers see genuine complementarity, not aggressive extraction. The organization grows by deepening relationships, not maximizing conversion per transaction.

---

### Section 4: Implementation

Start by mapping what you already know but haven't yet named. Gather your sales team, support team, and product leads in one room (or async workspace) with a simple prompt: *Which products have you seen hurt each other? Which ones make each other stronger?* You'll uncover buried patterns—the upsell that always leads to churn, the bundle that delights, the recommendation that creates confusion.

Build your Product Relationship Matrix as a living document, not a frozen spreadsheet. Use a simple structure: rows are products, columns are other products, cells capture the relationship type (substitute, complement, independent, cannibalizes) plus a short note on when and why. Include pricing tiers, target customer sizes, and use cases. Make it visible to everyone who talks to customers—not hidden in a database.

Next, establish **recommendation governance**: explicit rules for when and how to suggest additional products. These might read like:
- "Offer Product B only to customers using Product A for more than 3 months"
- "If a customer licenses Feature X, they qualify for Tier 2, not Tier 3"
- "Never sell both A and C to the same customer unless they have explicit use-case separation"

Train sales and support to see themselves as relationship stewards, not slot machines. Give them language: *"This might not be right for you yet, but here's what would unlock it"* or *"These two solve the same problem—let's figure out which one fits."*

Establish a monthly or quarterly review cadence where you examine win/loss data, churn patterns, and customer feedback against your matrix. When you notice a recommendation pattern that's failing, update the rules. When you discover a new complementarity, document it. This keeps the system alive and truthful.

Finally, tie compensation and metrics to relationship health metrics—retention, expansion revenue per customer, customer satisfaction—not just attachment rate or cross-sell velocity. Align the incentive with the intent.

### Section 5: Consequences

When this pattern takes root, several things flourish. Customers feel genuinely advised, not preyed upon. They're more likely to expand willingly because they've experienced genuine fit. Retention improves because you're solving real problems, not creating debt. Your team operates with confidence because the rules are transparent—they know when a recommendation is legitimate. Word-of-mouth strengthens because customers trust your judgment.

Inside the organization, you reduce friction between sales and customer success. Both teams work from the same Product Relationship Matrix, so handoff conversations become easier. You also reduce internal politics—arguments about cross-selling give way to data-driven governance.

But there are real risks if this pattern isn't tended. The matrix can calcify, becoming dogma instead of living knowledge. If you stop updating it, you'll miss genuine new complementarities or fail to remove obsolete cannibalization fears. Teams can revert to old habits—the incentive structure you've created can be quietly undermined by commissions or targets that slip back toward pure attachment.

There's also a subtler risk: if your governance rules become *too* restrictive, you'll miss legitimate upsells. A customer might genuinely be ready for Product B, but your rules say "not yet," and so the recommendation never surfaces. You'll need active judgment, not just rule-following.

Finally, customers can sense when a stewardship posture is performative. If you've built the matrix and governance but still push products that don't fit, you'll damage trust more than if you'd never tried.

### Section 6: Known Uses

**Basecamp** (project management software) famously narrowed their product line and made explicit choices about what they would *not* sell together. They documented that their email tool solves a different problem than their messaging tool and built governance around when each made sense. This reduced feature bloat, simplified their sales conversations, and deepened customer loyalty. Sales teams stopped fighting with each other about which tool to push.

**Patagonia** (outdoor retail and apparel) has long practiced a form of product relationship stewardship by refusing to sell products that cannibalize or substitute poorly with their core mission. They'll recommend competitors' products if they're better-fitted to a customer's actual need. This counterintuitive practice—recommending *against* your own products—has built legendary customer trust and actually increased lifetime value.

**M-Pesa** (mobile money platform in Kenya) built its ecosystem by carefully governing which financial products and services could be layered on top of the base platform. They were explicit about which products complemented the core wallet experience and which would cannibalize it. Third-party developers operated within transparent rules about what fit. This prevented the chaos that often follows rapid product proliferation in emerging markets and kept the platform trustworthy and coherent.

### Section 7: Cognitive Era

AI amplifies both the power and the risk of this pattern. With machine learning, you can build *predictive* product relationship matrices—systems that learn which products genuinely fit which customers based on behavioral signals, not just rules you've written. This is powerful: a recommendation engine can surface the right product at the right moment, making stewardship feel intuitive and effortless.

But this same capability makes the pattern more fragile. If your AI system optimizes for attachment rate rather than customer fit, it will weaponize itself—learning to make increasingly sophisticated arguments for products that harm the relationship. The matrix becomes invisible, buried in weights and gradients.

The antidote is to keep the governance *legible*. Don't let the AI become a black box. Use it to surface patterns and suggest rules, but require your human teams to understand and debate those rules. Make the Product Relationship Matrix explainable: "Why did the system recommend Product B?" should have a human-readable answer, not just a probability score.

In distributed organizations and platform ecosystems, this becomes harder. You're no longer controlling all the products; third parties are. Your job shifts from governing the matrix to *democratizing* access to it—making sure every partner can see the relationship rules you've established, so they align their recommendations too.

### Section 8: Vitality

**Signs of life:** Your sales team spontaneously uses language like *"Let's check if that fits"* rather than *"Let me add that to your plan."* Customers upgrade without prompting because they've experienced genuine value and the next step feels obvious. Your Product Relationship Matrix gets updated monthly because new patterns emerge and you're paying attention. When a customer churns, you can trace it back to a recommendation that didn't fit—and you learn from it. Compensation structures reward long-term customer health, not short-term attachment velocity. Your support team feels trusted to redirect customers away from products that don't fit.

**Signs of decay:** Your sales team has reverted to aggressive cross-selling. The Product Relationship Matrix exists but hasn't been updated in 6+ months. Customers complain that they're sold things they didn't need. Churn accelerates after upsells. Your incentive structures still reward pure revenue attachment, creating incentive drift. Internal conflicts re-emerge between sales and customer success about what to recommend. Customers describe your approach as "predatory" or "pushy" in reviews or conversations.

**Diagnostic question:** If you asked your customers *"Did [Company] recommend something that didn't work out for you?"* what percentage would say yes? If it's more than 15-20%, the pattern has broken. If it's near zero, you may be being *too* conservative. The sweet spot is customers feeling advised, not constrained—they sense you're looking out for them, even when that means sometimes saying no.
