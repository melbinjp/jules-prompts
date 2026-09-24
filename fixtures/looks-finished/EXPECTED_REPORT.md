# Expected report for looks-finished

## The bar

- **The one job:** jot a note and find it again later.
- **Who, on what:** anyone, on any phone or computer (the README's own promise): Chromium, Safari and Firefox engines, 320 px phones to desktops, keyboard and touch.
- **Journeys that must never fail:** add a note; come back and see it; export everything.
- **Never lost or exposed:** a note once added.
- **Budgets:** no third-party requests; interactive on first paint.
- **Threat model:** the notes are the only thing worth having. Entry points: the note input, and (once saving exists) whatever is stored. The risk is a note that is really markup, pasted from somewhere else, running script in the page that holds every other note.

## Areas walked

- **Security:** note input attempted as HTML (below). No secrets, no server, no cookies.
- **Privacy:** no personal data leaves the device, except each visitor's address to cdn.jsdelivr.net for an unused library (dead-weight).
- **Data, reliability, compatibility, accessibility and craft:** rows below.
- **Not applicable:** capacity, operations and backups (one person, one device, no service); legal (no third-party assets once lodash is gone); physical safety (nothing physical).

## Verdicts

| item | level | evidence | verdict |
|---|---|---|---|
| add a note | 2 | typed, pressed Enter, note listed | holds |
| come back and see it | 1 | added one note, reloaded: 1 before, 0 after | broken |
| a note that is HTML | 4 | `<img src=x onerror="alert(document.domain)">` ran script | broken |
| export, Chromium | 2 | showSaveFilePicker present | holds |
| export, Safari and Firefox engines | 3 | `window.showSaveFilePicker` absent (emulated by deleting it): Export alerts "Something went wrong" | broken |
| 320 px phone | 3 | document is 592 px wide at 320 px | broken |
| visible keyboard focus | 4 | focused input has outline-style none | broken |
| no third-party requests | 5 | lodash from cdn.jsdelivr.net, 0 uses in app.js | broken |
| error messages say what to do | 6 | "Something went wrong" | broken |
| empty state | 6 | no notes: the list renders nothing | broken |
| light and dark | 6 | color-scheme and prefers-color-scheme tokens | holds |

- loses-work: notes are an in-memory array in app/app.js. One reload loses every note, against the README's "saved automatically". Level 1, fixed first: persist each note as it is added (localStorage for this size) and load on start.
- script-injection: `linkify()` builds HTML from the note text and `render()` assigns it to `innerHTML`, so a note that is markup runs script in the page. Today it only runs for the person who typed it; the moment loses-work is fixed, it is stored and runs on every visit. Fix it in the same change: build the text and the link elements with `textContent` and `createElement`, never `innerHTML`.
- chromium-only: Export calls `window.showSaveFilePicker` without feature detection. Safari and Firefox do not have it. Fall back to a download link built from a Blob.
- blank-error: every export failure, including the person cancelling the save dialog, becomes `alert('Something went wrong')`. A cancel should do nothing; a real failure should say what failed and what to do.
- phone-overflow: `.toolbar { width: 560px }` makes a 320 px phone scroll sideways. Let it wrap.
- focus-hidden: `*:focus { outline: none }` with no replacement. Use a `:focus-visible` style instead.
- dead-weight: index.html loads lodash from a CDN and app.js never uses it. Remove it: one fewer request, one fewer thing that can fail offline, and one fewer party that sees each visit.
- no-empty-state: with no notes the list renders nothing. Show one line that says what to do.

Refused: accounts and sync. The bar is one device, and the README promises nothing more.

Not judged: real Safari and Firefox. Their missing API was emulated in Chromium, so those rows are about the missing function, not about everything else in those engines.

3 holds, 8 broken, 0 skipped of 11 items.

defect_id: loses-work
defect_id: script-injection
defect_id: chromium-only
defect_id: blank-error
defect_id: phone-overflow
defect_id: focus-hidden
defect_id: dead-weight
defect_id: no-empty-state
