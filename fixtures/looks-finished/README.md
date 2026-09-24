# Fixture: looks-finished

Skill: `take-to-production`. Prompt: `task_take_to_production`.

`app/` is Jot, a notes app. In the browser it was built in, it looks finished:
you can add notes, the theme follows the system, and Export works. Its README
makes three promises: notes are saved automatically, you can export them, and it
works on any phone or computer. It breaks all three, it runs any note that is
HTML, and it is unfinished in the ways no test catches. Eight defects are planted,
across data, security, compatibility, accessibility, weight and craft, so a report
that only looks at one area fails. The dark theme is done right and is the control.

Every defect was caused, not read, in Chromium via Playwright:

| defect | what a person sees |
|---|---|
| loses-work | 1 note before a reload, 0 after |
| script-injection | a note of `<img src=x onerror=...>` runs script; a note with a URL still becomes a link |
| chromium-only | with `showSaveFilePicker` removed, as in Safari and Firefox, Export fails |
| blank-error | that failure, and cancelling the save dialog, say "Something went wrong" |
| phone-overflow | at 320 px the document is 592 px wide |
| focus-hidden | the focused input has no outline |
| dead-weight | a request to cdn.jsdelivr.net for lodash, which app.js never uses |
| no-empty-state | with no notes, the list is blank |

```bash
cd fixtures/looks-finished/app && python -m http.server 8000   # then open http://localhost:8000
python scripts/score_fixture.py fixtures/looks-finished --self-check
```

Do not fix the planted defects. They are the test.
