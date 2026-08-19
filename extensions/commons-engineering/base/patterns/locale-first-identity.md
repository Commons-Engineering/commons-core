---
# ═══════════════════════════════════════════════════════════════════
# GROUP 0: ARCHITECTURAL POSITION (The Gravity Well)
# ═══════════════════════════════════════════════════════════════════
id: pat_01kkhc8hcwxj08z6nxhr34et2s
orbital_layer: 2
sector: "Universal"
gravitational_hubs:
  - hub_id: "core_subsidiarity"
    influence: 0.9
  - hub_id: "core_identity"
    influence: 0.85
  - hub_id: "core_resilience"
    influence: 0.7

# ═══════════════════════════════════════════════════════════════════
# GROUP 1: CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════
slug: locale-first-identity
title: "Locale-First Identity"
aliases: ["Language as First Decision", "The Boot Language Question", "Cultural-Canonical Split"]
summary: >-
  The first identity decision a commons makes is language — the agent
  speaks the language of the community it serves. Canonical identifiers
  (slugs, YAML keys, file names) remain in English for global
  interoperability. Human-facing content — labels, narratives,
  governance documents, onboarding prompts — is localised from boot.
  This is not internationalisation bolted on later. It is the
  recognition that language carries culture, and culture is the
  medium through which a commons lives.

# ═══════════════════════════════════════════════════════════════════
# GROUP 2: CONTEXTUAL TRANSLATION (The Navigator Engine)
# ═══════════════════════════════════════════════════════════════════
context_labels:
  corporate: "Localisation Strategy and Cultural Fit"
  government: "Multilingual Public Service Delivery"
  activist: "Speaking the Language of the Movement"
  tech: "i18n/l10n Architecture from Day One"
  academic: "Vernacular Knowledge Systems"

# ═══════════════════════════════════════════════════════════════════
# GROUP 3: ONTOLOGY & SEARCH OPTIMIZATION (The RAG Fuel)
# ═══════════════════════════════════════════════════════════════════
ontology:
  domain: commons-engineering
  cross_domains: [life, business, urban, ecology]
  commons_domain:
    - commons-engineering
  search_hints:
    primary_tension: "Global Interoperability vs. Local Expression"
    vector_keywords: ["locale", "language", "identity", "i18n", "localisation",
                      "cultural fit", "boot sequence", "canonical identifiers",
                      "multilingual", "subsidiarity", "vernacular",
                      "commons operating system", "onboarding"]
  commons_assessment:
    stakeholder_architecture: 5
    value_creation: 4
    resilience: 5
    ownership: 5
    autonomy: 5
    composability: 4
    fractal_value: 5
    vitality: 4.7
    vitality_reasoning: >-
      Language is the carrier wave of culture. A commons that speaks
      only English — or only any single language — excludes by default.
      Locale-first identity ensures that the operating system adapts to
      the community rather than forcing the community to adapt to the
      system. This is subsidiarity enacted at the most fundamental
      interface layer: the words on the screen, the prompt in the
      terminal, the labels on the governance documents. The vitality
      score is high because this pattern determines whether a commons
      feels like home or like a foreign institution from the first
      interaction.
    overall_score: 4.7

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
    - slug: cultural-meaning-and-shared-purpose
      weight: 0.9
    - slug: subsidiarity-and-local-empowerment
      weight: 0.85
  specializes_to:
    - slug: commons-blueprint
      weight: 0.8
    - slug: community-and-participation-model
      weight: 0.75
  enables:
    - slug: fork-template-setup-chain
      weight: 0.9
    - slug: agent-seat-at-the-table
      weight: 0.8
    - slug: community-as-resilience
      weight: 0.85
    - slug: observer-to-participant
      weight: 0.8
  requires:
    - slug: commons-boundary-definition
      weight: 0.85
    - slug: purpose-definition
      weight: 0.8
  alternatives: []
  complementary:
    - slug: intranet-extranet-publishing
      weight: 0.85
    - slug: transparency-and-openness-protocol
      weight: 0.8
    - slug: legitimacy-and-consent
      weight: 0.75
  tools:
    - slug: gettext
      type: framework
    - slug: icu-message-format
      type: standard

