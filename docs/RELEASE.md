# Release: the conductor as the one entry point

Version 3.0.0 of the plugin and 2.0.0 of the MCP server. The conductor replaces the 26-skill
library everywhere it was published.

## Supported scope

- **What it is for.** Delivering a project of any kind, software, physical, service, creative or hybrid.
  It starts from nothing, a single word, an idea, an existing build or a live product, and ends at a result
  the owner accepts. It hands over whatever must keep running.
- **How it is installed.** Copy the whole `conductor/` folder (`SKILL.md`, `guidance/`, `templates/`) into
  `.agents/skills/` or `.claude/skills/`. Or use the zip at `/.well-known/agent-skills/conductor.zip`, or the
  Claude Code plugin `jules-prompts`. Over MCP it is the prompt `conductor`, with each guidance and template
  file as a further prompt and as a resource.
- **Where it runs.** With any agent that reads a file or fetches a URL. It assumes no hosted service and no
  network, and the MCP server can run from a local copy with the network refused.
- **What stays.** `harness/AGENTS.md` (standing rules, now pointing at the conductor), `harness/check_trace.py`
  (for projects that already keep the older ledger; unchanged), `harness/conformance.py` (for harnesses a model
  built for itself), and the 26 fixtures as the conductor's regression cases.
- **What is checked structurally.** Package integrity and references. Byte-for-byte agreement of every
  generated form with the source. A reproducible archive with a stated digest. The MCP server against a real
  client. A real build of the site. Each fixture's expected report against its planted defects.
  `docs/migration/checks.md` says which check protects which behaviour.

## Known limitations

- Structural checks do not show that an agent delivers a project. That is what the trials in
  `docs/trials/` are for, and the section below points at their record.
- The fixtures are scored by whether a report names each planted defect. The scorer reads strings, so a
  report can name a defect without understanding it; review of the substance is separate.
- The conductor's guidance is text an agent may follow badly. A small local model may not manage its longer
  sections; qualify a model on a fixture before routing work to it.
- Steps that need a person (an inspection the law requires, an owner's approval, a client's acceptance)
  stay pending until that person acts. The conductor records them as not verified and does not replace them.
- The MCP server in network mode reads GitHub at start-up. It was tested against a real client from a local
  copy; the network path is exercised by CI on the pushed commit.
- Search engines will keep showing the old description of the site until they crawl it again.
- Who can push to `main` decides what every agent that loads the conductor is told to do. That is a branch
  protection setting, not something this repository can check.

## Evidence

EVIDENCE: filled in from docs/trials/runs/status.md

## Migration from the 26-skill library

- **Source.** `conductor/` is the only procedure source. `_prompts/`, `workflow.json` and `compact/` are
  removed; the last commit that has them is tagged `library-26-final`.
- **Rules.** Every rule, step, fixture defect and check of the old library is mapped to where it now lives in
  `docs/migration/coverage-map.md`. What each old check protected, and what replaced it, is in
  `docs/migration/checks.md`.
- **Records.** The `PROJECT.md` ledger, the `decisions/` format and the `Serves:` and `Verified:` lines are
  replaced by the project's own records and ADRs. Projects that already keep the ledger keep it, and keep
  running `harness/check_trace.py`.
- **Reports.** Holds, broken and skipped become verified, failed and not verified, with not applicable and
  exception as separate outcomes that are never counted as passes. Reports still end with their counts.
- **The path.** The fixed eleven-step path and the entry states are replaced by the control loop in
  `SKILL.md`, which starts where the project's first unmet acceptance is.
- **Addresses.** The site's old pages (`/prompts/task_*.html`, `/tasks.html`, `/workflow/`, `/prompts-guide/`,
  `/environment-setup/`) redirect to the conductor or to the guidance page that holds their content. Each old
  skill's `SKILL.md` address serves a short notice naming the conductor, and `/workflow.json` serves a notice
  in JSON. `llms.txt` and the discovery index now list the conductor.
- **Plugin.** Version 3.0.0 carries `skills/conductor/`. Reinstall it; the 26 old skills are no longer in it.
- **MCP.** The prompts `task_*` are replaced by `conductor` and `conductor-guidance-*` and
  `conductor-template-*`. Placeholder arguments are gone: the conductor has none.
- **Fixtures.** They stay in place. Their `skill` field names the retired skill each was written for and is
  kept as provenance. The request for each is in `docs/trials/tools/requests.json`.
