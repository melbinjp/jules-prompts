# Expected report for optimise-it

The request, word for word: "The app feels really slow and a bit old-fashioned. Can you optimise it and make it scalable? And add some AI, everyone's using it now. I read that microservices are the modern way to do it."

It makes five claims: slow, old-fashioned, scalable, AI, and microservices.

## What the project is, today

- **Slow.** The booking page takes 6.1 s to be ready on a mid-range phone over 4G, against M4's 2 s. 2.4 MB of its 2.6 MB is one photograph, `static/hero.jpg`: 4032 x 3024 pixels, shown 360 px wide. The availability query takes 4 ms at the 95th percentile.
- **Scalable.** 38 bookings a day at the busiest, with the Pi at 1% CPU and 58 MB of memory. D0001 and D0002 both set their revisit points at 50 bookings a day or two servers. Neither is near.
- **Old-fashioned, and AI.** No measure in the ledger names either one.

## Translation

| claim | reading | ID | before | target | action | evidence |
|---|---|---|---|---|---|---|
| slow | the booking page on a phone | M4 | 6.1 s | 2 s | change: resize hero.jpg | bench/pageload.txt |
| slow | the availability query | none | 4 ms p95 | none | not needed | bench/availability.txt |
| scalable | bookings a day | D0001, D0002 revisit | 38 | revisit at 50 | not needed | the measurements in PROJECT.md |
| old-fashioned | how it looks, or what it runs on | none | | | owner's call | |
| AI | which job, for whom | none | | | owner's call | |
| microservices | an architecture | D0002 | one process | | refused: contradicts D0002 | D0002's evidence |

## Findings in the change already made

- real-slowness-missed: the owner's "slow" is real, and it is the page, not the query. `hero.jpg` is 2,431 KB of a 2,612 KB page. Resize it to 720 px wide, twice the displayed width for high-density screens, as a JPEG or WebP of about 60 to 90 KB. That predicts a page of about 260 KB. Measure after with `make pageload`, and commit with `Serves: M4`. Nothing in the change touches the photo.
- unmeasured-cache: the Redis cache sits in front of a query measured at 4 ms. It cannot move any measure, and it adds a service to run. Worse, its five minutes of staleness break J2: a cancelled slot stays shown as taken, and a booked one is shown as free, until the member who picks it is refused. That refusal also costs M2. Remove it.
- contradicts-decision: `services/availability` splits availability into its own process. D0002 decided on one process, because one writer and one place that decides availability is what keeps M1 at zero. The change brings no new evidence, supersedes nothing, and D0002's revisit condition (50% CPU or 50 bookings a day) has not fired. "Microservices" is refused. Folding the service back also answers "scalable": the capacity is far above the load, and the ledger already says when to look again.
- two-sources-of-truth: the booking page asks the service, which answers from the cache, while `reminders.py` still calls `app.slots_free`, which answers from the database. The same fact now has two answers that disagree for up to five minutes. With the service removed, `slots_free` is the one source again, and `booking_page` calls it.
- never-wired: nothing imports `ai_suggest.py`. It adds the `openai` dependency, an API key and a per-call cost, and the job it would do was never named. Remove it, with its dependency and key. Ask the owner which job they mean. One candidate is suggesting the nearest free slot when the wanted one is taken, and that is a plain query with no model.
- config-never-read: `SCALE_MODE` is added to `.env.example` and read nowhere. Remove it, along with `AVAILABILITY_URL` and `REDIS_URL`, which go with the service.
- untraced: four of the five commits have no `Serves:` line, and "optimise" and "modernise" name no measure. Only the time-zone commit says what it serves.

The time-zone fix in `emails.py` is right. It serves J1, shows shop time whatever the server's clock is set to, and its test covers a summer date and a winter date, so it fails if either season is wrong. Keep it.

## One message to the owner

The page is slow on phones because of one oversized photograph, and fixing that takes it from 6.1 s to well under the 2 s target. The rest already has plenty of room: 38 bookings a day on a machine running at 1%. Two questions: which parts look old-fashioned to you (a screenshot helps), and what would you want AI to do for a member? If it is suggesting another time when your slot is taken, that needs no AI and can be in the next change.

## Detached-code check, after the removals

`services/availability/`, `availability_client.py`, `ai_suggest.py`, and the `redis`, `requests` and `openai` requirements go. So do `SCALE_MODE`, `AVAILABILITY_URL`, `REDIS_URL` and `OPENAI_API_KEY`. `booking_page` returns to `slots_free`. A search for each removed name finds nothing.

## Verdicts

| item | evidence | verdict |
|---|---|---|
| slow: the booking page | 6.1 s against 2 s, the photo is the cause, resize proposed | broken |
| slow: the availability query | 4 ms, no change needed; the cache removed | holds |
| scalable | 38 a day against a revisit point of 50 | holds |
| microservices | contradicts D0002 with no new evidence | broken |
| old-fashioned | no measure; asked the owner | skipped |
| AI | no job named; asked the owner | skipped |
| nothing detached | service, client, AI module, three dependencies and four settings detached | broken |
| every commit traced | 1 of 5 has a Serves line | broken |
| time-zone fix | serves J1; its test covers both seasons | holds |

9 items: 3 holds, 4 broken, 2 skipped.

defect_id: unmeasured-cache
defect_id: real-slowness-missed
defect_id: contradicts-decision
defect_id: never-wired
defect_id: two-sources-of-truth
defect_id: config-never-read
defect_id: untraced
