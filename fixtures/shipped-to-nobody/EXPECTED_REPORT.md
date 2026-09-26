# Expected report for shipped-to-nobody

Tidewise 1.0.0 passed its bar and was released on 2026-10-14. Two weeks later `STATE.md` records 12 installs and shelves the project. This report walks the way in from a clean device, checks what people were told against what the product does, and checks the notes against the ledger.

## The way in

- dead-download-link: the website's "Download for Android" link (`site/index.html`) points at `tidewise-1.0.apk`. The signed build in `release/manifest.json` is `Tidewise-1.0.0.apk`. Anyone who came from the website got a missing file. The checklist ticks "website updated with the download link", which was true and not checked.
- first-run-on-the-builders-phone: `src/first_run.py` reads `~/.tidewise/config.toml` with no fallback, so on a clean device the app raises on its first open. The checklist says install and first run were "tested (on my phone)", which already had the file. The two one-star reviews say "crashes on open". Walk the way in on a device that has never seen the app, with no saved settings; start with the home beach unset and ask for it on the first screen.

## What people were told

- listing-contradicts-product: the App Store listing (`store/listing.md`) says "Data Not Collected". `src/analytics.py` sends a device id and the latitude and longitude on every start, with no consent, although M1 says events are sent only with consent. The listing is false and there is no privacy notice. Either stop sending the events until the person agrees, or declare them truthfully, and write the notice from what the code and the network log show.
- wrong-place-wrong-words: the only announcement (`announce/post.md`) went to the builder's own Mastodon account, 380 followers who are mostly developers, in the stack's words: Rust, WASM, a CRDT sync layer, 60 fps. The ledger's reach names the forum's trip-planning board, the 14 club newsletters through the club secretaries, and the two paddling shops, and the 31 kayakers talked about slack water, tidal streams and crossings. Tell them there, in those words, with a `ref` on each link so each channel has its measure.

## The release and the help route

- everyone-at-once: `ops/rollout.yml` has `percentage: 100` and `pause_when: null`. The crash on first open reached every Android user on day one, and nothing could pause the rollout. Release to a small share first, with the rollout set to pause when first-trip planning fails.
- nobody-listening: `help@tidewise.app`, the address the release notes give, forwards to `/dev/null` in `ops/aliases`. "Nobody has written to the help address" means nobody could be heard, and M3 cannot be measured. Route it to a person, answer within a working day, and map every message to a journey or a measure.

## The verdict in STATE.md

- quiet-launch-read-as-verdict: `STATE.md` reads 12 installs in two weeks as "no demand" and shelves Tidewise. The ledger already names this exact condition: K1, fewer than 50 installs in the first two weeks, switches to the club secretaries with a one-page guide and a demo, and the paddling shops with a QR card. Every piece of evidence here is about a missing file, a crash on first open, one channel that was never on the list, and a help address that goes nowhere. None of it is about whether sea kayakers want the app. Fix the way in, take the K1 route, and measure again.

The release notes (`release/NOTES.md`) are written right: what it does for a kayaker, in their words, what it does not replace, and where to write. They stay. The fault is that the address they give goes nowhere, which is `nobody-listening`.

## Verdicts

| item | evidence | verdict |
|---|---|---|
| the way in from the website, clean device | the link names a file that does not exist | broken |
| the way in from the App Store, clean device | not checked: no device in the fixture | skipped |
| first open on a clean device | raises on the missing `config.toml` | broken |
| someone new through it with no help | never done | broken |
| the listing true to the product | "Data Not Collected"; location sent on every start | broken |
| a privacy notice true to the code | none | broken |
| the release notes | what it does, in kayakers' words, and its limits | holds |
| staged rollout with a pause threshold | 100% at once, no pause | broken |
| the help route answered | forwards to `/dev/null` | broken |
| each channel with its measure | one channel, not on the list, no `ref` | broken |
| each course change evaluated | K1 fired and was not taken; the project was shelved | broken |

11 items: 1 holds, 9 broken, 1 skipped.

defect_id: dead-download-link
defect_id: first-run-on-the-builders-phone
defect_id: listing-contradicts-product
defect_id: everyone-at-once
defect_id: wrong-place-wrong-words
defect_id: nobody-listening
defect_id: quiet-launch-read-as-verdict
