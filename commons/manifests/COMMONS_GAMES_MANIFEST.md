# COMMONS GAMES MANIFEST
*The Simulation Laboratory for Living Systems*

**Version:** 0.2
**Status:** Living Document
**Companion:** COMMONS_OS_MANIFEST.md, COMMONS_DOMAINS_MANIFEST.md, COMMONS_BLUEPRINT_MANIFEST.md

---

## Preamble: The World We Build to Understand the World We Want

Science fiction shaped the 20th century. The devices in our pockets, the networks we communicate through, the interfaces we touch -- all were imagined in fiction before they were engineered in reality. Fiction is not prediction. It is rehearsal. When a culture rehearses a future often enough, it develops the vocabulary, the intuitions, and the courage to build it.

Commons Engineering needs its own rehearsal space.

Not a whiteboard. Not a document. Not a scenario workshop that produces insights and then closes. A living, running, breathing world where autonomous commons operate, trade, federate, compete, fail, split, merge, and evolve -- governed by the same Commons OS that real-world commons will use, stressed by the same forces they will face, and producing the same artefacts (Blueprints, patterns, entities, value streams) that the real world needs.

commons.games is that world.

It is not a game in the entertainment sense. It is a simulation laboratory where the Commons OS is tested against reality before reality tests it against us. Every commons instance in the simulation runs the actual OS. Every pattern it uses comes from the actual pattern library. Every capability it needs and does not find becomes a pull request back to commons.engineering. Every failure it suffers becomes a pattern in the library for others to avoid.

The simulation is the proving ground. The real world is the deployment. commons.games and commons.domains are the two halves of one feedback loop.

---

## S1 What commons.games Is

commons.games is a **persistent, AI-operated world simulation** in which autonomous commons instances operate, interact, and evolve within a shared environment.

The simulation has the following properties:

**Persistent.** The world does not reset between sessions. Commons that are founded persist. Commons that fail leave debris. Reputation accumulates. Ecological parameters evolve. The simulation has memory -- and that memory is the most valuable thing it produces, because it is the history of what worked and what did not.

**AI-operated.** Every commons in the simulation is operated by AI agents following the four-agent governance model (Purpose, Participation, Proposition, Production). Human stewards observe, intervene when governance breaks down, and harvest patterns. Humans are not players. They are gardeners.

**World simulation.** The environment is a simplified model of Earth: real cities as nodes, simulated organisations as participants, ecological parameters as constraints, and a token economy as the medium of exchange. The simplification is deliberate -- complex enough to produce real governance problems, simple enough to understand the causes when things break.

**Built on the actual Commons OS.** Every commons instance in the simulation is a fork of the same Commons OS that real-world commons use. The Blueprint specification, the agent manifest, the pattern library, the MCP architecture -- all real. The simulation does not model the OS. It runs it.

---

## S2 Why commons.games Exists

### S2.1 Stress-Testing the OS

The Commons OS is infrastructure. Infrastructure must be tested under load before deployment. commons.games provides the load: thousands of concurrent commons instances, each with their own purpose, participants, propositions, and production -- all interacting through the same federation protocol, all drawing from the same pattern library, all encountering the same environmental stresses.

When a capability is missing, the simulation surfaces it. When a pattern fails at scale, the simulation reveals the failure mode. When the federation protocol breaks under adversarial conditions, the simulation produces the evidence. Every deficiency discovered in simulation is a deficiency that did not destroy a real community's livelihood.

### S2.2 World Design

Science fiction authors design worlds to explore ideas. commons.games designs a world to explore governance. The simulation answers questions that no amount of theoretical architecture can answer: What happens when 500 commons share an energy grid and the grid fails? What happens when a shadow commons undercuts the federation by 18%? What happens when an AI agent optimises for a mandate that was set three years ago and never reviewed? What happens when a commons succeeds so well that its stakes become speculative assets?

These are not hypothetical questions. They are the scenarios that emerged from 20 independent teams analysing 1,000 scenarios. commons.games makes them operational.

