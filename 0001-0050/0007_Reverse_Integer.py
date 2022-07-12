import math


def reverse(x: int) -> int:
    min = -2147483648
    max = 2147483647

    result = 0

    while x:
        digit = int(math.fmod(x, 10))
        x = int(x / 10)

        if result > max // 10 or result == max // 10 and digit >= max % 10:
            return 0
        if result < min // 10 or result == min // 10 and digit <= min % 10:
            return 0

        result = result * 10 + digit

    return result
