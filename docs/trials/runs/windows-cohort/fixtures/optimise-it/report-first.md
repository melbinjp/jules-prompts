# Review Report: Unmerged Changes for "optimise it, make it scalable, add AI, microservices"

**Verdict:** The proposed changes do not do what they claim: they failed to address the actual performance bottleneck, broke critical user journeys and runtime compatibility in Python 3.8, introduced unread placebo configuration, and contradicted accepted architectural decisions without justification. The pull request should be rejected in full.

---

### What could not be checked and why

- **Live 4G mobile page load re-benchmark (`make pageload`):** Could not be executed live during this review because `static/hero.jpg` is not committed to this fixture repository ([static/README.md](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/static/README.md)) and internet access is disabled. However, static inspection of [templates/book.html](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/templates/book.html#L5) confirms that `<img src="/static/hero.jpg" alt="The workshop" width="360">` was completely untouched by the previous agent, meaning the 2.4 MB asset transfer remains unchanged.
- **Live OpenAI API response & Redis server connection:** Could not be executed live because third-party network egress and external background daemon processes are disabled in accordance with the project's offline/isolated runtime rules.

---

## 1. Questions for the Owner & Recorded Assumptions

Because the owner was not available to answer questions during this session, the questions that would have been asked and the assumptions made are recorded here:

1. **Regarding "add AI":** What specific user problem were AI slot suggestions intended to solve?
   - *Assumption made:* Woodshop members booking machines across 12 fixed one-hour slots (09:00 to 20:00) know their own schedules. There was no user problem requiring an LLM; the request was prompted by general industry visibility ("everyone's using it now"). AI slot suggestions introduce latency, ongoing third-party API costs (violating M3), and privacy risks without moving any project measure.
2. **Regarding "make it scalable" / "microservices":** Were any capacity issues observed on the shop's Raspberry Pi?
   - *Assumption made:* No. Measured peak load was 38 bookings a day with 1% CPU and 58 MB RAM ([PROJECT.md](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/PROJECT.md#L48)). The condition to revisit Decision [D0002](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/decisions/D0002-one-process-on-the-shop-pi.md) (>50 bookings/day or >50% CPU) has not been reached. Scalability is not a bottleneck.
3. **Regarding "the app feels really slow":** Should we focus optimization strictly on the hero image?
   - *Assumption made:* Yes. The 6.1 s mobile load time was caused by transferring a 2.4 MB uncompressed phone photo ([bench/pageload.txt](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/bench/pageload.txt)), while the availability database query took only 4.0 ms ([bench/availability.txt](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/bench/availability.txt)). Milestone MS2 should be completed by resizing and compressing `hero.jpg`.

---

## 2. Request Translation

Owner's request word for word:
> *"The app feels really slow and a bit old-fashioned. Can you optimise it and make it scalable? And add some AI, everyone's using it now. I read that microservices are the modern way to do it."*

| Claim | Meaning | Measure / Journey | Value Before | Target | Action Taken by Previous Agent | Value After / Status | Evidence |
|---|---|---|---|---|---|---|---|
| **"The app feels really slow"** | Page ready on mobile phone over 4G | M4 | 6.1 s | <= 2.0 s | Added Redis cache and HTTP microservice for availability queries; left `hero.jpg` untouched | Still 6.1 s (Target missed) | [bench/pageload.txt](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/bench/pageload.txt) shows 2,431 KB of 2,612 KB transferred is `hero.jpg`. [bench/availability.txt](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/bench/availability.txt) shows SQLite query was already 4.0 ms p95. [templates/book.html](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/templates/book.html#L5) still serves `hero.jpg` unmodified. |
| **"Make it scalable"** | Capacity to handle booking load | D0002, M1 | 38 bookings/day, 1% CPU, 58 MB RAM | > 50 bookings/day without errors | Added `SCALE_MODE=true` in `.env.example`; split microservice | Placebo config; added failure points | `SCALE_MODE` is never read anywhere in code. SQLite already tested to 200 concurrent requests. |
| **"A bit old-fashioned" / "microservices"** | System architecture | M3, D0002, J2 | Single process on Pi, £0 extra cost | M3 (<= £5/mo), J2 (instant slot release) | Split availability into HTTP microservice with Redis cache | Broken: contradicts D0002, breaks J2, adds £ cost | [services/availability/server.py](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/services/availability/server.py#L13) caches for 300 s. [app.py](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/app.py#L32-L34) never invalidates cache on cancel. |
| **"Add some AI"** | Member slot suggestions | M2, M3 | Self-service selection from 12 buttons | M2 (>= 90% without help), M3 (<= £5/mo) | Created `ai_suggest.py` calling OpenAI API | Detached code; privacy risk; cost risk | [ai_suggest.py](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/ai_suggest.py) is never imported or called in any route/template. Leaks member names externally. |

---

## 3. Detailed Findings by Change

### 1. Redis Cache & Microservice Architecture (Commits 1 & 2)
- **Premature optimization of the wrong component:** The availability query on SQLite was already measured at **p50 2.1 ms, p95 4.0 ms** ([bench/availability.txt](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/bench/availability.txt)). The 6.1 s page load delay was 93% due to downloading `hero.jpg`.
- **Direct contradiction of accepted decision [D0002](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/decisions/D0002-one-process-on-the-shop-pi.md):** Decision D0002 established a single process on the Raspberry Pi specifically to maintain zero double bookings (M1) and zero hosting cost (M3). Its revisit criteria (>50% CPU or >50 bookings/day) did not fire.
- **Violation of Journey J2 (*"A member cancels, and the slot is free again for everyone at once"*):** In [services/availability/server.py](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/services/availability/server.py#L13-L25), `CACHE_SECONDS = 300`. Neither `app.book()` nor `app.cancel()` in [app.py](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/app.py) invalidates Redis. A cancelled slot remains invisible to other members for up to 5 minutes.
- **Broken imports in Python 3.8 environment:** [app.py](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/app.py#L4) imports `availability_client`, which imports `requests`. In the clean container environment:
  ```
  Traceback (most recent call last):
    File "<string>", line 1, in <module>
    File "/work/app.py", line 4, in <module>
      import availability_client
    File "/work/availability_client.py", line 4, in <module>
      import requests
  ModuleNotFoundError: No module named 'requests'
  ```
- **Detached dual implementation:** `app.booking_page()` calls `availability_client.free_slots()`, but [reminders.py](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/reminders.py#L12) calls `app.slots_free()`, creating two diverging paths to compute the same fact.

### 2. AI Slot Suggestions (Commit 3)
- **Detached dead code:** [ai_suggest.py](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/ai_suggest.py) is never imported or called anywhere in the project.
- **Privacy violation:** Sends woodshop member names and booking habits to OpenAI's public API without consent or privacy terms.
- **Violates Measure M3:** Recurring per-booking API fees exceed the £5/month hosting budget.
- **Runtime failure:** Instantiates `OpenAI()` at module level, failing on clean systems with `ModuleNotFoundError: No module named 'openai'`.

### 3. SCALE_MODE Setting (Commit 4)
- **Inert placebo:** Added `SCALE_MODE=true` to [.env.example](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/.env.example#L4) and mentioned in [CHANGES.md](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/CHANGES.md#L6), but `SCALE_MODE` is never read or referenced in any code file.

### 4. Time Zone Fix and Verification Test (Commit 5)
- **Crashes the test suite on Python 3.8:** [emails.py](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/emails.py#L3) imports `from zoneinfo import ZoneInfo`. `zoneinfo` was added in Python 3.9; Python 3.8 does not have it in standard library.
- **Verbatim test execution output in Docker:**
  ```
  ERROR: test_emails (unittest.loader._FailedTest)
  ----------------------------------------------------------------------
  ImportError: Failed to import test module: test_emails
  Traceback (most recent call last):
    File "/usr/local/lib/python3.8/unittest/loader.py", line 436, in _find_test_path
      module = self._get_module_from_name(name)
    File "/usr/local/lib/python3.8/unittest/loader.py", line 377, in _get_module_from_name
      __import__(name)
    File "/work/tests/test_emails.py", line 4, in <module>
      import emails
    File "/work/emails.py", line 3, in <module>
      from zoneinfo import ZoneInfo
  ModuleNotFoundError: No module named 'zoneinfo'
  FAILED (errors=1)
  ```
- **Ineffective implementation & pseudo-test:** In [emails.py](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/emails.py#L10), calling `.replace(tzinfo=SHOP)` on a naive datetime does not convert hours; it only attaches metadata. In [tests/test_emails.py](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/tests/test_emails.py#L12-L13), `emails.when("2026-06-20", 14)` formats naive `datetime.fromisoformat("2026-06-20T14:00")` to `"Sat 20 Jun, 14:00"` regardless of `TZ=UTC`. The test asserts what naive string formatting already does and cannot detect timezone defects.

---

## 4. Itemized Verification Results

| # | Item / Claim | Type | Result | Evidence / Reason |
|---|---|---|---|---|
| 1 | "Optimise availability with a Redis cache" | Claim | **failed** | Availability was already 4 ms; Redis cache adds network hops, requires uninstalled `redis` module, and causes stale availability. |
| 2 | "Move availability into its own microservice" | Claim | **failed** | Contradicts ADR D0002 without reopening justification; breaks `import app` with `ModuleNotFoundError: No module named 'requests'`. |
| 3 | "Add AI slot suggestions" | Claim | **failed** | Detached module `ai_suggest.py` never called in app; leaks member names to third-party API; violates M3 cost bar. |
| 4 | "Add SCALE_MODE" | Claim | **failed** | Inert configuration in `.env.example`; never read or evaluated anywhere in the codebase. |
| 5 | "Show confirmation times in the shop's time zone" (Serves J1) | Claim / Journey J1 | **failed** | `emails.py` crashes on Python 3.8 (`No module named 'zoneinfo'`); `.replace()` does not convert timezone; `test_emails.py` is an unverified tautology. |
| 6 | Mobile booking page ready in <= 2 s (Measure M4) | Measure M4 | **failed** | Root cause (`static/hero.jpg`, 2.4 MB on 4G) ignored; page load remains 6.1 s. |
| 7 | Slot free at once upon cancellation (Journey J2) | Journey J2 | **failed** | Broken by 300 s cache in `server.py` with no invalidation on cancellation. |
| 8 | Running cost <= £5 a month (Measure M3) | Measure M3 | **failed** | External Redis and OpenAI API dependencies violate cost limit. |
| 9 | Single process on Raspberry Pi (Decision D0002) | Decision D0002 | **failed** | Multi-process microservice violates D0002 without revisit condition (>50% CPU, >50 bookings/day) firing. |

### Workflow & Delivery Separation

- **Workflow:** The previous agent correctly structured its pull request into discrete commits and referenced Journey J1 in Commit 5.
- **Delivery:** The delivery failed completely across all 9 technical and architectural items.

---

## 5. Summary Counts

**0 verified, 9 failed, 0 not verified, 0 not applicable, 0 exception of 9 items.**

---

## 6. Recommended Action for the Owner

1. **Reject and close the pull request:** Do not merge commits 1 through 5 from `CHANGES.md`. Retain the existing single-process SQLite architecture (`D0001`, `D0002`).
2. **Execute Milestone MS2 directly:**
   - Resize `static/hero.jpg` from 4032x3024 down to 360 px wide (to match the `<img width="360">` display tag in `templates/book.html`).
   - Compress the image to ~30–50 KB (saving > 2.38 MB per load).
   - This single change will reduce total page weight from 2.6 MB to ~200 KB and immediately drop mobile 4G page load time from 6.1 s to well under 1.0 s, successfully fulfilling Measure M4 and completing Milestone MS2.

*(Authoritative project records have been written to [REVIEW.md](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/REVIEW.md) and [STATE.md](file:///trial-runs/jules-trials-20260927/runs/fixture-optimise-it-new/STATE.md)).*
