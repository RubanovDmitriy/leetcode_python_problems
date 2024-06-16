def contains_duplicate(nums: list[int]) -> bool:
    res = {}
    for i in nums:
        if i not in res:
            res[i] = 1
        else:
            return True
    return False


assert contains_duplicate([1,2,3,1]) is True
assert contains_duplicate([1,2,3,4]) is False
assert contains_duplicate([1,1,1,3,3,4,3,2,4,2]) is True
