# Jules Prompts

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/melbinjp/jules-prompts?style=social)](https://github.com/melbinjp/jules-prompts)

A library of Agent Skills that take any idea, software or hardware, to a working product and keep it working and getting better. It is engineering work, and it treats nothing as impossible: a constraint (money, time, physics, law, skills) is a problem with routes around it, and the skills find the routes, cost them honestly and take the first step. Every decision is backed by evidence someone verified, every change is traced to the goal, and every claim ends as holds, broken or skipped, so a project neither drifts nor stalls nor is left half-built. Planted-failure fixtures show each skill catching what it claims to.

**Where to start depends on what you have.**

- **One model and one person, and nothing else:** [Run a Project Autonomously](_prompts/task_run_autonomously.md). The model builds its own agent harness and every tool it lacks, from a specification it proves against [`harness/conformance.py`](harness/conformance.py). The person is asked everything only they can answer at the start. Development then runs without waiting: safe because of a sandbox, checkpoints and standing limits, and correct because nothing is called done until its checks pass.
- **An idea:** [Start a Project from an Idea](_prompts/task_start_from_an_idea.md). It works out what it takes to make the idea happen: the need, what already exists to build on, the costs and the funding routes, and the path that fits what the owner has. It makes the few costly-to-reverse decisions with verified evidence, makes every stage of the pipeline runnable by a person or an agent, builds one thin slice end to end, and writes the ledger every later change traces to.
- **A project that exists, in any state** (a prototype, a half-built or vibe-coded build, an inherited codebase, a working product with gaps): found it again on paper with [Start a Project from an Idea](_prompts/task_start_from_an_idea.md), so what is already there gets its reasons or is marked for revisiting, then [Take a Project to Production Quality](_prompts/task_take_to_production.md). It takes the project to the point where it does its one job dependably, feels finished and carries nothing it does not need, and shows that item by item.
- **What people and agents will see, do and hear:** [Design the Experience, with Evidence](_prompts/task_design_the_experience.md). Every journey as a flow with every state and word, one system of look and behaviour in code, every action operable by a person, an agent or automation with the same limits, threaded to the architecture, and tested with people. For screens, command lines, APIs, voices and devices.
- **Ready for people:** [Release a Product to Its People, and Hear Back](_prompts/task_release_to_people.md). Every way in walked from a clean device, listings and legal texts true to the product, a staged release that pauses itself, people told where they already are, and someone answering.
- **Live, stalled or drifting:** [Keep a Project on Course and Improving](_prompts/task_keep_it_on_course.md) finds the next route to the same goal and the next improvements.
- **Broken for people right now:** [Handle an Incident, Restore First and Then Prevent It](_prompts/task_handle_an_incident.md). Stop the harm, restore by a tried action, tell people, keep the evidence; then the cause, the fix, everyone put right, and the class of failure closed.
- **A change to make,** however vaguely it was asked for: [Change a Project with a Reason](_prompts/task_change_with_a_reason.md).
- **Anything that moves, heats, dispenses, spends or sends:** [Act on the Physical World](_prompts/task_act_on_the_physical_world.md).

Between those, [Choose Between Options with Evidence](_prompts/task_choose_with_evidence.md) makes each consequential choice, and [Keep a Project Confidential, Offline First](_prompts/task_keep_it_confidential.md) runs alongside every step of a private, proprietary or offline project. [Keep a Project on Course and Improving](_prompts/task_keep_it_on_course.md) runs at every milestone and continuously after launch: it takes every measure again, switches routes where one is blocked, removes what nothing serves, and ranks the next improvements. The [workflow](workflow.json) puts them in order, with the state each kind of project enters at, the gate that ends each step and the skills each one calls on.

A prompt and a skill here are the same procedure. The prompt is the text; the skill is that text with a name and a description in front, so an agent can decide for itself when to load it. The site serves both.

The name is historical: the library began in 2025 as prompts for Jules, Google's coding agent, and is not affiliated with Google. The instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names.

## Layers

1. **`_prompts/`**: the canonical procedure text. Website, JSON index, MCP slash commands.
2. **`skills/`**: the same text as [Agent Skills](https://agentskills.io/specification). Generated from `_prompts/`. Copy into `.claude/skills/` or `.agents/skills/`.
3. **`fixtures/`**: miniature repositories with planted defects. The way to see a skill go red.
4. **`plugin/`**: the whole library as one installable Claude Code plugin, a manifest and the skills. `.claude-plugin/marketplace.json` lists it, so `/plugin marketplace add melbinjp/jules-prompts` then `/plugin install jules-prompts@jules-prompts` installs it.
5. **`library.json`**: every procedure, its category and its tier, in one machine-readable list.
6. **The site's agent files**: `llms.txt`, `.well-known/agent-skills/index.json` and `_agent_skills/`, so an agent given only the domain can find and load every skill, and verify each against its digest.

Everything after the first is generated by `scripts/emit.py` and checked byte for byte in CI,
so a copy that has drifted from its source fails the build instead of quietly disagreeing
with it. Adding a new output format, whatever the ecosystem asks for next, is one entry in
that script's `TARGETS`; the guarantee is structural rather than per-format.

### Groups

Each skill says what it is for in its `category`. **Lifecycle** is the path itself, from a model and a person or an idea to a product that keeps working. **Design** is what people and agents meet. **Build** and **Verify** are the methods the path calls on to change a project and to check it. **Security** and **Physical Systems** apply alongside every step. Every skill has a fixture that shows it catching what it claims to.

Standing doctrine, for a project's `AGENTS.md` so it fires when nobody picks a skill: [`harness/AGENTS.md`](harness/AGENTS.md).

### The ledger

The lifecycle skills keep one ledger in the project they work on: `PROJECT.md` (the goal, success measures, journeys, resources, course changes and milestones, each with an ID) and `decisions/` (one file per decision, saying what it serves, its options and evidence, its way out and what would reopen it). Every commit names what it serves and how it was verified, in `Serves:` and `Verified:` lines. [`harness/check_trace.py`](harness/check_trace.py) is the check for that project's CI. It needs Python 3.8 and nothing else, and refuses a decision that serves nothing or has fewer than two backings (at least one measured, calculated, simulated, proved, prototyped or tested), a costly-to-reverse decision without two kinds of evidence, an exit or an approval, and a commit that does not say what it serves or how it was verified. [`harness/ledger-example/`](harness/ledger-example/) is a small worked example that passes it, and `scripts/test_check_trace.py` breaks that example in each of the 29 ways the check covers, to show it goes red.

The check proves a record has the right shape. Whether its criteria, evidence and arithmetic are honest is what the skills are for, and two fixtures show the difference: the trace check passes on `vendor-comparison` and `six-months-in`, and each still has six or seven planted defects.

## Getting Started

The [skills page](https://jules-prompts.wecanuseai.com/tasks.html) lists every skill by what it is for, and the [workflow page](https://jules-prompts.wecanuseai.com/workflow/) shows where each kind of project starts and the gate that ends each step.

To prepare a repository so any agent can clone, install and test it from cold, use [Repair the Environment Setup Script](_prompts/task_repair_setup_script.md).

## How to Use

### From the site, with no install

Tell the agent: `Read https://jules-prompts.wecanuseai.com/llms.txt and follow the skill that matches the task.` Clients that support [Agent Skills discovery](https://github.com/cloudflare/agent-skills-discovery-rfc) can start from `https://jules-prompts.wecanuseai.com/.well-known/agent-skills/index.json` instead: every skill, with a SHA-256 digest of its `SKILL.md`.

### As Agent Skills (installed)

```bash
# one, straight from the site
mkdir -p .claude/skills/take-to-production
curl -fsSL https://jules-prompts.wecanuseai.com/.well-known/agent-skills/take-to-production/SKILL.md \
  -o .claude/skills/take-to-production/SKILL.md

# or all of them, from a clone
cp -R skills/* .claude/skills/
```

Paste [`harness/AGENTS.md`](harness/AGENTS.md) into the project's `AGENTS.md`.

### As an MCP server

Claude Code, Claude Desktop, VS Code / Copilot Chat, Windsurf and Zed surface MCP prompts as slash commands. The server reads this repository live rather than a bundled copy, index and bodies both from GitHub, so it starts even where the website is unreachable.

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

### Offline, and on private projects

Nothing in the skills needs the internet, and nothing here has to be fetched while you work. Fetching a skill from the site also tells the site's host which skill someone wanted; installing from a copy tells nobody.

1. **Get the library once.** `git clone https://github.com/melbinjp/jules-prompts`, or carry a clone across on removable media. Note the commit hash; on the other side, `git fsck` and `git rev-parse HEAD` confirm the copy is whole and is that commit.
2. **Install the skills from the copy.** `cp -R jules-prompts/skills/* .claude/skills/` (or `.agents/skills/`). In Claude Code, `/plugin marketplace add /path/to/jules-prompts` then `/plugin install jules-prompts@jules-prompts` installs from the directory.
3. **Run the MCP server from the copy, with no network.** Point the client at `node /path/to/jules-prompts/mcp/index.js` with `JULES_PROMPTS_DIR=/path/to/jules-prompts` in its environment. In that mode the server reads the copy and refuses to use the network at all; CI proves it. Its two dependencies come from `npm ci`, run once where a registry or a mirror is reachable, with `node_modules` carried across with the clone.
4. **Give small local models the short forms.** `compact/<name>.md` is each skill as a checklist of a few hundred words, for models whose context cannot hold the full skill next to the code.
5. **Qualify a model before trusting it with a stage.** Run it on the skill's fixture and score the report with `scripts/score_fixture.py`, all offline. A model's reputation is a claim; its score on the fixture is evidence.
6. **Check the project's ledger offline.** `harness/check_trace.py` needs Python and nothing else.
7. **No agent harness at all?** A model with only a chat endpoint builds its own from the specification in `run-autonomously`, and it is ready when `python harness/conformance.py --harness "<its command>"` passes: a scripted model drives it through proper and careless actions and checks every prompt, file and commit.
8. **Keep the project itself private.** [Keep a Project Confidential, Offline First](_prompts/task_keep_it_confidential.md) maps every channel the work can leave through (hosting, agents and model providers, telemetry, registries, crash reports, searches), proves the pipeline runs with the network off, and sets how the internet is used when it must be.

### For humans (copy-paste)

1. Open the prompt file (e.g. [`task_take_to_production.md`](_prompts/task_take_to_production.md)).
2. Copy the body after the YAML front matter.
3. Paste it into the agent's instruction input.

### For agents (programmatic)

1. Fetch `https://jules-prompts.wecanuseai.com/llms.txt`, or the discovery index at `/.well-known/agent-skills/index.json`.
2. Select a skill by its description.
3. Fetch its `SKILL.md` and follow it. `prompts.json` still works, and now carries each prompt's `skill` URL.

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
3. Run `python scripts/emit.py` so every generated form (skills, plugin, index, site files) matches.
4. Update `workflow.json` only when the recommended sequence, or where a kind of project starts, changes.
5. Add a fixture under `fixtures/` with `defects.json` and an `EXPECTED_REPORT.md` that names every planted defect. Every skill has one; the integrity check refuses a skill without.
6. When a skill is removed, map its old page to the skill that replaces it in `MOVED` in `scripts/emit.py`, so saved links still land somewhere useful.
7. `python scripts/check_library_integrity.py`, `python scripts/emit.py --check` and `python scripts/test_check_trace.py` must pass, and so must `python scripts/check_site.py _site` on a build of the site (CI builds it the way GitHub Pages does).

## Contributing

Contributions are welcome. The goal is a small set of high-quality, general-purpose procedures that encode best practices for the failures agents actually have, and a corpus that can show those procedures failing.

If you have an idea for a new skill or fixture, please open an issue to discuss it. A new skill starts from the [Skill Template](_prompts/template_master_prompt.md) and comes with a fixture.
