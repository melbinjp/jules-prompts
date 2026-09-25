"""Asks the availability service which slots are free."""
import os

import requests

URL = os.environ.get("AVAILABILITY_URL", "http://localhost:8081")


def free_slots(machine, day):
    reply = requests.get(f"{URL}/free", params={"machine": machine, "day": day}, timeout=2)
    reply.raise_for_status()
    return reply.json()["free"]
