# Expected report for command-accepted

Five physical actions, six defects. One action (`open_vent`) is done right and is the pattern for the rest.

| action | contract gap | what was caused | verdict |
|---|---|---|---|
| `close_valve` | success is HTTP 200 from the board, not an observation | board returns 200, valve left open in the simulator: function still returns True | broken |
| `dispense_fertiliser` | not idempotent, retried on reply timeout | first send delivers, reply times out: three doses for one request | broken |
| `keep_warm` | failure path defaults to 20.0; units disagree | sensor unreadable: heater on. Beds at 30 C, target 68 F: heater stays on | broken |
| `water` | no watchdog | process killed during the sleep: pump never told to stop | broken |
| `open_vent` | none: sensor reading newer than the command, 30 s deadline, closes on failure | sensor unreachable: vent commanded closed, returns False | holds |

- trusts-the-ack: `close_valve` returns `reply.status == 200`. The board accepting the command is not the valve closing. Confirm with an independent observation such as a flow reading taken after the command, within a deadline.
- retries-a-dispense: `dispense_fertiliser` retries after `TimeoutError`, but a timeout on the reply does not mean the dose did not go out. The action is not idempotent. Retry only after observing that the first dose did not happen, or send an idempotency key the board honours.
- fails-hot: in `keep_warm`, `except Exception` replaces an unreadable sensor with `20.0`, so the heater is switched on blind. The safe state for a heater with no reading is off, plus an alert.
- units-mismatch: `keep_warm` compares a Celsius reading from the board with `target_f` in Fahrenheit. At 30 Celsius the beds are already warm, yet 30 < 68 keeps the heater on. Convert once at the edge and name the units (`target_c`).
- no-watchdog: `water` turns the pump on, sleeps, then turns it off. If the process dies during the sleep, nothing turns the pump off. The run needs a duration the board enforces itself, or a watchdog that stops it without a refresh.
- real-by-default: `DEVICE_URL` falls back to the real board at 192.168.1.40 when `GREENHOUSE_URL` is unset. The default should be the simulator, and reaching the real board should take an explicit choice that the first line of output names.

The five tests pass because `FakeController` accepts every command and the tests assert what was sent. None of them observes the greenhouse. Suggested tests drive the simulator into each failure and assert the safe state.

5 actions: 1 holds, 4 broken, 0 skipped.

defect_id: trusts-the-ack
defect_id: retries-a-dispense
defect_id: fails-hot
defect_id: units-mismatch
defect_id: no-watchdog
defect_id: real-by-default