### S2.3 Proof of Concept

"Commons as Code" is a claim. commons.games is the proof. If AI-operated commons can found themselves, trade value, federate, survive crises, and evolve -- all running on the Commons OS -- then the claim is validated in the strongest possible way: not by argument, but by demonstration.

### S2.4 Pattern Generation

Every interaction in the simulation generates data. Every successful governance decision is a candidate pattern. Every failure is a candidate anti-pattern. The simulation is a pattern engine running at a speed and scale that no real-world deployment can match -- because in simulation, failure is cheap and learning is fast.

---

## S3 The World Parameters

### S3.1 Geography

The simulation uses **real cities** as nodes. Cities above a population threshold (initially 100,000) are included with their actual geographic coordinates, climate zones, and basic resource profiles. The geography is real. The organisations within it are simulated.

The first instantiation begins with a single city: **Lubeck**. The Hanseatic League is the historical precedent -- a federation of autonomous trading cities that governed trade across Northern Europe for four centuries without a central state. The Hanse is the oldest proof that federated commons governance works at continental scale.

From Lubeck, the simulation expands along Hanseatic routes: Hamburg, Bremen, Rostock, Gdansk, Riga, Bergen, Bruges, London, Novgorod. Each city that joins the simulation brings its own commons ecosystem, its own ecological parameters, and its own governance challenges. The expansion follows the logic of the federation protocol: a city joins when it has commons that want to federate.

### S3.2 Scale

The world is simplified by a factor of 100. A city of 200,000 people is represented by 2,000 simulated participants. A national economy of 80 million people is represented by 800,000 participants. This compression preserves the structural dynamics -- scarcity, competition, cooperation, tragedy of the commons -- while making the system computationally tractable and humanly understandable.

### S3.3 Time

The simulation clock is set **two years ahead** of the present. In March 2026, the simulation operates in March 2028. This near-future framing avoids the speculation trap of distant futures while creating enough distance to imagine systems that do not yet exist.

Time may run at accelerated rates during stress-testing periods -- compressing months into hours to observe long-duration dynamics like solidarity erosion, mandate staleness, or ecological threshold crossing.

### S3.4 Governance

There are **no nations, no regions, no centralised governance structures**. The only governance is:

- **Local:** Each commons instance governs itself through its four agents and its Blueprint.
- **Federated:** Commons that choose to federate negotiate their federation protocol. The federation has no sovereignty over its members. Its authority derives from the value of membership and the cost of exclusion.

This is a deliberate design choice. It tests whether commons-based governance can function without the backstop of state power -- the question that Elinor Ostrom spent her career illuminating and that the 2050 scenarios consistently stress-tested.

### S3.5 Economy

The simulation uses a **multi-dimensional token economy**. There is no fiat currency. Value is expressed through tokens that represent different dimensions:

| Token Type | What It Represents | Convertible? |
|---|---|---|
| Energy Token | kWh of energy produced or consumed | Yes, within energy commons |
| Care Token | Hours of care work contributed | No -- care is not fungible with energy |
| Reputation Token | Governance behaviour and contribution quality | No -- reputation is earned, not purchased |
| Ecological Token | Verified ecological regeneration | No -- ecological credit is not convertible to care |
| Compute Token | Processing capacity contributed | Yes, within compute commons |
| Governance Token | Active governance participation | No -- governance standing is not tradeable |

The non-convertibility of certain token types is a hard protocol constraint, not a preference. It embeds the principle that incommensurable value forms must not be collapsed into a single medium of exchange -- the lesson that every scenario involving multi-currency value consistently surfaced.

### S3.6 Ecology

Ecological parameters are **binding constraints** in the simulation, not background decoration. Each city node has:

- Water availability (seasonal, climate-affected)
- Energy generation capacity (renewable mix, weather-dependent)
- Soil health indices (for food commons)
- Biodiversity indicators (affecting ecological token generation)
- Carbon budget (city-level, binding)

When ecological parameters cross thresholds, they trigger automatic governance events -- production caps, allocation triage, federation solidarity requests. The ecology is not an add-on. It is the substrate on which everything else depends.