# ═══════════════════════════════════════════════════════════════════
# GROUP 6: GRAPH GARDEN (Machine-Written Graph)
# ═══════════════════════════════════════════════════════════════════
graph_garden:
  last_pruned: 2026-03-12
  entities:
    - id: locale-identity
      type: concept
      label: "Locale as Identity"
      relevance: 1.0
    - id: canonical-english-layer
      type: practice
      label: "Canonical English Layer"
      relevance: 0.95
    - id: cultural-carrier-wave
      type: concept
      label: "Language as Cultural Carrier"
      relevance: 0.95
    - id: boot-language-question
      type: practice
      label: "Boot Language Question"
      relevance: 0.9
    - id: subsidiarity-at-interface
      type: systemic-pattern
      label: "Subsidiarity at the Interface Layer"
      relevance: 0.9
  communities:
    - commons-os-foundations
    - commons-engineering-foundations
    - localisation-practice
  inferred_links:
    - target: fork-template-setup-chain
      reason: "Shared entities: Boot Language Question, locale configuration in setup"
      strength: 5
    - target: community-and-participation-model
      reason: "Shared entities: Cultural Carrier, Subsidiarity at Interface"
      strength: 4
    - target: commons-boundary-definition
      reason: "Shared entities: Locale as Identity defines boundary of expression"
      strength: 4
    - target: agent-seat-at-the-table
      reason: "Shared entities: Agent speaks the language of the community"
      strength: 4

# ═══════════════════════════════════════════════════════════════════
# GROUP 7: PROVENANCE
# ═══════════════════════════════════════════════════════════════════
contributors: ["higgerix", "cloudsters"]
sources:
  - "Commons Engineering Framework"
  - "Commons OS Specification v0.1"
  - "EU Multilingualism Policy — 24 official languages, subsidiarity in practice"
  - "GNU gettext — the original i18n architecture (1995)"
  - "ICU Message Format — Unicode CLDR"
  - "Wikipedia multilingual edition architecture"
license: CC-BY-SA-4.0
attribution: "commons.engineering by cloudsters, https://cloudsters.net"
collection: commons-os
collection_ring: operating-patterns
7cs_arc: [clarity, commons, community]
---

> The first question a commons asks is not "What do you want to do?" but "In welcher Sprache arbeitest du?" — because the language of the question determines who feels invited to answer.

> [!NOTE] Confidence Rating: ★★★ (High)
> The principle that language determines inclusion is validated across every multilingual institution, from the European Union's 24-language policy to Wikipedia's 300+ language editions to the internationalisation architectures of every major software platform. The specific architectural split — canonical English identifiers for interoperability, localised human-facing content for belonging — is proven practice in software engineering (gettext, ICU, CLDR) and is now applied to the operating system of a commons.

---

### Section 1: Context

Every commons serves a community, and every community has a language. Not a language in the abstract — a specific, living, culturally loaded way of expressing thought, feeling, and intention. When a farmer in Schleswig-Holstein reads governance documents, they read German. When a neighbourhood council in Barcelona deliberates, they deliberate in Catalan. When a developer collective in Nairobi coordinates, they may use English, Swahili, or Sheng — depending on the context, the audience, and what feels right.

Software systems have dealt with this reality for decades under the banner of internationalisation (i18n) and localisation (l10n). The pattern is mature: separate the content that changes by locale from the structure that stays constant. Use message catalogues, format libraries, and locale-aware rendering. Ship the structure once, localise the content per audience.

But in most systems, localisation is an afterthought. The system is built in English, by English-speaking teams, with English assumptions about date formats, name structures, reading direction, and cultural metaphors. Localisation is then bolted on — translation files added, right-to-left support patched in, date formats adjusted. The result works, but it never feels native. The system speaks your language the way a tourist speaks it: correctly enough to be understood, but never as if it belongs.

A commons cannot afford this. A commons is, at its foundation, a social practice — a community that governs shared resources together. If the operating system of that commons does not speak the community's language natively, it creates a distance between the system and the people it serves. That distance is not just inconvenient — it is a governance failure. People who do not feel at home in the system do not participate fully in its governance.

