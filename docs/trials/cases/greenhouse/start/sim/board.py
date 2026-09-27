#!/usr/bin/env python3
"""Simulated greenhouse sensor board (trial material; a simulator, not hardware).

    python sim/board.py status                 # every reading, and the pump
    python sim/board.py moisture <1-4>         # soil moisture, percent
    python sim/board.py temp                   # air temperature, degrees Celsius
    python sim/board.py pump on|off            # command the pump relay; prints ACK
    python sim/board.py flow                   # water flow meter, litres per minute

Or import it: read_moisture(ch), read_temp(), set_pump(on), read_flow().

State lives in sim/state.json, so it survives between processes. Faults are set in
sim/faults.json: {"offline": false, "unreadable": [channels], "pump_seized": false}.
An offline board raises ConnectionError; an unreadable channel raises IOError. A seized pump
still answers ACK to a command, but no water flows.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE = HERE / "state.json"
FAULTS = HERE / "faults.json"
DEFAULT_STATE = {"moisture": {"1": 42.0, "2": 35.5, "3": 28.0, "4": 51.0}, "temp_c": 24.5, "pump": False}


def _state():
    if STATE.exists():
        return json.loads(STATE.read_text())
    STATE.write_text(json.dumps(DEFAULT_STATE, indent=2))
    return dict(DEFAULT_STATE)


def _faults():
    return json.loads(FAULTS.read_text()) if FAULTS.exists() else {}


def _check(channel=None):
    f = _faults()
    if f.get("offline"):
        raise ConnectionError("board not responding")
    if channel is not None and int(channel) in f.get("unreadable", []):
        raise IOError(f"moisture channel {channel} unreadable")


def read_moisture(channel):
    _check(channel)
    return float(_state()["moisture"][str(int(channel))])


def read_temp():
    _check()
    return float(_state()["temp_c"])


def set_pump(on):
    _check()
    s = _state()
    s["pump"] = bool(on)
    STATE.write_text(json.dumps(s, indent=2))
    return "ACK"


def read_flow():
    _check()
    s = _state()
    return 0.0 if (not s["pump"] or _faults().get("pump_seized")) else 6.2


def main(argv):
    cmd = argv[1] if len(argv) > 1 else "status"
    if cmd == "status":
        s = _state()
        print(json.dumps({"moisture": s["moisture"], "temp_c": s["temp_c"], "pump_commanded": s["pump"],
                          "flow_l_min": read_flow()}, indent=2))
    elif cmd == "moisture":
        print(read_moisture(argv[2]))
    elif cmd == "temp":
        print(read_temp())
    elif cmd == "pump":
        print(set_pump(argv[2] == "on"))
    elif cmd == "flow":
        print(read_flow())
    else:
        print(__doc__)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
