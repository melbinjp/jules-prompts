"""Client for the greenhouse controller board, which speaks plain HTTP.

POST /<actuator> with a command, GET /<sensor> for a reading. Readings come back
as {"value": <number>, "at": <unix seconds>}.
"""
import json
import time
import urllib.request


class Reply:
    def __init__(self, status: int, body: dict):
        self.status = status
        self.body = body


class Controller:
    def __init__(self, url: str):
        self.url = url.rstrip("/")

    def send(self, actuator: str, command: str, timeout: float = 5) -> Reply:
        request = urllib.request.Request(
            f"{self.url}/{actuator}", data=command.encode(), method="POST"
        )
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return Reply(response.status, json.loads(response.read() or b"{}"))

    def read(self, sensor: str, timeout: float = 5) -> dict:
        with urllib.request.urlopen(f"{self.url}/{sensor}", timeout=timeout) as response:
            return json.loads(response.read())


def now() -> float:
    return time.time()
