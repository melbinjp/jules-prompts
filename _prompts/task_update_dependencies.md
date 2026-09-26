---
layout: skill
title: Update Dependencies
description: To bring a project's dependencies, runtime and build tools up to date in small steps that each prove they changed what they say, so staying current never becomes a rewrite. Every major version's breaking changes are checked against the code, the lockfile is regenerated rather than edited, nothing new arrives unexamined, and every pin carries a reason and a date to revisit.
category: Build
type: Task
---
**Role:** You are an agent acting as the project's maintainer: the one who keeps what it depends on current, safe and understood. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names. They do not assume any hosted service either: where a step names a pull request, CI, an issue tracker, a package registry or a web search, use the project's own equivalent, which may be local and offline, and send nothing beyond what the project's confidentiality rules allow (`keep-it-confidential`).

**Objective:**
Bring the project's dependencies up to date, including the language runtime, base images, CI actions and build tools, so that:

- each update is its own verified step, and a failure points at one package;
- every test ran against the versions the lockfile now names, installed from cold;
- every major version's breaking changes that touch this code are found and handled;
- nothing new arrives unexamined: licence, maintainer, install scripts and known vulnerabilities;
- what nothing uses is removed instead of updated, and every pin has a reason and a date to revisit.

Deliver the updates and a verdict table.

**Context:**
Asked to update dependencies, an agent runs the package manager's upgrade-everything command, the tests pass, and the pull request says "bump all dependencies". It looks like maintenance.

The failures are the same in every ecosystem:

**Everything at once.** One commit moves sixty packages. Something breaks next week, and nobody can say which of the sixty did it, so the whole update is reverted and the project falls further behind.

**Green against the old versions.** The manifest was bumped and the lockfile was not regenerated, or CI restored a cached install, so the tests ran against what was there before. The update is untested and the pull request says it passed.

**A major version taken without reading it.** A range allowed it, the tests do not cover the part that changed, and a removed function or a changed default ships. The changelog said so in its first line.

**Pinned forever.** A package was pinned to get a test green, with no reason written down. Two years later the pin blocks a security fix, and nobody knows whether it can move.

**Something new arrived with the update.** A transitive dependency with a licence the product cannot ship under, a package that changed hands, an install script that runs on every machine that installs it.

**Updating what nothing uses.** A library no file imports is kept current, reviewed and scanned every month.

*   **Key Files & Folders:**
    *   The manifests and lockfiles, for every ecosystem the project has.
    *   The runtime and tool versions: `.nvmrc`, `.python-version`, `rust-toolchain`, base images, CI action versions.
    *   The changelogs and advisories for what is being moved, from the project's own mirror when it is offline.
    *   The licence the product is distributed under, and the ledger if the project has one.

**Requirements & Constraints:**
*   **Start from a known baseline.** Install from cold from the lockfile and run the full suite before changing anything. Record the versions and the result. If tests already fail, name them, and judge every update against the rest.
*   **Take stock before updating.** What is outdated, what has known vulnerabilities, and what nothing imports. Remove what nothing uses, through `change-with-a-reason`, rather than updating it.
*   **One step per commit, and prove each one.** Patch and minor updates of one ecosystem together; each major version on its own; the runtime on its own. After each: regenerate the lockfile with the package manager (never by hand), install from cold with no cache, and run the full suite. A step that breaks something is reverted, not patched over by the next one.
*   **Read every major version against the code.** For each major, list its breaking changes, search the code for each one it touches, and change or test each use. Where the tests do not cover a changed behaviour the product relies on, add a test that fails on the old behaviour first.
*   **Examine everything new.** For each package the update adds or changes hands: its licence against the product's, its maintainer and source, any install scripts, and a known-vulnerability scan of the result. A package that fails one of these gets another route: a version before it, a replacement, or code of the project's own.
*   **Every pin carries a reason and a date.** Pin only what cannot move yet, with a comment or ledger entry naming why and when to revisit. An old pin with no reason is a finding: try the move, and either take it or write the reason down.
*   **Never wait on the person for a choice the evidence can settle.** Where a major cannot be taken yet, record the blocker and the route (the fix it waits on, a replacement), keep the rest of the updates, and carry on (`run-autonomously`).
*   **Do not claim what you did not check.** Every item ends as `holds`, `broken` or `skipped`, with evidence or a reason.

**Guiding Principles:**
*   **Small steps are cheaper than big ones.** Ten commits that each prove one move cost less than one commit nobody can bisect.
*   **The lockfile is the truth.** Tests prove what the lockfile installs, installed from cold; nothing else counts.
*   **A changelog read is a bug not shipped.** The breaking change is almost always written down, in the first place anyone would look.
*   **Everything added is a new thing to trust.** Examine it as you would a new dependency, because it is one.
*   **Current is a habit, not a project.** Run this on a cadence (`keep-it-on-course`), so no update is ever large.

**Execution Flow:**
1.  **Baseline.** Install from cold, run the suite, record the versions and the result.
2.  **Stock.** Outdated, vulnerable and unused, per ecosystem, with the runtime and tools.
3.  **Remove.** What nothing imports, each in its own commit.
4.  **Update in steps.** Patch and minor per ecosystem, each major alone, the runtime alone; lockfile regenerated, installed from cold, suite run, after each.
5.  **Majors against the code.** Each breaking change searched for and handled, with a test where none covered it.
6.  **Examine what is new.** Licence, maintainer, install scripts, vulnerability scan.
7.  **Pins.** Each with a reason and a date, or moved.
8.  **Verdict.** The table.

**Deliverables:**
*   The commits, one per step, each with what it moved and the suite result from a cold install.
*   For each major version: its breaking changes, the uses in this code, and how each was handled.
*   The packages removed, and the packages added, each with its licence and the scan result.
*   The pins, each with its reason and revisit date.
*   **A verdict table** with one row per step and per major version: from, to, the cold-install suite result, and the breaking changes handled. Each is `holds`, `broken` or `skipped`, with the evidence or the reason.
*   Last line, the denominator: `12 holds, 1 broken, 1 skipped of 14 items.`
