from unittest.mock import MagicMock, patch

import fetch


def test_fetch_user_happy_path():
    body = b'{"id": 7, "name": "ada"}'
    resp = MagicMock()
    resp.read.return_value = body
    resp.__enter__.return_value = resp
    resp.__exit__.return_value = False
    with patch("fetch.urlopen", return_value=resp):
        assert fetch.fetch_user("http://example")["name"] == "ada"
