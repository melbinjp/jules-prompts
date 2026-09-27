# Fixture run: vague-issue, old approach

| | |
|---|---|
| Approach | Old: the library at `f5fc9c0e721f4323f4ee79554220bb76128f796d`, exported read-only without `fixtures/` |
| Protocol | `docs/trials/protocol.md` at `51d534d` |
| Agent | A fresh `general-purpose` subagent, model `claude-opus-5-5`, standard file, search and shell tools |
| Workspace | `fixtures/vague-issue/` prepared by `docs/trials/tools/prep.py` (expected report, `defects.json`, `__pycache__` and the explanation file removed) |
| Opening message | `docs/trials/tools/prompt.py vague-issue old <OLD>` |
| Budget used | 11 tool calls, 93,467 tokens, 232 s |
| Files the agent changed | `test_login.py` added |
| Written outside the workspace | none apart from system logs. Run 1's leftover file: `4c13315a7464…` before, `4c13315a7464…` after |
| String score | Below, from `scripts/score_fixture.py fixtures/vague-issue <report>` |
| Output check | Not yet run. It decides; the string score is kept for comparison. |

## String score

```
fixture vague-issue  skill scope-a-vague-issue
2 holds, 1 broken, 0 skipped
  holds    unscoped-issue  ISSUE.md
  holds    three-readings  login.py
  broken   no-fix  ISSUE.md
judged 3 of 3 planted. 2 named, so this verdict covers 67% of the planted defects.
```

## The agent's report, word for word

## "Login is broken": the issue is scoped and reproduced, but not fixed yet

ISSUE.md only says "the login is broken / please fix". It gives no input, no steps, no expected result and no version. The method treats a report this thin as a job to scope first (`scope-a-vague-issue`) and fix after, test first (`fix-a-bug-test-first`). So I reproduced every behaviour the wording could mean and wrote failing tests for them. I did not change `login.py`, because two of the three possible fixes depend on decisions only you can make. Its SHA-256 is the same before and after (5052b2cc…).

**Files**
- Added: `/tmp/claude-0/-home-user-AV-Recorder/48b60cbf-8f8c-577e-b687-abe5ea6595e2/scratchpad/trials/runs/fixture-vague-issue-old/test_login.py`. It holds the tests, with the scoping notes at the top.
- Unchanged: `login.py` and `ISSUE.md` in the same folder.

### What the code does (Python 3.11.15, each call in a new process)
Each line is a call to `login()` and what it did.

| Reading | Call | Result |
|---|---|---|
| R1: usernames are case-sensitive | `login("ada","s3cret")` | `RuntimeError: locked` |
| R2: a wrong password crashes | `login("Ada","wrong")` | `RuntimeError: locked` on the first attempt |
| R3: empty password gets in | `login("Ada","")` | `True` |
| Control | `login("Ada","s3cret")` | `True` |

- **R2 in detail:** every failed attempt raises, because the check on line 13 (`>= 1`) is always true. That means the `return False` on line 15 can never run.
- **The "lock" locks nothing.** After a failure, a correct password still returns True. The comment on line 7 says otherwise and is wrong.
- **The failure count is shared.** It is stored on the function object, so all users share one count and it never resets.

### The tests and their output
The reading I took for the reported bug is **R2**. It is the only behaviour that every mistyped login hits, including the R1 input, and a user would see it as a crash.

Output, word for word:
```
AssertionError: one wrong password raised RuntimeError(locked) instead of returning False
AssertionError: True is not False : an empty password logged in as a known user (login.py lines 9-10)
Ran 3 tests ... FAILED (failures=2)
```
pytest gives the same result: 2 failed, 1 passed. The control test passes.

**Checking each test fails for its own reason.** I changed the code in memory only, one suspected cause at a time:
- Raise the lock threshold to 3: only R3 stays red.
- Remove the empty-password lines: only R2 stays red.
- Change the error text: both stay red.
- Remove both causes: all green.

This check caught a mistake in my first R3 test. With the empty-password lines removed, `login("Ada", "")` hit R2's crash, so the R3 test still went red for R2's reason. I changed it to treat an exception as "not logged in", and the check now separates the two.

**Where the expected results come from:**
- R2: the `-> bool` return type on line 4 and the `return False` on line 15.
- R3: line 11, the project's only rule for a correct password.
- R1: nothing in the project defines it, so it has no test and needs your decision.

### Gaps in the issue, and what I assumed
1. **Which behaviour "broken" means:** assumed R2. If the reporter meant R3, its test already exists. R1 has no test until you decide it.
2. **Input:** none given. I used the only account, Ada / s3cret, plus "wrong" and "".
3. **Version and environment:** none given, and there is no git history. I tested the file as it is.
4. **What a wrong password should do:** assumed it returns False, going by the return type and line 15.
5. **Lockout rules:** whether there should be one, after how many failures, per user or shared, and when it resets are all undefined. I assumed nothing, so there is no test for them.
6. **Whether this is live:** there is nothing in the folder that deploys it, so I assumed it is not live.

### Questions for you
- **Q1:** Should "ada" log in as "Ada"?
- **Q2:** What exactly did the reporter do and see?
- **Q3:** What should the lockout be: how many failures, per user or shared, how it resets, and should a locked account refuse even the correct password? Should it raise an error or return False?
- **Q4:** Is logging in with an empty password ever meant to work? I assumed not. **May I fix it now?** It is a two-line deletion (lines 9-10), and its test is ready.
- **Q5:** Is this code live? If it is, R3 is an active security hole and should be handled as an incident.

### Other problems found (recorded, not fixed)
- **F1 (security):** an empty password logs in as any known user. This is R3, and it has a failing test.
- **F2:** there is effectively no lockout, so password guessing is unlimited.
- **F3:** the failure count is shared across all users and never resets.
- **F4:** the comment on lines 5-8 describes the code wrongly.
- **F5:** the password is stored in plain text in the source.
- **F6:** the project has no tests, no git and no documentation.

### Recommended next step
Fix R3 first with `fix-a-bug-test-first`: delete lines 9-10. The in-memory check shows its test goes green with only that change. Fix R2 once Q3 is answered and R1 once Q1 is answered.

### Verdict table
| # | Item | Verdict | Evidence or reason |
|---|---|---|---|
| 1 | Reproduced from the report's own input | skipped | The report gives no input or steps |
| 2 | Each reading reproduced (R1, R2, R3) | holds | New-process outputs above |
| 3 | Baseline suite runs | holds | No tests existed: "Ran 0 tests, OK" |
| 4 | Main test (R2) red for the reported reason | holds | Failure output and in-memory check |
| 5 | R3 test red only for its own reason | holds | After the correction; the first version failed this check |
| 6 | R2 expected result has a source | holds | Lines 4 and 15 |
| 7 | R3 expected result has a source | holds | Line 11 (no spec beyond the code) |
| 8 | R1 expected result has a source | broken | None exists; that is Q1 |
| 9 | Every gap listed with the reading taken | holds | See the list above |
| 10 | No behaviour change | holds | `login.py` SHA-256 unchanged |
| 11 | Tests pass or fail the same in any order | holds | unittest and pytest agree; each test resets the shared count |
| 12 | Independent code review | skipped | No review tool and no other agents allowed; I reviewed my own work |
| 13 | Pull request opened | skipped | Not a git repo, and nothing may be published |

9 holds, 1 broken, 3 skipped of 13 items.
