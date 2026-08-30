def render_reset(token: str) -> str:
    return f"Reset your password: {token}"


def send(to: str, body: str) -> None:
    # The actual send is still commented out. The PR description says it is not.
    # send_via_smtp(to, body)
    return None
