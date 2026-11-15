# Commons Core

**Keep shared value creation relevant.**

A commons is shared value creation: a life, an organisation, a community, a city or an ecosystem. Commons Engineering is the discipline of keeping it relevant, systematically. A Commons CORE is its cybernetic model. It is a shared basis for understanding how value is created, for exploring futures and for guiding real change.

This template is the starting point for your own CORE. It begins as one small Git repository of plain files that people and agents read and work on together. Your commons controls its model, its decisions and its access.

## Why a Commons CORE

AI and robotics change what people and machines can do together. Needs, expectations and ways of creating value can change with them. Continuing yesterday's work gives little guidance on where your commons' value creation could or should go.

![Illustrative trajectories of available intelligence, the unit cost of cognitive and machine work, and possible gains or losses in a commons' relevance.](docs/images/why-relevance.svg)

*Development hypotheses, not forecasts. Each curve has its own relative scale; intersections imply no quantitative comparison.*

A CORE gives people and agents a shared context for better questions. Whom do we create value for? What must work together? What is changing? Which next step will help? The aim is better alignment, useful work and a more resilient future.

## How it works

The CORE first learns from reality. Its current model describes the near future and gives the work its orientation. Its Git history records earlier states of the model, and observations show what actually happened.

From experience, evidence and scenarios, people and agents **project possible futures**. From the commons' identity, purpose and design intent, they **give desired futures concrete form**. Alternative futures live as worlds, in structurally comparable COREs, so that their differences, dependencies and promising increments can be explored together.

Loops turn findings into work. People and agents investigate, draft and build within their mandates, and accountability always resolves to a human. Progress in the model and impact in lived practice are reviewed separately. Change succeeds when people can put it into practice.

## Set up your CORE

One command takes a new CORE from this template to a checked model, a generated agent file and an agent that reads the CORE through its own MCP.

**You need** Git, Python 3.11 or newer, and two Python packages:

```sh
python -m pip install pyyaml jsonschema
```

**Create your repository.** Choose **Use this template** and create a repository under your own owner. Give it a name ending in `.core`, and select **Private**. Then clone it and enter it:

```sh
git clone https://github.com/<owner>/<name>.core.git
cd <name>.core
```

**Name your commons.** Open `.commons/commons.yml` and fill in four fields, and a fifth if you can already say it:

| Field | Form | Example |
| --- | --- | --- |
| `id` | lowercase letters and digits, words joined by hyphens; stable, never reused | `ada-household` |
| `name` | the name people read | `Ada's Household` |
| `code` | two capital letters | `AH` |
| `language` | the two-letter code of the commons' language | `en`, `de` |
| `purpose` | optional: the commons' purpose in one sentence, in your own words; otherwise your agent asks for it in the founding dialogue | `We keep our household fair and calm.` |

The `code` is the commons' short sign. It forms the handles of the Bodies that carry the commons' work, such as `@D1-AH`.

**Run the set-up:**

```sh
python bootstrap.py --you <your-github-login>
```

`--you` is your GitHub login, for example `ada`.

Without `--domain`, the set-up installs the Commons model and the patterns, and your agent finds the fitting domain model with you in the founding dialogue. If you already know it, name it, for example `--domain life`:

| `--domain` | Fits |
| --- | --- |
| `life` | a person, a family or people living together |
| `business/startup` | a young or small organisation, one site and a few people, from its founding onward |
| `business/corporate` | an established organisation with several units and a governance of its own; a startup grows into it |
| `health` | a health system |
| `urban` | a city or a settlement |

The set-up takes a few minutes. The script stops at the first step that fails and says what went wrong. Fix what it names and run it again: steps already done are skipped. When it is done, commit what changed. The commit is large, because the Commons model, the patterns extract and the domain model are installed into your own repository, whole and unchanged:

```sh
git add -A
git commit -m "Set up the CORE"
git push
```

If your repository has no remote, leave out `git push`.

Then open the CORE with your agent. Its `AGENT.md` holds the **founding dialogue** of the Commons model (core R41): the agent asks what you want to model and why, proposes the domain model that fits, and sketches the model with you as it grows. Bring it a concrete need of your own. The CORE matches the words of your question against your own records, the installed models and the patterns. The records of your own model and of the domain model weigh more than patterns, so once a domain model is installed, a new CORE answers first from it. Patterns come up where their own words fit the question, and through the value-stream families of the records it finds. Name the work, the people or the thing your question is about. With `life`, for example: *"How do I keep track of what comes in and what goes out of my household?"* With `--domain`, the set-up suggests one for that domain when it is done.

## Step by step

`bootstrap.py` does nothing you could not do by hand. Here is what it does, in its order.

**1 · The library.** [federation.library](https://github.com/cloudsters/federation.library) holds the released models and the patterns extract. Its `index.yml` lists each release with its folder and the record digest that proves it unchanged. The script uses the library at `../library`, beside the CORE, and clones it there if it is missing:

```sh
git clone --depth 1 https://github.com/cloudsters/federation.library.git ../library
```

**2 · The Commons model.** The Commons model brings the discipline's specifications and its tools. Its own `install.py` checks the copy against the digest in `index.yml`. Only then does it move the copy into `models/commons/commons-engineering/commons/` and record it in `.commons/lock.yml`. If the check fails, nothing is written:

```sh
python ../library/<folder>/specs/tools/install.py . --from ../library/<folder> --expect <digest>
```

From then on, the tools run from the installed copy, `models/commons/commons-engineering/commons/specs/tools/`.

**3 · The patterns extract.** The extract is the released pattern language. The same `install.py` installs it, whole and read-only, under `patterns/commons/commons-engineering/`.

**4 · The domain model,** when `--domain` names it, or later in the founding dialogue. It offers value streams, capabilities and other archetypes to adopt into your own model. It is installed the same way, under `models/commons/commons-engineering/<model>/`, and a variant under `models/commons/commons-engineering/business/<variant>/`. The script then names it in the graph's register, `graph/sources.yml`, beside your own records, your knowledge and the patterns, so that its records answer your questions.

**5 · You, under SEED, and the founding.** The script names you in `.commons/access.yml` as one of the founders, the innermost shell:

```yaml
users:
  - account: account:<you>
    shell: SEED
```

It then records the founding: one event in `lifecycle/events/`, dated today, and the stage `Seed` in `lifecycle/stage.yml`.

**6 · The check and the agent file.** `check_core.py` reports each finding as **fail**, **should** or **gap**. A new CORE has no fail, and a gap is a question to work on, not a defect. `make_agent.py` then generates `AGENT.md`, the common orientation for every agent. Run both again whenever the records change:

```sh
python models/commons/commons-engineering/commons/specs/tools/check_core.py .
python models/commons/commons-engineering/commons/specs/tools/make_agent.py .
```

When the check names `check_model.py`, run it on your own model to see each finding:

```sh
python models/commons/commons-engineering/commons/specs/tools/check_model.py models/runtime
```

**7 · The connector for your agent.** Your CORE serves itself to agents through its own MCP. Locally, over stdio, it needs no account at any service. The script writes the connector entry into `.mcp.json` at the root of the CORE. Clients that read `.mcp.json` pick it up from there:

```json
{
  "mcpServers": {
    "commons": {
      "command": "python",
      "args": ["models/commons/commons-engineering/commons/specs/tools/serve_mcp.py", ".", "--stdio", "--as", "account:<you>", "--state", "../.mcp-state"]
    }
  }
}
```

For a client that keeps its own list of servers, add the same `commons` entry there, with the CORE's folder as the working directory. `--state ../.mcp-state` lies beside the CORE, not in it, because it holds the operating state of the MCP, which is no part of the CORE.

`federation.mcp` will serve the depth of the domain models to members after signing in; once it is in operation, its entry is added to `.mcp.json`.

Your CORE's MCP offers three tools:

| Tool | Does |
| --- | --- |
| `answer` | finds the records and patterns that fit a question best, each with its title, summary and id |
| `node` | reads one of them whole, by its id |
| `propose` | opens one item for people to decide, such as a change, a question or a correction; it changes nothing in the CORE itself |

To check the MCP without an agent, ask it once from the shell; `--text` prints each candidate as title, summary and id:

```sh
python models/commons/commons-engineering/commons/specs/tools/serve_mcp.py . answer "question=How do I keep track of what comes in and what goes out of my household?" --as account:<you> --state ../.mcp-state --text
```

## Words you will meet

| Word | Means |
| --- | --- |
| **shell** | how close someone stands to the commons' model; what they may read and write follows from it. From the centre: SEED, CORE, PEER, OPEN, DOCK, ROAM |
| **SEED** | the innermost shell, the commons' founders |
| **grant** | what one call may read and write, given by the caller's shell; every answer names it |
| **fail** | a defect to fix; the check ends with an error while one is left |
| **should** | worth a look, not a defect |
| **gap** | something not there yet: a question to work on, not a defect |

## Start with one real question

Begin with a concrete need, for example:
- understand a service;
- explore a new offer;
- prepare for an interruption;
- work out which capabilities a desired future will require.

Follow its relationships, and build a useful view of the whole as you go. For now the answer matches the words of a question, not its meaning, so a question in the domain's own words works best, in English, the language of the canon, the models and the patterns. Your agent asks the CORE in English for them and in your commons' language for your own records, and answers you in your language. Open the CORE with an agent that can read and work on its files, and start the conversation with:

```text
Read AGENT.md and the records in this repository.
Follow its founding dialogue to establish the commons this CORE will represent.
Ask about its purpose, boundaries, accountable people and one real question.
Propose the smallest useful model and a first piece of work.
Keep evidence, assumptions and open questions distinct.
Work in small, reviewable increments and name the decisions you need from me.
```

## What your CORE holds

The model uses **five dimensions, thirteen value-stream families and nine elements**. It connects stakeholders, journeys, touchpoints and value exchanges with value streams and their steps, capabilities, entities, solutions, and the responsible Bodies and their Posts.

| Place | Holds |
| --- | --- |
| `.commons/` | identity and settings (`commons.yml`), access (`access.yml`) and the lock of installed releases (`lock.yml`) |
| `models/runtime/` | the commons' own model, one record per file, with its loops and their state |
| `models/commons/` | the installed models, whole and read-only, one folder per library |
| `models/emulation/` | models the commons tries before adopting them |
| `patterns/` | the installed patterns extract under `patterns/commons/commons-engineering/`, and the commons' own patterns |
| `knowledge/` | evidence, sources and claims, kept apart from the model |
| `lifecycle/` | the founding, the stage and dated events |
| `workshop/` | work, studies and the continuity of roles |
| `views/` | views of the model for people, created when first needed |
| `people.yml` | the register of people, kept apart from the model |
| `AGENT.md` | the generated orientation, followed by the commons' own guidance |

As needed, **FABRIC** adds operational readings, **GRAPH** connects registered sources, and **MCP** serves permitted context and receives proposals. Components can begin inside the CORE and move out as they grow. Existing AI platforms and systems of record keep their responsibilities.

## Work independently and learn together

Your CORE works offline from what it holds. The shared canon of the Commons lies in the public [federation.library](https://github.com/cloudsters/federation.library), readable by anyone without an account. Each commons controls what it shares, and reading another CORE follows the grant its holder records.

Versioned releases make change explicit. Your commons decides when to take up a newer release and what to adapt, and an installed copy is never changed in place. The CORE follows the releases it installs rather than continuously copying this template.

Learn more about the discipline at [Commons Engineering](https://github.com/Commons-Engineering).

## License

See [LICENSE](LICENSE) for the terms that apply to content and code.

Commons Engineering and this template are stewarded by the **cloudsters FEDERATION** ([cloudsters.net](https://cloudsters.net)).
