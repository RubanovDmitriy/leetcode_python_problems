def find_judge(n: int, trust: list[list[int]]) -> int:
    if len(trust) == n:
        return -1
    if len(trust) == 0 and n == 1:
        return 1
    trust_table = dict()
    for i in trust:
        if i[1] not in trust_table:
            trust_table[i[1]] = 1
        else:
            trust_table[i[1]] += 1

    print(trust_table)
    if len(trust_table) == n:
        return -1

    for key, val in trust_table.items():
        if val == n - 1:
            print(key)
            return key
    else:
        return -1



# find_judge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]])

assert find_judge(2, [[1, 2]]) == 2
assert find_judge(3, [[1, 3], [2, 3]]) == 3
assert find_judge(3, [[1, 3], [2, 3], [3, 1]]) == -1
assert find_judge(3, [[1, 2], [2, 3]]) == -1
assert find_judge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]) == 3
