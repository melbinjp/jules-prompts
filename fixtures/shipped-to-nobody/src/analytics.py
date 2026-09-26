"""Usage events. Sent to the analytics service on every app start."""
import json
import urllib.request

ENDPOINT = "https://events.example-analytics.com/v1/track"


def app_started(device_id, latitude, longitude):
    body = json.dumps({"event": "app_started", "device": device_id,
                       "lat": latitude, "lon": longitude}).encode()
    urllib.request.urlopen(urllib.request.Request(ENDPOINT, data=body,
                                                  headers={"Content-Type": "application/json"}))
