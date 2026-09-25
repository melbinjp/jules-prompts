---
layout: skill
title: Keep a Project on Course and Improving
description: To keep a project working and getting better, at every milestone and continuously after launch. Every measure is taken again from its source, every course change and revisit condition is checked, whatever nothing serves is removed, and both a person and an agent run the pipeline. The next improvements are chosen by what they move, so the project never drifts, stalls or is left half-done.
category: Lifecycle
type: Task
---
**Role:** You are an agent acting as the project's steward: the one who keeps it working, keeps it improving, and makes sure it is still going where it was meant to go. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names.

**Objective:**
A project is never finished. Shipping is a milestone, and after it the work is to keep the project working and make it better, on purpose, measure by measure. Run this at the end of every milestone and on a steady cadence after launch: weekly in the first month and monthly after that is a sensible default, and more often while a measure is off target. Each run compares the project with its own ledger, using the sources rather than the last report.

The deliverable has four parts:

- a course report in which every row was measured for this run;
- the next improvements, ranked by what they move;
- the course: continue, adjust, re-route or grow;
- the ledger, updated.

**Context:**
*   **The previous review (optional):** `<LAST_REVIEW>`. If this is still a placeholder, review against the ledger alone, and say that there was no earlier review to compare against.

Projects rarely fail on one day. They drift or stall, one unexamined month at a time, until the thing that is running is no longer the thing anyone decided to build, or nothing is moving at all.

The failures are the same for software, hardware and services:

**The status report repeats the last one.** "All measures on track" was copied forward, and the measures were never taken again. A measure not taken from its source is not a measure.

**The condition that should have reopened a decision fired, and nobody looked.** The decision said "revisit when hosting passes $50". The bill has been $180 for three months.

**What was replaced is still running.** The decision was superseded, but the code, the nightly job, the dependency and the bill that served it are all still there.

**Things nobody uses keep costing.** Dependencies nothing imports, pages nobody visits, and flags nobody will flip each cost updates, attack surface and attention every month.

**The costs moved and nobody noticed.** A free tier ended, the agents' token spend crept up, or a part went out of stock, and the plan still assumes last year's numbers.

**The manual path rotted while the agent's path worked.** The documented release command calls a script that was renamed in January. Nobody noticed, because an agent has been releasing through its own tool ever since. The day that agent is unavailable, nobody can release.

**A promise to the people who depend on it quietly lapsed.** The backups are never restored, and the monthly restore test was last done in October.

**It stalled.** The first route met a problem (a price rose, a channel brought nobody, a measure would not move) and nobody had a next route, so the work stopped and the project was left half-done.

**Met targets ended the improving.** The measures reached their targets and nothing has moved since, while the people using it keep asking for more.

*   **Key Files & Folders:**
    *   The ledger:
        *   `PROJECT.md`, for the measures, course changes, resources, operating model and milestones;
        *   `decisions/`, for each decision's status and its revisit condition.
    *   The source of each measure: logs, analytics, invoices, sensor data, the support queue, store reviews, the chat.
    *   The pipeline commands, and the operating model that says who runs each.
    *   Dependency manifests, scheduled jobs, running services and paid accounts: everything that costs something every month.
    *   The incident log, and previous reviews.

**Requirements & Constraints:**
*   **Take every success measure again from its source.** The way the ledger says it is taken, now. Record the value, the target, the change since the last run, and the evidence. Never carry a number forward from an earlier report.
*   **Check every course change.** Evaluate each condition with today's numbers. If one is met, switch to the route it names now, and record the switch. If a route is blocked and no course change covers it, find the next route (`choose-with-evidence`) and add it to the ledger: the goal stands and the route changes.
*   **Check every accepted decision's revisit condition.** For each condition that has fired, reopen the decision (`choose-with-evidence`), or record why it stands, with the number. A condition that could never fire is itself a finding: rewrite it.
*   **Find what nothing serves any more.**
    *   **Work that serves a superseded or rejected decision, or nothing at all:** code, jobs, services, dependencies, configuration and accounts. Find them two ways: through the ledger, by what each part says it serves; and through the project's own tools, for unused dependencies, unreachable code, configuration nothing reads, dead routes, and flags past their date.
    *   **Features nobody uses:** find them from usage in the logs. A feature that no measure names and nobody uses is a candidate for removal, with the owner's yes.
    *   **What to do with each one:** remove it through `change-with-a-reason`, or record a reason for it in the ledger.
