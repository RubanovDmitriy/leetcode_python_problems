def climb_stairs(n: int) -> int:
    one, two = 1, 1
    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp

    return one


assert climb_stairs(2) == 2
assert climb_stairs(3) == 3
