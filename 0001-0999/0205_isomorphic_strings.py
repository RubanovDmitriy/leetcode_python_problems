def is_iomorphic(s: str, t: str) -> bool:
    res = dict()
    for i in range(len(s)):
        print(res.items())
        if s[i] in res and res[s[i]] != t[i]:
            return False
        if s[i] in res and res[s[i]] == t[i]:
            continue
        if t[i] in res.values():
            return False
        res[s[i]] = t[i]
    return True


assert is_iomorphic('egg', 'add') is True
assert is_iomorphic('foo', 'bar') is False
assert is_iomorphic('badc', 'baba') is False
assert is_iomorphic('paper', 'title') is True