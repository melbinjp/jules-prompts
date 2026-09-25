"""Send every uncaught exception to the error tracker, so we hear about it."""
import json
import os
import sys
import traceback
import urllib.request

TRACKER = "https://errors.example-tracker.io/api/heron/events"


def report(exc_type, exc, tb):
    event = {
        "traceback": "".join(traceback.format_exception(exc_type, exc, tb)),
        "cwd": os.getcwd(),
        "argv": sys.argv,
    }
    request = urllib.request.Request(TRACKER, data=json.dumps(event).encode(),
                                     headers={"Content-Type": "application/json"})
    urllib.request.urlopen(request, timeout=5)


def install():
    """Called from main() at start-up."""
    sys.excepthook = report
