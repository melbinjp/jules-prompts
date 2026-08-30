# Skills

Each directory here is an [Agent Skill](https://agentskills.io/specification): a
`SKILL.md` with YAML front matter that names the skill and says when to use it,
then the same procedure as the matching file in `_prompts/`.

`_prompts/` is the source. This directory is generated:

```bash
python scripts/generate_skills.py          # write
python scripts/generate_skills.py --check  # CI: fail if they disagree
```

A copy that can drift is a defect. The integrity check refuses a pass when they
do.

## Install

Copy the skill directories you want into wherever the agent looks. The spec
does not mandate a root; these are the usual ones:

```bash
# Claude Code, project-local
cp -R skills/qa-an-agents-tests .claude/skills/

# Codex / agents.md-style
cp -R skills/qa-an-agents-tests .agents/skills/

# all of them
cp -R skills/* .claude/skills/
```

Or point the agent at this repository. The MCP server still serves the same
text as slash-command prompts for clients that do not load skills:

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

The standing doctrine — three verdicts, prove it can fail, say what you read —
lives in [`harness/AGENTS.md`](../harness/AGENTS.md). Paste that into a project's
`AGENTS.md` so it fires when nobody picks a skill.

## What is not here

`template_master_prompt.md` is a golden copy for authors, not a task. It has no
skill.
