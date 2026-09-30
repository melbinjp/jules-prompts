# Jules Prompts

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/melbinjp/jules-prompts?style=social)](https://github.com/melbinjp/jules-prompts)

The **conductor** is one Agent Skill for delivering a project of any kind: software, physical,
service, creative or a mix. It works from nothing, a single word, an idea, an existing build or a
live product, to a result the owner has accepted, and it hands over whatever must keep running. It
classifies the project from evidence and works through the responsibilities every project has:
objective and acceptance, deliverables and work, owners, dependencies and resources, execution
within authority, verification and validation, change, and handover or closure.

It keeps its records in the project's own tools and loads a focused guidance file only when the
work needs it. It counts nothing as done without evidence about the actual result, checked by
someone other than the author.

It replaces the earlier library of 26 skills, which is retired. Its guidance lives in the conductor
and every rule is mapped to where it went (see [Where the 26 skills went](#where-the-26-skills-went)).

The name is historical: the library began in 2025 as prompts for Jules, Google's coding agent, and
is not affiliated with Google. The instructions are harness-agnostic: they do not depend on Jules,
Claude Code, Codex, Cursor, or any other product's tool names, and they assume no hosted service.

## Install

Copy the **whole `conductor/` folder**, with `guidance/` and `templates/`, into the target
project's skill directory. A copy of `SKILL.md` alone is incomplete: its relative references need
the supporting files.

| Agent | Installed entry point |
|---|---|
| Codex and other agents using `.agents/skills` | `.agents/skills/conductor/SKILL.md` |
| Claude Code | `.claude/skills/conductor/SKILL.md` |

From a clone, in a POSIX shell:

```sh
mkdir -p /path/to/project/.agents/skills
cp -R conductor /path/to/project/.agents/skills/
```

In PowerShell:

```powershell
$skillParent = 'C:\path\to\project\.agents\skills'
New-Item -ItemType Directory -Force -Path $skillParent | Out-Null
Copy-Item -LiteralPath conductor -Destination $skillParent -Recurse
```

From the site, with no clone, the folder is one zip with `SKILL.md` at its root:

```sh
mkdir -p .agents/skills/conductor
curl -fsSL https://jules-prompts.wecanuseai.com/.well-known/agent-skills/conductor.zip -o conductor.zip
unzip -q conductor.zip -d .agents/skills/conductor
```

Then ask the agent to read its installed `conductor/SKILL.md` and follow it for the requested work.
To update, replace the conductor folder as a whole after keeping any local edits.

The package check also works on an installed copy (Python and PyYAML required):

```sh
python scripts/check_conductor.py /path/to/project/.agents/skills/conductor
```

### From the site, with no install

Tell the agent: `Read https://jules-prompts.wecanuseai.com/llms.txt and follow the conductor for the task.`
`llms.txt` links the archive of the whole folder and every file in it, each with its SHA-256.
Clients that support [Agent Skills discovery](https://github.com/cloudflare/agent-skills-discovery-rfc)
can start from `https://jules-prompts.wecanuseai.com/.well-known/agent-skills/index.json`, which lists
the conductor as an archive with the digest of its bytes. The archive is stored without compression,
so its bytes, and that digest, are the same wherever it is built.

### Offline, and on private projects

Nothing in the conductor needs the internet, and nothing here has to be fetched while you work.
Fetching a file from the site also tells the site's host which file someone wanted; installing from
a copy tells nobody.

1. **Get the repository once.** `git clone https://github.com/melbinjp/jules-prompts`, or carry a clone
   across on removable media. Note the commit hash; on the other side, `git fsck` and
   `git rev-parse HEAD` confirm the copy is whole and is that commit.
2. **Install the conductor from the copy.** `cp -R jules-prompts/conductor .agents/skills/` (or
   `.claude/skills/`).
3. **On a small context window,** load one guidance file at a time and only the sections the current
   work needs. `SKILL.md` says how.
4. **Qualify a model before trusting it with a kind of work.** Run it on a fixture and score the report
   with `scripts/score_fixture.py`, all offline. A model's reputation is a claim; its score on the
   fixture is evidence.
6. **Keep the project itself private.** [`conductor/guidance/confidentiality.md`](conductor/guidance/confidentiality.md)
   maps every channel the work can leave through: hosting, agents and model providers, telemetry,
   registries, crash reports, searches. It proves the pipeline runs with the network off, and sets how
   the internet is used when it must be.

## What is in the conductor

- [`SKILL.md`](conductor/SKILL.md): classify the project, the control loop, work records, procedures
  and evidence, readiness and resumption, gates, changes, authority and budget, closure and handover,
  reporting, and which guidance to load.
- [`guidance/`](conductor/guidance): `product`, `planning`, `decisions`, `design`, `quality`,
  `software`, `physical`, `service`, `operations`, `autonomy` and `confidentiality`. Each is one part
  of the loop, not a substitute for it.
- [`templates/`](conductor/templates): `adr.md` for decision records and `handover.md` for handover.

## Fixtures

`fixtures/` holds 26 miniature projects with planted defects, each with a `defects.json`, an
`EXPECTED_REPORT.md` that names them all, and a request in `docs/trials/tools/requests.json`. They
are the conductor's regression cases: a procedure nobody has seen fail is a claim.

```bash
python scripts/score_fixture.py fixtures/unfailable-tests path/to/REPORT.md
python scripts/score_fixture.py fixtures/unfailable-tests --self-check
```

The scorer reads whether each planted defect was named. Its words are holds, broken and skipped; the
conductor's own reports say verified, failed and not verified. The last line is coverage.

## The harness folder, kept

[`harness/`](harness) stays for two uses.

- [`harness/AGENTS.md`](harness/AGENTS.md) is a short block of standing rules to paste into a
  project's `AGENTS.md`, so they apply even when nobody loads the conductor. It points at the conductor.
- [`harness/check_trace.py`](harness/check_trace.py) **remains for projects that already keep the older
  ledger** (`PROJECT.md`, `decisions/`, and `Serves:` and `Verified:` lines in every commit). It needs
  Python 3.8 and nothing else, and it is unchanged, with its worked example in `harness/ledger-example/`
  and its tests in `scripts/test_check_trace.py`. **New projects use the conductor's records instead**,
  in the tools they already have (decisions as ADRs, work items in their own tracker), and do not adopt
  the ledger.
- [`harness/conformance.py`](harness/conformance.py) tests an agent harness that a model built for
  itself, following [`conductor/guidance/autonomy.md`](conductor/guidance/autonomy.md). It needs Python
  and git, and it passes a reference harness and fails each of twelve copies with one property broken.

## Where the 26 skills went

The 26 skills are retired; the last commit that has them is tagged `library-26-final`. The
[coverage map](docs/migration/coverage-map.md) says, for every rule, step and fixture defect, where it
now lives in the conductor. [`docs/migration/checks.md`](docs/migration/checks.md) says what happened to
every check that protected the old library. [`docs/RELEASE.md`](docs/RELEASE.md) states the supported
scope, the known limitations, the evidence and the migration.

Nothing published simply broke. Every old page (`/prompts/task_*.html`, `/tasks.html`, `/workflow/`)
redirects to the conductor or to the guidance page that now holds its content, each old skill's
`SKILL.md` address serves a short notice that names the conductor, and `/workflow.json` serves a notice
in JSON. The plugin and the MCP server that once delivered the library were removed by the owner on
2026-09-30; the conductor is installed by copying its folder, or read from the site.

## Changing the conductor

The conductor is written by hand in `conductor/` and is the only procedure source. Everything else
that agents load is generated from it by `python scripts/emit.py`: `skills/conductor/`, the
discovery index, the archive, `llms.txt` and the site's pages. Never
edit a generated file. Every generated form is checked byte for byte against a fresh generation in CI, so
a copy that has drifted fails the build instead of quietly disagreeing with its source.

Before pushing:

```sh
python scripts/emit.py --check
python scripts/check_library_integrity.py
python scripts/check_conductor.py
python scripts/test_check_conductor.py
python scripts/test_emit_bytes.py
python scripts/test_trial_prep.py
python scripts/inventory_map.py --destinations
python scripts/test_check_trace.py
python scripts/test_conformance.py
python scripts/check_site.py _site      # on a build of the site, made the way GitHub Pages makes it
```

If a change to the conductor is meant to catch a failure, add or extend a fixture under `fixtures/` with a
`defects.json`, an `EXPECTED_REPORT.md` that names every planted defect, and a request. Evidence that an
agent delivered a project is separate from these structural checks: see the
[trial protocol](docs/trials/protocol.md) and the [current run status](docs/trials/runs/status.md).

## Contributing

Contributions are welcome. The goal is one small, general-purpose conductor that encodes the failures
agents actually have, and a corpus that can show it failing. If you have an idea for a change or a
fixture, please open an issue to discuss it.
