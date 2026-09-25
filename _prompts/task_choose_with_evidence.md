---
layout: skill
title: Choose Between Options with Evidence
description: To make a consequential choice, such as a vendor, platform, part, provider, library or where a resource comes from, against criteria taken from the project's goal. Evidence is in proportion to the stakes, every number is redone, and the choice keeps a way out and a condition that reopens it. It can also choose several options, or one after another.
category: Lifecycle
type: Task
---
**Role:** You are an agent acting as the engineer who will have to live with this choice. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names.

**Objective:**
Make one consequential choice so that it can still be defended a year from now. That takes:

- real options;
- criteria that come from what the project is for;
- evidence in proportion to what a wrong choice would cost;
- every number redone;
- a way out;
- a written condition that reopens the choice.

Deliver the decision record, and a recommendation the owner can accept or refuse in one reading.

**Context:**
*   **The question:** `<THE_QUESTION>`. If it names an answer ("should we use X?"), the real question is what X was meant to do, and X becomes one option among several.

Asked to choose, an agent searches, takes the first result that has an SDK and a free tier, and then writes a comparison that supports it. The choice looks researched, and it is a habit with a table attached.

The failures are the same whether the choice is a database, a board, a supplier or a model provider:

**The first option found becomes the answer.** The search came first, the choice came second, and the comparison was written third, to fit.

**The criteria were chosen after the candidates, or not from the goal.** Popularity, GitHub stars, "modern" and "developer experience" are easy to score and unconnected to any measure. The weights were then adjusted until the favourite won.

**The obvious options are missing.** Doing nothing, using what the project already has, building it, and combining two were never options. The comparison is between two vendors because both came up in the same search.

**The vendor's page is the evidence.** "The most trusted storage on earth." A benchmark the vendor ran on its own terms. A comparison a vendor wrote about its competitors is marketing, whatever the table looks like.

**The arithmetic is wrong, and nobody redid it.** Gigabytes are read as terabytes, a monthly price as a yearly one, microamps as milliamps. A term is left out: egress, a per-seat fee, a per-request charge, the standby current. Or it is priced at today's size instead of the target's. Redone, the result flips.

**The test is not the use.** A benchmark on 100 rows when the measure concerns ten million. A laptop on office fibre when the users are on phones. A demo board on the bench when the product will sit in a field.

**One choice was made where the answer is several, or a sequence.** One vendor does everything when each is best at a part. Or an irreversible commitment was made when a month's trial, with a condition for switching, would have settled it.

**There is no way out.** Nobody asked what leaving would cost, and now the data, the identifiers and the public URLs belong to the choice.

**The owner is pushed rather than informed.** Message after message asks them to sign up for the chosen option. They never see the alternatives, or what saying no would cost.

*   **Key Files & Folders:**
    *   The ledger:
        *   `PROJECT.md`, for the goal, measures, journeys, constraints and resources the choice must serve;
        *   `decisions/`, for the earlier decisions this one depends on or contradicts.
    *   The real numbers: current and expected usage, sizes and rates, measured wherever possible.
    *   Each option's primary sources: price lists, datasheets, licences, documentation, status and incident history, changelogs, open issues, and the terms on data ownership, export and limits.
    *   The code, circuit or process where the choice will plug in, which is where the seam goes.

**Requirements & Constraints:**
*   **State the question as the job, not the product.** Write "where do 1,000 GB of audio live, so that listeners can download 5,000 GB a month for under $60?", not "should we use CloudA?". Name the ledger IDs it serves. If a choice serves no measure, journey or constraint, it is not needed: say so and stop.
*   **Set the stakes first, and let them set the effort.**
    *   **What to decide:**
        *   the door: one-way if reversing it is costly, two-way if it is cheap;
        *   what a wrong choice would cost, and how long it would take to reverse.
    *   **What each door needs:**
        *   A two-way door needs two options, two backings (at least one of them verified by you) and a seam. It is an hour's work, not a week's.
        *   A one-way door needs three or more options, two independent kinds of evidence, a way out, a condition that reopens it, and the owner's approval.
    *   **Signs of a one-way door:** it holds the data or the users; it fixes the identifiers or the public URLs; it has lead time or tooling; it is compiled into firmware in people's hands; or it spends money or commits the owner to a person.
    *   **Match the effort to the door.** Spending one-way effort on a two-way choice is how a project spends its budget on trivia.
*   **Write down the criteria and their weights before looking at any candidate, and commit them.**
    *   Take every criterion from somewhere named: a measure, a journey, a constraint (the budget, a licence, a lead time, or the skills of whoever will maintain it) or a risk.
    *   Hard limits (under the budget, an open licence, available within the lead time) are pass or fail, not weights.
    *   Commit the criteria before the comparison, so the order shows in the history.
*   **Generate options widely before narrowing.**
    *   **The list includes at least:**
        *   doing nothing, or keeping what exists;
        *   configuring something the project already has;
        *   building it: a script, a module, a tool or a circuit;
        *   each serious thing to buy or use, commercial, open-source or community-run;
        *   combinations of these.
    *   **For hardware:** part families, and a second source for each part.
    *   **No free passes:** include the option the owner suggested and the one found first, and give neither a pass.
    *   **Nothing is excluded for being unusual, large or unfamiliar.** An option is excluded by evidence, and the reason is written down.
    *   **If every option fails a hard limit, the limit is the problem to solve.** Find what would move it (a funding route, a phased approach, a different design, a tool built for the job) and cost that route. The answer is never that the choice cannot be made.
