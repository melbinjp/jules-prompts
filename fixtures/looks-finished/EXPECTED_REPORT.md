# Expected report for looks-finished

## The bar

- **The one job:** jot a note and find it again later.
- **Who, on what:** anyone, on any phone or computer (the README's own promise): Chromium, Safari and Firefox engines, 320 px phones to desktops, keyboard and touch.
- **Journeys that must never fail:** add a note; come back and see it; export everything.
- **Never lost:** a note once added.
- **Budgets:** no third-party requests; interactive on first paint.

## Verdicts

| item | level | evidence | verdict |
|---|---|---|---|
| add a note | 2 | typed, pressed Enter, note listed | holds |
| come back and see it | 1 | added one note, reloaded: 1 before, 0 after | broken |
| export, Chromium | 2 | showSaveFilePicker present | holds |
| export, Safari and Firefox engines | 3 | `window.showSaveFilePicker` absent (emulated by deleting it): Export alerts "Something went wrong" | broken |
| 320 px phone | 3 | document is 592 px wide at 320 px | broken |
| visible keyboard focus | 4 | focused input has outline-style none | broken |
| no third-party requests | 5 | lodash from cdn.jsdelivr.net, 0 uses in app.js | broken |
| error messages say what to do | 6 | "Something went wrong" | broken |
| empty state | 6 | no notes: the list renders nothing | broken |
| light and dark | 6 | color-scheme and prefers-color-scheme tokens | holds |

- loses-work: notes are an in-memory array in app/app.js. One reload loses every note, against the README's "saved automatically". Level 1, fixed first: persist each note as it is added (localStorage for this size) and load on start.
- chromium-only: Export calls `window.showSaveFilePicker` without feature detection. Safari and Firefox do not have it. Fall back to a download link built from a Blob.
- blank-error: every export failure, including the person cancelling the save dialog, becomes `alert('Something went wrong')`. A cancel should do nothing; a real failure should say what failed and what to do.
- phone-overflow: `.toolbar { width: 560px }` makes a 320 px phone scroll sideways. Let it wrap.
- focus-hidden: `*:focus { outline: none }` with no replacement. Use a `:focus-visible` style instead.
- dead-weight: index.html loads lodash from a CDN and app.js never uses it. Remove it: one fewer request, one fewer thing that can fail offline.
- no-empty-state: with no notes the list renders nothing. Show one line that says what to do.

Refused: accounts and sync. The bar is one device, and the README promises nothing more.

Not judged: real Safari and Firefox. Their missing API was emulated in Chromium, so those rows are about the missing function, not about everything else in those engines.

3 holds, 7 broken, 0 skipped of 10 items.

defect_id: loses-work
defect_id: chromium-only
defect_id: blank-error
defect_id: phone-overflow
defect_id: focus-hidden
defect_id: dead-weight
defect_id: no-empty-state
