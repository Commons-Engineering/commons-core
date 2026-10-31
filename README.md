# Commons Core

**The starting point for the CORE of a commons:** an organisation, a district, a care network, any community that wants to see and steer how it creates value together.

A CORE is one repository that holds the commons' own model of its shared value creation, on the body of knowledge of [Commons Engineering](https://commons.engineering). People and their agents work in it side by side. Everything in it belongs to the commons.

## Why a Commons Core

Every organisation, community or city creates value together with others. What carried it yesterday does not carry it tomorrow by itself: needs change, and cognitive and machine work becomes cheaper and available everywhere. A commons that only continues can lose its relevance without doing anything wrong.

A Commons Core is where a commons keeps one shared picture of how it creates value: whom it serves, how value flows, what it relies on, who answers for what. The picture is kept as plain files that its people and any AI agent can read. With it, people and agents test alternatives before change is forced on them, decide the next step together, and see afterwards what actually changed.

| What a commons gets | |
|---|---|
| **One shared model** | its value creation in one grammar, comparable with every other commons |
| **People and agents on the same page** | one generated `AGENT.md` for agents of any vendor; access by shell; decisions stay with people |
| **Its own, always** | a private repository it owns; works offline; nothing is written into it from outside |
| **Shared knowledge on its own terms** | takes up checked releases by its own decision; reads other commons only under their grant |
| **Staying current** | release notes say what changed; the commons decides when it takes them up |

## Start

| | What to do | What it does |
|---|---|---|
| 1 | Press **Use this template**, choose an owner and a name ending in `.core`, and choose **Private** | the commons gets its own repository |
| 2 | In `.commons/commons.yml`, set `id`, `name`, `code` and `language`. In `people.yml`, name who founds it, and in `.commons/access.yml` add them under `users` in the shell `SEED` | the CORE says which commons it is and who answers for it |
| 3 | Install the release of Commons Essentials that `commons.yml` pins (`commons-essentials` 0.1.0) into `specs/` | the commons receives the specifications and the tools that check it |
| 4 | Record the founding as the first event in `lifecycle/events/`, and its stage in `lifecycle/stage.yml` | the commons' path begins |

Then run `specs/tools/check_core.py .` and `specs/tools/make_agent.py .`. The first tells what is still missing; the second writes the agent file `AGENT.md` from the CORE's records.

## What lives where

| Place | Holds |
|---|---|
| `.commons/` | the settings (`commons.yml`), who takes part by shell (`access.yml`), and later the lock of what is installed |
| `registry/` | the commons' own model, one record per file, in one folder per element |
| `lifecycle/` | the stage and the dated events of its path |
| `operations/` | the loops through which the commons steers itself |
| `workshop/` | open work, studies, start files and handover notes |
| `people.yml` | the one place that names people |
| `AGENT.md` | generated from the records; never edited by hand above its own guidance |

## Staying current

A CORE follows Commons Essentials, never this template. When a newer release exists, the commons reads which parts it changed and takes it up by a decision of its own (`specs/extension.md` R20). The structure moves in one run (`specs/core.md` R8).

## License

See [LICENSE](LICENSE).
