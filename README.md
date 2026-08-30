# Jules Prompts

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/melbinjp/jules-prompts?style=social)](https://github.com/melbinjp/jules-prompts)

A curated library of machine-readable task prompts, Agent Skills, and planted-failure fixtures for coding agents. The procedures cover the failures agents actually have: broken setup scripts, vague issues, tests that need services a sandbox cannot start, and pull requests that only read as finished.

The name is historical. The instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names.

## Three layers

1. **`_prompts/`** — the canonical procedure text. Website, JSON index, MCP slash commands.
2. **`skills/`** — the same text as [Agent Skills](https://agentskills.io/specification). Generated from `_prompts/`. Copy into `.claude/skills/` or `.agents/skills/`.
3. **`fixtures/`** — miniature repositories with planted defects. The way to see a skill go red.

Standing doctrine, for a project's `AGENTS.md` so it fires when nobody picks a skill: [`harness/AGENTS.md`](harness/AGENTS.md).

## Getting Started

The [library guide](PROMPTS_GUIDE.md) explains each prompt and a recommended sequence.

To prepare a repository so an agent can clone, install, and test it, see the [Environment Setup Guide](ENVIRONMENT_SETUP.md).

## How to Use

### As Agent Skills (preferred)

```bash
cp -R skills/qa-an-agents-tests .claude/skills/
# or all of them
cp -R skills/* .claude/skills/
```

Paste [`harness/AGENTS.md`](harness/AGENTS.md) into the project's `AGENTS.md`.

### As an MCP server

Claude Code, Claude Desktop, VS Code / Copilot Chat, Windsurf and Zed surface MCP prompts as slash commands. The server reads this repository live rather than a bundled copy.

```json
{
  "mcpServers": {
    "jules-prompts": {
      "command": "npx",
      "args": ["-y", "github:melbinjp/jules-prompts"]
    }
  }
}
```

Prompts that contain placeholders such as `<PR_URL_OR_DIFF_RANGE>` expose them as arguments, so the client asks for the value and the server substitutes it before handing over the text.

### For humans (copy-paste)

1. Open the prompt file (e.g. [`task_audit_repo.md`](_prompts/task_audit_repo.md)).
2. Copy the body after the YAML front matter.
3. Paste it into the agent's instruction input.

### For agents (programmatic)

1. Fetch `https://jules-prompts.wecanuseai.com/prompts.json`.
2. Select a prompt by title, description, or category.
3. Fetch the rendered prompt from its `url`, or read `_prompts/<slug>.md`.

### Against fixtures (proof)

```bash
python scripts/score_fixture.py fixtures/unfailable-tests path/to/REPORT.md
python scripts/score_fixture.py fixtures/unfailable-tests --self-check
```

Verdicts are **holds** / **broken** / **skipped**. The last line is coverage.

## Keeping the library current

New prompts are useful when they cover a recurring task that the existing set does not handle clearly. Do not add prompts only to increase the count.

When adding or revising a prompt:

1. Keep its YAML front matter aligned with the other files in `_prompts/`.
2. Write harness-agnostic instructions: no `You are Jules`, no `set_plan` / `submit` / `request_code_review`.
3. Run `python scripts/generate_skills.py` so `skills/` matches.
4. Update `PROMPTS_GUIDE.md` when its purpose or recommended use changes.
5. Update `workflow.json` only when the recommended sequence changes.
6. If the prompt exists to catch a failure, add a fixture under `fixtures/` with `defects.json` and an `EXPECTED_REPORT.md` that names every planted defect.
7. Keep `AGENTS.md`, this README, and the generated `prompts.json` fields aligned.
8. `python scripts/check_library_integrity.py` must pass.

## Contributing

Contributions are welcome. The goal is a small set of high-quality, general-purpose procedures that encode best practices for the failures agents actually have — and a corpus that can show those procedures failing.

If you have an idea for a new prompt, skill, or fixture, please open an issue to discuss it.
