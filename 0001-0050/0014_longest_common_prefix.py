def longest_common_prefix(strs: list[str]) -> str:
    res = ""
    strs = sorted(strs)
    shortest_word = min(strs, key=len)
    first, last = strs[0], strs[-1]
    for i in range(len(shortest_word)):
        if first[i] != last[i]:
            return res
        res += (first[i])
    return res