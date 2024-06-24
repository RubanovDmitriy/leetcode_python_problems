def number_of_lines(widths: list[int], s: str) -> list[int]:
    mapa = {x[0]: x[1] for x in zip("abcdefghijklmnopqrstuvwxyz", widths)}
    lines = 1
    line_length = 0
    for i in s:
        if (line_length + mapa[i]) > 100:
            lines += 1
            line_length = 0
        line_length += mapa[i]

    return [lines, line_length]


assert number_of_lines(
    [
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
    ],
    "abcdefghijklmnopqrstuvwxyz",
) == [3, 60]

assert number_of_lines(
    [3, 4, 10, 4, 8, 7, 3, 3, 4, 9, 8, 2, 9, 6, 2, 8, 4, 9, 9, 10, 2, 4, 9, 10, 8, 2],
    "mqblbtpvicqhbrejb",
) == [1, 100]

assert number_of_lines(
    [
        4,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
    ],
    "bbbcccdddaaa",
) == [2, 4]