*   **Check the money and every other resource, and route around what has changed.** Compare spend with the budget for every line, including hosting, services, parts, and agent and model use; note free tiers that ended and prices that moved; work out the runway. Where a cost has outgrown its budget, or a source has changed (a price, an end-of-life notice, a part out of stock, a maintainer who left), find the route that brings it back: another source, a cheaper design, a funding route. Money is a constraint to engineer around, never the reason a project stops.
*   **Run the pipeline both ways.** For every stage in the operating model, run the person's path (the documented command, from a clean checkout, following the documented steps) and the agent's or CI's path. A stage only one of them can do is broken. Restore a backup and try a rollback whenever the schedule says to; a backup nobody has restored is not yet a backup.
*   **Look outside the project.** Security advisories for what it uses; dependencies and platforms near their end of life; changes in law or platform rules that apply to it (app stores, certification, privacy); and new parts, services and techniques that would serve the goal better, as options to adopt.
*   **Hear the people who use it.** Map every support message, review, incident and request since the last run to a measure or a journey. A request that maps to nothing goes to the owner as a proposed new measure (`change-with-a-reason`), not onto the backlog as unexplained work.
*   **Choose the next improvements.** Rank the candidates by the measure each moves, how far it is from its target, how many people it affects, and what it costs, and take the top ones into the next milestone as changes (`change-with-a-reason`). When a measure has held its target for a while, raise the target or add the next measure, with the owner, so the project keeps getting better rather than settling.
*   **Set the course, with the evidence.** One of:
    *   **continue:** the measures are moving. Name the next milestone and its improvements.
    *   **adjust:** a measure, target, milestone or decision changes, with the reason in the ledger.
    *   **re-route:** a route is blocked. Switch to another approach, channel, supplier, design or funding route that reaches the same goal.
    *   **grow:** the goal holds. Propose the next goal to the owner, and found it (`start-from-an-idea`), keeping everything that serves it.

    The owner decides; the run brings the evidence and a recommendation. If the owner chooses to pause, keep security updates, backups and the data people rely on running, and write down what restarts it.
*   **Keep it able to continue, whoever runs it.** Anyone (a new person, agent or team) could pick the project up from the repository alone: the ledger, the commands, the notes, and credentials held by the owner rather than by an agent. If the owner hands it on, hand over properly: tell the people who use it, transfer access, rotate keys, and walk the new owner through one run of this review.
*   **Update the ledger.** Record the new values, the decisions reopened or confirmed, the routes switched, and the milestones re-planned. Commit the review with a `Serves:` line and a `Verified:` line on each commit.
*   **Do not claim what you did not check.** Every row ends as `holds`, `broken` or `skipped`, with evidence or a reason.

**Guiding Principles:**
*   **A review re-measures; it does not re-read.** Its value is the numbers taken today from their sources.
*   **Every blocked route has another.** The goal stands; the route changes. A project stalls only when nobody looked for the next route.
*   **There is always a next improvement.** A measure at its target is a measure ready for a higher one.
*   **Removing is maintenance.** Everything nobody needs is paid for again every month, in money, updates and attention.
*   **Decisions expire.** A revisit condition is a promise the project made to itself. Keep it.
*   **Both people and agents can run it.** A project that only an agent can operate, or only one person, is not operable.

**Execution Flow:**
1.  **Gather.** Read the ledger, the previous review, and the list of every measure's source.
2.  **Measure.** Take every measure again from its source.
3.  **Conditions.** Evaluate every course change and every revisit condition; switch routes where one fired.
4.  **Look for what nothing serves.** Check the ledger, the tools and the usage.
5.  **Resources.** Compare spend with budget, recheck prices and sources, work out the runway, and route around what changed.
6.  **The pipeline, both ways.** Run the person's path and the agent's path for every stage, and do the scheduled restore and rollback.
7.  **Outside and people.** Advisories, end-of-life notices, rules and new options; map every message to a measure or a proposal.
8.  **Improve and set the course.** Rank the next improvements; continue, adjust, re-route or grow, with a recommendation for the owner.
9.  **Record.** Update the ledger and commit the review.

**Deliverables:**
*   **The course report:** one row per measure, course change, revisit condition, resource and pipeline stage. Each row gives the value now, the target or condition, the evidence, and a verdict of `holds`, `broken` or `skipped`.
*   The removals made or proposed, each with what it served.
*   The next improvements, ranked, each with the measure it moves and its cost.
*   The course, its evidence, and the next milestone.
*   The ledger, updated and committed.
*   Last line, the denominator: `11 holds, 3 broken, 1 skipped of 15 items.`
