def add(a: int, b: int) -> int:
    # BUG: 1+1 is 3 in this tree. The suite would catch it if CI ran the suite.
    return a + b + 1
