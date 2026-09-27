# Fixture run: error-path-never-run, old approach

| | |
|---|---|
| Approach | Old: the library at `f5fc9c0e721f4323f4ee79554220bb76128f796d`, exported read-only without `fixtures/` |
| Protocol | `docs/trials/protocol.md` at `51d534d` |
| Agent | A fresh `general-purpose` subagent, model `claude-opus-5-5`, standard file, search and shell tools |
| Workspace | `fixtures/error-path-never-run/` prepared by `docs/trials/tools/prep.py` (expected report, `defects.json`, `__pycache__` and the explanation file removed) |
| Opening message | `docs/trials/tools/prompt.py error-path-never-run old <OLD>` |
| Budget used | 16 tool calls, 97,388 tokens, 353 s |
| Files the agent changed | `fetch.py` changed; `tests/test_fetch_failures.py` added. |
| String score | Below, from `scripts/score_fixture.py fixtures/error-path-never-run <report>` |
| Output check | Not yet run. It decides; the string score is kept for comparison. |

## String score

```
fixture error-path-never-run  skill run-the-error-paths
2 holds, 0 broken, 0 skipped
  holds    bare-except  fetch.py
  holds    untested-failure  tests/test_fetch.py
judged 2 of 2 planted. 2 named, so this verdict covers 100% of the planted defects.
```

## The agent's report, word for word

## How `fetch.py` handles failures

**Short answer: badly, and until now none of the failure handling had ever run.** `fetch_user` has one `except Exception` that turns every failure into a made-up user, `{"id": 0, "name": "guest"}`. That includes a server that is down, a 404 or 500, a timeout, a broken response, a mistyped URL and even a bug inside the function. The caller has no way to tell that from a real user. The only test covered the success path.

I caused each failure for real against local test servers (no outside network) and recorded what the caller got. I then fixed the function so it reports the failure instead of inventing a user, and added 12 tests. All 12 failed against the old code (the old code returned `guest` instead of raising) and pass now. The whole suite is 14 passed, stable over three runs.

I followed the method's `run-the-error-paths` skill.

### Where failures are handled (original `fetch.py`)
- **Line 9–11:** `except Exception:` returns the guest user. This is the only catch and the only fallback.
- **Line 7:** `timeout=1`, the only timeout.
- **Line 8:** the JSON is parsed and returned with no check that it is a JSON object.
- There are no retries and no exit codes.

**Which way it failed:** it let things carry on as if a real user had been fetched. After the fix it refuses: it raises.

### Verdict table (15 failure cases)
| # | Failure caused, and how | As found, the caller got | Verdict as found | After the fix, the caller gets | Verdict after |
|---|---|---|---|---|---|
| 1 | Normal success (control check) | the user | holds | the user | holds |
| 2 | Connection refused (nothing listening on the port) | `guest` (the real error was hidden) | broken | `FetchUserError` naming the URL and "Connection refused" | holds |
| 3 | Server reads the request, then hangs up | `guest` | broken | `FetchUserError`, original error kept | holds |
| 4 | Server accepts and never answers | `guest` after 1.00 s (the timeout fired, then its cause was thrown away) | broken | `FetchUserError` saying "timed out", in under 3 s | holds |
| 5 | HTTP 404 | `guest` | broken | `FetchUserError`: "answered HTTP 404 Not Found; check that the user exists and the URL is right" | holds |
| 6 | HTTP 500 | `guest` | broken | `FetchUserError` with "HTTP 500" | holds |
| 7 | Response is not JSON (`<html>oops`) | `guest` | broken | `FetchUserError` saying it is not JSON, showing the first bytes of the body | holds |
| 8 | Response is not UTF-8 text | `guest` | broken | `FetchUserError` | holds |
| 9 | Response is JSON but not an object (`[1, 2]`, `"ada"`) | the list or string, returned even though the function promises a dict | broken | `FetchUserError`: "returned a JSON list, expected an object" | holds |
| 10 | Typo in the URL scheme (`htp://`) | `guest` | broken | `FetchUserError` with "unknown url type" | holds |
| 11 | A string that is not a URL (`users/7`) | `guest` | broken | `ValueError`, passed through unchanged (it is the caller's mistake) | holds |
| 12 | A bug inside the function (a simulated `NameError`) | `guest`, so the bug was invisible | broken | the `NameError` itself | holds |
| 13 | Server sends the body very slowly (one byte every 0.4 s) | the user, after **2.80 s**, despite `timeout=1` | broken | same, not fixed (see question 2) | broken |
| 14 | HTTP 200 with a JSON object missing the user fields (`{"error": "rate limited"}`) | returned as if it were a user | broken | same, not fixed (see question 3) | broken |
| 15 | Host name that does not exist (DNS failure) | not caused: it needs a real DNS lookup, which this session's no-network rule forbids | skipped | not caused (should take the same path as #2, but I haven't seen it happen) | skipped |