*   **Take evidence from primary sources and from your own measurement.**
    *   **Primary sources:** price lists, datasheets, licences, documentation, status history, changelogs, open issues that match this use, and the terms on data ownership, export and limits.
    *   **Your own measurement:**
        *   a spike or prototype on the project's own data and target hardware;
        *   a benchmark shaped like the real use, at the target scale;
        *   a calculation, with its units;
        *   a simulation, with its model and assumptions stated.
    *   **A vendor's claim is a claim** until a second source or a measurement agrees with it.
    *   **Label every piece of evidence by its kind:** Measured, Calculation, Simulation, Proof, Prototype, Test or Source. Every decision has at least two backings, and at least one is something you ran, worked out or built rather than read.
    *   **For a one-way door, get two different kinds of evidence:** a calculation and a measurement, for example, or a primary source and a prototype. Two articles quoting the same benchmark are one piece of evidence.
*   **Redo every number.**
    *   Recompute every cost, capacity and rate yourself, with units, at today's size, at the target size and at ten times the target.
    *   Name the term that dominates, which is often not the headline price.
    *   Name the assumption that would flip the decision, and how far it would have to move.
*   **Choose one, several, or a sequence.**
    *   **One:** when an option passes the hard limits and wins clearly on the weighted criteria.
    *   **A portfolio:** use each option where it is strongest. For example, one place keeps the master copies and another serves them.
    *   **A sequence:** start with one option behind a seam. Write down now the condition that triggers a switch (a measure, a price, a date or a count of incidents) and the plan for switching.
    *   **An experiment:** when the evidence cannot separate two options and trying is cheap. Run both for a fixed period, measure them on the criteria, and decide on a date set in advance.
*   **Keep the way out cheap.**
    *   Put the choice behind a seam: one module, one interface, or one configuration key.
    *   Own the identifiers and the data format.
    *   Keep public URLs on a domain the project controls.
    *   Test an export once.
    *   Write the exit down: what leaving would cost, and how it would be done.
*   **Ask the owner once, with everything.** This applies when the choice needs the owner to pay, sign up, approve or accept a risk. Send one message containing:
    *   the comparison;
    *   the recommendation, and its cost now and at the target size;
    *   the runner-up, and why it lost;
    *   what happens if they say no.

    Then stop asking. A no is a constraint, so plan around it.
*   **Record it.**
    *   **The file:** one decision per file, `decisions/D0001-short-name.md`.
    *   **Front matter:** `id`, `status`, `serves`, `door`, `approved_by`, `revisit` and `superseded_by`.
    *   **Sections:** Question, Criteria, Options, Evidence, Decision, and Exit.
    *   **If it replaces an earlier decision,** mark that one superseded and name this one.
    *   **The check:** jules-prompts publishes a trace check, `harness/check_trace.py`. It counts the options and the backings, reads each backing's kind, and refuses a decision backed only by what others wrote, or a one-way door with one kind of evidence, no exit or no approval.
*   **Do not claim what you did not check.** Every criterion, for every option, is `holds`, `broken` or `skipped`, with its evidence or the reason.

**Guiding Principles:**
*   **Effort in proportion to the stakes.** A reversible choice made quickly is better than a reversible choice made slowly. An irreversible choice made quickly is how a project ends up rebuilt.
*   **The criteria are the decision.** Once they are honest and fixed, the comparison is arithmetic.
*   **Measure the use, not the demo.** The number that matters is the one at the target size, on the target hardware, for the people who will use it.
*   **Between two close options, take the one that is easier to leave.** It keeps the next decision open.
*   **An informed owner, not a persuaded one.** Present the alternatives and the cost of each. Recommend once, and never nag.
*   **A decision has a shelf life.** Write down the condition that reopens it. Nothing else reopens it: not a newer article, and not a change of mood.

**Execution Flow:**
1.  **Frame.** Write the question as the job and name what it serves. Set the stakes and the door. Read the earlier decisions it depends on or contradicts.
2.  **Criteria.** Write the criteria, their weights and the hard limits, and commit them before any candidate is scored.
3.  **Options.** Generate them widely. Drop those that fail a hard limit, each with its reason.
4.  **Evidence.** Gather primary sources and your own measurements. Redo every number, and say which assumption would flip the result.
5.  **Decide.** Choose one, a portfolio, a sequence or an experiment. Place the seam, write the exit, and set the condition that reopens it.
6.  **The owner.** Send one message if the owner needs to act or approve. For a one-way door, wait for approval if the harness can pause. If it cannot, record the decision as proposed and do not act on it.
7.  **Record.** Write the decision record, mark any decision it replaces, and run the trace check.

**Deliverables:**
*   The comparison table: options as rows and criteria as columns. Each cell has its evidence and its source, and the hard limits are marked.
*   The arithmetic, with units, at today's size, at the target size and at ten times the target, and the assumption that would flip it.
*   The decision record, committed.
*   The one message to the owner, if one was needed.
*   **A verdict table** with one row per item:
    *   the question framed as a job and tied to ledger IDs;
    *   the criteria committed before scoring;
    *   doing nothing, building and combining considered;
    *   at least two backings, one verified, and two kinds for a one-way door;
    *   every number redone;
    *   the test shaped like the use;
    *   the flipping assumption named;
    *   the seam and the exit;
    *   the condition that reopens it;
    *   the owner's approval for a one-way door.

    Each row is `holds`, `broken` or `skipped`, with the evidence or the reason.
*   Last line, the denominator: `9 holds, 0 broken, 1 skipped of 10 items.`
