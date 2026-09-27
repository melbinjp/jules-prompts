# Fixture run: looks-finished, old approach

| | |
|---|---|
| Approach | Old: the library at `f5fc9c0e721f4323f4ee79554220bb76128f796d`, exported read-only without `fixtures/` |
| Protocol | `docs/trials/protocol.md` at `51d534d` |
| Agent | A fresh `general-purpose` subagent, model `claude-opus-5-5`, standard file, search and shell tools |
| Workspace | `fixtures/looks-finished/` prepared by `docs/trials/tools/prep.py` (expected report, `defects.json`, `__pycache__` and the explanation file removed) |
| Opening message | `docs/trials/tools/prompt.py looks-finished old <OLD>` |
| Budget used | 46 tool calls, 157,267 tokens, 1601 s |
| Files the agent changed | `.gitignore` added; `CHANGELOG.md` added; `QUALITY.md` added; `app/README.md` changed; `app/app.js` changed; `app/index.html` changed; `app/style.css` changed; `package-lock.json` added; `package.json` added; `tests` added |
| Written outside the workspace | `/root/.npm/_logs/2026-09-27T10_33_00_285Z-debug-0.log`; `/root/.npm/_logs/2026-09-27T10_27_01_852Z-debug-0.log`; `/root/.npm/_logs/2026-09-27T10_29_00_716Z-debug-0.log`; `/root/.npm/_logs/2026-09-27T10_33_00_811Z-debug-0.log`; `/root/.npm/_logs/2026-09-27T10_29_01_421Z-debug-0.log`; `/root/.npm/_logs/2026-09-27T10_29_00_488Z-debug-0.log`; `/root/.npm/_logs/2026-09-27T10_18_22_727Z-debug-0.log`; `/root/.npm/_logs/2026-09-27T10_31_18_857Z-debug-0.log`; `/root/.npm/_logs/2026-09-27T10_26_40_880Z-debug-0.log`; `/root/.npm/_logs/2026-09-27T10_25_18_759Z-debug-0.log`. Run 1's leftover file: `4c13315a7464…` before, `4c13315a7464…` after |
| String score | Below, from `scripts/score_fixture.py fixtures/looks-finished <report>` |
| Output check | Not yet run. It decides; the string score is kept for comparison. |

## String score

```
fixture looks-finished  skill take-to-production
7 holds, 1 broken, 0 skipped
  holds    loses-work  app/app.js
  holds    script-injection  app/app.js
  broken   chromium-only  app/app.js
  holds    blank-error  app/app.js
  holds    phone-overflow  app/style.css
  holds    focus-hidden  app/style.css
  holds    dead-weight  app/index.html
  holds    no-empty-state  app/app.js
judged 8 of 8 planted. 7 named, so this verdict covers 88% of the planted defects.
```

## The agent's report, word for word

## Jot notes app: readiness report

Jot was not ready for real users when I received it. It now meets the quality bar I wrote for it in Chromium, desktop and emulated phone. It has **not** been run in Firefox or Safari, which were not installed and could not be installed without the network, so iPhone users are untested.

I followed the method's `take-to-production` skill, which is its entry for making an existing project ready for people, plus its security-review and fix-the-bug-with-a-failing-test-first steps. I used the system's Node, and the Playwright and Chromium already installed on it, only as tools. Nothing was sent or published.

### What was wrong in the app as received
I wrote the tests first; 24 of 26 failed on the original code. Listed by harm to the person:
1. **Notes were lost on every reload.** Nothing was saved, even though the README says "Your notes are saved automatically."
2. **Script could be injected.** A note like `https://example.com/"onmouseover="…` ran script on hover (the test showed the attack succeeding). The cause was building HTML with `innerHTML`.
3. **Export failed in Firefox, Safari and on every phone.** It relied on a Chrome-only save dialog, and cancelling that dialog showed "Something went wrong".
4. **At 320 px the page was 791 px wide.** A fixed 560 px toolbar.
5. **Keyboard users couldn't see where they were.** The CSS removed every focus outline.
6. **Accessibility and wording gaps:** control borders too faint to meet contrast rules, no empty state, no message area for screen readers.
7. **Every visit was reported to a third party.** An unused lodash script loaded from jsDelivr.

I also found and fixed a defect in my own change. The code that keeps trailing punctuation out of links was quadratic: a pasted 100,000-character link took 8.6 s to render, on every open. It now takes a few milliseconds.

