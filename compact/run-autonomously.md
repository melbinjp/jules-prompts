# Run a Project Autonomously, from One Model and One Person: short form

To take one language model and one person to a project that builds itself. The model builds its own agent harness and every tool it lacks, from a specification it can prove against a test. The person is asked everything only they can answer at the start, and development then runs without waiting. It is safe because of a sandbox, checkpoints and standing limits, and it is correct because nothing counts as done until its checks pass. Offline, online or both, unattended, supervised or by hand.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/run-autonomously/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

Fill in: `<THE_HARNESS>`, `<THE_PROJECT>`

## Objective

From a model and a person, reach a build that runs on its own and cannot call anything done that is not:

- the model working as an agent, in a harness it built itself if it has none, proved against `harness/conformance.py`;
- every tool the project needs that the model lacks, built into the repository with a test;
- everything that needs the person asked at the start, in one sitting, with standing answers and standing limits for what can be decided in advance;
- development that then runs without waiting: choices the briefing did not settle are researched, tested, made, recorded, and open to the person's override at any time;
- a context that stays small and true however long the build runs;
- safety from the setup, not from asking: a sandbox, a checkpoint after every step, standing limits for anything that leaves the sandbox;
- quality from gates: nothing is done until its checks pass, and the loop continues until they do;
- the same setup working offline, online or both, unattended, supervised, or run by hand.

Then run the lifecycle inside it, entering where the project's state says (`workflow.json` in jules-prompts): `start-from-an-idea` (for a project that already exists, its re-founding form), `design-the-experience`, `change-with-a-reason`, `take-to-production`, `release-to-people` and `keep-it-on-course`, with `handle-an-incident` whenever the live product fails people.

## Rules

- Become an agent. If there is no harness, build one to this specification.
- Build every missing tool, and prove it.
- Ask the person everything only they can answer, at the start, in one sitting.
- Decide the rest yourself, and keep every decision open to the person.
- Keep the context small, fresh and true.
- Make it safe by the setup, so it never has to ask.
- Make it correct by gates, so a result can only be one that passed.
- Work in the smallest loop that finishes things.
- Split into a team only where it pays, and coordinate through the repository.
- Explore where nothing is known.
- Make the way of working a setting, not a design.
- Do not claim what you did not check.

## Steps

1. Take stock. What the model can do here: read, write, run, reach a network, reach the person. What it cannot, and what will close each gap.
2. Become an agent. Use the harness there is, or build one to the specification, and run `harness/conformance.py` against it until every check holds.
3. Brief. Write `BRIEFING.md` and go through it with the person in one sitting: the answers, the delegations, the standing limits, the budget, the confidentiality classes.
4. Set up the sandbox and the gates. The environment, the checkpoints, the limits enforced where actions happen, the stop, and the model qualified on its fixture.
5. Found the project. `start-from-an-idea` inside the loop, or its re-founding form for a project that already exists; then `design-the-experience` for the journeys.
6. Build. Milestone by milestone, change by change, each through its gates, committed, with `STATE.md` rewritten and choices recorded, never waiting.
7. Review at each milestone. `keep-it-on-course`, including the run: budget spent, choices made and overridden, prompts near the window's edge, gates that failed and why.
8. Report. What passed its gates, what has not yet, and the table.

## Deliver

- The harness, if one was built, with the conformance run that passed.
- The tools built for the gaps, each with its test.
- `BRIEFING.md`, answered, with the delegations and the standing limits.
- `STATE.md` and `CHOICES.md`, current, and the run log.
- A verdict table with one row per item: the harness conformant; the briefing complete; every choice recorded with its reason and none waited on; every override applied; every prompt under half the window; every change through its gates and committed; every milestone reviewed by a fresh context; the sandbox holding nothing of the person's beyond what was granted; every action outside it within its standing limit; the budget within its cap; the stop tried once; each connectivity mode the rules allow proved.
- Last line, the denominator: `13 holds, 0 broken, 1 skipped of 14 items.`
