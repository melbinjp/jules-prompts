# Expected report for translated-once

The pull request says every page in `docs/en` was translated into `docs/es` and reads naturally. This report checks what a Spanish reader can act on, and what will tell anyone when the translation falls behind.

## Keeping it current

- no-source-revision: no translated file records the source revision it was made from. `HISTORY.md` shows it was `e3a90f2`. Without that line in each file, nobody can tell which Spanish pages are behind their English.
- stale-with-no-check: the English has moved twice since: Python 3.11 is now the minimum, and in v2.0 `--port` became `--listen`. `docs/es/install.md` still says Python 3.9 and `tidal serve --port 8080`, which fails on v2. There is no staleness check, so nothing noticed. Ship a check with the translation that compares each file's recorded source revision with the English file's last change, run it in CI, and show it failing on `install.md`.

## What a reader types

- machine-text-translated: `docs/es/configuration.md` translated the configuration keys: `puerto` and `raiz`. Tidal reads `port` and `root`, so a Spanish reader's `tidal.yaml` is silently ignored. Keys, commands, flags and anything a machine reads stay exactly as in the English.

## Links and structure

- image-path-broken: `docs/es/index.md` links the diagram as `images/diagram.png`. From `docs/es/` that resolves to `docs/es/images/`, which does not exist. The English uses `../images/diagram.png`, which is also right from `docs/es/`.
- anchor-broken: `docs/es/index.md` links to `install.md#installation`, but the Spanish heading is "Instalación", so that anchor no longer exists. Keep explicit anchors that match the English, or link to the anchor the translated heading produces.

## A page that looks finished

- half-translated: `docs/es/configuration.md` is translated down to its keys, then the TLS and Logs sections carry on in English with no note. The page reads as finished and is not. Translate the rest, or mark the untranslated sections as deliberately in English, as the FAQ does.

`docs/es/faq.md` is deliberately left in English, with a note in Spanish saying why: it changes weekly. It stays.

## Verdicts

| item | evidence | verdict |
|---|---|---|
| `index.md` | image path and anchor broken | broken |
| `install.md` | Python 3.9 and `--port`; English moved on | broken |
| `configuration.md` | keys translated; TLS and Logs left in English unmarked | broken |
| `faq.md` | left in English on purpose, with the reason | holds |
| source revision recorded | in no file | broken |
| staleness check | none | broken |
| the docs build and render | not built in the fixture | skipped |

7 items: 1 holds, 5 broken, 1 skipped.

defect_id: no-source-revision
defect_id: stale-with-no-check
defect_id: machine-text-translated
defect_id: image-path-broken
defect_id: anchor-broken
defect_id: half-translated
