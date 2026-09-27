# AGENTS.md

> How an AI agent finds and uses the skills in this repository, and how to change the library itself.

## What this repository is

Two forms currently coexist: the existing 26-skill library, and a candidate conductor under
evaluation. Neither depends on a particular agent or harness. The existing library remains the
website, plugin, MCP and generated `skills/` interface; each of its skills is one self-contained
Markdown procedure with a planted-defect fixture. The conductor is a multi-file skill for
delivering software, physical, service, creative and hybrid projects, including finite projects
that close after accepted delivery.

## Use the candidate conductor

- Read `conductor/SKILL.md`, then the guidance it selects. It is the canonical candidate
  source; `guidance/` and `templates/` are required parts of the package.
- Install by copying the whole `conductor/` directory into `.agents/skills/` or
  `.claude/skills/` in the target project. Do not copy only `SKILL.md`, or place a hand-edited
  copy in this repository's generated `skills/`: the emitter treats ungenerated files as stale.
- Follow its reporting and work-record conventions when it is selected; the legacy three
  verdicts and custom ledger below describe the existing library, not conductor requirements.
- The coverage map is `docs/migration/coverage-map.md`; trial requirements and current evidence
  are in `docs/trials/protocol.md` and `docs/trials/runs/status.md`. Structural checks are not
  delivery acceptance. Compatibility migration and default replacement await the trial review.

## Find a skill in the existing library

- **By where the project is:** `workflow.json`. Its `entries` say where each kind of project starts (an idea and only a model, a project that already exists in any state, broken for people right now, and so on), its `steps` give the path in order with each step's `done_when` gate and the `branches` it calls on, and `throughout` names the skills that apply alongside every step. The same, readable: `https://jules-prompts.wecanuseai.com/workflow/`.
- **By task:** `GET https://jules-prompts.wecanuseai.com/llms.txt` lists every skill with its description and the link to its `SKILL.md`, starting with where to start by state.
- **By the Agent Skills discovery convention:** `GET https://jules-prompts.wecanuseai.com/.well-known/agent-skills/index.json`. Each entry has `name`, `type`, `description`, `url` and `digest`, the SHA-256 of the served `SKILL.md`; verify it.
- **From a clone:** `skills/<name>/SKILL.md`, or the source in `_prompts/`. Copy skills into `.claude/skills/` or `.agents/skills/`. `prompts.json` is an older index, still served.

Paste [`harness/AGENTS.md`](harness/AGENTS.md) into a target project's `AGENTS.md` so its rules apply even when nobody picks a skill.

## Use a skill in the existing library

1. Load the matching `SKILL.md`. The procedure starts after its front matter.
2. Fill any placeholders, such as `<THE_IDEA>`; a skill says what to do if one is left unfilled.
3. Follow it. Report every claim as `holds`, `broken` or `skipped`, and end with the count of each.
4. To see whether an agent or model can follow a skill, run it on the skill's fixture and score the report: `python scripts/score_fixture.py fixtures/<name> REPORT.md`.

## Offline and private use

The skills need no network. On a private or air-gapped project, install from a clone (`skills/`, or `/plugin marketplace add /path/to/clone`), run the MCP server with `JULES_PROMPTS_DIR=/path/to/clone` (it then refuses to use the network), give small local models the short forms in `compact/`, and qualify each model on the fixtures before routing work to it. `keep-it-confidential` covers the project's own confidentiality.

## Change the library

- The source of each existing library skill is `_prompts/task_<name>.md`; a new one starts from the Skill Template, `_prompts/template_master_prompt.md`. Its distributed forms (`skills/`, `plugin/`, `compact/`, `_agent_skills/`, the indexes, `llms.txt`, the workflow includes and the redirect stubs) are generated from it and from `workflow.json` by `python scripts/emit.py`; never edit a generated file.
- Edit the candidate directly in `conductor/`. `scripts/check_conductor.py` validates its metadata, file membership and local file/section references, including a copied installation. `scripts/test_check_conductor.py` must reject deliberately broken packages. These checks also run through library integrity and CI; the delivery trials remain separate.
- Every existing library skill needs a fixture in `fixtures/` whose `EXPECTED_REPORT.md` names every planted defect; the integrity check refuses a skill without one. Keep these cases during conductor evaluation.
- A removed skill's old page is mapped to its replacement in `MOVED` in `scripts/emit.py`.
- Before pushing: `python scripts/emit.py --check`, `python scripts/check_library_integrity.py`, `python scripts/test_check_conductor.py`, `python scripts/test_check_trace.py`, `python scripts/test_conformance.py`, and `python scripts/check_site.py _site` on a build of the site. Preserve the plugin and MCP interfaces and run the MCP smoke check when those change.

## Repository structure

```
conductor/               candidate entry point, guidance and templates; canonical, not generated
docs/migration/          coverage and migration evidence
docs/trials/             trial protocol, runs and their current status
_prompts/                 the skills, one Markdown file each (the source)
workflow.json             where each kind of project starts, and the path with its gates
fixtures/                 a planted-defect project for every skill, with defects.json
harness/AGENTS.md         standing rules to paste into a target project's AGENTS.md
harness/check_trace.py    the ledger check for a target project's CI (Python 3.8+, no dependencies)
harness/conformance.py    the test a harness a model built for itself must pass
harness/ledger-example/   a small ledger that passes the check
scripts/                  emit.py (generates every form) and the checks
skills/ plugin/ compact/  generated: Agent Skills, the Claude Code plugin, short forms
_agent_skills/ redirects/ generated: the served SKILL.md files, and stubs for removed pages
mcp/                      the MCP server
```
