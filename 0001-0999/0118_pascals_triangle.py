def generate(num_rows: int) -> list[list[int]]:
    res = []
    for x in range(num_rows):
        row_to_append = [0 for _ in range(x + 1)]
        row_to_append[0] = 1
        row_to_append[-1] = 1
        if len(row_to_append) > 2:
            for p in [_ for _ in range(1, len(row_to_append) - 1)]:
                row_to_append[p] = res[x-1][p] + res[x-1][p-1]
        res.append(row_to_append)

    return res


assert generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
assert generate(1) == [[1]]
