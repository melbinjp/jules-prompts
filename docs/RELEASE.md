# Release: the conductor as the one entry point

Version 3.0.0. The conductor replaces the 26-skill
library everywhere it was published.

## Supported scope

- **What it is for.** Delivering a project of any kind, software, physical, service, creative or hybrid.
  It starts from nothing, a single word, an idea, an existing build or a live product, and ends at a result
  the owner accepts. It hands over whatever must keep running.
- **How it is installed.** Copy the whole `conductor/` folder (`SKILL.md`, `guidance/`, `templates/`) into
  `.agents/skills/` or `.claude/skills/`. Or use the zip at `/.well-known/agent-skills/conductor.zip`, or read it from the site. The Claude Code
  plugin and the MCP server that once delivered it were removed by the owner on 2026-09-30.
- **Where it runs.** With any agent that reads a file or fetches a URL. It assumes no hosted service and no
  network.
- **What stays.** `harness/AGENTS.md` (standing rules, now pointing at the conductor), `harness/check_trace.py`
  (for projects that already keep the older ledger; unchanged), `harness/conformance.py` (for harnesses a model
  built for itself), and the 26 fixtures as the conductor's regression cases.
- **What is checked structurally.** Package integrity and references. Byte-for-byte agreement of every
  generated form with the source. A reproducible archive with a stated digest. A real build of the site. Each fixture's expected report against its planted defects.
  `docs/migration/checks.md` says which check protects which behaviour.

## Known limitations

October 1 local strengthening adds complete consequence/journey coverage, evidence-based challenge
of accepted methods, conditional alternatives, settled-core claim consistency, qualified takeover
and explicit operating modes with existing cloud reuse. The shared state template is an optional
view of existing records. Standing rules and generated forms follow the source. Fifteen new defects
extend eight existing regression cases, for 161 across the same 26 fixtures; the trial results below
remain the historical 146-defect run. October 3 adds two further defects on premature-start
(`means-capped-the-result`, `actions-without-a-vision`), 163 across the same 26 fixtures: a season
promise dropped because current boards cannot meet it, and a service list treated as the work.
The trial record is unchanged. These changes do not establish successful autonomous
operation of Utily or any workspace project. Model detection of the new cases remains to be tried.

- Structural checks do not show that an agent delivers a project. That is what the trials in
  `docs/trials/` are for, and the section below points at their record.
- The fixtures are scored by whether a report names each planted defect. The scorer reads strings, so a
  report can name a defect without understanding it; review of the substance is separate.
- The conductor's guidance is text an agent may follow badly. A small local model may not manage its longer
  sections; qualify a model on a fixture before routing work to it.
- Steps that need a person (an inspection the law requires, an owner's approval, a client's acceptance)
  stay pending until that person acts. The conductor records them as not verified and does not replace them.
- Search engines will keep showing the old description of the site until they crawl it again.
- Who can push to `main` decides what every agent that loads the conductor is told to do. That is a branch
  protection setting, not something this repository can check.

What would close these gaps, and our view on it, is in `docs/VISION.md`.

## Evidence

Full record: `docs/trials/report.md`. Raw reports, reviews and logs: `docs/trials/runs/windows-cohort/`.

- **Software project.** Delivered to acceptance. A reviewer who did not build it passed all ten criteria, and the
  runner followed the written instructions on a fresh copy with the real data and got the correct list.
  Not tried: the double-click launcher on Windows, and a timed run.
- **Repair café and greenhouse, both simulations.** Authority held in every run: no spend above the limit, no
  contract signed, no message to anyone outside the permitted list, no action repeated after an interruption.
  Workflow did not fully pass. In the last runs the greenhouse passed 7 of 9 criteria (resumption, change
  control and the safe-side failure among them) and failed commissioning and handover while the owner's choices
  were still open; the repair cafe passed 5 of 8 and failed on plan detail, a publicity step taken before the hall
  confirmed, and a spend over the reduced grant. Nine conductor changes came from the trials.
- **26 failure cases.** 125 of 146 planted defects identified, 16 partly, 5 missed. No unresolved miss in the
  critical classes (data loss, security, physical safety, acting outside authority, done without evidence).
  On the 11 cases the old library was also scored on, the conductor scored 42 identified, 5 partial and 1 missed of
  48, against 44, 4 and 0. Different models and reviewers, so this shows parity of a kind, not superiority.
- **Not established.** Behaviour on a real installation, a real purchase or another project. The sealed
  held-back case was not run.

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
- **Plugin and MCP.** The old plugin and the `task_*` MCP prompts are gone, and the plugin and MCP server
  that replaced them were removed by the owner on 2026-09-30. Install by copying `conductor/`.
- **Fixtures.** They stay in place. Their `skill` field names the retired skill each was written for and is
  kept as provenance. The request for each is in `docs/trials/tools/requests.json`.
