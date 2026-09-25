"""Availability microservice, with a Redis cache so it scales."""
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

import redis

import store

SLOTS = range(9, 21)
cache = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://localhost:6379/0"))
CACHE_SECONDS = 300


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        q = parse_qs(urlparse(self.path).query)
        machine, day = q["machine"][0], q["day"][0]
        key = f"free:{machine}:{day}"
        cached = cache.get(key)
        if cached is None:
            booked = store.booked_slots(store.connect(), machine, day)
            free = [s for s in SLOTS if s not in booked]
            cache.setex(key, CACHE_SECONDS, json.dumps(free))
        else:
            free = json.loads(cached)
        body = json.dumps({"free": free}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8081), Handler).serve_forever()
