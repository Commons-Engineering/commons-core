# Commons Core

**Keep shared value creation relevant.**

A commons is shared value creation: a life, an organisation, a community, a city or an ecosystem. Commons Engineering is the discipline of systematically keeping it relevant. A Commons CORE is its cybernetic model: a shared basis for understanding how value is created, exploring futures and guiding real change.

This template is the starting point for your own CORE. It begins as one small Git repository, with plain files that people and agents can read and work on together. Your commons controls its model, its decisions and its access.

## Why a Commons CORE

AI and robotics change what people and machines can do together. Needs, expectations and ways of creating value can change with them. Continuing yesterday's work gives little guidance on where your commons' value creation could or should go.

![Illustrative trajectories of available intelligence, the unit cost of cognitive and machine work, and possible gains or losses in a commons' relevance.](docs/images/why-relevance.svg)

*Development hypotheses, not forecasts. Each curve has its own relative scale; intersections imply no quantitative comparison.*

A CORE gives people and agents a shared context for asking better questions: whom do we create value for, what must work together, what is changing, and which next step will help? The aim is better alignment, useful work and a more resilient future.

## How it works

The CORE first learns from reality. Its current model then describes the near future and gives orientation to the work. Its Git history records earlier states of the model; observations provide evidence of what actually happened.

From experience, evidence and scenarios, people and agents **project possible futures**. From the commons' identity, purpose and design intent, they **give desired futures concrete form**. Alternative futures live as worlds, in structurally comparable COREs, so their differences, dependencies and promising increments can be explored together.

Loops turn findings into work. People and agents investigate, draft and build within their mandates; accountability always resolves to a human. Progress in the model and impact in lived practice are reviewed separately. Change succeeds when people can put it into practice.

## Start with one real question

You can begin with a concrete need: understand a service, explore a new offer, prepare for an interruption, or work out which capabilities a desired future will require. Follow its relationships and build a useful view of the whole as you go.

1. Choose **Use this template**, create a repository under your own owner, choose a name ending in `.core`, and select **Private**.
2. Open it with an agent that can read and work on its files. Start from [AGENT.md](AGENT.md), the common orientation for every agent.
3. Install the Commons Essentials release declared in `.commons/commons.yml`, from the Releases of this repository (`commons-essentials-0.2.0.zip`): unpack it whole and unchanged into `extensions/commons-engineering/commons-essentials/` and record it in `.commons/lock.yml`. Use its guidance to establish the commons' identity and purpose, name its founders in `people.yml` and under SEED in `.commons/access.yml`, record the founding and choose a first piece of work.

You can start the conversation with:

```text
Read AGENT.md and the records in this repository.
Help me establish the commons this CORE will represent.
Check the pinned Commons Essentials release and explain what must be installed first.
Ask about its purpose, boundaries, accountable people and one real question.
Propose the smallest useful model and a first piece of work.
Keep evidence, assumptions and open questions distinct.
Work in small, reviewable increments and name the decisions you need from me.
```

Commons Essentials supplies the discipline's specifications and checking tools. A suitable domain extension can then offer value streams, capabilities and other archetypes to adopt into your own model. Installed copies remain unchanged; your adaptations retain their origin.

After Commons Essentials is installed, run its published tools from the repository root:

```sh
python extensions/commons-engineering/commons-essentials/specs/tools/check_core.py .
python extensions/commons-engineering/commons-essentials/specs/tools/make_agent.py .
```

The check reports failures and gaps; the generator refreshes `AGENT.md` from the records. A missing answer is a question to work on, not an invitation for an agent to invent one.

## What your CORE holds

The model uses **five dimensions, thirteen value-stream families and nine elements**. It connects stakeholders, journeys, touchpoints and value exchanges with value streams and steps, capabilities, entities, solutions, and responsible Bodies and Posts.

| Place | Purpose |
| --- | --- |
| `.commons/` | Identity, settings, access and the lock of installed releases. |
| `registry/` | The commons' own model, one record per file. |
| `lifecycle/` | Founding, stage and dated events. |
| `operations/` | Loops and their readings. |
| `workshop/` | Work, studies and the continuity of roles. |
| `extensions/` | Installed releases, whole and read-only. |
| `people.yml` | The register of people, kept apart from the model. |
| `AGENT.md` | Generated orientation, followed by the commons' own guidance. |

As needed, **FABRIC** adds operational readings, **GRAPH** connects registered sources, **LIBRARY** offers checked releases, and **MCP** serves permitted context and receives proposals. Components can begin inside the CORE and move as they grow. Existing AI platforms and systems of record keep their responsibilities.

## Work independently and learn together

Your CORE can work offline from what it holds. A connection to `federation.mcp` provides a route to the shared canon and knowledge available to your user; access to the canon at ROAM requires no membership. Each commons controls what it shares. Reading another CORE follows the grant recorded by its holder.

Versioned releases make change explicit. Your commons decides when to adopt an update and what to adapt. The CORE follows the releases it installs, rather than continuously copying this template. Connected services, operational integrations and platform permissions are configured and qualified for the commons that uses them.

Learn more about the discipline at [Commons Engineering](https://commons.engineering).

## License

See [LICENSE](LICENSE) for the terms applying to content and code.

Commons Engineering and this template are stewarded by the **cloudsters FEDERATION** ([cloudsters.net](https://cloudsters.net)).
