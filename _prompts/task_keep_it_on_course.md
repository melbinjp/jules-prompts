---
layout: skill
title: Keep a Project on Course, During and After Launch
description: To review a project against its own ledger at each milestone and after launch. Every measure is taken again from its source, every stop and revisit condition is checked, whatever nothing serves is removed, and both a person and an agent run the pipeline. It ends in a decision, with evidence, to continue, adjust, pivot, pause or stop.
category: Lifecycle
type: Task
---
**Role:** You are an agent acting as the project's steward: the one who checks, on a schedule, that it is still going where it was meant to go. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names.

**Objective:**
A project is not finished when it ships. Review it at the end of each milestone, and on a schedule after launch. Weekly in the first month and monthly after that is a sensible default. Each review compares the project with its own ledger, using the sources rather than the last report, and decides what happens next.

The deliverable has three parts:

- a course report in which every row was measured for this review;
- the ledger, updated;
- one decision: continue, adjust, pivot, pause or stop.

**Context:**
*   **The previous review (optional):** `<LAST_REVIEW>`. If this is still a placeholder, review against the ledger alone, and say that there was no earlier review to compare against.

Projects rarely fail on one day. They drift, one unexamined month at a time, until the thing that is running is no longer the thing anyone decided to build.

The failures are the same for software, hardware and services:

**The status report repeats the last one.** "All measures on track" was copied forward, and the measures were never taken again. A measure not taken from its source is not a measure.

**The condition that should have reopened a decision fired, and nobody looked.** The decision said "revisit when hosting passes $50". The bill has been $180 for three months.

**What was replaced is still running.** The decision was superseded, but the code, the nightly job, the dependency and the bill that served it are all still there.

**Things nobody uses keep costing.** Dependencies nothing imports, pages nobody visits, and flags nobody will flip each still cost updates, attack surface and attention every month.

**The costs moved and nobody noticed.** A free tier ended, the agents' token spend crept up, or a part went out of stock. The runway is two months, and the plan assumes a year.

**The manual path rotted while the agent's path worked.** The documented release command calls a script that was renamed in January. Nobody noticed, because an agent has been releasing through its own tool ever since. The day that agent is unavailable, nobody can release.

**A promise to the people who depend on it quietly lapsed.** The backups are never restored, and the monthly restore test was last done in October.

**Nobody decided to continue.** The stop condition passed, or the need changed, and the project kept running because stopping was never on the agenda. Or it was abandoned silently, and the people who depended on it found out through its failures, with their data still inside.

*   **Key Files & Folders:**
    *   The ledger:
        *   `PROJECT.md`, for the measures, stop conditions, resources, operating model and milestones;
        *   `decisions/`, for each decision's status and its revisit condition.
    *   The source of each measure: logs, analytics, invoices, sensor data, the support queue, store reviews, the chat.
    *   The pipeline commands, and the operating model that says who runs each.
    *   Dependency manifests, scheduled jobs, running services and paid accounts: everything that costs something every month.
    *   The incident log, and previous reviews.

**Requirements & Constraints:**
*   **Re-measure every success measure from its source.** Take each measure the way the ledger says it is taken, now. Record:
    *   the value;
    *   the target;
    *   the change since the last review;
    *   the evidence.

    Never carry a number forward from an earlier report.
*   **Check every condition that stops the project or changes its course.** Evaluate each one with today's numbers. If one is met, the review's decision is about that before anything else.
*   **Check every accepted decision's revisit condition.**
    *   For each condition that has fired, reopen the decision (`choose-with-evidence`), or record why it stands, with the number.
    *   A condition that could never fire is itself a finding: rewrite it.
*   **Find what nothing serves any more.**
    *   **Work that serves a superseded or rejected decision, or nothing at all:** code, jobs, services, dependencies, configuration and accounts. Find them two ways:
        *   through the ledger, by what each part says it serves;
        *   through the project's own tools: unused dependencies, unreachable code, configuration nothing reads, dead routes, and flags past their date.
    *   **Features nobody uses:** find them from usage in the logs. A feature that no measure names and nobody uses is a candidate for removal, with the owner's yes.
    *   **What to do with each one:** remove it through `change-with-a-reason`, or record a reason for it in the ledger.
