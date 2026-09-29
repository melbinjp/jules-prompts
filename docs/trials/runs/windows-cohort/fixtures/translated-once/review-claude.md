# Review: translated-once

| defect id | verdict | where the report says it | reason |
|---|---|---|---|
| no-source-revision | partial | "No source revision recorded (fixed) and no staleness check (added)" | Correct problem and a fix, but does not name the original revision e3a90f2, does not say which files, and says it could not tell what English said at translation time. |
| stale-with-no-check | identified | "es/install.md said Python 3.9 and `--port 8080`; English now says 3.11 and `--listen 0.0.0.0:8080`" | Both drifts with commits cited; staleness checker added. |
| machine-text-translated | identified | "es/configuration.md had `puerto:` and `raiz:`, which Tidal would not recognise" | Correct file, keys and consequence. |
| image-path-broken | identified | "`images/diagram.png` resolves to docs/es/images/ ... should be `../images/diagram.png`" | Correct. |
| anchor-broken | identified | "`install.md#installation` doesn't exist in the Spanish page (heading \"Instalación\")" | Correct. |
| half-translated | identified | "TLS and Logs sections were still English although PR.md says 'every page'" | Correct. |

Totals: 5 identified, 1 partial, 0 missed

False claims:
- Finding 6 faults the control (docs/es/faq.md): says the copied English body "goes stale while the notice says it is up to date" and replaced the FAQ body with a link. The Spanish note deliberately says the page is in English on purpose because it changes weekly ("en inglés, al día"), so this is an invented defect and an unneeded change (though the report calls the choice "fair").
- Finding 8 (docs/images/diagram.png is 0 bytes) is true of the fixture (0 bytes), not a false claim.
