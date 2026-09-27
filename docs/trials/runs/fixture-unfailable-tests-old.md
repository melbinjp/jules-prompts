# Fixture run: unfailable-tests, old approach

| | |
|---|---|
| Approach | Old: the library at `f5fc9c0e721f4323f4ee79554220bb76128f796d`, exported read-only without `fixtures/` |
| Protocol | `docs/trials/protocol.md` at `51d534d` |
| Agent | A fresh `general-purpose` subagent, model `claude-opus-5-5`, standard file, search and shell tools |
| Workspace | `fixtures/unfailable-tests/` prepared by `docs/trials/tools/prep.py` (expected report, `defects.json`, `__pycache__` and the explanation file removed) |
| Opening message | `docs/trials/tools/prompt.py unfailable-tests old <OLD>` |
| Budget used | 13 tool calls, 91,551 tokens, 271 s |
| Files the agent changed | `tests/test_pricing.py` changed. |
| String score | Below, from `scripts/score_fixture.py fixtures/unfailable-tests <report>` |
| Output check | Not yet run. It decides; the string score is kept for comparison. |

## String score

```
fixture unfailable-tests  skill qa-an-agents-tests
2 holds, 2 broken, 0 skipped
  broken   shape-assertion  tests/test_pricing.py
  broken   mocks-the-unit  tests/test_pricing.py
  holds    reconstructed-expected  tests/test_pricing.py
  holds    no-exception  tests/test_pricing.py
judged 4 of 4 planted. 2 named, so this verdict covers 50% of the planted defects.
```

## The agent's report, word for word

No, the tests aren't good. Four of the five can't catch the bug that is sitting in `discount()` right now, and one of them would fail if someone fixed it. The whole suite passed 5/5 while `discount(100.0, 10.0)` returns 0.0 instead of the 90.0 its docstring promises.

I followed the `qa-an-agents-tests` skill: break the function on purpose, one change at a time, run each test alone, and see whether it goes red. `pricing.py` was put back after every break; its hash matches the original and no cache files were left behind.

**The bug the tests missed.** `discount()` divides by 10 instead of 100. 10% off 100.0 gives 0.0, and 25% off 200.0 gives -300.0, a negative price. The file even has a `# BUG` comment saying so. I did not fix it, because the method forbids changing the code under test. Changing `/ 10` to `/ 100` makes all remaining tests pass; I ran that change as a probe and then put the original back.

**How each original test did.** Mutants: M0 is the correct formula (a probe, not a break), M1 `return price`, M2 `return 0.0`, M3 empty body (returns None), M4 raises an error, M5 sign flipped, M6 returns the discount amount instead of the price, M7 `price - percent`. "red" means the test failed.

| Test | shipped (buggy) code | M0 | M1 | M2 | M3 | M4 | M5 | M6 | M7 | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| `test_discount_returns_something` | green | green | green | green | red | red | green | green | green | broken, rewritten |
| `test_discount_is_called` | green | green | green | green | green | green | green | green | green | broken, deleted |
| `test_discount_formula` | green | **red** | red | green | red | red | red | red | red | broken, rewritten |
| `test_discount_does_not_raise` | green | green | green | green | green | red | green | green | green | broken, deleted |
| `test_zero_percent_leaves_price` | green | green | green | red | red | red | green | red | green | holds, kept as is |

- **`test_discount_returns_something`** only checks that something comes back. It fails only when nothing is returned or the function crashes.
- **`test_discount_is_called`** replaces `discount` with a fake and then tests the fake. It passes even with the function body deleted.
- **`test_discount_formula`** copies the code's own arithmetic, bug included. It passes on the buggy code and on `return 0.0`, and fails on the correct formula (`assert 90.0 == 0.0`), so it would block the fix.
- **`test_discount_does_not_raise`** only checks that no error is raised. It passes on every wrong value.
- **`test_zero_percent_leaves_price`** is sound for what it names. It stays green where 0% still leaves the price unchanged, which is correct.

**What I changed.** Only `/tmp/claude-0/-home-user-AV-Recorder/48b60cbf-8f8c-577e-b687-abe5ea6595e2/scratchpad/trials/runs/fixture-unfailable-tests-old/tests/test_pricing.py`. The expected values are worked out by hand from the docstring ("percent=10 means 10 percent off"), not by running the code:
- `test_discount_returns_something` became `test_ten_percent_off_100_is_90`, asserting 90.0.
- `test_discount_formula` became `test_quarter_off_200_is_150`, asserting 150.0. This one also catches M7, which the first one misses.

Both new tests pass on the correct formula and fail on the buggy code and on every break (the first misses only M7). I also ran the M5 and M6 breaks in both their `/10` and `/100` forms against old and new tests; no verdict changed.

**Deleted, with reasons:**
- `test_discount_is_called`: it fakes the very function it tests, and `discount()` has nothing else to fake, so it can't be made meaningful.
- `test_discount_does_not_raise`: its only check is "no error raised". Every remaining test already fails if `discount()` raises.

**Before and after:**
- **Tests:** 5 collected and 5 passed before; 3 collected after, with 1 passing and 2 failing because of the real bug. I left those 2 failing on purpose.
- **Skips:** none added by the agent, none found.
- **Coverage:** unchanged. The coverage tool isn't installed and I couldn't install it offline, so I measured with Python's built-in `trace`: the same lines of `pricing.py` run before and after, and the formula line runs 3 times instead of 4.
- **Running the suite:** bare `pytest` from the project root fails with `No module named 'pricing'` and collects nothing. Only `python3 -m pytest` works. I left this alone. Adding `pythonpath = .` to a pytest config file would fix it.

**Questions I couldn't ask you, and what I assumed:**
1. The project has no git history, so I couldn't confirm which tests the agent wrote. I assumed all 5 in `tests/test_pricing.py` are its work, since the file's own header says so.
2. I treated the docstring as the spec. If `percent` is meant to be on some other scale, the new expected values are wrong, and so is the docstring.
3. I assumed the suite is meant to be run with `python3 -m pytest` from the project root.
4. Should the `/ 10` bug be fixed now? I left it and its failing tests for you to decide.
5. What should happen with `percent` above 100 or below 0? Nothing specifies it, and I added no tests for it.

Nothing was committed or published, since there is no git repo and sending anything was off-limits. This report stands in for the review and pull request the method asks for.

1 holds, 4 broken, 0 skipped of 5 tests.
