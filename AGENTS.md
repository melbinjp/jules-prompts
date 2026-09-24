# AGENTS.md, Machine-Readable Instructions for AI Agents

> This file tells AI agents how to discover and use the procedures in this repository.

## What This Repository Is

A curated library of **pre-made, machine-readable task prompts**, **Agent Skills**, and **planted-failure fixtures** for coding agents (Jules, Claude Code, Codex, Cursor, Copilot, Windsurf, and anything that reads `AGENTS.md` or `SKILL.md`). Each prompt is a structured markdown file that guides an agent through a specific software engineering task. The instructions are harness-agnostic: they do not depend on any product's tool names.

## How to Discover Prompts

### 1. From the site (Recommended)

```
GET https://jules-prompts.wecanuseai.com/llms.txt
```

Every skill with a one-line description and a link to its `SKILL.md`. Pick the one that matches the task, fetch it, follow it. Each is self-contained.

For clients that implement [Agent Skills discovery](https://github.com/cloudflare/agent-skills-discovery-rfc):

```
GET https://jules-prompts.wecanuseai.com/.well-known/agent-skills/index.json
```

Each entry has `name`, `type` (`skill-md`), `description`, `url` and `digest` (the SHA-256 of the served `SKILL.md`; verify it). The files are served byte for byte from `skills/`.

The older index is still served, and each entry now carries a `skill` URL:

```
GET https://jules-prompts.wecanuseai.com/prompts.json
```

### 2. Direct File Access

All prompts are in `_prompts/` as markdown files. Each file has YAML front matter with `title`, `description`, and `category`, followed by the procedure.

### 3. Agent Skills

`skills/<name>/SKILL.md` is the same procedure in the [Agent Skills](https://agentskills.io/specification) format. Generated from `_prompts/` by `python scripts/emit.py`. Copy into `.claude/skills/` or `.agents/skills/`.

### 4. Standing doctrine

[`harness/AGENTS.md`](harness/AGENTS.md) is a fragment to paste into a *target* repository's `AGENTS.md` so three-verdict, prove-it-can-fail instructions fire on every task.

## How to Use a Prompt

1. **Select** a prompt from the JSON index, or load the matching skill.
2. **Fetch** the prompt content from its `url` or `source_path`.
3. **Parse** the markdown, the procedure starts after the YAML front matter (`---`).
4. **Fill placeholders**: some prompts contain placeholders like `<REPO_OR_SITE_URL>`.
5. **Execute**: use the prompt as the task instruction.
6. **If the task is one the fixtures cover**, write a report that names planted defects by the strings in `fixtures/<name>/defects.json`, then run `python scripts/score_fixture.py fixtures/<name> REPORT.md`.

## Prompt Categories

| Category | Description |
|----------|-------------|
| **End to End** | Taking a project in any state to production quality (`take-to-production`) |
| **Physical Systems** | Commands to hardware, devices and real-world services (`act-on-the-physical-world`) |
| **Initial Scoping** | First-pass tasks for new or unknown projects (audit, hardening, frontend build) |
| **Iterative Development** | Tasks for improving existing code (fix & refine, UI/UX, build from plan) |
| **Maintenance** | Ongoing tasks (dependency updates, curation, agent-PR review) |
| **Security** | Security review of agent-written code |
| **Meta** | Templates and prompt-generation tools |

## Recommended Workflow

For taking a project in any state to production, in this order:

1. `task_repair_setup_script`: make it run from cold
2. `task_take_to_production`: write the bar, close the gap, end in a verdict table (repeatable)
3. `task_review_an_agent_pr`: review each pull request the agent produced (repeatable)
4. `task_update_dependencies`: keep it current (optional, repeatable)

See `workflow.json` for the machine-readable workflow graph.

## Repository Structure

```
_prompts/           → Canonical procedure markdown (Jekyll collection)
skills/             → Agent Skills generated from _prompts/
_agent_skills/      → The same SKILL.md files, wrapped so the site serves them verbatim
.well-known/agent-skills/index.json → Agent Skills discovery index, with digests
llms.txt            → Every skill, for an agent given only the domain
fixtures/           → Planted-failure trees + defects.json
harness/AGENTS.md   → Standing doctrine fragment for other repos
prompts.json        → Machine-readable prompt index (JSON API)
scripts/            → emit.py (generates every form), the integrity, site and fixture checks
workflow.json       → Machine-readable workflow graph
AGENTS.md           → This file (agent instructions for *this* repo)
PROMPTS_GUIDE.md    → Human-readable prompt library guide
ENVIRONMENT_SETUP.md → Guide for configuring repos so agents can run
```