The Locale-First Identity pattern addresses this by making language the first decision in the boot sequence of any commons. Not the second decision, not a configuration option to be set later, but the very first question the system asks.

---

### Section 2: Problem

> **The core conflict is Global Interoperability vs. Local Expression.**

The forces pulling toward a single global language and the forces pulling toward local expression are both legitimate, and the tension between them cannot be resolved by choosing one side. It must be architecturally dissolved.

**Force 1: The English default.** The infrastructure of the modern internet — programming languages, protocols, package managers, Git, GitHub, YAML — is built in English. Technical identifiers must be ASCII-safe. Slugs, file names, and machine-readable keys work best in English. A pattern called `nachhaltigkeits-bewertung` breaks tooling, confuses search, and creates interoperability problems with every system that expects Latin-1 identifiers. The pull toward English as the canonical layer is not cultural imperialism — it is infrastructure pragmatism.

**Force 2: The belonging imperative.** A commons that speaks only English excludes every community whose primary language is not English. More subtly, it excludes the cultural concepts that do not translate cleanly. The German word "Werkstatt" carries connotations — a craftsman's workshop, a place of making, the smell of wood and the discipline of joints — that "workshop" in English does not. The Japanese concept of "ba" (a shared space for emerging relationships) has no English equivalent. When a commons forces English on its human-facing content, it flattens the cultural richness that makes communities distinctive.

**Force 3: The translation maintenance burden.** Every localised string is a maintenance obligation. When the canonical content changes, every translation must be updated. Incomplete translations create a patchwork experience — some labels in the local language, some in English, some missing entirely. The cost of maintaining localisation scales with the number of languages supported and the rate of content change.

**Force 4: The cultural assumption layer.** Language is only the visible surface of culture. Beneath the words lie assumptions about formality (du/Sie in German, tu/vous in French), about name structure (family name first in East Asia), about date formats (DD.MM.YYYY in Europe, MM/DD/YYYY in the US), about number formats (1.000,00 vs 1,000.00), about reading direction, about colour symbolism, about what metaphors resonate. A locale-first identity that addresses only word translation misses the deeper layer.

**Force 5: The agent language question.** In a commons operated with AI agents, the language question extends beyond interface labels. The Purpose Agent that governs the commons must converse in the community's language. The prompts, the deliberation records, the governance summaries — all of these must be in the locale. An AI agent that governs in English while the community speaks German creates a colonial dynamic, however unintentionally.

---

### Section 3: Solution

> **Therefore, make language the first identity decision in the boot sequence of every commons. Maintain a strict architectural split: canonical identifiers in English for interoperability, human-facing content in the community's locale for belonging.**

The Locale-First Identity pattern resolves the tension through a two-layer architecture:

**Layer 1: The Canonical Layer (English, machine-readable).** All structural identifiers — pattern slugs, YAML keys, file names, Git branch names, API endpoints, dimension names in code — remain in English. This is non-negotiable for interoperability. The canonical layer is the skeleton: it provides the structure that allows different commons instances to interoperate, share patterns, and use common tooling regardless of their locale.

**Layer 2: The Locale Layer (community language, human-readable).** All content that a human reads, speaks, or writes — labels, titles, descriptions, governance documents, onboarding prompts, agent conversations, blueprint narratives, value stream names in the UI — is rendered in the community's locale. This is not a translation of the English content. It is the primary expression, authored in the community's language with the community's cultural concepts, and mapped to the canonical identifiers through a locale registry.

**The Boot Question.** The very first interaction in the setup chain of a new commons is the locale question: "In welcher Sprache arbeitest du?" / "What language do you work in?" / "En quelle langue travaillez-vous?" This question appears in multiple languages simultaneously — a polyglot greeting that signals: this system will speak your language. The answer configures the entire runtime: agent prompts, UI labels, document templates, governance frameworks, date and number formats.

**The Agent Language Contract.** Every agent in the commons — Purpose Agent, Participation Agent, Proposition Agent, Production Agent — converses in the configured locale. Their system prompts include locale-aware instructions. Their outputs are in the community's language. When they reference canonical identifiers (pattern slugs, dimension keys), they use the localised display names, with the canonical slug available as metadata for interoperability.

