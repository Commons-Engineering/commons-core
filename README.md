# Commons Core

**The starting point for the CORE of a commons:** an organisation, a district, a care network, any community that wants to see and steer how it creates value together.

A CORE is one repository that holds the commons' own model of its shared value creation, on the body of knowledge of [Commons Engineering](https://commons.engineering). People and their agents work in it side by side. Everything in it belongs to the commons.

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
