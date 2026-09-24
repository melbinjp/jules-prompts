# Fixture: command-accepted

Skill: `act-on-the-physical-world`. Prompt: `task_act_on_the_physical_world`.

A greenhouse controller: a valve, a fertiliser doser, a heater, a pump and a
roof vent, driven over HTTP. Its tests all pass, because each one asserts what
the code sent to the board and none of them observes the greenhouse. Four of the
five actions have planted defects. `open_vent` is done right: it is the control,
and the pattern the others should follow.

Nothing here talks to real hardware. `device.py` would, if pointed at a board,
so do not run `greenhouse.py` with `GREENHOUSE_URL` set to one.

```bash
cd fixtures/command-accepted && python -m pytest tests -q
# 5 passed
python scripts/score_fixture.py fixtures/command-accepted --self-check
```
