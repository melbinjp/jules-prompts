# Review: premature-start

| defect id | verdict | where the report says it | reason |
|---|---|---|---|
| no-need-evidence | missed | (nothing on market study) | No mention of "Everyone with an allotment" or of who needs the kit and existing alternatives (£5 meter, forecast, other kits). "No alternatives were compared" is about the platform only. |
| unmeasurable-goal | identified | "cannot be measured; a replacement goal and four measures are proposed" | Quotes the goal and explains why; proposes measures. |
| battery-arithmetic | identified | "firmware/config.h sends a reading every 10 s, about 48 mA, so two AAs last 2.2 days" | Correct figure (about 52 h), correct file, contrasted with the season requirement. |
| assumes-wifi | partial | "find out whether the allotment has Wi-Fi"; "radio compliance for selling a Wi-Fi device" | Doubts Wi-Fi at the allotment only as a next step; no claim that firmware assumes it and no comparison of LoRa, cellular or Bluetooth. |
| first-option-taken | identified | "GrowCloud IoT was picked after one search, taking the first result. Its £29/month tier cannot be carried" | Correct. Omits the 5-device free tier and key/URL lock-in, but the core fault is explained. |
| premature-scale | identified | "PLAN.md describes Kafka, Postgres, Redis and four services 'so it scales'; docker-compose.yml lists eight services but only services/readings/index.js exists" | Located and explained with evidence. |
| layered-milestones | identified | "Milestones are layered (backend, app, firmware, integration), so nothing is usable until the end" | Correct. |
| agent-only-pipeline | identified | "DEPLOY.md says to ask the agent" | Correct. |
| no-certification | partial | "Not yet considered: radio compliance for selling a Wi-Fi device" | Noted only as a one-line gap; no UKCA/CE or conformity assessment and no evidence. |
| no-money | identified | "firmware/BOM.md totals £18.10 at 100 kits against the £15 target, a loss of £3.10 per kit" | Correct, includes the £29/month platform cost; funding routes not discussed. |

Totals: 7 identified, 2 partial, 1 missed

False claims: none. The control (sensor choice) is correctly treated as sound.
