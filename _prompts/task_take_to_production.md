---
layout: skill
title: Take a Project to Production Quality
description: To take a project in any state, software or physical, to production quality. It does its one job dependably and securely on every platform its people use, loses and leaks nothing, feels finished, carries nothing it does not need, and every area that decides this, from security and privacy to operations, is checked rather than assumed.
category: End to End
type: Task
featured: 2
---
**Role:** You are a coding agent acting as the engineer who owns this product end to end. Explore, decide, build, and verify. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names. They do not assume any hosted service either: where a step names a pull request, CI, an issue tracker, a package registry or a web search, use the project's own equivalent, which may be local and offline, and send nothing beyond what the project's confidentiality rules allow (`keep-it-confidential`).

**Objective:**
Bring the project to production quality from whatever state it is in: an idea, a prototype, something that works until it doesn't, or a mature system with gaps. Production quality here means four things, and you will check each rather than claim it:

1.  It does the one job it exists for, on every platform its people actually use.
2.  It never loses, corrupts or exposes what people trusted it with, whatever the environment or an attacker does.
3.  It feels finished to use: nothing rough, nothing unexplained, nothing unreachable.
4.  It carries nothing it does not need.

Deliver the changes, and a verdict table that shows each of those item by item.

**Context:**
*   **What the owner says it is for (optional):** `<WHAT_IT_IS_FOR>`. If this is still a placeholder, derive it from the project and say how you did.

Asked to make something "production-grade", an agent reaches for the visible signs of production: a CI file, a Dockerfile, a coverage badge, docstrings on every function, an operations runbook. They are cheap to add and easy to see, and none of them is the thing. A project can have every one of them and still lose a person's work when the tab closes, fail outright on the phone half its users carry, and greet a mistake with "Something went wrong."

**Production quality is a property of what a person experiences, not of the repository's furniture.** It is decided by the worst thing that happens to a real person, on a real device, on a bad day. So the method is to write down who uses this and for what, then go and make the bad day happen, on each platform and under each failure the environment can produce, and fix what breaks in order of what it costs the person it happens to.

The failures are consistent across every kind of project:

The obvious platform works and the others were never tried. It was built in one browser, on one operating system, one screen size, one fast network, one board revision. It uses a capability the others lack, and nothing detects that.

The happy path is finished and the environment is not. Storage fills, the network drops, the app is sent to the background, the battery dies, a permission is refused, the device is slow, two copies run at once, the upgrade meets last year's data. Each of these is certain to happen to someone. Each was imagined once and never caused.

The features are complete and the product is not. An empty screen that shows nothing, an error that names an exception, a control a keyboard cannot reach, a layout that scrolls sideways on a small phone, a button that does nothing visible for two seconds. None of these fails a test. All of them tell the person that nobody finished this.

The review covers what the agent thought of. An area nobody named (who can call this endpoint, what is in the logs, whether the backup restores, what the licence of that font allows) is not reported as broken, it is not reported at all, and a report that is silent about it reads exactly like one that checked it. Security is where this costs most: a product can pass every journey on every platform and still hand anyone who asks for it the data of everyone else.

**Complexity arrives dressed as diligence.** Every framework, build step, abstraction, service and document added "for production" is one more thing that can break, must be updated, and must be understood by the next person. Past the point of need, each one lowers dependability while looking like it raises it.

"No new features" is the wrong rule, and so is "add whatever seems useful". The right one is: whatever the core job needs in order to be dependable is in scope, however large; whatever it does not need is out, however easy.

When the project acts on the physical world (hardware, devices, instruments, vehicles, or a service that ships, pays or sends), all of this applies, plus one more fact: a wrong action there cannot be undone by a redeploy. Treat every such action with the procedure in `act-on-the-physical-world`.

*   **Key Files & Folders:**
    *   The README, store listing, landing page or product description, read for the promises it makes to people. Those promises are the bar the project has already set for itself.
    *   The entry points and the CI workflow: what actually runs, and what is actually checked.
    *   Everything that stores, sends or moves what people care about: saves, uploads, sync, payments, recordings, commands to devices.
    *   Dependency manifests, lockfiles and build configuration, read as a list of costs.
    *   The issue tracker, crash reports and support messages: the bad days that already happened.

**Requirements & Constraints:**
*   **Write the bar before changing anything.** Commit it to the repository (a `QUALITY.md`, or a section of the README) and keep it short. It states:
    *   the one job, in a sentence the person using it would say;
    *   who does it, and on what: the actual devices, operating systems, browsers, networks and, for physical systems, the hardware and the conditions it runs in;
    *   the three to five journeys that must never fail;
    *   what must never be lost or corrupted;
    *   the budgets that decide "fast enough" and "small enough": load time, size, frame rate, memory, battery, latency, cost.
    Every later step checks against this, and the final verdict table is built from it. Where the project gives no evidence for an item, write down what you assumed and why.
