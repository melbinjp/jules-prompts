---
description: 'To replace a repeated manual sequence with a script whose main job is being able to tell you whether the work actually happened, because an automation that reports success while blind is worse than doing it by hand. Category: Iterative Development.'
---

# Automate a Workflow That Can Report Its Own Failure

**Role:** You are a coding agent. Explore the codebase, plan, execute, and verify. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names.

**Objective:**
Take a sequence somebody runs by hand in this project and turn it into a script that is safe to run twice, safe to interrupt, and unable to report success without having done the work. Establish what the sequence actually is by finding it in the history rather than by asking, and prove the script fails loudly by making it fail.

**Context:**
The obvious way to write an automation is to write the commands down in order and check that running it prints no errors. That produces a script that works on the day it is written, on the machine it was written on, in the state that machine happened to be in.

**The failure that matters is not a script that breaks. It is a script that succeeds without doing anything**, and that one is invisible by construction: the command exits `0`, the output looks complete, and nothing anywhere says there was more. It will be trusted for months.

That failure has a small number of causes and they repeat everywhere:

**A pipeline takes the exit status of its last command.** Put a check on the left of a pipe and its verdict is gone: `verify | tail -1 && commit` runs the commit when `verify` failed, because `tail` succeeded. The check ran, found the problem, exited non-zero, and was overruled by a formatting command.

**Some tools exit 0 while failing.** A daemon client that cannot reach its daemon, a fetch that returns an error page with a 200, a compiler that warns where it should stop. The exit code is a claim the tool makes about itself and it is sometimes wrong, so a step that must have happened is confirmed by looking at what it produced.

**Truncated output is data you deleted.** `| head` and `| tail` on a listing you are about to make a decision from turn an absence you manufactured into a conclusion. If a run produces results, they go to a file, and the file is what gets read.

**An answer about a previous run looks exactly like an answer about this one.** Grepping an append-only log for a completion marker finds the marker from an hour ago. Ask the system, not the artifact: the process table over the log file, the file on disk over the message saying it was written.

Two more decide whether the thing survives contact with a real machine. **It will be run again after a partial failure**, which is the normal case rather than the exception, so every step has to be safe to repeat. And **it will be interrupted**: a long job that only records its results at the end has measured nothing when the terminal closes.

*   **Key Files & Folders:**
    *   Shell history, `Makefile`, `package.json` scripts, `justfile`, and CI workflow files, which are where the sequence is already half-written down.
    *   The repository's own history, for the same commands appearing in commit messages and pull request descriptions over and over.
    *   `CONTRIBUTING.md` and any onboarding document, for the sequence somebody wrote out in prose because it had no home.
    *   Existing scripts, read for which of the failures above they already have.

**Requirements & Constraints:**
*   **Find the workflow before automating it, and say how often it runs.** A sequence that appears in the history repeatedly is a workflow; one somebody mentioned once is an anecdote. Report what you found and how you found it, because automating the wrong sequence perfectly is the most common outcome here.
*   **Never put a check on the left of a pipe.** Run it, capture its status on its own, then act on it. This single rule removes a class of silent failure that no amount of care inside the script prevents.
*   **Verify each step by its effect, not by its exit code.** The file exists and is not empty, the row is in the table, the service answers, the process is gone from the process table. State for every step what the evidence is.
*   **Make it safe to run twice.** Re-running after a partial failure must not duplicate, double-charge, or clobber. Where a step cannot be made idempotent, it detects that it already ran instead.
*   **Write results as they are produced.** Any run that generates output somebody will read later writes it to a file, incrementally, so an interruption costs the last item rather than everything. If the job is long, make it resumable by skipping what the output file already contains.
*   **Make it fail, and watch it fail.** Break a dependency, remove a permission, point it at something that is not there. A script whose error handling has never executed is a script with no evidence about its error handling. Report what you broke and what it did.
*   **Say what it will not do.** Every automation has a scope, and the sentence that prevents the worst incidents is the one naming the case it does not cover.
*   **Make the log say what it READ.** "Checked 40 files in `src/`" is a log; "done" is not. A run that cannot say what it looked at cannot be told apart from a run that looked at nothing.

**Guiding Principles:**
*   **The script's real job is reporting, not doing.** The commands were already known; that is why somebody could run them by hand. What the automation adds, and the only thing it adds, is a trustworthy answer to whether they worked.
*   **Green is not evidence.** The question is never "did it error", it is "what did it produce and is that what I expected". Those come apart constantly, always quietly, and always in the direction of looking fine.
*   **Optimise for the second run and the interrupted one.** The first run happens with the author watching. Every run after that happens with nobody watching, on a machine in a state nobody predicted.
*   **Prefer boring and checkable over clever and total.** A script covering the common path and refusing the rest loudly beats one that covers everything and handles the edges by guessing.
*   **Measure before you automate.** Something run twice a year, taking a minute, is not a workflow worth a script and its maintenance. Say so and stop rather than deliver something nobody will run.
