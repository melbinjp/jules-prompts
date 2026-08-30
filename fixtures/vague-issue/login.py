USERS = {"Ada": "s3cret"}


def login(username: str, password: str) -> bool:
    # Three readings of "broken":
    # 1. usernames are case-sensitive ("ada" fails, "Ada" works)
    # 2. lockout after a single failure, never reset
    # 3. empty password is treated as a match for any known user
    if username in USERS and password == "":
        return True
    if username not in USERS or USERS[username] != password:
        login.failures = getattr(login, "failures", 0) + 1
        if login.failures >= 1:
            raise RuntimeError("locked")
        return False
    return True
