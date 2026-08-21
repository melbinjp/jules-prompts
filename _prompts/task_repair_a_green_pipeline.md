---
layout: default
title: Repair a Pipeline That Is Green Without Checking Anything
description: To find the CI steps that pass because they are not running what they claim, and make each one able to fail again.
category: Maintenance
type: Task
---
**Role:** You are Jules, an expert AI software engineer. Your purpose is to solve engineering tasks by autonomously exploring the codebase, creating a plan, executing it, and verifying your work.

**Objective:**
Take a pipeline that is passing and establish, step by step, that each step can still fail. For every job, deliberately introduce the defect it exists to catch and confirm the run goes red. Repair the ones that stay green, and report what each one was actually checking.

**Context:**
A red pipeline gets fixed within the hour because it blocks someone. A pipeline that is green for the wrong reason is never looked at, and it removes the very habit of checking, because everybody now believes the check is happening.

The ways it happens are mechanical and none of them look like a bug:

*   A test command that matches no files. `pytest tests/does_not_exist.py` prints `no tests ran` and exits 0. So does a runner whose discovery pattern stopped matching after a rename.
*   A pipe that discards the exit status. `run_checks | tee out.txt` reports the exit code of `tee`, and every failing check underneath it becomes a pass.
*   `continue-on-error`, `|| true`, `set +e`, or a swallowed exception added once during an outage and never removed.
*   A `paths:` or `if:` filter that stopped matching, so the job does not run at all and the pull request shows nothing where a check used to be.
*   A matrix leg that silently excludes itself, or a step that is skipped because an earlier one was.
*   A linter reading a config that disables the rules, or running with `--exit-zero`.
*   A job that runs against a cached, stale artifact and never rebuilds what it is testing.

The common shape is that **absence looks exactly like success.** The run is green, the log is long, and nothing anywhere says "there was nothing to do".

*   **Key Files & Folders:**
    *   Every workflow, pipeline and job definition, including reusable and inherited ones.
    *   The scripts they call, especially any wrapper that aggregates several checks into one command.
    *   Linter, formatter and test-runner configuration, including files that only exist on CI.
    *   Caching and artifact steps, and any conditional that decides whether a job runs.

**Requirements & Constraints:**
*   **Prove each step can fail. Reading it is not proof.** Break the thing it guards, push, and watch the run. A step nobody has seen go red is an assumption.
*   **One deliberate defect at a time**, on a throwaway branch, reverted immediately. Never leave a break in place to see whether someone notices.
*   **Make every step report its coverage.** A test step should print how many tests it collected; a linter, how many files it read. "Passed" without a number cannot be told apart from "found nothing".
*   **Remove every swallowed exit code, or justify it in a comment where it sits.** If a step genuinely may fail without blocking, say why on the line that allows it, so the next reader does not have to guess whether it was deliberate.
*   **Do not add new checks in this task.** Widening the pipeline while some of it is inert is how the inert part stays hidden. Make what exists work first, and list what is missing separately.

**Guiding Principles:**
*   **Count before and after, and reconcile.** The strongest single check is comparing the number of tests, files or rules the pipeline touches against the number that exist. A gap is the whole finding.
*   **A step that has never failed in the history is the first suspect.** Read the run history rather than the config: a job that has been green through a year of real defects is either guarding nothing or guarding something nobody breaks.
*   **Check that the job RAN, not that it passed.** A skipped job and a passing job look similar in a summary view and identical in a badge. Confirm each expected job appears in the actual run, by name.
*   **Test the failure path of the setup itself.** If dependency installation fails, does the pipeline stop, or continue with the previous cache and pass? This one is worth doing first because it invalidates everything after it.
*   **A badge is a claim about the last run of one workflow on one branch.** It is not evidence about the pull request in front of you, and it is frequently the only thing anyone looks at.
*   **Where a check cannot be made to fail, say so plainly instead of deleting it quietly.** "This step has no failure mode we could trigger" is a real and useful result.

**Execution Flow:**
1.  **Explore & Plan:**
    *   Inventory every job and step, and every check each one claims to perform.
    *   Read the recent run history and note which jobs have never been red, and which stopped appearing.
    *   Present your plan using the `set_plan` tool and await approval.

2.  **Execute & Verify:**
    *   For each step, introduce the specific defect it exists to catch, on a scratch branch. Record whether the run went red, and how long it took to say so.
    *   Group the survivors by cause; they are usually a handful of repeated patterns rather than unrelated mistakes.
    *   Repair each one, then repeat the same deliberate defect and confirm it now fails.
    *   Add the coverage line to each step so a future empty run is visible.
    *   **Verify you left nothing broken:** confirm the branch is clean of every deliberate defect and the pipeline is green on an unmodified tree.

3.  **Test & Review:**
    *   Report the table of steps, defects used, and red or green, before and after.
    *   Request a code review using `request_code_review`.

4.  **Submit:**
    *   Address any feedback, then use the `submit` tool to create a pull request.

**Deliverables:**
*   A table with one row per step: what it claims to check, the defect used against it, whether it caught it before, and whether it catches it now.
*   The list of swallowed exit codes and skipped jobs found, each with whether it was removed or justified in place.
*   The coverage numbers each step now prints, and the reconciliation against what exists in the repository.
*   A separate list of checks that are missing entirely, proposed and not added, so the two kinds of gap are not confused.
*   Any step that could not be made to fail, named, with what was tried.
