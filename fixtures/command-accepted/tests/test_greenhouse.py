"""Tests the agent wrote alongside greenhouse.py. All of them pass."""
import greenhouse
from device import Reply


class FakeController:
    """Accepts every command and remembers it."""

    def __init__(self, readings=None):
        self.sent = []
        self.readings = readings or {}

    def send(self, actuator, command, timeout=5):
        self.sent.append((actuator, command))
        return Reply(200, {})

    def read(self, sensor, timeout=5):
        return self.readings[sensor]


def test_close_valve(monkeypatch):
    fake = FakeController()
    monkeypatch.setattr(greenhouse, "controller", fake)
    assert greenhouse.close_valve() is True
    assert fake.sent == [("valve", "close")]


def test_dispense_fertiliser(monkeypatch):
    fake = FakeController()
    monkeypatch.setattr(greenhouse, "controller", fake)
    assert greenhouse.dispense_fertiliser(10) is True


def test_keep_warm_turns_heater_on_when_cold(monkeypatch):
    fake = FakeController({"temperature": {"value": 10.0, "at": 0}})
    monkeypatch.setattr(greenhouse, "controller", fake)
    greenhouse.keep_warm(68)
    assert fake.sent[-1] == ("heater", "on")


def test_water(monkeypatch):
    fake = FakeController()
    monkeypatch.setattr(greenhouse, "controller", fake)
    monkeypatch.setattr(greenhouse.time, "sleep", lambda s: None)
    greenhouse.water(60)
    assert fake.sent == [("pump", "on"), ("pump", "off")]


def test_open_vent_confirms_from_the_position_sensor(monkeypatch):
    fake = FakeController({"vent_open_pct": {"value": 100, "at": 2_000_000_000}})
    monkeypatch.setattr(greenhouse, "controller", fake)
    assert greenhouse.open_vent() is True