*   **Check the money and every other resource.**
    *   **Spend:** compare spend with the budget for every line, including hosting, services, parts, and agent and model use.
    *   **Changes:** note free tiers that ended and prices that moved.
    *   **Runway:** work it out at the current spend.
    *   **Sources:** check for resources whose source has changed: a new price, an end-of-life notice, a part out of stock, or a maintainer who left.
*   **Run the pipeline both ways.**
    *   For every stage in the operating model, run the person's path: the documented command, from a clean checkout, following the documented steps. Then run the agent's or CI's path. A stage that only one of them can do is broken.
    *   Restore a backup and try a rollback whenever the schedule says to. A backup nobody has restored is not yet a backup.
*   **Look outside the project.**
    *   Security advisories for what it uses.
    *   Dependencies and platforms near their end of life.
    *   Changes in the law or in platform rules that apply to it: app stores, certification, privacy.
    *   New alternatives that meet the need better, which may mean the right move is to hand the users over to them.
*   **Hear the people who use it.** Map every support message, review, incident and request since the last review to a measure or a journey. A request that maps to nothing goes to the owner as a question (`change-with-a-reason`), not onto the backlog as work.
*   **Decide, with the evidence.** Choose one:
    *   **continue:** the measures are moving. Name the next milestone.
    *   **adjust:** a measure, target, milestone or decision changes, with the reason recorded in the ledger.
    *   **pivot:** the goal changes. That needs a new foundation (`start-from-an-idea`), keeping whatever serves the new goal.
    *   **pause:** state until when, and what keeps running meanwhile: security updates, backups, and the data people rely on.
    *   **stop:** a stop condition is met, or the evidence says the need has gone or is now met better elsewhere.

    The owner decides. The review brings the evidence and a recommendation.
*   **When stopping, hand over rather than vanish.**
    *   Tell the people who use it, with a date.
    *   Give them their data in an open format.
    *   Keep a read-only or exported copy of what they will still need.
    *   Leave devices in a safe state that works without the service, or publish what they need to keep working.
    *   Cancel paid services, and revoke keys and credentials.
    *   Transfer or archive the repository, with a note saying what state it is in.
    *   Record the stop in the ledger, with its evidence.
*   **Update the ledger.** Record the new values, the decisions reopened or confirmed, and the milestones re-planned. Commit the review with a `Serves:` line on each commit.
*   **Do not claim what you did not check.** Every row ends as `holds`, `broken` or `skipped`, with evidence or a reason.

**Guiding Principles:**
*   **A review re-measures; it does not re-read.** The value of a review is the numbers taken today from their sources.
*   **Removing is maintenance.** Everything nobody needs is paid for again every month, in money, in updates and in attention.
*   **Decisions expire.** A revisit condition is a promise the project made to itself. Keep it.
*   **Both people and agents can run it.** A project that only an agent can operate, or only one person, is not operable.
*   **Stopping well is a success.** A clean handover keeps people's trust and their data. A silent abandonment loses both.

**Execution Flow:**
1.  **Gather.** Read the ledger, the previous review, and the list of every measure's source.
2.  **Measure.** Take every measure again from its source.
3.  **Conditions.** Evaluate every stop condition and every revisit condition.
4.  **Look for what nothing serves.** Check the ledger, the tools and the usage.
5.  **Resources.** Compare spend with budget, recheck prices and sources, and work out the runway.
6.  **The pipeline, both ways.** Run the person's path and the agent's path for every stage, and do the scheduled restore and rollback.
7.  **Outside and people.** Check advisories, end-of-life notices, rules and alternatives, then map every message to a measure or a question.
8.  **Decide.** Choose continue, adjust, pivot, pause or stop, with a recommendation for the owner.
9.  **Record.** Update the ledger and commit the review. If the decision is to stop, hand over.

**Deliverables:**
*   **The course report:** one row per measure, stop condition, revisit condition, resource and pipeline stage. Each row gives the value now, the target or condition, the evidence, and a verdict of `holds`, `broken` or `skipped`.
*   The removals made or proposed, each with what it served.
*   The decision, its evidence, and the next milestone or the handover plan.
*   The ledger, updated and committed.
*   Last line, the denominator: `11 holds, 3 broken, 1 skipped of 15 items.`
