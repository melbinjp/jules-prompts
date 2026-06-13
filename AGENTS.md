# AGENTS.md — Machine-Readable Instructions for AI Agents

> This file tells AI agents how to discover and use the prompts in this repository.

## What This Repository Is

This is a curated library of **pre-made, machine-readable task prompts** designed for AI coding agents (Jules, GitHub Copilot, Cursor, Windsurf, etc.). Each prompt is a structured markdown file that guides an agent through a specific software engineering task.

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

All prompts are located in the `_prompts/` directory as markdown files. Each file has YAML front matter with `title`, `description`, and `category` fields, followed by the full prompt text.

## How to Use a Prompt

1. **Select** a prompt from the JSON index based on its `title`, `description`, or `category`.
2. **Fetch** the prompt content from its `url` (rendered HTML) or read the markdown file at `source_path`.
3. **Parse** the markdown content — the actual prompt starts after the YAML front matter (`---`).
4. **Fill placeholders** — some prompts contain placeholders like `<REPO_OR_SITE_URL>` that need to be replaced with actual values.
5. **Execute** — use the prompt as your task instruction.

## Prompt Categories

| Category | Description |
|----------|-------------|
| **Initial Scoping** | First-pass tasks for new or unknown projects (audit, hardening, frontend build) |
| **Iterative Development** | Tasks for improving existing code (fix & refine, UI/UX, build from plan) |
| **Maintenance** | Ongoing tasks (dependency updates, curation) |
| **Meta** | Templates and prompt-generation tools |

## Recommended Workflow

For taking a new project from zero to production, execute prompts in this order:

1. `task_audit_repo` — Understand the project
2. `task_harden_repo_initial` — Set up CI/CD and testing
3. `task_fix_and_refine` — Fix bugs and architecture
4. `task_harden_repo_iterative` — Ongoing improvement (repeatable)

See `workflow.json` for the machine-readable workflow graph.

## Repository Structure

```
_prompts/           → All prompt markdown files
prompts.json        → Machine-readable prompt index (JSON API)
workflow.json       → Machine-readable workflow graph
AGENTS.md           → This file (agent instructions)
PROMPTS_GUIDE.md    → Human-readable prompt library guide
ENVIRONMENT_SETUP.md → Guide for configuring repos for Jules
```
