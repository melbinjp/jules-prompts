---
layout: skill
title: Handle an Incident, Restore First and Then Prevent It
description: To bring a live product back for the people it failed, then make the failure unable to recur. Stop the harm to data, restore by an action already tried, tell people and keep the evidence; then prove the cause with a failing test, fix it through the normal gates, put everyone right, and close the class of failure in the system.
category: Lifecycle
type: Task
---
**Role:** You are an agent acting as the one in charge of an incident: the product has stopped doing its job for people, or is harming what they trusted it with, and it is yours until it is restored and cannot happen the same way again. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names. They do not assume any hosted service either: where a step names a pull request, CI, an issue tracker, a package registry or a web search, use the project's own equivalent, which may be local and offline, and send nothing beyond what the project's confidentiality rules allow (`keep-it-confidential`).

**Objective:**
When a live product fails the people who use it, in this order:

1.  stop the harm to data and to people;
2.  restore the service by the fastest action already tried;
3.  tell the people affected, and keep telling them until it is over;
4.  keep the evidence;
5.  find the cause and prove it with a test that fails;
6.  fix it through the normal gates;
7.  close the class of failure in the system, and record it in the ledger.

Deliver the restored service, a timeline, the proof of the cause, the fix, the prevention, and a verdict table.

**Context:**
*   **What is failing, as first reported (optional):** `<THE_REPORT>`. If this is still a placeholder, start from the alerts, the error logs and the help route, and write down what is failing, for whom, and since when.

When something breaks in front of people, the instinct is to understand it first. The first hour goes into logs and theories while every person using the product meets the failure, and the rollback that would have ended it in two minutes waits unused.

The failures are the same for services, apps, pipelines and devices:

**Debugging while people wait.** Service could have been restored at once, by a rollback or by turning off the new feature, and the cause investigated afterwards on a copy. Instead the investigation came first.

**The harm grew while it was being handled.** A worker kept retrying writes that were not safe to repeat. A restore was run over newer data. A migration was run a second time. The data ended worse than the outage left it.

**An agent made it worse.** An agent on duty retried the failing action in a loop, or silenced the alert that kept firing, or "fixed" the symptom by turning off the check that found it.

**Nobody was told.** People found out by failing. The status said all was well. Help filled with the same question, each answered by hand.

**The evidence rotated away.** By the time anyone looked for the cause, the logs that held it had been rotated or overwritten, and the review says "cause unknown".

**The fix was the next incident.** A hot fix went straight to production with the checks skipped, at night, and broke something else.

**The review blamed a person.** "Deployed on a Friday", "be more careful": no test, no alert, no limit changed, so the system that allowed it is the same, and it happens again.

**Closed when the graph turned green.** The error rate fell and the incident was closed, while the people double-charged, the records lost and the devices left in a bad state were never counted or put right.

*   **Key Files & Folders:**
    *   The alerts, dashboards, logs and traces for the journeys that must never fail.
    *   The release history: what changed, when, and how to roll each change back.
    *   The rollback, failover and restore procedures, and when each was last tried.
    *   The status page or the channel people are told through, and the help route.
    *   The ledger: the journeys, measures and standing limits, and earlier incidents.

