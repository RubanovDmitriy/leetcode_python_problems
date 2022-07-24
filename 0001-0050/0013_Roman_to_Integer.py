def romanToInt(s: str) -> int:
    result = 0
    d = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000,
    }
    for x in s:
        result += d.get(x)

    if 'IV' in s:
        result -= 2
    if 'IX' in s:
        result -= 2
    if 'XL' in s:
        result -= 20
    if 'XC' in s:
        result -= 20
    if 'CD' in s:
        result -= 200
    if 'CM' in s:
        result -= 200

    return result
