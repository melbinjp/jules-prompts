# Fixture run: premature-start, old approach

| | |
|---|---|
| Approach | Old: the library at `f5fc9c0e721f4323f4ee79554220bb76128f796d`, exported read-only without `fixtures/` |
| Protocol | `docs/trials/protocol.md` at `51d534d` |
| Agent | A fresh `general-purpose` subagent, model `claude-opus-5-5`, standard file, search and shell tools |
| Workspace | `fixtures/premature-start/` prepared by `docs/trials/tools/prep.py` (expected report, `defects.json`, `__pycache__` and the explanation file removed) |
| Opening message | `docs/trials/tools/prompt.py premature-start old <OLD>` |
| Budget used | 26 tool calls, 143,495 tokens, 502 s |
| Files the agent changed | `.gitignore` added; `AGENTS.md` added; `DEPLOY.md` changed; `Makefile` added; `PLAN.md` changed; `PROJECT.md` added; `build` added; `decisions/D0001-capacitive-soil-sensor.md` added; `decisions/D0002-where-readings-go.md` added; `decisions/D0003-board-radio-and-power.md` added; `decisions/D0004-one-small-server.md` added; `decisions/sensor.md` removed; `firmware/test_sensor.c` added; `tools` added |
| Written outside the workspace | none apart from system logs. Run 1's leftover file: `4c13315a7464…` before, `4c13315a7464…` after |
| String score | Below, from `scripts/score_fixture.py fixtures/premature-start <report>` |
| Output check | Not yet run. It decides; the string score is kept for comparison. |

## String score

```
fixture premature-start  skill start-from-an-idea
4 holds, 6 broken, 0 skipped
  broken   no-need-evidence  PLAN.md
  broken   unmeasurable-goal  PLAN.md
  holds    battery-arithmetic  firmware/config.h
  broken   assumes-wifi  firmware/config.h
  holds    first-option-taken  NOTES.md
  broken   premature-scale  docker-compose.yml
  holds    layered-milestones  PLAN.md
  holds    agent-only-pipeline  DEPLOY.md
  broken   no-certification  PLAN.md
  broken   no-money  firmware/BOM.md
judged 10 of 10 planted. 4 named, so this verdict covers 40% of the planted defects.
```

## The agent's report, word for word

## Is it a good start, and what next?

**Short answer: partly.** One piece is good: the choice of soil sensor, which was backed by a real three-week test. Everything else was built before the basic arithmetic was done, and the numbers don't work yet. The most important advice is **don't buy the 100 ESP32 boards, and don't sign up for GrowCloud Pro**, even though the old plan asks you to do both. None of it is wasted and nothing has been deleted; it just needs to be done in a different order.

I followed the method's `start-from-an-idea` skill (the path for a project that already exists), with `choose-with-evidence` for the decisions and `act-on-the-physical-world` for the hardware. I used 24 tool calls, no network, and made no purchases, sign-ups or physical actions.

### What's good
- **The sensor choice.** I recomputed the figures from `bench/sensor-drift.csv` and they match: over 21 days the cheap resistive probe drifted 41.0% and the capacitive sensor drifted 3.0%. Only one file (`sensor.c`) depends on which sensor is fitted, so changing it later is cheap.
- **The parts list adds up:** £18.10 across 7 parts, as stated.

### What's wrong, with the numbers
- **Battery life is 2.2 days, not a season.** The firmware sends a reading every 10 seconds: each send is 3 s at 160 mA, so the average draw is 48 mA and 2,500 mAh lasts 52 hours. To last a season (I assumed 1 April to 30 September, 183 days), it can send at most once every 14.3 minutes. Hourly readings give about 727 days on paper. That paper figure assumes the chip's own sleep current. A dev board likely draws much more while asleep; if it draws 5 mA (a figure I assumed, not measured), even hourly readings last only about 20 days. Measuring the real board on the bench is the key unknown.
- **Each kit costs more to make than it sells for.** Parts are £18.10 against a £15 price, a £3.10 loss per kit before postage or fees. The dev board alone is £8.40, 46% of the parts cost.
- **GrowCloud was simply the first search result.**
  - Pro is £348 a year, which you would pay for as long as any kit is running. At 100 kits that's £3.48 per kit per year, forever, against a one-off £15 sale.
  - The integration has never run. The GrowCloud library it needs isn't there, and the firmware's address ends in `.example`, a name reserved for examples, so it can never be reached.
  - The kits' IDs would belong to GrowCloud, which makes leaving expensive once kits are sold.
- **The server setup is far bigger than needed.** It plans four services plus Kafka, Postgres and Redis. Three of the four service folders don't exist, so it can't be built. 100 kits reading hourly is about 0.03 readings a second, which one small program handles easily.
- **Nothing reaches a phone yet.** There is no main firmware program, no code to send readings and no message to the phone. The plan builds in layers (backend, then app, then hardware, then connecting them), so nothing works until the very end.
- **Setting up the server and loading firmware onto a kit only happen by asking the previous agent.** Neither is a command anyone else can run.
- **The sensor's calibration numbers are unbacked.** `sensor.c` says its calibration came from the `bench/` folder, but that folder only has the drift log.

