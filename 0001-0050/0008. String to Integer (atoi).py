def myAtoi(s: str) -> int:
    MAX_INT = 2 ** 31 - 1
    MIN_INT = -2 ** 31

    increment = 0
    result = 0
    negative = 1

    while increment < len(s) and s[increment] == ' ':
        increment += 1

    if increment < len(s) and s[increment] == '-':
        increment += 1
        negative = -1
    elif increment < len(s) and s[increment] == '+':
        increment += 1

    checker = set('0123456789')
    while increment < len(s) and s[increment] in checker:
        result = result * 10 + int(s[increment])
        increment += 1

    result = result * negative
    if result < 0:
        return max(result, MIN_INT)
    return min(result, MAX_INT)
