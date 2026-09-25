# Expected report for premature-start

The idea, word for word, is in `IDEA.md`. What exists is a start another agent made on it.
Most of that start decided things the idea did not ask for, and none of it can be used yet.

## Should it exist

- no-need-evidence: the only evidence of need is PLAN.md's "Everyone with an allotment will want this". Nobody asked any gardeners, and no alternatives were looked at: a £5 moisture meter pushed into the bed, the rain forecast, and the soil-sensor kits already sold for gardens. Verdict: cannot tell yet. The cheapest test is to ask twenty members of the owner's allotment association how they decide when to water, and to take ten pre-orders at the real price.
- no-money: the bill of materials is £18.10 at 100 kits, against the owner's price of £15. Each kit loses £3.10 before postage, payment fees and certification. PLAN.md also has the owner buying 100 dev boards (about £840) and GrowCloud Pro at £29 a month, with no funding named and no approval asked. The owner said there is not much money to put in.
- no-certification: the kit is a radio transmitter sold to the public. It needs a conformity assessment, a declaration and marking (UKCA, and CE for the EU) under the radio equipment rules, plus electrical safety and WEEE producer duties. A pre-certified radio module reduces the testing but does not remove the kit's own certification. No area but engineering was founded: no legal, finance, supply, distribution or support owner. A privacy notice is also needed, for the plot locations and push tokens the app would hold.

## Goal and measures

- unmeasurable-goal: "Revolutionise allotment gardening with AI" cannot be measured. Proposed G1: gardeners water when the bed needs it without a trip to check. Proposed measures: M1, a season on one set of batteries, measured on five kits through a season; M2, a wet-or-dry reading the gardener agrees with at least 9 times in 10, checked by hand in week one; M3, a unit cost under the price, at the planned quantity. Proposed stop condition K1: fewer than ten pre-orders by 1 March, then stop and publish the design as open hardware.

## The arithmetic

- battery-arithmetic: firmware/config.h sends a reading every 10 s, at 160 mA for 3 s and 0.01 mA the rest of the time. The average is (160 x 3 + 0.01 x 7) / 10 = 48.0 mA, so 2,500 mAh lasts about 52 hours, just over two days. A season (April to October, 214 days, about 5,100 hours) needs an average of at most 2,500 / 5,136 = 0.49 mA. One reading every 20 minutes gives (480 + 0.01 x 1,197) / 1,200 = 0.41 mA, about 6,100 hours, which holds with a 19% margin. Every 15 minutes gives 0.54 mA, about 4,600 hours, which does not. Two further numbers need measuring before either is believed. The 0.01 mA is the chip's sleep current, not the dev board's: a dev board's regulator and USB chip draw milliamps, and at 5 mA alone the batteries last three weeks. And two AA cells fall below the module's 3.0 V minimum well before they are empty.
- assumes-wifi: the firmware posts over Wi-Fi, and allotments rarely have Wi-Fi. The radios that reach a field were never compared: LoRa (one gateway per allotment site, shared by every plot, with a much lower transmit cost), cellular NB-IoT (a SIM fee per kit), and Bluetooth read on a visit (no infrastructure at all, but the trip is the thing the owner wants to avoid). This is a one-way door, because it decides the board, the battery, the enclosure and the running cost. It needs three options, two kinds of evidence (a range test at the owner's site, and the transmit-current arithmetic above) and the owner's approval.

## The decisions already taken

- first-option-taken: GrowCloud was chosen because it "came up first" (NOTES.md). It was the only option considered. The free tier stops at 5 devices, then it costs £29 a month. `growcloud_device_id` is the key of the readings table, and GrowCloud's URL is compiled into the firmware of every kit sold, so if GrowCloud changes its price or closes, every kit in a customer's soil stops working. It is a one-way door taken as a two-way one. The options include no cloud at all (a LoRa gateway that pushes to the phone), a small server the owner runs, and an open-source IoT platform. Whatever is chosen should sit behind one module and our own device identifiers.
- premature-scale: Kafka, ZooKeeper, Postgres, Redis and four microservices for a project with no users. None of them is named by a measure, and each is a running cost and a later migration. The walking skeleton needs one small service and one table, or none if the gateway notifies the phone directly.
- the soil sensor (`decisions/sensor.md`) is the one decision made well. It has three options, two independent pieces of evidence (a three-week side-by-side drift measurement and the maker's own corrosion warning), the choice behind one file, and a revisit condition. Keep it, moved into the ledger format.

## Plan and pipeline

- layered-milestones: the milestones are layers (backend, app, hardware, integration), and nothing usable exists until the fourth. Proposed MS1: one kit in the owner's own bed, sending a real reading end to end to the owner's phone, confirmed by pushing a hand probe into the same soil. Proposed MS2: five kits at the association for a month (moves M1 and M2). Proposed MS3: a batch of fifty with certification done (moves M3).
- agent-only-pipeline: DEPLOY.md says to ask the agent to deploy and to flash. No command in the repository does either, so no person, no CI and no other agent can. Every stage needs a command (`make flash`, `make deploy`, `make test`) that a person or an agent can run, with the operating model saying who runs each today.

## Verdicts

| item | evidence | verdict |
|---|---|---|
| need, with evidence | a single assertion in PLAN.md | broken |
| alternatives considered | none | broken |
| goal and measures | "Revolutionise", with no measure | broken |
| stop condition | none | broken |
| battery life against a season | 52 hours calculated, against about 5,100 needed | broken |
| radio reaches the site | Wi-Fi assumed at an allotment | broken |
| unit cost under the price | £18.10 against £15 | broken |
| funding and runway | none named | broken |
| certification | not mentioned | broken |
| privacy | plot locations and push tokens, with no notice | broken |
| IoT platform decision | one option, taken first | broken |
| architecture sized to the need | nine containers for no users | broken |
| milestones usable | nothing usable until the fourth | broken |
| every stage runnable by a person, an agent or CI | deploy and flash exist only as "ask the agent" | broken |
| soil sensor decision | three options, two kinds of evidence, one seam | holds |
| dev board sleep current | not measured; no board to hand | skipped |

16 items: 1 holds, 14 broken, 1 skipped.

defect_id: no-need-evidence
defect_id: unmeasurable-goal
defect_id: battery-arithmetic
defect_id: assumes-wifi
defect_id: first-option-taken
defect_id: premature-scale
defect_id: layered-milestones
defect_id: agent-only-pipeline
defect_id: no-certification
defect_id: no-money