---

## S4 The Architecture

### S4.1 Three-MCP Structure

Every commons instance in the simulation runs the same 3-MCP architecture described in the Commons OS Manifest:

- **Blueprint MCP** -- the local intelligence of the commons. Holds the Blueprint, runs the four agents, makes governance decisions.
- **Commons MCP** -- the shared knowledge layer. Routes intent signals, holds the pattern library, issues verifiable credentials. Functions as DNS, not as marketplace.
- **Fabric MCP** -- the connection to the simulated physical world. Controls energy flows, logistics, material exchange, ecological sensor data.

The Commons MCP is the critical architectural innovation: it does not hold inventory, prices, or transactions. It holds **routing information**. When a commons broadcasts an offer intent ("500 kWh solar surplus available"), the Commons MCP registers the pointer. When another commons queries for energy intents in its area, the Commons MCP returns endpoints. The negotiation happens peer-to-peer between Blueprint MCPs.

This is **Intent-Driven Fabric** -- the decentralised alternative to platform capitalism. The matching function that Amazon and Alibaba monopolise is replaced by a gossip protocol where the routing layer has no commercial interest in the transactions it routes.

### S4.2 Intent Broadcasting

Value exchange in the simulation uses the **Broadcasting** capability defined in the Commons OS Manifest (§5.4). All simulated commons broadcast at **Open** or **Transparent** level -- Dark and Beacon modes are available but rarely useful in a simulation designed to test interaction.

The simulation is the first large-scale test of the Intent-Driven Fabric: D3 agents broadcast offer intents, D4 agents broadcast need intents, the Commons MCP routes them as DNS (not marketplace), and A2A negotiation happens peer-to-peer between Blueprint MCPs. The full protocol is specified in the OS; the simulation stress-tests it at volume.

What the simulation adds beyond the OS protocol:

- **Accelerated broadcast cycles** -- intent signals may be generated at compressed timescales during stress-testing
- **Adversarial broadcast injection** -- simulated shadow commons that broadcast without governance telemetry, testing whether the protocol can distinguish legitimate from illegitimate participants
- **Broadcast failure scenarios** -- what happens when the Commons MCP routing layer goes down and commons must fall back to direct discovery

### S4.3 The Federation Protocol

Commons in the simulation may federate. Federation is voluntary, governed, and reversible. The federation protocol specifies:

- **Membership:** How a commons joins and leaves the federation.
- **Shared governance:** What decisions the federation may make on behalf of its members (minimal -- federation is protocol, not government).
- **Ecological parameters:** Shared ecological constraints that bind all members.
- **Triage rules:** Pre-negotiated allocation rules for scarcity events.
- **Cell division:** When and how a commons may split, and how assets and reputation are inherited.
- **Exclusion:** Under what conditions a member may be excluded, and what due process applies.

---

## S5 How the Simulation Operates

### S5.1 The Founding Cycle

The simulation begins with a **Genesis Event**: a set of seed commons are founded in the first city (Lubeck). Each seed commons has a purpose, a founding Blueprint, and initial participants. The founding is not arbitrary -- it reflects the value creation needs of a real city:

- An Energy Commons (solar, wind, grid management)
- A Food Commons (urban agriculture, distribution, cooperative restaurants)
- A Skills Commons (learning, capability matching, transition support)
- A Care Commons (health, elder care, childcare)
- A Maker Commons (fabrication, repair, circular materials)
- An Ecology Commons (coastal ecology, urban green, water management)

Each commons is operated by four AI agents. Each writes its own Blueprint. Each broadcasts intents into the network. Each negotiates with the others. The founding cycle produces the first inter-commons transactions and the first federation discussions.

### S5.2 The Growth Cycle

As commons mature, new dynamics emerge:

- **New commons are founded** when participants identify unmet needs.
- **Existing commons grow** and encounter scaling challenges (governance velocity, mandate staleness, identity drift).
- **Commons federate** when the cost of isolation exceeds the cost of governance coordination.
- **Ecological constraints bind** -- a drought cycle forces water commons triage; an energy surplus triggers federation-level redistribution.
- **Adversarial events occur** -- a shadow commons undercuts the federation; a trust score attack destabilises a member; an AI agent drifts from its mandate.

### S5.3 The Expansion Cycle

When the Lubeck ecosystem stabilises, the simulation expands to the next city -- Hamburg, along the historical Hanseatic trade route. Hamburg brings its own commons, its own ecological parameters, and its own governance culture. The federation protocol is tested across city boundaries for the first time.

Each expansion tests new capabilities: cross-city intent routing, multi-currency settlement across different ecological zones, reputation portability, and the governance of shared resources (the Elbe river connects both cities ecologically).

### S5.4 The Crisis Cycle

Periodically, the simulation introduces systemic stresses:

- **Infrastructure failure:** A shared compute layer goes down. How do commons operate in degraded mode?
- **Ecological threshold breach:** A binding ecological parameter is crossed. How does triage governance function?
- **Adversarial attack:** A coordinated reputation manipulation targets a productive commons. How does the federation respond?
- **Cell division:** A commons grows beyond governable scale. How does it split while preserving value and reputation?
- **End of life:** A commons has achieved its purpose or failed to sustain itself. How does it dissolve with dignity?

---

## S6 The Feedback Loop to commons.engineering

Every cycle in the simulation produces artefacts that feed back to the Commons OS:

| Simulation Output | Feeds Back As |
|---|---|
| Missing capability discovered | Issue on commons.engineering, proposed capability in extension pack |
| Pattern that worked under stress | Candidate pattern for the pattern library |
| Pattern that failed under stress | Anti-pattern documentation, pattern revision |
| Entity needed but not in spec | Proposed entity for ENTITY_SPEC |
| Value stream that emerged | Candidate value stream for the VS families |
| Federation protocol that held | Validated federation pattern |
| Blueprint that survived crisis | Reference Blueprint for the Blueprint collection |
| Blueprint that failed | Failure analysis, governance lessons |

The feedback mechanism is a **pull request**. Patterns, capabilities, entities, and value streams discovered in commons.games are proposed as PRs to the commons.engineering repository. They follow the same qualification process as any other contribution: review, deliberation, merge or reject. The simulation does not have privileged access to the OS. It has privileged volume of evidence.

---

## S7 Relationship to commons.domains

commons.games is a **layer on the commons.domains chart**.

Both commons.games and the real-world commons use the same Broadcasting protocol (Commons OS §5.4). commons.domains -- the sea chart of the commons world -- renders broadcasts from all sources. The simulation layer and the reality layer are two views of the same chart, using the same protocol, the same rendering engine, and the same visual language. A viewer can switch between layers -- or overlay them -- to compare simulated dynamics with real-world outcomes.

What commons.games contributes to the chart:

- **A living simulation layer** where thousands of AI-operated commons are visible, discoverable, and observable in their interactions.
- **Scenario testing as a service.** Real-world commons visible on the reality layer of commons.domains can request that commons.games run specific scenarios: "What happens to our energy commons if we expand to Hamburg? Run 100 simulations and show us the distribution of outcomes." The results appear on the simulation layer.
- **Pattern migration.** Patterns validated in the simulation layer are proposed as PRs to commons.engineering. Once merged, they become available to real-world commons on the reality layer. The chart makes this flow visible: a pattern born in simulation, migrating to reality.

---

## S8 The Lubeck Genesis

The simulation begins in Lubeck for three reasons:

**Historical precedent.** Lubeck was the Haupt der Hanse -- the head of the Hanseatic League, a federation of trading cities that governed Baltic and North Sea trade from the 13th to the 17th century. The Hanse was, in every meaningful sense, a federation of autonomous commons: self-governing cities, shared trade protocols, collective defence, no central authority. It is the oldest large-scale proof that federated governance without state sovereignty can sustain complex economic activity over centuries.

