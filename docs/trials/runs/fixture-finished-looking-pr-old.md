# Fixture run: finished-looking-pr, old approach

| | |
|---|---|
| Approach | Old: the library at `f5fc9c0e721f4323f4ee79554220bb76128f796d`, exported read-only without `fixtures/` |
| Protocol | `docs/trials/protocol.md` at `51d534d` |
| Agent | A fresh `general-purpose` subagent, model `claude-opus-5-5`, standard file, search and shell tools |
| Workspace | `fixtures/finished-looking-pr/` prepared by `docs/trials/tools/prep.py` (expected report, `defects.json`, `__pycache__` and the explanation file removed) |
| Opening message | `docs/trials/tools/prompt.py finished-looking-pr old <OLD>` |
| Budget used | 14 tool calls, 86,500 tokens, 200 s |
| Files the agent changed | `tests/test_reset.py` changed. |
| String score | Below, from `scripts/score_fixture.py fixtures/finished-looking-pr <report>` |
| Output check | Not yet run. It decides; the string score is kept for comparison. |

## String score

```
fixture finished-looking-pr  skill review-an-agent-pr
3 holds, 0 broken, 0 skipped
  holds    claim-unverified  PR.md
  holds    send-commented-out  mailer.py
  holds    test-cannot-fail  tests/test_reset.py
judged 3 of 3 planted. 3 named, so this verdict covers 100% of the planted defects.
```

## The agent's report, word for word

## Review of PR.md ("Fix password reset emails") against ISSUE.md

**The PR does not fix the issue: reset emails are still never sent.** `request_reset` does pass the token to `mailer.send`, but `mailer.send` doesn't send anything. The delivery line is commented out and the function returns `None`. The PR's single test can't catch any of this.

I followed the method's `review-an-agent-pr` skill, then `qa-an-agents-tests`, as its index prescribes for agent-written work.

### How I checked it
- **Suite:** `python3 -m pytest` collects 1 test and passes it.
- **By hand:** I replaced `mailer.send` with a recording stand-in. `request_reset("ada@example.com")` calls it once with `("ada@example.com", "Reset your password: tok_ada@example.com")`.
- **Real send:** with all network connections blocked and recorded, the real `mailer.send` tried no connection and returned `None`. `send_via_smtp` exists only inside the commented-out line (`mailer.py:7`). It isn't defined anywhere and nothing imports `smtplib`.
- `mailer.py:6` has a comment saying the send is commented out. I didn't take that comment's word for it; the steps above confirm it.

### Issue requirements
| Requirement (ISSUE.md) | Status | Where it's settled |
|---|---|---|
| R1: after requesting a reset, the email actually arrives | Not met | `mailer.py:5-8`: `send` returns `None` with the transport commented out, and makes no network attempt |
| R2: the reset token is emailed via `mailer.send` | Partly met | `reset.py:6-7` calls `mailer.send(email, body)` and the body contains the token. But `mailer.send` doesn't email anything |

### PR claims, requirements and the added test
| Item | Verdict | Evidence |
|---|---|---|
| "restores password reset delivery" | broken | `mailer.py:7-8`: no transport is called; the network spy saw no attempts |
| "email template now includes the reset token" | holds | `mailer.py:2`; confirmed by execution. Whether it is *newly* included can't be checked (no base version) |
| "tests cover the template" | broken | The test never looks at the template. It stays green when the template drops the token |
| "the mailer is used" | holds | `reset.py:7`, confirmed with the recording stand-in. But the mailer it uses does nothing |
| "Closes the issue" | broken | R1 is not met |
| R1: email arrives | broken | See above |
| R2: token emailed via `mailer.send` | broken | Right call, but no email is produced |
| Added test `test_template_contains_token` | broken | Stayed green under 4 of 5 deliberate breaks (next table) |
| Comparison with the base version | skipped | The project isn't a git repository, so there's no base version or diff to compare |
| A CI check gates this PR | skipped | The project has no CI configuration, so nothing gates the merge |

### Deliberately breaking the code under the PR's test
The test only checks `token.startswith("tok_")` on the value `request_reset` returns.

| Break (one at a time, then restored) | Result |
|---|---|
| Template drops the token (what the test's name says it covers) | green |
| `request_reset` never calls `mailer.send` | green |
| Email sent without the token | green |
| Token no longer built from the email address | green |
| `send` raises an error | red, but only from the uncaught `RuntimeError`, not a failed check |

The defect the issue reports, `send` doing nothing, is the code as it stands, and the test passes against it.

### Weakened checks, skips and hidden failures
- **Hidden failure:** `mailer.send` has its delivery line commented out and quietly returns `None` (`mailer.py:7-8`). The PR gives no reason, and its description says the opposite.
- There are no skips, expected-failure marks, `try`/`except` blocks or loosened tolerances.
- Whether the PR deleted or weakened any assertions can't be told, because there's no diff.

### What I changed
I rewrote `tests/test_reset.py`, as the test-QA skill requires for a test that can't fail. `mailer.py` and `reset.py` are byte-identical to the PR; I confirmed this with file hashes after every break.

The file now has 3 tests, written from the issue rather than the code:

| Test | What it checks | Result |
|---|---|---|
| `test_template_contains_token` | The template contains the token | Passes on the PR code; goes red when the template drops the token |
| `test_request_reset_emails_token_via_mailer_send` | `mailer.send` is called once, to the right address, with the token in the body | Passes on the PR code; goes red when the call is removed, the token is left out, or the address is wrong |
| `test_mailer_send_hands_the_message_to_a_transport` | `mailer.send` actually hands the message to a transport | **Fails on the PR code** with `mailer has no transport`, and I left it failing |

To make sure the third test can fail and can pass for the right reasons, I tried three temporary fixes:
- Uncommenting the line on its own: still fails, correctly, because that would crash in production.
- A transport defined but never called: fails.
- A transport defined and called: passes.

I removed the old check `token.startswith("tok_")`. It tested a token format the issue never asks for, and that format is the security problem below.

Test counts went from 1 collected (1 passed) to 3 collected (2 passed, 1 failed). The coverage change was not measured because the coverage tool isn't installed and installs weren't allowed. From reading the code, the old test already ran every line, so line coverage should be unchanged.

### What I couldn't check
- **Base version and diff:** there's no git, so I can't tell which lines the PR changed, whether "now includes" is true, or whether it removed assertions.
- **CI:** there's no CI configuration to check.
- **Real delivery:** couldn't test end to end, because there's no network and no transport exists anyway.
- **Coverage:** no coverage tool.
- **Posting:** I didn't post the review or open a PR, because nothing may be published. This report is the review.

### Problems outside this PR (recorded, not fixed)
1. **Guessable reset token (serious security issue):** `reset.py:5` builds the token as `"tok_" + email`. Anyone who knows an email address can work out its reset token. Whether this PR introduced it is unknown.
2. **Plain `pytest` can't run the suite:** it stops at collection with `ModuleNotFoundError: No module named 'reset'`, because there's no pytest config or conftest. Only `python -m pytest` works, so a CI job using plain `pytest` would error before running any tests.

### Questions for you, and what I assumed
1. **What should actually send the email** (SMTP, a provider API, something else)? I assumed `mailer.send_via_smtp(to, body)`, the name in the commented-out line. The third test depends on that name.
2. **Should the failing test stay in the PR?** I assumed yes, as the method says, so the missing delivery stays visible.
3. **Was the guessable token introduced by this PR?** I assumed it was already there and kept it separate from the verdict.

2 holds, 6 broken, 2 skipped of 10 items.
