---
description: 'To find the failure handling that has never once executed, by causing each failure on purpose and watching what the code actually does. Category: Maintenance.'
---

# Run the Error Paths

**Role:** You are a coding agent. Explore the codebase, plan, execute, and verify. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names.

**Objective:**
Find every place this project handles a failure, make that failure actually happen, and record what the code does. Fix the handlers that swallow the cause, mislead the caller, or fail in the dangerous direction. Report each one as executed, unreachable, or wrong, with the evidence.

**Context:**
Error handling is the least-executed code in most repositories and the most confidently written. It is typed once, at the moment of imagining the failure, and then never runs again, because the tests exercise the path where nothing goes wrong. The result is a body of code whose correctness nobody has any evidence about.

**An error path that has never executed is indistinguishable from one that works.** That is the whole difficulty and it is not a metaphor: both are green, both are covered by a passing suite, and both read fine. There is no signal that separates them until production supplies one. So the method here is not to read the handlers and judge them. It is to cause the failure and watch.

The failures are specific and they repeat across languages:

A handler catches everything, so it also catches the bug. `except Exception`, `catch (e)`, `rescue` with no class - the disk being full and a misspelled variable name arrive at the same line and get the same treatment, and the second one is now invisible forever.

A handler swallows and continues. The function returns as though it succeeded, the caller writes the empty result to a file, and the failure surfaces three layers away as something that makes no sense.

**A retry loop lengthens the outage it is waiting out.** Retrying a rate limit without a cap and without a change of strategy sends more of the requests that caused the limit. Retrying a non-idempotent write does the write twice.

A fallback picks the unsafe side. When a flag file cannot be read, a permissions check cannot reach its server, or a config value fails to parse, the code proceeds as though permission was granted - because the failure branch was written to keep things moving rather than to keep them safe.

An error message names the exception and not the remedy. "Connection failed" tells a user nothing they did not already know; the useful sentence says which host, which credential, and what to do next.

*   **Key Files & Folders:**
    *   Every `try`/`except`, `catch`, `rescue`, `recover`, and every `if err != nil` - especially the short ones, which is where swallowing hides.
    *   Anything that retries, backs off, times out, or has the word `fallback`, `default`, or `safe` in its name.
    *   Boundaries where other people's failures arrive: network calls, subprocess invocations, file and database access, parsing anything the project did not write.
    *   The tests, read for the opposite of the usual reason: what is NOT there is the finding.

**Requirements & Constraints:**
*   **Cause each failure for real.** Point at a host that is not listening, revoke the permission, fill the disk, corrupt the file, kill the subprocess, return the malformed payload. A handler you reasoned about is not a handler you tested, and reasoning is exactly what produced the current state.
*   **Where you cannot cause it, say so and mark it unreachable.** That is a finding about the code, not a gap in the report. Handlers that cannot be triggered are usually either dead or guarding something that cannot happen, and both are worth knowing.
*   **Every broad catch must be narrowed or justified in a comment that says what it expected.** If it genuinely must be broad - a top-level loop that has to survive anything - then it logs the exception with its traceback and does not pretend to have handled it.
*   **State the direction of failure and check it is the safe one.** Write it down for each handler: when this cannot tell, does it allow or refuse? An unreadable permission file must read as "no". An unparseable limit must read as "the limit applies". Getting this backwards is the failure that does the damage.
*   **A retry needs a cap, a reason, and idempotence.** How many attempts, why more attempts should help, and whether repeating the operation is safe. If repeating it is not safe, the retry is a bug however carefully it is written.
*   **Do not add a test that asserts the handler was called.** Assert what the caller SEES: the value returned, the exception raised, the file left on disk, the exit code. A test that mocks the failure and checks the mock was reached passes on code that does the wrong thing with it.
*   **Report the denominator.** Handlers found, executed, unreachable, wrong. A report naming four bad handlers without saying how many were examined cannot be told apart from one that stopped after four.

**Guiding Principles:**
*   **Execute, do not read.** The entire method is that a failure you have caused is worth more than a handler that reads correctly. Where a failure resists being caused, that resistance is itself the finding.
*   **Catching everything is the same as catching nothing.** A handler that cannot distinguish a network timeout from a typo has not handled either; it has only made them quiet.
*   **The exit code and the cause both get laundered.** A pipeline takes the status of its last command, and a broad catch takes the meaning out of its exception. Both turn a failure into something that looks exactly like success, and both are invisible in a passing run.
*   **Ask what happens on the second call.** Most error handling is written for one failure in isolation. The interesting behaviour is what the retry, the fallback, or the cleanup does when it runs twice, runs concurrently, or runs after a partial write.
*   **A message is for the person who will read it at three in the morning.** They have the message and nothing else. Name the thing that failed, the input that caused it, and the next action.
