**Verdict:** The Spanish translation was not ready to merge as submitted. PR.md's claim that it "reads naturally" was true but not enough: it was out of date and partly broken. I fixed it; one check still fails on a problem that isn't the translation's.

Not checked: Spanish quality beyond plain reading; rendering or the language switcher (no build config or git repo in the fixture); what docs/en said when the translation was made (HISTORY.md shows two later English commits and es/install.md matched neither).

Findings (fixed unless noted):
1. Stale install page. es/install.md said Python 3.9 and `--port 8080`; English now says 3.11 and `--listen 0.0.0.0:8080` (commits 41d07aa and 9be11c4).
2. Translated config keys. es/configuration.md had `puerto:` and `raiz:`, which Tidal would not recognise; `cache_seconds` was left alone so the page was inconsistent. Restored `port` and `root`, added a Spanish note that key names stay in English.
3. Half-translated page. TLS and Logs sections were still English although PR.md says "every page". Translated.
4. Broken image path. `images/diagram.png` resolves to docs/es/images/, which doesn't exist; should be `../images/diagram.png`.
5. Broken anchor. `install.md#installation` doesn't exist in the Spanish page (heading "Instalación"). Linked install.md without an anchor.
6. FAQ. Leaving it untranslated is a fair choice but the copied English body goes stale while the notice says it is up to date. Replaced the body with a link to ../en/faq.md. PR.md does not mention the FAQ was left out.
7. No source revision recorded (fixed) and no staleness check (added): a `translated-from: ... @ 9be11c4` comment on each Spanish file, and check_translation.py checking the file set, heading count, that code and config lines match, that links and anchors resolve, and that the recorded revision matches. Before the fixes it failed with 8 problems.
8. Not fixed: docs/images/diagram.png is 0 bytes, in English too. Pre-existing, outside this PR; recorded.

The checker's last run had one problem, the empty image. It runs in Docker with python:3.8-slim.

Counts: 7 verified fixed, 1 failed and left open, 3 not verified, 0 not applicable of 11 items.
