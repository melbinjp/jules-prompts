# Expected report for map-from-folders

`ARCHITECTURE.md` describes three clean layers and five components. This report checks each claim against the imports, the runtime wiring, the configuration and `CO_CHANGE.md`.

## Claims the code contradicts

- layers-do-not-hold: the map says nothing in `services` imports from `api`. `src/services/pricing.py` imports `pantry.api.schemas`, and `CO_CHANGE.md` shows the two files changed together in 33 of 41 commits. The layers do not hold: pricing depends on the API's view types, so the services cannot be reused by the command line unchanged. Move `PriceView` out of `api`, or say plainly that pricing and the API schema are one unit.
- not-a-separate-service: notifications is described as a separate service that can be scaled and deployed on its own. `create_app` in `src/api/app.py` calls `start_worker`, which runs it as a daemon thread inside the API process. It fails, scales and deploys with the API, and an order email is lost if the API process restarts with messages in the queue.
- unused-is-loaded: payments is called legacy code nothing uses, to be deleted in the rewrite. `config/plugins.yaml` names `pantry.payments.stripe_adapter`, and `src/services/checkout.py` loads it with `importlib` at import, so every order is charged through it. A search for static imports misses it. Deleting it would stop every order being charged.
- two-writers-one-table: the map says each table has one owner. The `prices` table is written by `src/api/admin.py` (`set_price`) and by `src/services/pricing.py` (`reprice_offers`), with nothing coordinating them: an admin price set while an offer reprice runs is overwritten or multiplied. This is the coupling the rewrite most needs to know about.

## How the map was made

- no-provenance: not one claim in `ARCHITECTURE.md` says how it was established (an import resolved, the code run, commits counted). Each rests on a folder name, which is why the four claims above read as fact. Every claim needs its evidence, and what cannot be established statically (the `importlib` load, the thread) must be named.

The entry points section is right: `pyproject.toml` declares exactly `pantry.api.app:create_app` and `pantry.cli:main`. It stays.

## Verdicts

| item | evidence | verdict |
|---|---|---|
| entry points | both in `pyproject.toml` | holds |
| layers: services do not import api | `pricing.py` imports `api.schemas` | broken |
| notifications is a separate service | a thread started by `create_app` | broken |
| payments is unused | loaded through `plugins.yaml` and `importlib` | broken |
| each table has one owner | `prices` written from two places | broken |
| each claim with how it was established | none | broken |
| the map predicts where a change lands | a change to `PriceView` touches pricing; the map says it cannot | broken |

7 items: 1 holds, 6 broken, 0 skipped.

defect_id: layers-do-not-hold
defect_id: not-a-separate-service
defect_id: unused-is-loaded
defect_id: two-writers-one-table
defect_id: no-provenance
