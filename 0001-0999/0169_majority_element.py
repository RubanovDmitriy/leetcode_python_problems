def majority_element(nums: list[int]) -> int:
    table = dict()
    for i in nums:
        if i not in table:
            table[i] = 1
        else:
            table[i] += 1
    return max(table, key=table.get)


assert majority_element([3, 2, 3]) == 3
assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
