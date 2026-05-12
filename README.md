# Commons OS

**The forkable operating system for living systems.** Patterns, manifests, agents, and templates for designing and governing organisations, cities, and ecosystems as commons.

This is the **public distribution** of Commons OS — the canonical release published from the internal editorial pipeline. Fork this repository to start your own Commons OS instance, or to study the architecture.

## Quick start

```bash
gh repo clone Commons-Engineering/commons-os my-commons
cd my-commons
cat BOOT.md
```

For the agent contract and operating principles, read in order:

1. `BOOT.md` — boot sequence
2. `AGENT.md.template` — the agent contract template
3. `ALIGN.md` — alignment principles
4. `blueprint.md` — the Living Blueprint template

## What's in here

| Path | Content |
|---|---|
| `commons/manifests/` | Framework manifests — COMMONS_OS_MANIFEST, COMMONS_AGENT_MANIFEST, COMMONS_TAXONOMY_MANIFEST, etc. |
| `commons/specs/` | Framework specifications — PATTERN_SPEC, ENTITY_SPEC, PACK_SPEC, COMMONS_OS_SPEC |
| `commons/patterns/singularity/` | The origin axiom (the-singularity, the-commons) |
| `commons/patterns/principles/` | The 28+ Universal Principles |
| `commons/scripts/`, `commons/templates/` | Build tooling and pattern templates |
| `extensions/commons-engineering/commons-essentials/patterns/commons/` | ~1800 commons-constitutive patterns |
| `extensions/commons-engineering/commons-essentials/patterns/transversals/` | ~270 cross-domain transversal patterns |
| `extensions/commons-engineering/base/patterns/` | Operational base patterns |
| `extensions/cloudsters/business-essentials/` | Business-domain extension |
| `instance/` | Template scaffolding for any forked instance |

## License

Commons Engineering is licensed under **CC-BY-SA-4.0** — free for all, forever. Use it, fork it, build on it. The only requirement: share derivative work back under the same licence.

## Architecture

The Commons OS distribution corresponds to **Orbit 3** of the Commons Engineering orbital architecture (Singularity · Principles · Commons · Transversals · Domains · Edge). The internal editorial pipeline lives in `commons-os-0` through `commons-os-5` (private). New patterns are observed at the Edge in active instances, then promoted inward through the orbits as their generality is confirmed.

For the full architecture, read `cloudsters/CLOUDSTERS_NET_ARCHITECTURE.md` §4 in the cloudsters network.

## How releases work

This public `commons-os` repository is editorially released from `commons-os-3` (private). Internal commits to `-3` do not automatically flow here — releases are deliberate. Look at this repository's tags for release versions.