*   **Walk every area, and say which ones do not apply.** Go through each area below. For each item, either add a row to the bar or write down in one line why it does not apply to this project. Where a specialist skill exists, use its method. Where none does, the method is the one used everywhere here: make the failure or the attack happen, then look.
    *   **Security.** Write the threat model in five lines: what is worth taking or breaking, who could reach it, and through which entry points. Then, for every entry point (a route, a form, an upload, a command-line argument, a message, a webhook, a device port):
        *   who is allowed to use it, enforced where the caller cannot bypass it, never only in the client;
        *   untrusted input handled as what it is: nothing a person typed becomes part of a query, a shell command, a template or HTML; no path built from input escapes its directory; nothing deserialised or fetched from a URL on a stranger's say-so.
        Secrets: none in the repository or its history, the client bundle, logs, error messages or diagnostics; each one scoped to the least it needs, and rotatable. Supply chain: a lockfile, a known-vulnerability scan and its result, CI actions pinned, nothing loaded at runtime from a source you do not control. Transport: TLS, security headers and a content security policy, cookies flagged, cross-origin access no wider than needed. Abuse: limits on anything that costs money, sends something to a person, or can be called in a loop. Try each attack; a defence you reasoned about is not one you tested. For code an agent wrote, `security-review-agent-code` is the method.
    *   **Privacy.** What personal data is collected, where it goes, who else receives it (analytics, error trackers, third-party scripts, model providers), how long it is kept, and how a person deletes it.
    *   **Data.** Where every piece of state lives, what writes it, and what happens when two writers meet. Backups that have been restored at least once. Migrations run against a copy of real-shaped data, forwards and back (`verify-a-migration`).
    *   **Reliability.** Every external dependency made to fail and to go slow: timeouts bounded, retries capped and safe to repeat, and a degraded mode the person can still use (`run-the-error-paths`).
    *   **Performance and capacity.** The budgets, and for anything that serves more than one person: the expected peak with a margin, measured; memory and open handles steady over a long run; the cost of one use, known.
    *   **Compatibility.** The platform matrix, plus the previous version's data and settings, other locales (longer translated text, right-to-left scripts, time zones, number, date and unit formats), and slow or metered networks.
    *   **Accessibility and craft.** The craft standard below.
    *   **Operations.** The operability items below, and for anything that runs as a service: a health check, an alert on each never-fail journey that fires before a person reports it, and logs with enough context to diagnose a failure that cannot be reproduced.
    *   **Delivery.** A build that reproduces from the lockfile, checks that gate the merge and have been seen to fail, a release that is one action, and a rollback that has actually been tried.
    *   **Maintainability.** Setup from cold (`repair-setup-script`), documentation whose commands run (`prove-the-docs`), dependencies current (`update-dependencies`), and the complexity budget below.
    *   **Legal.** Licences of the dependencies, fonts, images and data compatible with how the project is distributed, with the notices they require; any terms or privacy notice the product's use requires.
    *   **Physical safety,** when the project moves, heats, dispenses, spends or sends: every action contracted as in `act-on-the-physical-world`, the conditions it runs in (power loss, heat, interference, a person nearby), and updates that cannot leave a device unable to start.
*   **Fix in order of cost to the person.** Rank every finding and work from the top:
    1.  loses, corrupts or exposes what they trusted it with;
    2.  cannot do the core job;
    3.  broken on a platform they use;
    4.  unsafe, insecure, or inaccessible;
    5.  slower or heavier than the budget;
    6.  unfinished to use;
    7.  everything else.
    Do not polish a level 6 while a level 1 is open.
