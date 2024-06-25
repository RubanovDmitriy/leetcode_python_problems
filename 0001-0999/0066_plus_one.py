def plus_one(digits: list[int]) -> list[int]:
    res = 0
    res_list = []
    zeroes = len(digits) - 1
    for i in digits:
        b = i * pow(10, zeroes)
        zeroes -= 1
        res += b

    res += 1

    while res:
        res_list.append(res % 10)
        res //= 10

    return res_list[::-1]


assert plus_one([1, 2, 3]) == [1, 2, 4]
assert plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]
assert plus_one([9]) == [1, 0]
