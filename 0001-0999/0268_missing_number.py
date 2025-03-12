from functools import reduce
from operator import xor

# Bruteforce
def missingNumber(nums: list[int]) -> int:
    snums = sorted(nums)
    for x in range(len(snums) + 1):
        try:
            if x != snums[x]:
                return x
        except IndexError:
            return x


# Propper Solution
def missingNumber(nums):
    return reduce(xor, (i ^ v for i, v in enumerate(nums, 1)))
