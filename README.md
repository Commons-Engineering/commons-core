# Commons OS

**The forkable operating system for living systems.**

Commons OS is a complete operating environment for any commons — an organisation, a city district, a personal system, an ecological watershed, or any community that chooses to govern itself as a living system.

---

## Why

The Cognitive Age creates extraordinary new possibilities for shared value creation — at every scale, from a local cooperative to a global enterprise. But without deliberate architecture, the tools, platforms, and intelligence of this era concentrate into fewer hands. Organisations become tenants of their own future.

**A commons systematically creates value that is alive, shared, just, and built to last.**

Commons OS is the infrastructure that makes this buildable. It gives every commons — regardless of domain — the same quality of sovereign operating system that today only trillion-dollar platforms possess. Human-governed. AI-driven. Open source. Near-zero cost.

> **[▶ Watch the Deck — The Age of Living Systems](https://commons-engineering.github.io/commons-os/deck/)**
> The full 20-slide strategic presentation, playable directly in your browser.

---

## How to Start Your Commons

There are three ways to begin, depending on your needs:

| Path | Best for | How |
|---|---|---|
| **Template** (private) | Individuals, internal teams, private experiments | Click **Use this template** → **Create a new repository** → choose **Private** → follow `BOOT.md` |
| **Fork** (public) | Open source projects, public communities | Click **Fork** → follow `BOOT.md` |
| **Lighthouse** (guided) | Established organisations seeking a co-creation partnership | [Contact Commons Engineering](mailto:contact@commons.engineering) |

### After You Template or Fork

1. **Rename** your repository to `[your-commons]` (e.g., `luebeck-os`, `my-life`, `acme-commons`)
2. **Edit** `.commons/identity.yml` — set your slug, name, purpose, domain, and locale
3. **Copy** `AGENT.md.template` → `AGENT.md` — this is the OS-standard AI governance configuration
4. **Wire** your AI tool to `AGENT.md` (see `BOOT.md` for tool-specific instructions)
5. **Read** `BOOT.md` — the Purpose Agent guides you through the founding conversation

The boot process takes 2-4 hours. It is a founding act, not a setup wizard. The quality of your boot determines everything that follows.

### Set up your working environment

Get a working environment in one of two ways — both lead to the same place: your AI working agent, ready to build with you. The agent then runs `commons/setup/ONBOARDING.md` to wire you up.

| Door | Best for | How |
|---|---|---|
| **One-click installer** | your own computer | Run `commons/setup/commons-setup.cmd` (Windows) or `commons/setup/commons-setup.command` (macOS). Installs the toolchain and your agent locally. |
| **Browser — zero install** | locked-down or shared machines, or no install rights | [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Commons-Engineering/commons-os?quickstart=1) — everything runs in the cloud; nothing touches your machine. |

---

## What You Get

| Component | What it does |
|---|---|
| **Commons** | Upstream patterns, manifests, specifications, templates — with upstream sync |
| **Extensions** | Domain-specific extension packs (business-essentials, urban-essentials, life-essentials, ecology-essentials) |
| **Instance** | Your space — registry (workspace), operations, portals, workshop, and local patterns |
| **Agent Configuration** | AI-ready governance with 4-agent board architecture |
| **Living Blueprint** | Single-document, 9-layer architecture for your commons |
| **MCP Connections** | Shared intelligence (Commons MCP) + local knowledge (Blueprint MCP) + your systems (Fabric MCPs) |

### The Four Universal Dimensions

Every commons, regardless of domain, operates across four dimensions:

| Dimension | What it governs |
|---|---|
| **D1 — Definition & Purpose** | Direction, governance, impact, architectural integrity |
| **D2 — Participation & Relationship** | Community, stakeholders, workforce, non-human participants |
| **D3 — Proposition & Exchange** | Value creation, products, services, knowledge exchange |
| **D4 — Production & Resilience** | Infrastructure, production lines, delivery, economics |

Each dimension has an **agent** (conversational governance) and may have **engines** (production at volume, supervised by D4).

### The Intelligence Grid

Your fork connects you to a shared intelligence network:

| Asset | Scale |
|---|---|
| **Documented patterns** | 64,000+ across business, urban, ecology, and life |
| **Business lighthouses** | 1,000+ documented organisations |
| **Urban lighthouses** | 1,400+ documented places |
| **Access method** | Model Context Protocol (MCP) — native AI retrieval |

Every pattern and lighthouse is connected through a knowledge graph and retrievable for every Commons OS fork.

---

## Architecture

### Directory Structure

```
[your-commons]/
├── AGENT.md.template          Agent configuration (copy to AGENT.md)
├── BOOT.md                    Boot guide — the founding conversation
├── ALIGN.md                   Alignment check rules
├── blueprint.md               Living Blueprint (L1-L9)
├── .commons/                  Identity and configuration
├── commons/                   THE LIBRARY — upstream patterns, manifests, specs, templates
├── extensions/                EXTENSION PACKS — domain-specific (business, urban, life, ecology)
├── instance/                  YOUR SPACE — sovereign, never touched by upstream
│   ├── registry/              THE WORKSPACE — journeys, touchpoints, value streams, capabilities, entities
│   ├── operations/            Operating rhythms and processes
│   ├── portals/               Intranet and extranet (including the Lighthouse deck)
│   └── workshop/              THE FORGE — experiments, drafts, WIP
└── ...
```

### Three Layers

| Layer | Path | Who owns it | Sync behaviour |
|---|---|---|---|
| **Commons** | `commons/` | Upstream (commons-os template) | Read-only in forks, updated via upstream sync |
| **Extensions** | `extensions/{provider}/{pack}/` | Pack providers (any Commons Incubator) | Loaded via Commons MCP, cached locally |
| **Instance** | `instance/` | Your commons | Yours entirely — upstream never touches it |

### Everything is Open

| What | License | Cost |
|---|---|---|
| Content (manifests, specs, patterns) | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) | Free |
| Code (scripts, workflows, templates) | [MIT](https://opensource.org/licenses/MIT) | Free |
| Hosting | GitHub | Free |
| AI integration | Any MCP-compatible model | Your choice |

See [LICENSE](LICENSE) for details.

---

## Documentation

| Document | What it covers |
|---|---|
| `BOOT.md` | The founding conversation — how to boot your commons |
| `ALIGN.md` | Alignment rules — how to keep your commons healthy |
| `blueprint.md` | The Living Blueprint — 9-layer architecture template |
| `commons/manifests/COMMONS_OS_MANIFEST.md` | What Commons OS is — vision, principles, architecture |
| `commons/manifests/COMMONS_AGENT_MANIFEST.md` | The 4-agent governance model |
| `commons/specs/COMMONS_OS_SPEC.md` | Technical specification — directory structure, lifecycle, layers |
| `commons/specs/COMMONS_MCP_ARCHITECTURE_SPEC.md` | The 3-MCP channel architecture |
| `commons/specs/PATTERN_SPEC.md` | How patterns work — orbital layers, structure, vitality |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to contribute patterns, improvements, and fixes back upstream.

---

*Commons OS is part of [Commons Engineering](https://commons.engineering) and distributed by [cloudsters](https://cloudsters.net).*

*Licensed under CC-BY-SA-4.0 — Distributed by cloudsters*


---

## How releases work

This public `commons-os` repository is editorially released from `commons-os-3` (private). Internal commits to `-3` do not automatically flow here — releases are deliberate. See this repository's tags for release versions, and `commons/manifests/COMMONS_OS_MANIFEST.md` for the full chain architecture.