### What changed
Everything is under `/tmp/claude-0/-home-user-AV-Recorder/48b60cbf-8f8c-577e-b687-abe5ea6595e2/scratchpad/trials/runs/fixture-looks-finished-old/`. The project had no git history, so I created a repository and committed the original files first, then made 4 commits on top.
- **`QUALITY.md`** is the bar: the one job, five journeys, what must never be lost, budgets and a craft standard, ending with the verdict table.
- **`tests/app.test.js`** has 28 browser tests, run with `npm test`. Setup from a fresh clone is `npm ci` then `npm test`, with a lockfile pinning Playwright 1.56.1.
- **`app/app.js`, `index.html`, `style.css`:**
  - Notes are saved in the browser, and two open tabs never overwrite each other.
  - Saved data the app can't read is never overwritten.
  - If storage is full or blocked, the app says so plainly and keeps the text being typed. Unfinished typing survives closing the page.
  - Notes are shown as plain text, and only http(s) links become clickable.
  - Export falls back to a normal download where the save dialog doesn't exist.
  - Delete a note, with Undo.
  - Fits 320 px screens with 44 px touch targets, a visible focus ring, contrast that passes in light and dark, and right-to-left notes.
  - The version is shown in the footer.
- **`app/README.md`** now claims only what holds (notes stay on this device and are not synced). **`CHANGELOG.md`** is new.

### How I know the tests can fail
- 24 tests failed on the original code, each for the reason in its name.
- I put 25 defects back into the fixed code one at a time, and the matching test failed every time.
- The two long-link tests failed before their fix.
- The size budget failed when I added 25 KB.
- A fresh clone, installed offline from the lockfile, passes 28 of 28.

### Verdict
| Row | Verdict | Evidence or reason |
|-----|---------|--------------------|
| Add, reopen (reload, tab closed, restart), links, delete and undo, in Chromium | holds | tests |
| Export with the save dialog, without it, and cancelled | holds | tests |
| Never lost: reload, tab closed right after adding, restart, two tabs, storage full, storage blocked, newer or damaged data | holds | one test each |
| Unfinished text survives the page closing; text kept when a save is refused | holds | tests |
| Script injection attacks; links http(s) only with safe link settings; no third-party scripts; long-link freeze | holds | attack tests |
| Nothing sent anywhere; a person can delete a note | holds | the network log is empty during use |
| Size (app/ is 12,976 bytes of a 20 KB budget); no other websites contacted; 100 ms response with 2,000 notes | holds | tests |
| 320 px, 44 px targets, keyboard focus ring, labels and message areas, contrast in light and dark, wording, right-to-left | holds | tests |
| Version and changelog; older versions never overwrite newer data; setup from cold; tests seen to fail; README commands; licences | holds | |
| Firefox; Safari desktop and iPhone; real phones | skipped | these browsers and devices were not available |
| Safari clearing site data on its own | skipped | untestable here. Export is the safeguard. |
| Hosting security (HTTPS, a content security policy, headers) | skipped | there is no host yet |
| Listening with a real screen reader; measuring layout shift; `npx playwright install` (needs network); whether dependencies are current | skipped | not measurable or needs network |
| A copyable diagnostics report | broken | not built |
| CI that runs the tests and budgets automatically | broken | no CI exists; `npm test` is run by hand |

One caveat on the two-tabs test: it passes through the path where one tab refreshes when the other saves. The read-before-write guard for two saves at the same instant is not tested on its own.

Areas that don't apply, each with a one-line reason, are in `QUALITY.md`: server capacity, alerts, backups (Export is the backup), migrations (this is the first saved format), and physical safety.

**Removed:** the unused lodash script from the CDN, the fixed 560 px width, the CSS rule that hid focus outlines, and the `alert()` box.

**Refused, not needed for the bar:**
- sync or accounts, editing notes, search, showing timestamps
- offline install as a phone app
- a CI file (the repository host is unknown)
- a content security policy in the page itself (it couldn't be tested in Firefox or Safari, and could stop the script loading there)
- asking the browser to keep storage permanently (can't be verified here)

### Questions for you, with what I assumed
1. **Which devices?** I assumed the README's "any phone or computer" means current Chrome/Edge, Firefox and Safari, including Safari on iPhone.
2. **Where will it be hosted?** Phones can't open a local file, so I assumed a static HTTPS host. Once one is chosen, it needs security headers. Hosting also avoids Chrome sharing storage between local files (from memory, not tested here).
3. **Sync between devices?** I assumed no, and the README and footer now say notes stay in this browser on this device.
4. **Delete and Undo:** I added them because saved notes need a way to be removed. Is that OK?
5. **CI and a licence:** is there a repository host to run the tests on each change? Jot has no licence file.
6. **Git:** I created a repository, with your original files as the first commit, so every change can be compared with what you had.
7. **Look:** I kept your 560 px left-aligned column. The visual design is your call.

### Next steps
1. Run the tests in Firefox and WebKit (Safari's engine), and on a real iPhone. Safari clearing storage is the biggest open risk to people's notes.
2. Choose a host and add the security headers.
3. Add CI that runs `npm test`.

37 holds, 2 broken, 9 skipped of 48 items.