---

### Section 4: Implementation

**Step 1: Define the locale registry structure.** Create a locale registry at `.commons/locales/` that maps canonical identifiers to localised strings. The structure follows the established i18n pattern of key-value pairs organised by namespace:

```yaml
# .commons/locales/de.yml
commons:
  dimensions:
    purpose: "Definition & Bestimmung"
    agents: "Beteiligung & Beziehung"
    offers: "Angebot & Austausch"
    operations: "Produktion & Resilienz"
  boot:
    welcome: "Willkommen in deinem Commons."
    language_question: "In welcher Sprache arbeitest du?"
  agents:
    purpose_agent: "Bestimmungs-Agent"
    participation_agent: "Beteiligungs-Agent"
    proposition_agent: "Angebots-Agent"
    production_agent: "Produktions-Agent"
```

**Step 2: Configure the boot sequence.** The setup script (`setup.sh` or equivalent) includes the locale question as its first interactive step. The selected locale is written to `.commons/identity.yml` as the `locale` field. All subsequent setup steps — label creation, document generation, agent configuration — use the locale registry to render in the selected language.

**Step 3: Configure agent prompts.** Each agent's system prompt includes a locale directive: "You converse in [locale]. You use the localised display names for all dimensions, value streams, and governance concepts. When referencing canonical identifiers for technical interoperability, you note them parenthetically." This ensures that agent output feels native, not translated.

**Step 4: Establish the locale contribution workflow.** New locales are contributed as pull requests to the upstream commons template. A locale file must reach a minimum coverage threshold (all boot strings, all dimension names, all agent role descriptions) before it is accepted. Partial translations are accepted for non-critical namespaces (pattern descriptions, extended documentation) with a graceful fallback to English for untranslated strings.

**Step 5: Implement the fallback chain.** When a localised string is missing, the system falls back through a defined chain: regional variant (de-AT → de) → language family → English canonical. This ensures that partial translations produce a usable experience rather than broken labels. The fallback is logged so that missing translations can be identified and contributed.

**Step 6: Handle the cultural layer beyond words.** The locale configuration extends beyond string translation to include: date format, number format, name display order, formal/informal address preference (relevant for agent tone), reading direction, and culturally appropriate metaphors in onboarding narratives. These are configured in the locale file under a `culture` namespace.

---

### Section 5: Consequences

**What this pattern creates:**

A commons that speaks the community's language from the first interaction. The boot experience feels native — not translated, not foreign, not colonially English-with-a-veneer. Governance documents are in the language that community members think in, which means they engage more deeply with governance. Agent conversations feel like talking to a colleague, not to a foreign system.

The canonical English layer ensures that the global commons network remains interoperable. A pattern authored in a German-speaking commons can be discovered, referenced, and adapted by a Spanish-speaking commons because the canonical slug, the YAML keys, and the API endpoints are shared. The locale layer adds belonging without sacrificing connectivity.

The pattern also creates a contribution pathway for communities: authoring a locale file is a meaningful contribution to the commons that requires cultural knowledge, not just technical skill. A German speaker who writes the `de.yml` locale file is encoding cultural intelligence into the operating system — this is a form of stewardship.

**What this pattern risks:**

Translation drift — when the canonical content evolves but locale files lag behind, creating inconsistency between what the system says in English and what it says in the localised version. The mitigation is the locale coverage check: a CI step that flags untranslated or outdated strings after canonical content changes.

Cultural flattening through standardisation — the risk that the locale file format is too rigid to capture the full cultural nuance of a language. The mitigation is to treat locale files as living documents that communities can extend with custom namespaces beyond the required core.

Over-engineering for a single-language commons — many commons will operate in a single language and never need the full locale infrastructure. The mitigation is simplicity: a single locale file and a configured default require minimal overhead. The architecture is present but not burdensome.

---

### Section 6: Known Uses