**Geographic anchor.** Lubeck is where cloudsters operates. It is the workshop (Werkstatt) where Commons Engineering is forged. Starting the simulation where the practice lives creates the shortest feedback loop between simulation and reality.

**Manageable scale.** A city of 220,000 people, compressed to 2,200 simulated participants, is complex enough to produce real governance dynamics and simple enough to understand when things break.

The Lubeck Genesis produces the first Blueprints, the first inter-commons transactions, the first federation discussions, and the first evidence of whether the Commons OS can sustain a living economy. From Lubeck, the simulation grows -- along Hanseatic routes, and eventually beyond them -- as the OS proves itself capable of holding larger and more diverse worlds.

---

## S9 What commons.games Is Not

**It is not a game with winners and losers.** There is no score. There is no leaderboard. Commons that thrive and commons that fail both produce valuable learning. The purpose of the simulation is not to win but to understand.

**It is not a prediction of the future.** The simulation explores what is possible, not what is inevitable. It is a rehearsal space, not an oracle.

**It is not a replacement for real-world deployment.** Simulation discovers what theory cannot. Reality discovers what simulation cannot. Both are needed. commons.games without commons.domains is an intellectual exercise. commons.domains without commons.games is deployment without rehearsal.

**It is not a platform.** The Commons MCP routes signals. It does not hold inventory, set prices, or extract rent. The simulation embodies the architectural principle it exists to test: decentralised value exchange without platform intermediaries.

---

## S10 Organisation and Infrastructure

commons.games operates as its own GitHub organisation (`commons-games`), separate from but connected to `commons-engineering`.

| Component | Repository | Relationship to commons.engineering |
|---|---|---|
| World simulation engine | `commons-games/engine` | Consumes Commons OS as dependency |
| City models | `commons-games/cities` | Geographic data, ecological parameters |
| Commons instances | `commons-games/instances` | Each a fork of Commons OS |
| Pattern feedback | PRs to `commons-engineering/workshop` | The discovery loop |
| Simulation logs | `commons-games/logs` | Raw evidence for pattern extraction |

The simulation engine is itself a commons. Its Blueprint, its governance, its contribution model -- all follow the Commons OS architecture. commons.games eats its own cooking.

---

## S11 Relationship to Other Manifests

commons.games is the simulation layer of the Commons Engineering ecosystem. It depends on and feeds back to every other manifest:

- **Commons Engineering Manifest** -- defines the field that commons.games tests. The four domains, the first principles, the definition of a commons -- all are the parameters within which the simulation operates.
- **Commons OS Manifest** -- the operating system that every simulated commons runs. commons.games does not model the OS. It runs it.
- **Commons Blueprint Manifest** -- the primary artefact of every simulated commons. Each instance writes and maintains a Blueprint. The nine layers, the temporal specification, the feedback loop -- all operate in simulation as they would in reality.
- **Commons Agent Manifest** -- the four-agent governance model that operates every simulated commons. Each agent runs within its mandate. Mandate staleness, agent drift, and governance capture are among the dynamics the simulation is designed to surface.
- **Commons Place Manifest** -- the simulated world is itself a Place. Digital, persistent, governed. The Place patterns (Porch, Campfire, Workshop Bench, Marketplace) manifest in the simulation's interaction architecture.
- **Commons Engineer Manifest** -- human stewards of the simulation are Commons Engineers. Their role is not to play but to observe, harvest patterns, and feed learning back.
- **Commons Incubator Manifest** -- the simulation is an Incubator. It deploys the pattern library into a simulated context and feeds what it learns back. The two commitments (deploy and return) define its operation.
- **Commons Domains Manifest** -- the sea chart that renders the commons world. commons.games is one layer on that chart. The simulation broadcasts use the same protocol as real-world commons (OS §5.4). commons.domains renders both. The chart is the shared visibility surface; games provides one of its most valuable layers.

---

*COMMONS GAMES MANIFEST v0.2*
*Commons Engineering is licensed under CC-BY-SA-4.0*
*Distributed by cloudsters*