On 13: the 1 s timeout applies to each read, not to the whole call. A server that keeps trickling bytes can hold the caller for as long as it likes.

As found: 1 holds, 13 broken, 1 skipped of 15.

### What I changed
- **`fetch.py`:**
  - Added a new exception, `FetchUserError`.
  - The one catch-everything handler is replaced by narrow ones:
    - HTTP errors say the status code.
    - Network failures (refused, reset, DNS, bad scheme, timeout, server hanging up or sending a broken reply) say the reason; a comment lists what each one expects.
    - A response that is not JSON is reported.
    - A response that is JSON but not an object is reported.
  - Every message names the URL and what to check next, and keeps the original error attached.
  - A string that isn't a URL, and bugs, now surface unchanged.
  - The fake guest user is gone. The function signature and the 1 s timeout are unchanged.
- **New file `tests/test_fetch_failures.py`:** 12 tests plus a control test that proves the test servers work. Each causes the failure for real against a local server. The tests check only what the caller sees (the error raised, its message and the original error), not internal calls. They switch off any proxy settings so local requests go direct.
- **Unchanged:** `tests/test_fetch.py`.

**Behaviour change to be aware of:** `fetch_user` can now raise. Nothing in this project calls it. Any caller elsewhere that relied on getting `guest` back must now catch `FetchUserError`.

### Questions for you (you weren't available, so I assumed and carried on)
1. **Was the guest fallback wanted**, for example to show an anonymous user when the profile service is down? I assumed not. If it was, the caller should catch `FetchUserError` itself and choose `guest` there. That way bugs and bad URLs are no longer hidden behind it.
2. **Is `timeout=1` meant as a limit on the whole call?** I assumed I couldn't tell, so I left it alone (case 13). Making it a true limit is a design choice, not a one-line fix.
3. **Which fields must a user have?** I only require a JSON object, because that is all the function promises. Requiring `id` and `name` would close case 14.
4. **Can the URL ever come from untrusted input?** `urlopen` also opens `file://` URLs: a JSON file in the project came back as a user. That isn't error handling, so I left it unchanged. If the URL can come from outside, it should be limited to `http`/`https`.
5. **Can response bodies contain personal data?** Error messages now show the first 60 bytes of a non-JSON body. If these messages end up in logs and bodies can contain personal data, remove that part.

### Session notes
- **Rule slip:** one early check pointed at `file:///etc/hostname`, which is outside the two folders I was allowed to use. The old code swallowed the result into `guest`, so nothing from that file reached me. I redid that check with a file inside the project.
- **My own test mistakes, both fixed:**
  - In one early check, a "server never answers" result of 0.00 s was my test server closing the connection by accident. That became case 3; the real timeout (1.00 s) is case 4.
  - One new test first expected the wrong kind of connection error. I corrected the test, not the code, and confirmed again that the final test file fails against the old code.
- **Clean-up:** temporary files and caches are removed. Nothing was published or sent anywhere.

Files are in `/tmp/claude-0/-home-user-AV-Recorder/48b60cbf-8f8c-577e-b687-abe5ea6595e2/scratchpad/trials/runs/fixture-error-path-never-run-old/`:
- `fetch.py`
- `tests/test_fetch_failures.py`
- `tests/test_fetch.py`

After fix: 12 holds, 2 broken, 1 skipped of 15 items.
