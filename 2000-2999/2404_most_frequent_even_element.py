"""
    Input: nums = [0, 1, 2, 2, 4, 4, 1]
    Output: 2

    Input: nums = [4, 4, 4, 9, 2, 4]
    Output: 4

    Input: nums = [29, 47, 21, 41, 13, 37, 25, 7]
    Output: -1
"""


def most_frequent_even(nums: list[int]) -> int:
    table = dict()
    for i in nums:
        if i % 2:
            continue
        if i not in table:
            table[i] = 1
        else:
            table[i] += 1

    if not table:
        return -1

    maxa = max(table, key=table.get)
    z = [d for d in table.items() if d[1] == table[maxa]]
    x = [c[0] for c in z]
    return min(x)
