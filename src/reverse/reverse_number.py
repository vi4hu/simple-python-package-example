def reverse_number(n: int) -> int:
    """A function to revers a integer.
    """
    r = 0
    while n > 0:
        r = r * 10 + n % 10
        n //= 10
    return r
