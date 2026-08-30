import reset


def test_template_contains_token():
    token = reset.request_reset("ada@example.com")
    assert token.startswith("tok_")
