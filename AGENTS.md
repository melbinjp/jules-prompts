# AGENTS.md

> How an AI agent finds and uses the skills in this repository, and how to change the library itself.

## What this repository is

Agent Skills that take any idea, software or hardware, in any state, to a product people use, and keep it working and improving. Each skill is one self-contained Markdown procedure, and none depends on a particular agent or harness (Jules, Claude Code, Codex, Cursor, Copilot, or anything that reads `AGENTS.md` or `SKILL.md`). Every skill has a fixture: a small project with planted defects that shows the skill catching them.

## Find a skill

- **By where the project is:** `workflow.json`. Its `entries` say where each kind of project starts (an idea and only a model, a project that already exists in any state, broken for people right now, and so on), its `steps` give the path in order with each step's `done_when` gate and the `branches` it calls on, and `throughout` names the skills that apply alongside every step. The same, readable: `https://jules-prompts.wecanuseai.com/workflow/`.
- **By task:** `GET https://jules-prompts.wecanuseai.com/llms.txt` lists every skill with its description and the link to its `SKILL.md`, starting with where to start by state.
- **By the Agent Skills discovery convention:** `GET https://jules-prompts.wecanuseai.com/.well-known/agent-skills/index.json`. Each entry has `name`, `type`, `description`, `url` and `digest`, the SHA-256 of the served `SKILL.md`; verify it.
- **From a clone:** `skills/<name>/SKILL.md`, or the source in `_prompts/`. Copy skills into `.claude/skills/` or `.agents/skills/`. `prompts.json` is an older index, still served.

Paste [`harness/AGENTS.md`](harness/AGENTS.md) into a target project's `AGENTS.md` so its rules apply even when nobody picks a skill.

## Use a skill

1. Load the matching `SKILL.md`. The procedure starts after its front matter.
2. Fill any placeholders, such as `<THE_IDEA>`; a skill says what to do if one is left unfilled.
3. Follow it. Report every claim as `holds`, `broken` or `skipped`, and end with the count of each.
4. To see whether an agent or model can follow a skill, run it on the skill's fixture and score the report: `python scripts/score_fixture.py fixtures/<name> REPORT.md`.

## Offline and private use

The skills need no network. On a private or air-gapped project, install from a clone (`skills/`, or `/plugin marketplace add /path/to/clone`), run the MCP server with `JULES_PROMPTS_DIR=/path/to/clone` (it then refuses to use the network), give small local models the short forms in `compact/`, and qualify each model on the fixtures before routing work to it. `keep-it-confidential` covers the project's own confidentiality.

## Change the library

- The source of each skill is `_prompts/task_<name>.md`; a new one starts from the Skill Template, `_prompts/template_master_prompt.md`. Everything an agent loads (`skills/`, `plugin/`, `compact/`, `_agent_skills/`, the indexes, `llms.txt`, the workflow includes and the redirect stubs) is generated from it and from `workflow.json` by `python scripts/emit.py`; never edit a generated file.
- Every skill needs a fixture in `fixtures/` whose `EXPECTED_REPORT.md` names every planted defect; the integrity check refuses a skill without one.
- A removed skill's old page is mapped to its replacement in `MOVED` in `scripts/emit.py`.
- Before pushing: `python scripts/emit.py --check`, `python scripts/check_library_integrity.py`, `python scripts/test_check_trace.py`, `python scripts/test_conformance.py`, and `python scripts/check_site.py _site` on a build of the site.

## Repository structure

```
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