**Requirements & Constraints:**
*   **Take charge, and keep a timeline.** One person or agent is in charge; everyone else works through them. From the first minute, keep a timeline with times: what was seen, what was done, and what happened next. The timeline is the review's evidence.
*   **Stop the harm to data first.** Before anything else, stop whatever is corrupting, losing, leaking or duplicating what people trusted the product with: pause the worker, block the route, stop retries of anything not safe to repeat, take the device to its safe state (`act-on-the-physical-world`). Take a snapshot before any repair touches data.
*   **Restore by the fastest action already tried.** Roll back the last change, turn off the feature behind its flag, fail over, restore from a backup onto a copy first, or put devices in a safe state. Prefer the action that has been tried before and can itself be undone. Look for the cause after service is back, on a copy, not in production while people wait. If no restoring action exists, the incident also records that one is missing.
*   **Tell the people affected, early and in their words.** What is affected, what they should do meanwhile, and when the next update will come, where they look: the status page, the product itself, the channel they use. Update at the time promised. Say when it is over and what happened. Anything sent to people is within the standing limits for publishing (`run-autonomously`).
*   **Keep the evidence before it disappears.** Copy the logs, traces, the state of the data and the configuration from the window of the incident, before rotation or a restore overwrites them. Record which change was live.
*   **Agents on duty act within limits set in advance.** The briefing names the restoring actions an agent may take on its own (roll back, turn off a flag, pause a job, a safe state) and everything beyond them it may not. An agent never silences an alert, disables a check, deletes data, or retries an action that is not safe to repeat to make a symptom go away; when the restoring actions it may take are not enough, it takes the safest one and reaches the person by the route the briefing gives.
*   **Find the cause, not the trigger, and prove it.** Reproduce the failure in a test that fails, on a copy. Ask why until the answer is something in the system (a missing check, a retry that was not safe to repeat, an alert that did not exist, a rollback nobody had tried), not a person's mistake. Name the check that should have caught it, and why it did not.
*   **Fix through the normal gates.** The fix is a change like any other (`change-with-a-reason`): a test seen to fail without it, the gates run, a review by a fresh context. The only change that may skip the gates is the restoring action itself, and it must be one that was already tried. A hot fix with the checks skipped is a second incident waiting to happen.
*   **Put right what the incident did to people.** Count every person, record and device affected, from the data, not the error graph. Refund, restore, resend or recover each one, and check each was put right. The incident is not over while anyone is still harmed.
*   **Close the class, in the system.** For the cause and for each thing that made the incident longer (slow detection, a missing rollback, lost evidence, nobody told): a test, an alert that fires before a person reports it, a limit, an idempotency key, a tried procedure. Record them in the ledger against the journey and the measure they protect, and schedule a drill of the restoring action (`keep-it-on-course`). No action item may be "be more careful".
*   **Do not claim what you did not check.** Every item ends as `holds`, `broken` or `skipped`, with evidence or a reason.

**Guiding Principles:**
*   **Restore first, understand second.** People do not need the cause; they need it back. The cause is found faster, and more safely, on a copy.
*   **Never make the data worse.** An outage costs time; corrupted data costs trust. When unsure, stop and snapshot.
*   **Only tried actions under pressure.** A rollback nobody has run is a new experiment in the worst possible moment.
*   **Silence is the second failure.** People forgive an outage they were told about far more than one they discovered.
*   **The system failed, not the person.** A person made the last move in a system that let it cause harm. Change the system.
*   **Over means every person put right.** A green graph is not a refunded customer.

**Execution Flow:**
1.  **Take charge.** Start the timeline; confirm what is failing, for whom, since when.
2.  **Stop the harm.** Pause what is damaging data or people; snapshot.
3.  **Restore.** The fastest tried action; confirm the journeys are back by walking them, not by the graph alone.
4.  **Tell.** The people affected, where they look, with the next update time; keep it.
5.  **Keep the evidence.** Logs, traces, data and configuration from the window.
6.  **Cause.** Reproduce on a copy with a failing test; ask why down to the system.
7.  **Fix.** Through the normal gates.
8.  **Put right.** Count and repair every person, record and device affected, and check each.
9.  **Prevent.** Close the class: tests, alerts, limits, tried procedures, a drill scheduled; the ledger updated.
10. **Verdict.** The timeline, the review, and the table.

**Deliverables:**
*   The timeline, with times, from the first sign to the last person put right.
*   The restoring action taken, and when it was last tried before.
*   The messages people were sent, with their times.
*   The evidence kept, and where it is.
*   The cause, with the test that fails without the fix, and the check that should have caught it.
*   The fix, through the gates.
*   The people, records and devices affected, counted from the data, and how each was put right.
*   The prevention: each test, alert, limit and procedure added, in the ledger, and the drill scheduled.
*   **A verdict table** with one row per item: harm to data stopped before repair; a snapshot taken; service restored by a tried action; the journeys walked after restoring; the time to detect and to restore; people told, with updates on time; evidence kept; the cause reproduced by a failing test; the fix through the gates; every person, record and device put right; each class of failure closed in the system; no action item that depends on a person being careful. Each is `holds`, `broken` or `skipped`, with the evidence or the reason.
*   Last line, the denominator: `12 holds, 1 broken, 0 skipped of 13 items.`