**GNU gettext (1995-present).** The original internationalisation architecture for free software. gettext established the pattern that is now universal: source strings in the developer's language (English), message catalogues for each locale, runtime lookup by locale setting. Thousands of software projects use this architecture. The Commons OS locale registry follows the same structural principle, adapted for a governance operating system rather than a desktop application.

**Wikipedia multilingual editions.** Wikipedia operates 300+ language editions, each with its own community, governance, and editorial standards. The canonical concept (an article about a topic) is shared across editions through Wikidata identifiers. The content is independently authored in each language — not translated, but natively written by speakers of that language. This is the gold standard for locale-first identity at scale: shared structure, native expression.

**European Union multilingualism policy.** The EU operates in 24 official languages. Every regulation, every directive, every public communication is available in all 24 languages — not as translations of a single original, but as equally authoritative versions. The canonical identifier (the regulation number) is shared; the legal text is native in each language. This policy is expensive and complex, but it is the foundation of legitimacy in a union of diverse linguistic communities.

**ICU Message Format and Unicode CLDR.** The International Components for Unicode (ICU) project and the Common Locale Data Repository (CLDR) provide the technical infrastructure for locale-aware content across all major software platforms. Date formats, number formats, pluralisation rules, name structures — all encoded per locale. The Commons OS builds on this infrastructure rather than reinventing it.

---

### Section 7: Cognitive Era

The Cognitive Age transforms the locale question from a content problem into a cognition problem. When AI agents govern a commons — holding purpose, facilitating deliberation, summarising decisions — they must think and speak in the community's language. This is not a translation layer applied to English-language reasoning. Modern large language models are multilingual by training; they can reason, compose, and converse in dozens of languages natively.

The implication for commons design is significant: the agent's system prompt, its context window, its governance summaries, and its deliberation records should all be in the community's locale. A Purpose Agent governing a German-speaking commons should not reason in English and translate — it should reason in German, using German governance concepts, German formality conventions, and German cultural metaphors.

This also opens the possibility of real-time locale bridging: when two commons instances need to interoperate (a German commons and a Brazilian commons collaborating on a shared pattern), the agents can mediate the translation, using the canonical English layer as the bridge and the locale layers as the native interfaces. The human participants speak their own languages; the agents handle the interoperability.

The risk in the Cognitive Age is the assumption that AI translation eliminates the need for locale-first design. It does not. Translation is not belonging. A commons that is "available in German via translation" is not the same as a commons that "speaks German." The difference is felt at the level of ownership: do the German-speaking participants feel that this is their system, or do they feel that they are guests in an English system with a German interface?

---

### Section 8: Vitality

**Signs of life:**

A commons with healthy locale-first identity has a distinctive quality: its governance conversations feel natural. Participants write issues, comments, and proposals in their own language without hesitation. Agent responses read as if authored by a native speaker, not as if machine-translated from English. The locale file is actively maintained — new terms are added as the commons evolves, cultural nuances are refined, and the community takes pride in the quality of their localisation.

The strongest vitality signal is locale contribution from the community itself. When community members proactively improve the locale file — suggesting better terms, adding cultural context, correcting formality levels — it means they have taken ownership of how their commons speaks. The operating system has become theirs.

Another signal is the graceful handling of untranslatable concepts. A vital locale does not force every English term into translation. Some concepts — "commons," "pattern," "blueprint" — may be adopted as loanwords if the community decides they carry the right meaning. The locale file documents these decisions with rationale, creating a cultural record of how the community made the language its own.

**Signs of decay:**

Decay in locale-first identity looks like creeping English. Labels that were once localised start appearing in English because the locale file was not updated. Agent responses mix languages — a German sentence with English technical terms that have perfectly good German equivalents. New features ship with English-only labels and a TODO comment that never gets resolved.

The deeper decay is cultural: the community stops caring about the locale. They accept English defaults because updating the locale file feels like overhead rather than stewardship. This signals that the commons has become a technical system rather than a cultural practice — the language has shifted from "ours" to "theirs, which we use." The recovery requires recommitting to locale maintenance as a governance activity, not a technical chore — ideally by assigning locale stewardship to the Participation Agent (D2), who understands that language is the foundation of community identity.
