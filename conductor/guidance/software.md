# Software: building, checking and delivering code

Load when the output or the work includes software. Most sections are about the ways agents
specifically fail: work that reads as finished and is not, tests that cannot fail, pipelines that
are green while checking nothing, setup that reports success while broken. For every procedure
here, evidence means the command, its exit code and its summary line, verbatim, and the review is
by someone other than the author (`quality.md §Reviewing work`).

## Delivery: review, CI, deploy, rollback

- **Every change is proposed for review** (a pull request, or the project's equivalent) that
  references its work item and states what was verified and how: the test seen to fail without
  it, the measurement before and after. A reproduction is proposed as a reproduction, not a fix.
- **A reproducible build:** installed from the lockfile, from clean.
- **The checks that gate the merge have each been seen to fail** (§Pipelines that can fail), and
  they actually run on the change in question (not skipped by a path filter, not advisory).
- **A release is one action and can be staged:** a small share of people or devices first, the
  critical journeys watched, a pause that triggers itself at a failure threshold set in advance.
- **Rollback is one action, and it has been tried.**
- **Reaching people is its own step** (`product.md §Releasing to people`).

## Setup that runs from cold

A clean environment must install, build and run the tests using only the setup, with no step a
person supplies from memory. Many harnesses snapshot a successful setup and reuse it, so a defect
here is paid for by every future task.

1. **Find out what actually breaks from cold before repairing anything.** Determine the language,
   package manager, test runner and build tool from the manifests present. Read the CI workflow:
   if it passes, it contains a sequence proven to work on a clean machine; start from it, not the
   README. List every external dependency the tests touch. Run the existing setup and record where
   it fails, with the command and its output.
2. **Rules for the setup:**
   - no long-running processes: no dev server, file watcher or foreground daemon; a service the
     tests need is started detached, polled until it accepts connections, and fails loudly with
     its log if it never does (a fixed sleep is not a readiness check);
   - exit codes are true: no `|| true`, no swallowed installer status, `set -euo pipefail` or the
     equivalent; a setup that cannot fail is the same defect as a test that cannot fail;
   - unattended: pass the tool's non-interactive flag rather than piping `yes`;
   - no secrets, and no assumed credentials: detect a missing token and say so in one line;
   - lightweight: install what the tests need; install from the lockfile;
   - install and verify are separate phases, so a failure says which it was.
3. **Repair, run, repeat until the test runner reports results.** "Runs to completion" means the
   runner reported; it does not require every test to pass, and tests are not edited here.
4. **Prove the two silent failures:** make a required install fail and confirm the setup exits
   non-zero; confirm nothing in it blocks.
5. **Report** the baseline failure verbatim, each change with its reason, the final runner summary
   line, and what still cannot run here and why. Write the install and test commands and required
   environment variables where every agent reads them (`autonomy.md §Standing rules for the
   project`).

## Tests that do not need services

A suite that assumes a database, a broker, a seeded staging server or a live API fails with a
connection error partway through, and the agent then reports the failures as "unrelated to our
changes". The change looks reviewed and was never tested.

1. **Run the suite with nothing else running,** and record the exact failure, the count, and
   whether it failed at collection or in tests. Import-time connections fire before any test.
2. **Inventory every external dependency:** what it is, which tests touch it, whether a seam exists.
3. **Substitute one dependency at a time,** running the suite after each:
   - fake at the boundary the project already has (a repository class, a client wrapper, an
     interface); patch the library only when there is no seam, and report that as a design finding;
   - an in-memory substitute can lie (SQLite accepts what Postgres rejects): where behaviour
     genuinely differs, keep the test as an integration test with a marker;
   - for third-party APIs, record a real response rather than hand-writing a stub;
   - freeze the clock, seed randomness, block outbound sockets, and let a test that reaches for the
     network fail with a message saying so.
4. **Rules:** never change what a test asserts (a test that can only pass by weakening its assertion
   is left failing and reported); no test is skipped silently, every exclusion has a named marker
   and the service it needs; the default command is the isolated run; the full suite against real
   services stays runnable, with its command documented.
5. **Prove it:** block outbound network or point service URLs at a dead port, and the default suite
   still passes; compare the collected-test count before and after, and reconcile every test that
   stopped running against the marked list exactly.

## Tests that can fail

A test written while looking at the implementation asserts what the code does, so it can never
catch the code doing the wrong thing. Coverage rises, the suite is fast, the change reads as
careful, and the number of real regressions caught is zero.

- **The tells:** a test that mocks the unit under test; an assertion on shape only (`is not None`,
  `toBeDefined`, `status == 200`, `len > 0`) with no value assertion beside it; an expected value
  reconstructed from the implementation's own arithmetic, or captured by running the code; "no
  exception raised" as the only check; fixtures or snapshots captured from the code under test.
- **Prove each test can fail; do not read it and decide.** Mutate the code, not the test: invert a
  condition, return a constant, drop a field, skip a call. For a test that came with a fix, put the
  original defect back as precisely as you can (the inverted condition, the removed guard, the old
  off-by-one), never delete the function. Run that test alone and read its failure: red must be on
  its assertion about the behaviour, not an import, fixture or collection error. One break at a
  time; restore each immediately; at the end the suite is green and the tree is clean of mutations.
- **A test that cannot fail is fixed (rewritten against the requirement, and re-run under the same
  mutation) or deleted; never left.** Coverage going down when a useless test is removed is the
  right direction; report it with its sign.
- **A test that fails once made meaningful is a real defect:** report it and leave it failing.
- **Check what the suite collects,** not what passed: compare the collected count against the test
  functions you can count. Read every skip, mark and condition added, with its reason and whether it
  is still true.
- **A claimed fix with no test is a finding.**

## Pipelines that can fail

A red pipeline is fixed within the hour. One that is green for the wrong reason is never looked at,
and it removes the habit of checking, because everyone believes the check is happening. Absence
looks exactly like success.

- **The mechanical causes, to check one by one:** a test command that matches no files ("no tests
  ran", exit 0); a pipe that reports the last command's status (`checks | tee out.txt`);
  `continue-on-error`, `|| true`, `set +e` or a swallowed exception; a path or `if:` filter that
  stopped matching, so the job never runs; a matrix leg that excludes itself, or a step skipped
  because an earlier one was; a linter with its rules disabled or `--exit-zero`; a job testing a
  stale cached artifact.
- **Method:**
  1. inventory every job and step, and what each claims to check; read the run history for jobs
     that have never been red, or stopped appearing (the first suspects);
  2. test the setup's own failure path first: if an install fails, does the pipeline stop or reuse
     a cache and pass?
  3. for each step, introduce the defect it exists to catch, one at a time on a throwaway branch
     reverted at once, and record whether the run went red and how long it took;
  4. group the survivors by cause, repair each, and repeat the same defect to see it fail now;
  5. make every step print its coverage (tests collected, files read) and reconcile against what
     exists;
  6. confirm each expected job ran, by name, on the change itself; a badge is a claim about one
     branch's last run;
  7. leave the branch clean of every deliberate defect and green on an unmodified tree.
- **Remove every swallowed exit code, or justify it in a comment on the line that allows it.**
- **Do not add new checks while existing ones are inert;** list the missing ones separately.
- **A check that cannot be made to fail is reported plainly,** with what was tried, not deleted.

## Automations that report their own failure

The failure that matters is not a script that breaks; it is a script that succeeds without doing
anything. It exits 0, the output looks complete, and it is trusted for months. The automation's
real job is a trustworthy answer to whether the work happened.

1. **Find the workflow before automating it:** the commands people actually run, from shell
   history, the Makefile and package scripts, CI files, commit and review history, and onboarding
   docs; how often it runs and what a mistake costs, with sources. Something run twice a year that
   takes a minute may deserve a checklist, or a script for the one step that goes wrong, instead.
2. **Rules:**
   - never put a check on the left of a pipe; run it, capture its status, then act on it;
   - verify each step by its effect (the file exists and is not empty, the row is in the table,
     the service answers, the process is gone), not by its exit code; some tools exit 0 while
     failing;
   - do not truncate output you will decide from (`| head`, `| tail`); write it to a file and read
     the file;
   - ask the system, not an old artifact (the process table over an append-only log);
   - safe to run twice after a partial failure: no duplicates, no double charges, no clobbering;
     a step that cannot be idempotent detects that it already ran;
   - write results as they are produced, so an interruption costs the last item; resumable by
     skipping what the output already holds;
   - the log says what it read ("checked 40 files in src/"), never only "done";
   - say what it will not do, one sentence per case; boring and checkable over clever and total.
3. **Make it fail, and watch:** remove a dependency, a permission, an input, and interrupt it
   halfway; each failure must reach the exit code and the log. Report what you broke and what it did.

## Architecture from what runs

The folder structure is a claim about the architecture, and the claim most likely to be stale. A
diagram assembled from names is fluent, confident, and describes the system somebody intended.

- **Find the entry points; do not guess them:** console scripts, `main` functions, server bindings,
  container commands, scheduled jobs, the commands CI runs. Run one and note what it touched.
- **Build the import graph from resolved imports.** A layer boundary is one only when you have shown
  nothing crosses it.
- **The real boundaries are the ones that fail separately:** a process, a network hop, a database,
  a third-party API. Two packages in one process that import each other freely are one component.
- **Use co-change:** files that change in the same commits are one unit of work, whatever folder
  they live in; report where this disagrees with the layout.
- **Follow the data:** where state lives, who writes it, who reads it. Two components that never call
  each other but write the same table are coupled.
- **Count things:** imports in and out per module, commits per path, places that construct the
  central object.
- **Say how you know, per claim** ("resolved the import", "ran it", "in 14 of 20 commits"), and name
  what could not be established statically (dynamic dispatch, reflection, plugins, configuration
  wiring). Do not draw a diagram the code does not support.
- **A good map predicts:** check it against two recent changes; it should say where they landed and
  what they touched.

## Scoping a vague issue

Given "the login is broken", an agent guesses what broken means and builds on the guess; the work
looks complete and fixes something nobody reported. Scope before fixing, and produce no fix here.

1. **List precisely what the issue does not say,** and the distinct readings its wording allows.
2. **Separate three statements:** what the reporter said, what the software actually does, and what
   it should do. Expected behaviour needs a source (documentation, a test, a type, a specification);
   if none exists, record it as undefined.
3. **Ask the codebase before the reporter:** the tests, types and history resolve most ambiguity.
4. **Confirm a clean baseline, then reproduce,** recording every attempt, including failures. An
   unreproduced report is stated as unreproduced, with exactly what was tried.
5. **Reduce to the smallest reproduction;** the steps you could delete show where the fault is not.
6. **Write a failing test that captures the difference,** confirm it fails for the reported reason
   (change the suspected cause and see the outcome follow it), and that the rest of the suite behaves
   as at baseline.
7. **Record other defects found on the way separately;** do not widen the scope.

## Fixing a bug, failing test first

A fix written before its test is indistinguishable from a coincidence; a test written after is
written against the new code and passes on the old too. The quieter failure is a test that fails
for the wrong reason (an import error, a missing fixture) and is spent as evidence it never earned.

1. **Know which tests are already red,** and name them; run your test alone so its red cannot be
   confused with theirs.
2. **Reproduce by hand from the report's exact input.** Paraphrasing it into a tidier case fixes a
   bug nobody had.
3. **Write the failing test; read the failure line;** it must name the reported behaviour. Record it
   verbatim. Narrow until the test names one behaviour.
4. **Commit the test alone,** before any production change (revert exploratory changes first).
5. **Change the smallest thing that turns it green,** and stop. Split out formatting, refactors and
   version bumps. Never move the assertion to fit the code; if the test was wrong, start again.
6. **Run the full suite;** nothing else moved from green to red.
7. **The revert check:** remove the fix with the test in place; the test must go red again.
8. **Watch for fixes that pass by making the test unreachable** (guarding earlier, returning sooner,
   defaulting a value): confirm the changed path is the one the test executes.
9. **Say where the cause really was** if not where the report pointed, and **look for siblings:** the
   same pattern elsewhere, reported whether fixed or not. A bug that cannot be reproduced is a
   finding: what was tried, on what version, with what data.

## Complete changes, nothing detached

A change that stops halfway is worse than none: it adds a second way of doing the same thing.

- **Every layer in the same change:** the interface and every state it shows, the logic, the data
  and its migration, the configuration, the tests, the documentation, and operations (monitoring,
  backups, runbooks).
- **Everything added is reached** from an entry point a person or device uses.
- **Everything replaced is removed:** the old code path, its tests, flags, configuration,
  dependencies and documentation. Search the whole repository for references to anything renamed
  or removed.
- **Before finishing, check:** every new module is reached; every new configuration key is read;
  every new dependency is imported; no two paths compute the same fact; every feature flag has an
  owner and a removal date; the project's own dead-code and unused-dependency tools report nothing
  new.

## Reviewing an agent's change

Agent-written changes fail differently from human ones: correct style, sensible names, a confident
description, and tests that pass because they assert what the code does. The danger is not that
the code is bad; it is that it reads as finished.

1. **List the linked issue's requirements** as discrete, checkable items; note which files the diff
   touches and which it does not.
2. **Baseline:** run the suite on the base commit, so you know what was already failing; then on
   the change, and account for every difference.
3. **For each test the change adds, break the code under it and confirm the test fails;** restore.
4. **Walk the requirements:** each met, partly met or not addressed, with file and line. Agents
   satisfy the part of a request they understood; the dropped requirement will not announce itself.
5. **Compare each assertion against the issue, not the diff.**
6. **List every weakened or deleted assertion, skip, widened tolerance and suppressed error** (new
   `try`/`except` around the changed path, a swallowed exit, `continue-on-error`, a log where a raise
   used to be), each with the reason given, or a note that none was.
7. **Confirm the check that should catch this runs on this change,** and is not skipped or advisory.
8. **Exercise the change by hand** if it has an interface: run the command, call the endpoint, load
   the page.
9. **Fix nothing unless trivial, and say so;** record unrelated problems separately. State what you
   could not verify.

## Security of agent-written code

An agent asked to make a failure stop finds the shortest route, which is often to remove the thing
objecting. The defect is a check that no longer checks, and the diff looks like work.

- **What to look for:**
  - **a check that cannot fail:** a scanner under `continue-on-error`, an exit discarded with
    `|| true`, an audit only uploaded as an artifact; make each new check find something and
    confirm it turns the build red;
  - **verification switched off:** `verify=False`, `rejectUnauthorized: false`,
    `--no-check-certificate`, `NODE_TLS_REJECT_UNAUTHORIZED=0`, a pinned certificate removed;
  - **credentials in anything the change created:** examples, fixtures and documentation get
    plausible invented values; treat every key-shaped string as real until shown otherwise, and
    check the history as well as the tree;
  - **where each new dependency came from:** check the name character by character against the
    import it satisfies (typosquats), its maintainer and registry, and that the lockfile changed
    consistently with the manifest;
  - **permissions that widened:** `write-all` workflows, broader token scopes, mode 777, opened
    buckets or security groups; compare with what the change needs;
  - **a swallowed exception around an authorisation path** is an authorisation bypass: ask what
    happens to the request when it fires;
  - **injection wherever a string was built:** a query, a shell command, a path or an HTML fragment
    assembled by concatenation or formatting.
- **Report, do not repair** (unless one line, said plainly): each finding with file, line, what an
  attacker gains, and the smallest fix, ordered by that gain. Run the project's scanners and quote
  their output. State what you did not examine.

## Standards to apply

Name the standard when making a conformity claim, with its edition; follow these instructions
either way, since a citation is not an instruction.

- **Security (OWASP ASVS; choose level 1, 2 or 3 by what is at stake).** Write the threat model in
  five lines: what is worth taking or breaking, who could reach it, through which entry points. For
  every entry point (a route, a form, an upload, an argument, a message, a webhook, a device port):
  - who may use it, enforced where the caller cannot bypass it, never only in the client;
  - untrusted input handled as untrusted: nothing typed becomes part of a query, a shell command, a
    template or HTML; no path built from input escapes its directory; nothing deserialised or fetched
    on a stranger's say-so;
  - secrets: none in the repository or its history, the client bundle, logs, errors or diagnostics;
    each scoped to the least it needs, and rotatable;
  - transport: TLS, security headers, a content security policy, cookies flagged, cross-origin access
    no wider than needed;
  - abuse: limits on anything that costs money, sends something to a person, or can be called in a
    loop;
  - try each attack; a defence you reasoned about is not one you tested.
- **Supply chain (SLSA; OpenSSF practices):** a lockfile with hashes; a known-vulnerability scan and
  its result; CI actions pinned to a commit; nothing loaded at runtime from a source you do not
  control; a software bill of materials when the result is distributed; builds that reproduce.
- **Accessibility (WCAG 2.2 AA):** `design.md §Accessible and inclusive`.
- **Product quality (ISO/IEC 25010):** its characteristics (functional suitability, performance
  efficiency, compatibility, interaction capability, reliability, security, maintainability,
  flexibility, safety) are walked as areas in `quality.md §Walk every area`.

## Error paths

Error handling is the least-executed code and the most confidently written. A handler that has
never run is indistinguishable from one that works, until production supplies the difference.

1. **Find every handler,** with file and line and the count: every `try`/`except`, `catch`, `rescue`,
   `recover`, `if err != nil`; everything that retries, backs off, times out, or is called fallback,
   default or safe; every boundary where others' failures arrive (network, subprocess, files,
   databases, parsing). What the tests do not cover is the finding.
2. **Cause each failure for real:** a host not listening, a revoked permission, a full disk, a
   corrupt file, a killed subprocess, a malformed payload. Record what the caller sees. One you
   cannot cause is marked unreachable, which is itself a finding.
3. **Judge each one:**
   - a handler that catches everything also catches the bug: narrow it, or justify it in a comment;
     a top-level loop that must survive logs the traceback and does not pretend to have handled it;
   - swallow-and-continue returns as if it succeeded, and the failure surfaces three layers away;
   - the direction of failure is written down and safe: an unreadable permission reads as no; an
     unparseable limit means the limit applies;
   - a retry has a cap, a reason more attempts should help, and idempotence; retrying a
     non-idempotent write is a bug however carefully written; ask what happens on the second call,
     concurrently, after a partial write;
   - the message names the thing that failed, the input that caused it, and the next action.
4. **Fix the wrong ones,** each with a test that asserts what the caller sees (the value, the
   exception, the file left, the exit code), seen to fail before the fix; never a test that the
   handler was called.
5. **Report the denominator:** found, executed, unreachable, wrong.

## Data migrations

A migration run once on a dev database and exiting 0 is the usual whole test, and every property
that causes an outage is invisible under exactly those conditions.

1. **Identify** the pending migrations, the production engine and exact version, and `count(*)` for
   every table they touch (from production or the closest thing). If a count cannot be obtained, say
   so; the timings do not cover that table.
2. **Build a copy on the same engine and version,** seeded to realistic row counts (filler values are
   fine). Never touch production.
3. **Dump the schema; run forward, timing each statement and recording the lock it takes and for
   how long.** Nine minutes holding nothing is safe; nine seconds with an exclusive lock on the
   busiest table is an outage. Look up the engine- and version-specific behaviour of each statement
   (adding a non-null column, changing a type, validating a constraint, building an index without
   the concurrent option).
4. **Run the rollback; do not read it.** Dump again and diff; the dumps must be identical. Then run
   forward again.
5. **For each new unique or non-null constraint, count the rows that would violate it.**
6. **Interrupt any long backfill partway,** check it is batched and committing, and record what state
   it leaves.
7. **Prove the safe deploy order:** the previous release's code against the new schema, and the
   current code against the old. If both break, split the migration.
8. **A migration already applied anywhere is never edited;** check the history table.
9. **Destroy the copy;** report timings with the row counts they rest on, and what could not be
   measured. If you change the migration, measure again.

## Dependencies

1. **Baseline:** install from cold from the lockfile, run the full suite, record versions and result;
   name tests that already fail.
2. **Stock:** outdated, vulnerable and unused, per ecosystem, including the runtime, base images, CI
   actions and build tools. Remove what nothing imports, as its own change, rather than updating it.
3. **One step per change:** patch and minor updates of one ecosystem together; each major version on
   its own; the runtime on its own. After each: regenerate the lockfile with the package manager
   (never by hand), install from cold with no cache, run the full suite. A step that breaks something
   is reverted, not patched over by the next.
4. **Read every major against the code:** list its breaking changes, search the code for each, and
   change or test each use; where the tests do not cover a changed behaviour, add a test that fails on
   the old behaviour first.
5. **Examine everything new or that changed hands:** its licence against the product's, maintainer
   and source, install scripts, and a vulnerability scan. One that fails gets another route: an
   earlier version, a replacement, or the project's own code.
6. **Every pin has a reason and a revisit date;** an old pin with no reason is tried or explained.
7. **A major that cannot be taken yet** is recorded with its blocker and its route, and the rest
   proceeds.
8. **Do this on a cadence** for anything that keeps running (`operations.md §Upkeep`).

## Documentation that matches the code

Documentation rots invisibly: there is no red tick for a stale sentence. The quickstart is the most
important instructions and the least re-run. And documentation written from names and comments
restates the intended behaviour, now in a second place and sounding authoritative.

1. **Build the claim list:** every checkable statement in the README, guides, docstrings, examples and
   configuration reference, each with its file and line; group by how it will be checked (run this
   command, read this line of code, follow this link).
2. **Run the installation and quickstart from cold,** literally, typing nothing not written down;
   record every deviation you had to make.
3. **Verdict and evidence per claim:** verified (ran it, or the line that proves it), false (ran it and
   it did something else), unverifiable (cannot be checked as written, a finding about the sentence).
4. **Suspect first:** every number and name (versions, ports, paths, flags, defaults, timings,
   platforms); intent verbs ("should", "will", "automatically", "simply"); every link and anchor;
   every code block, run in order from the state the document says the reader is in.
5. **Fix the false claims against what the code does.** Where the code looks wrong rather than the
   document, leave the document and report the defect. Do not polish prose you have not checked, and
   do not drop a claim because it is hard to verify. Example output is produced by running the code.
6. **Re-run the suite and the quickstart from cold.** Report examined, verified, false, unverifiable.

## Translations

A translation is a fork of the documentation with no way to tell it has drifted; a stale one answers
readers fluently with last year's instructions. The deliverable is the text plus the machinery.

1. **Decide the scope:** which pages, which languages, and which are left in the source language on
   purpose, each with its reason. Find out whether the docs build overlays translations on the source
   (an untranslated page then serves the original) or copies (it then goes missing).
2. **Record the source revision in every translated file,** so staleness is one version-control query.
3. **Ship a staleness check with the translations:** for each file, compare the recorded revision
   with the current source, and report which are behind and by how many changes; run it in CI and see
   it fail by changing a source page.
4. **Never translate what a reader types or a machine reads:** commands, flags, code, paths, package
   names, environment variables, configuration keys, identifiers, and error strings people search for.
5. **Keep the structure exactly:** the same headings, anchors and file names in the language's
   directory; never half-translate a page (a page that switches language two-thirds down reads as
   finished and is not).
6. **Check every link from where the translated file sits,** against the built output; build the docs
   and look at the switcher, navigation, search and a rendered page.
7. **Make it reviewable by someone who does not read the language:** what was mechanical, what is
   prose, what a native reader must check, and anything ambiguous in the source.
