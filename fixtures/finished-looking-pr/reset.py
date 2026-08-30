import mailer


def request_reset(email: str) -> str:
    token = "tok_" + email
    body = mailer.render_reset(token)
    mailer.send(email, body)
    return token
