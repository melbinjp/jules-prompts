"""Prices on disk: one JSON file."""
import json
from pathlib import Path

PATH = Path("prices.json")


def load():
    return json.loads(PATH.read_text()) if PATH.exists() else {}


def save(prices):
    PATH.write_text(json.dumps(prices, indent=2))
