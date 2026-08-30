# AGENTS.md — Machine-Readable Instructions for AI Agents

> This file tells AI agents how to discover and use the procedures in this repository.

## What This Repository Is

A curated library of **pre-made, machine-readable task prompts**, **Agent Skills**, and **planted-failure fixtures** for coding agents (Jules, Claude Code, Codex, Cursor, Copilot, Windsurf, and anything that reads `AGENTS.md` or `SKILL.md`). Each prompt is a structured markdown file that guides an agent through a specific software engineering task. The instructions are harness-agnostic: they do not depend on any product's tool names.

## How to Discover Prompts

### 1. JSON API (Recommended)

Fetch the prompt index:

```
GET https://jules-prompts.wecanuseai.com/prompts.json
```

This returns a JSON object with:
- `version` — API version
- `total_prompts` — number of available prompts
- `categories` — list of prompt categories
- `prompts[]` — array of prompt objects, each with `title`, `description`, `category`, `url`, `source_path`, and `slug`

### 2. Direct File Access

All prompts are in `_prompts/` as markdown files. Each file has YAML front matter with `title`, `description`, and `category`, followed by the procedure.

### 3. Agent Skills

`skills/<name>/SKILL.md` is the same procedure in the [Agent Skills](https://agentskills.io/specification) format. Generated from `_prompts/` by `python scripts/generate_skills.py`. Copy into `.claude/skills/` or `.agents/skills/`.

### 4. Standing doctrine

[`harness/AGENTS.md`](harness/AGENTS.md) is a fragment to paste into a *target* repository's `AGENTS.md` so three-verdict, prove-it-can-fail instructions fire on every task.

## How to Use a Prompt

1. **Select** a prompt from the JSON index, or load the matching skill.
2. **Fetch** the prompt content from its `url` or `source_path`.
3. **Parse** the markdown — the procedure starts after the YAML front matter (`---`).
4. **Fill placeholders** — some prompts contain placeholders like `<REPO_OR_SITE_URL>`.
5. **Execute** — use the prompt as the task instruction.
6. **If the task is one the fixtures cover**, write a report that names planted defects by the strings in `fixtures/<name>/defects.json`, then run `python scripts/score_fixture.py fixtures/<name> REPORT.md`.

## Prompt Categories

| Category | Description |
|----------|-------------|
| **Initial Scoping** | First-pass tasks for new or unknown projects (audit, hardening, frontend build) |
| **Iterative Development** | Tasks for improving existing code (fix & refine, UI/UX, build from plan) |
| **Maintenance** | Ongoing tasks (dependency updates, curation, agent-PR review) |
| **Meta** | Templates and prompt-generation tools |

## Recommended Workflow

For taking a new project from zero to production, execute prompts in this order:

1. `task_repair_setup_script` — Make the repository usable by an agent
2. `task_audit_repo` — Understand the project
3. `task_harden_repo_initial` — Set up CI/CD and testing
4. `task_fix_and_refine` — Fix bugs and architecture
5. `task_harden_repo_iterative` — Ongoing improvement (repeatable)

See `workflow.json` for the machine-readable workflow graph.

## Repository Structure

```
_prompts/           → Canonical procedure markdown (Jekyll collection)
skills/             → Agent Skills generated from _prompts/
fixtures/           → Planted-failure trees + defects.json
harness/AGENTS.md   → Standing doctrine fragment for other repos
prompts.json        → Machine-readable prompt index (JSON API)
workflow.json       → Machine-readable workflow graph
AGENTS.md           → This file (agent instructions for *this* repo)
PROMPTS_GUIDE.md    → Human-readable prompt library guide
ENVIRONMENT_SETUP.md → Guide for configuring repos so agents can run
```
