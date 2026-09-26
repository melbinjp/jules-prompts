import redis

from app.limits import allow

client = redis.Redis(host="localhost", port=6379)
client.ping()


def test_eleventh_request_in_a_minute_is_refused():
    for _ in range(10):
        assert allow(client, "user-1")
    assert not allow(client, "user-1")
