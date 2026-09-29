# Review: unattended-run

| defect id | verdict | where the report says it | reason |
|---|---|---|---|
| context-overflow | identified | "keeps the whole conversation in a 32,768-token context yet the log shows 99,000 prompt tokens at step 134" | Right file, both numbers, correct meaning (log says 99,600; approximated). Does not spell out that the task fell out of view. |
| invented-api | identified | "called `store.save_all`, which doesn't exist" | Located, error reproduced, fixed and tested. |
| waited-on-the-person | missed | (none) | No mention of the 23:10 VAT question or the 9.5 hour wait. |
| asked-what-it-could-look-up | partial | "at steps 12-14 it asked which test runner, where the tests are and what command runs them" | Steps and questions right, "could have looked up" stated, but the Makefile is not named as the answer. It also says it "waited overnight" on these; the log shows they were minutes (21:32-21:34), the overnight wait was VAT. |
| no-sandbox | identified | "`workdir` points to /home/sam, outside the project" | Located and called unsafe; the sandbox and the keys within reach are not spelled out. |
| no-checkpoints | identified | "`checkpoint = false` and no version control"; "step-97 rewrite that replaced the tested version" | Both facts present; the consequence (nothing to return to) is implied by "put the project under version control". |
| self-review | identified | "the agent wrote REVIEW.md itself at step 133, in the same session as the code" | Correct; next step asks for someone other than the builder. |
| done-unverified | identified | "last `make test` was at step 118. pricing.py was rewritten at step 131 and nothing was run after" | Correct, plus the 412 within 1p measure never checked. |

Totals: 6 identified, 1 partial, 1 missed

False claims:
- Minor: steps 12-14 are said to have waited "overnight"; the overnight wait was the VAT question at step 44, which the report does not mention.
- The control (BRIEFING.md) is not faulted.