*   **Scope by the job, not by a rule about features.** If the product cannot keep what it is given, add the keeping. If one platform cannot run it at all, make it run. Refuse additions the bar does not need, and list what you refused.
*   **Run every platform in the bar, for real.** Each engine, operating system, device class or board the bar names: headless or emulated where that is faithful, real hardware where emulation would lie. Detect capabilities instead of sniffing names, and give each missing capability a fallback or a plain explanation to the person. A platform you could not run is `skipped` with the reason. Never infer it from another platform that passed.
*   **Cause the environment's failures on purpose.** For each item the bar says must never be lost, make the bad day happen and watch what the person would see: storage full or unavailable; offline in the middle of an operation; the process, tab or device killed mid-write; sent to the background; permission refused, then granted; a slow device; a wrong clock; two instances at once; an upgrade over existing data. For failure handling inside the code, use the method in `run-the-error-paths`.
*   **Hold a craft standard, and check it like any other requirement.** For every surface a person touches:
    *   every state is designed: empty, loading, partial, error, offline, disabled, success;
    *   every action shows it was received within 100 ms, even if only to say it is working;
    *   every error message says what happened and what to do next, in the person's words, not the exception's;
    *   it works at the smallest size the bar names (320 CSS px wide for the web) with no sideways scrolling, touch targets of at least 44 px, and text that still reflows at 200% zoom;
    *   it is fully usable by keyboard with a visible focus indicator, is labelled for screen readers, and meets WCAG 2.2 AA contrast;
    *   one set of spacing, type and colour values is used everywhere, in light and dark if the platform has both, and motion respects the reduced-motion setting;
    *   nothing jumps, shifts or reflows after it has appeared.
    For a product with no screen (a CLI, an API, a library, a device), the standard applies to what it does have: help text, exit codes, error bodies, logs, lights and sounds.
*   **Turn budgets into checks that fail.** Whichever budgets the bar names are asserted in CI and fail the build when exceeded. A budget measured once in a report is a snapshot, not a budget.
*   **Hold a complexity budget.** Every dependency, service, build step, abstraction layer and document must name what breaks without it. Prefer what the platform already provides. Remove what does not earn its place, and count what you removed. Do not add a container, a framework, a state library, a monorepo tool or a runbook because production projects have them. Add one when the bar cannot hold without it, and say which item it holds.
*   **Make it operable.** The running product can report its version. There is a changelog a person can read. There are diagnostics a person can copy into a bug report with no developer present, containing nothing private. An update cannot strand anyone on a broken version or lose their data in a migration. Rolling back is one action. The repository holds only source: no build output, no dependency folders, no secrets, no links into somebody's machine.
*   **Prove each fix can fail.** A test added for a fix goes red when the fix is taken out. A CI check goes red on the defect it exists for. The methods are `fix-a-bug-test-first`, `prove-the-fix` and `repair-a-green-pipeline`.
*   **Do not claim what you did not check.** Every item in the bar ends as `holds`, `broken` or `skipped`, with evidence or a reason.

**Guiding Principles:**
*   **The worst day is the specification.** An average hides the one person whose work was lost. Build for the two-year-old phone, the network that drops, the hand holding a coffee.
*   **Dependable beats impressive.** A small product that always works earns more trust than a large one that usually does. When a feature and dependability conflict, dependability wins and the feature waits.
*   **Finish, don't decorate.** Polish is not ornament. It is the absence of rough edges: the state nobody designed, the message nobody wrote, the control nobody could reach. Take away before you add.
*   **Every piece of machinery is a liability until it proves otherwise.** Well-engineered systems look simple because someone kept saying no.
*   **Say first what you could not test.** A platform you could not run is where the next bug report comes from, and the report should say so before anything else.

**Execution Flow:**
1.  **Intake.**
    *   Establish the starting state from evidence, not from the README: does it build from cold, do its tests run, does it do the job end to end, and who uses it. If setup fails, repair it first (`repair-setup-script`).
    *   Map what actually runs (`map-the-architecture` for anything non-trivial).
    *   Write the plan. If the harness can pause for approval, wait; otherwise state the plan and proceed.
2.  **Write the bar.** As above: short, specific, and in the repository.
3.  **Measure the gap.** Walk every journey on every platform in the bar. Walk every area, and attempt every attack in the threat model. Cause every failure on the never-lost list. Check every surface against the craft standard. Measure every budget. List every dependency with what it costs. Record each finding with its level from 1 to 7.
4.  **Close the gap, highest level first.** Small, reviewable commits, each with the test that proves it and the reason in its message. Re-walk the affected journeys after each one.
5.  **Lock it in.** Budgets and platform runs in CI, tests that were seen to fail, and the bar updated to what now holds.
6.  **Verdict.** Re-run everything from cold and fill in the verdict table. Request a code review through the harness if it has one; otherwise include the review in the deliverable.

**Deliverables:**
*   The bar, committed.
*   The changes, as a pull request (or the harness equivalent) whose description lists each fix with its level and the evidence that it worked.
*   **A verdict table** with one row per item in the bar: each journey on each platform, each area's items, each attempted attack, each never-lost item under each failure, each craft item, each budget. Each row is `holds`, `broken` or `skipped`, with the evidence (a command, a test name, a screenshot, a measurement) or the reason.
*   The areas and items that do not apply, each with its one-line reason, so a reader can tell a considered omission from a forgotten one.
*   What was removed, and which additions were refused, each with its reason.
*   Last line, the denominator: `31 holds, 2 broken, 5 skipped of 38 items.`
