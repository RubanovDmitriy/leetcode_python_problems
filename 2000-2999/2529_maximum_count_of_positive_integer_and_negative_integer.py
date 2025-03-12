from bisect import bisect_left


def maximumCount(nums: list[int]) -> int:
    pos = [num for num in nums if num > 0]
    neg = [num for num in nums if num < 0]
    return max(len(pos), len(neg))

# On

def maximumCountlog(nums: list[int]) -> int:
    count_ones_or_more = len(nums) - bisect_left(nums, 1)
    count_negative = bisect_left(nums, 0)
    return max(count_ones_or_more, count_negative)

# O(log n)

