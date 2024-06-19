def str_str(haystack: str, needle: str) -> int:
    if needle == '':
        return 0

    for i in range(len(haystack) + 1 - len(needle)):
        if haystack[i: i + len(needle)] == needle:
            return i
    return -1

assert str_str('sadbutsad', 'sad') == 0
assert str_str('leetcode', 'leeto') == -1

