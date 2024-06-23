def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    f = [0] + flowerbed + [0]
    for i in range(1, len(f) - 1):
        if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
            f[i] = 1
            n -= 1
    return n <= 0


assert can_place_flowers([1, 0, 0, 0, 1, 0, 0], 2) is True
assert can_place_flowers([1, 0, 0, 0, 1], 1) is True
assert can_place_flowers([1, 0, 0, 0, 1], 2) is False
assert can_place_flowers([1, 0, 0, 0, 0, 1], 2) is False
assert can_place_flowers([1, 0, 0, 0, 0, 0, 1], 2) is True
assert can_place_flowers([0, 0, 1, 0, 1], 1) is True
