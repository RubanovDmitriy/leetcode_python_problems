def is_happy(n: int) -> bool:
    while n != 1 and n != 4:
        _sum = 0
        while n:
            _sum += (n % 10) ** 2
            n //= 10
        n = _sum

    return n == 1


assert is_happy(19) is True
