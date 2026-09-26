---
layout: skill
title: Skill Template
description: The shape every skill in this library follows, for anyone writing a new one. It is not a skill to load. Copy it, fill every part from the failures agents actually have on the task, and add a fixture that shows the skill catching them.
category: Meta
type: Task
---
**Role:** You are an agent acting as `<THE_ROLE>`: the one who owns this job and answers for its result. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names. They do not assume any hosted service either: where a step names a pull request, CI, an issue tracker, a package registry or a web search, use the project's own equivalent, which may be local and offline, and send nothing beyond what the project's confidentiality rules allow (`keep-it-confidential`).

**Objective:**
One sentence on the outcome in the world, then the three to six things the work delivers, each one checkable:

- `<WHAT_IS_TRUE_WHEN_IT_IS_DONE>`;
- ...

Deliver the changes, and a verdict table.

**Context:**
*   **The one input only the person can give (optional):** `<THE_INPUT>`. If this is still a placeholder, say where to find it instead (the ledger, the repository, the logs) and how to proceed without it.

What an agent does when asked for this, and why it looks like progress. Then the failures, the same across software and hardware, each with a bold name and one concrete case: a file, a number, a command. Write them from what agents have actually done, not from what could go wrong in principle; each becomes a planted defect in the fixture.

**The first failure.** A concrete case.

**The second failure.** A concrete case.

*   **Key Files & Folders:**
    *   Where the evidence for this task lives, and what each is read for.

**Requirements & Constraints:**
*   **Each rule starts with its lead in bold, as an instruction.** Then how to meet it, and how to tell that it was met. A rule that cannot be checked is advice; make it checkable or leave it out.
*   **Name the other skills a step relies on,** by name in backticks (`change-with-a-reason`), rather than repeating their methods.
*   **Say how a blocked route gets another route.** No skill concludes that an idea cannot be done or that a project should end; a constraint gets routes around it.
*   **Do not claim what you did not check.** Every item ends as `holds`, `broken` or `skipped`, with evidence or a reason.

**Guiding Principles:**
*   **Three to six short principles,** each a sentence that settles a case the rules do not cover.

**Execution Flow:**
1.  **The first step.** What is done, in order.
2.  **Verdict.** Everything again from cold, and the table.

**Deliverables:**
*   What the work leaves in the repository.
*   **A verdict table** with one row per item the Objective promises. Each is `holds`, `broken` or `skipped`, with the evidence or the reason.
*   Last line, the denominator: `9 holds, 1 broken, 1 skipped of 11 items.`