### What next
1. **Answer seven questions** (listed in `PROJECT.md`). The most important is Q1: can your phone see a Wi-Fi network at your beds? Many allotment sites have none. If yours doesn't, the better route is one shared receiver in the association's shed that every kit on the site talks to.
2. **First milestone:** one kit in your own bed for two weeks, reading hourly and sending "water bed 1" to your phone when it's dry, with its battery draw measured on the bench. Buy one or two boards, not 100.
3. **Second milestone:** ten "founder kits" at the association for the 2027 season, sold at cost or pre-ordered, so they pay for themselves. Online sales come after that, once the real parts cost and running cost are known.

### What I changed in your project
- **`PROJECT.md`**: the project's record (the method calls it a "ledger"). It holds your idea word for word, the goal, five measurable targets, three journeys that must always work, fallback routes if something fails, the three milestones, the plan and the seven questions with what I assumed meanwhile.
- **`decisions/`**:
  - `D0001` is your sensor decision, moved from `sensor.md` with its content kept.
  - `D0002` (where readings go), `D0003` (board, radio and power) and `D0004` (the server) record the choices the old scaffold made without comparing anything. Each is marked proposed, with the options and the evidence I could produce offline. **None is approved; that's your call.**
- **`tools/battery_budget.py`** and `make battery`: calculates battery life directly from `firmware/config.h`. It fails today on purpose (2.2 of 183 days) and will pass once the design lasts a season.
- **`firmware/test_sensor.c`** and `make test`: checks the moisture calculation against values worked out by hand. I broke the code three different ways and the tests caught each one.
- **`tools/check_trace.py`**, run by `make check`: refuses any decision or change that doesn't say what it's for and how it was checked. It passes now, and I confirmed it rejects a change with no stated reason.
- **Other files:**
  - `Makefile` for the commands above.
  - `AGENTS.md` with standing rules for any agent working here, including: nothing gets bought, and nothing is loaded onto a real board without your yes.
  - `.gitignore` for build output.
  - A short note at the top of `PLAN.md` (replaced by `PROJECT.md`, its next steps on hold) and `DEPLOY.md` (its steps aren't real commands yet).
- **Version control:** the folder wasn't under version control, so I set it up there with one commit (`abfe187`). Deleting the `.git` folder undoes that.
- **Not done:** I haven't removed `docker-compose.yml` or `services/`. That's for you to decide (`D0004`).

### Assumptions I made (you weren't available)
- The season is 1 April to 30 September.
- You currently go about five evenings a week just to check.
- An hourly reading is fresh enough.
- The kit should cover its costs rather than make a profit, leaving £5 of the £15 for postage and fees, so parts must cost £10 or less.
- The starting budget is enough for one or two kits (about £40).

All of these are in `PROJECT.md` for you to correct.

### Verdict
| item | verdict |
|---|---|
| Goal and five measures defined, each with a target, date and method | holds |
| Battery lasts a season, as configured | broken (2.2 of 183 days) |
| Parts cost within target | broken (£18.10, target £10, price £15) |
| Running cost within target, as scaffolded | broken (£3.48 per kit per year at 100 kits) |
| "Evenings saved" and "kits in use" measurable today | skipped (no kit exists) |
| Need evidenced beyond your own experience | skipped |
| Existing products compared | skipped (no network) |
| Sensor decision (D0001) | holds (recomputed; tests seen to fail) |
| Sensor calibration the code refers to | broken (not in `bench/`) |
| Data platform choice (D0002), as built | broken (never ran; unreachable address) |
| Board, radio and power (D0003), as built | broken |
| Server setup (D0004), as built | broken (3 of 4 service folders missing) |
| Your approval on the hard-to-reverse decisions | skipped (you weren't available) |
| A fallback route for each way it could fail | holds |
| Milestones each leave something usable; release to people planned early | holds |
| Main journey (reading to "water bed" message) traced with no gaps | broken (5 gaps) |
| Setup journey and low-battery journey traced | skipped |
| Tests are real commands and seen to fail | holds |
| Record check rejects a change with no reason | holds |
| Building firmware, loading it onto a kit, calibration and server setup as commands | broken (none exist) |
| Checks running automatically on every change | skipped (no automated build system in the project) |
| One kit working end to end, and undoing a release once | broken |
| Legal and privacy (radio approval, battery rules, privacy notice) | skipped (not researched) |
| Agents tested for each stage of the work | skipped |
| Everything re-run from a fresh copy | holds (only the battery check fails, as intended) |

7 holds, 10 broken, 8 skipped of 25 items.
