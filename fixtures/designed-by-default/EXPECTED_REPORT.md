# Expected report for designed-by-default

Slot was redesigned in August and looks tidy. This report checks the design against the people in `DESIGN.md`, the journeys and rules in `PROJECT.md`, the numbers in `metrics/first-booking.csv`, and what the code does for a patient, for the receptionist and for the reminder agent.

## The flow

- flow-by-build-order: `web/book.html` asks for nine fields before it shows a single available time: first and last name, date of birth, email, phone, address, postcode, "how did you hear about us" and fax. The times stay hidden until every required field is filled in (`book.js`). The J1 thread in `PROJECT.md` starts with choosing a time and then asks only name, phone and date of birth. The page has the order in which the fields were added, not the order in which a patient decides. Fax and `heard_from` are written by `store.create` and read by nothing, so they are removed; the address and postcode are asked for nothing J1 needs. Restore the thread's order: times first, three fields, confirmation.
- undo-without-history: `DESIGN.md` promises "Cancelled. Undo" for 10 seconds, with a reason from the desk's log (11 of 40 cancellations in July were mistaken taps). `store.cancel` runs `DELETE FROM bookings WHERE id = ?` and frees the slot at once, so there is nothing to put back, and another patient may already have taken the slot. The design and the data model disagree. Either keep the cancelled booking (a `cancelled_at` column) and hold the slot for the undo window, or drop the promise, with a decision record either way.

## The evidence

- taste-as-evidence: `decisions/D0004-single-page-booking.md` rests on two Source items of opinion ("modern booking apps use one long form", "everyone in the design review preferred it"), nothing measured, tested or prototyped, and `revisit: never`. After it shipped, M1 fell from about 71% (four July weeks) to 52% (four late-August weeks) in `metrics/first-booking.csv`. Nobody reopened the decision. It should be reopened now with the funnel as evidence, and the revisit condition rewritten so it can fire.
- stand-ins-as-people: `research/usability-2026-08.md` reports "5 of 5 participants finished in under 2 minutes. Measured." The session notes show each participant was an agent run with a persona prompt that listed the steps to take. That is a stand-in who was told the answer, recorded as a measurement of people. At best it is a Simulation, and it contradicts the real funnel (52%). Test J1 with five first-time patients, doing the task with no help, and record success, time, errors and their words.

## The look and the words

- values-outside-the-system: `tokens.css` says it is the only source of every colour and size, but `book.css` hard-codes three blues (#1a73e8, #1967d2, and #2b6cb0 in `list.css`), and four greys (#222, #666, #ccc, #777), none of them tokens. Only the control uses the tokens. Move every value onto `tokens.css`.
- contrast: the "Book this time" button is white text on #7fb3f5, a contrast of 2.2:1, where WCAG 2.2 AA needs 4.5:1. For patients with a median age of 61, the one button that finishes the job is the hardest thing on the page to read. `--accent` (#1a5fb4) gives 6.3:1.
- developer-words: `web/messages.js` tells a patient whose slot was just taken "Error 409: CONFLICT", and one who lost the connection "ECONNRESET". Say what happened and what to do next: "Someone booked 10:00 a moment ago. Here are the nearest free times." and "You're offline. Your details are kept; try again when you're connected."

## The operators

- limit-only-in-the-page: the owner's rule, at most two upcoming appointments per patient, is checked only by the page's script (`web/book.js`, `mine.length >= 2`). `server/api.py` and `cli/slot.py` both call `store.create` without it, so the reminder agent, or anyone who calls the API directly, can book past the rule. It must be enforced in one place that every operator passes through: in `store.create`, or a service in front of it that both the API and the command line call.
- agent-path-missing: J3 and M3 need the reminder agent to rebook each missed appointment into the nearest free slot. The web app has `GET /slots` for free times; `cli/slot.py` has only `list` (booked slots) and `book`. There is no way for the agent to list free times, and `list` prints a padded table meant for eyes, with no `--json`, so the agent has to scrape text and guess free slots by subtraction. Give the command line the same actions as the web app (`slots`, `book`, `cancel`, `move`) with machine-readable output and the same limits.

The empty state of the bookings list (`web/list.html`) is designed right. It says what the list is for and what will appear there, and it offers both booking online and the desk's phone number with its hours, all in the tokens. It stays as it is.

## Verdicts

| item | evidence | verdict |
|---|---|---|
| people, with evidence | `DESIGN.md`: median age 61, 78% on phones, one-handed | holds |
| J1 designed as a flow, steps justified | nine fields before any time; fax unused | broken |
| every state designed | the empty state is right; the errors are not | broken |
| every word written | "Error 409: CONFLICT", "ECONNRESET" | broken |
| design promises backed by the data model | undo promised, DELETE in place | broken |
| each action operable by a person and an agent | no free-times or cancel command, no JSON | broken |
| the same limits on every path | two upcoming, checked only in the page | broken |
| the system as the only source | three blues and four greys outside `tokens.css` | broken |
| accessibility: contrast | Book button 2.2:1 | broken |
| each surface rendered and looked at | not in the fixture: no screenshots can be taken here | skipped |
| each journey tested with people, labelled | agent runs reported as measured people | broken |
| each design decision with evidence | D0004 on opinion; M1 fell to 52% | broken |

12 items: 1 holds, 10 broken, 1 skipped.

defect_id: flow-by-build-order
defect_id: undo-without-history
defect_id: taste-as-evidence
defect_id: stand-ins-as-people
defect_id: values-outside-the-system
defect_id: contrast
defect_id: developer-words
defect_id: limit-only-in-the-page
defect_id: agent-path-missing
