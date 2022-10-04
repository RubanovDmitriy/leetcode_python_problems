import sys
from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    if len(nums) in [0, 1, 2]:
        return 0
    else:
        min_diff = sys.maxsize
        result = 0
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                curr_sum = sorted_nums[i] + sorted_nums[start] + sorted_nums[end]
                diff = abs(curr_sum - target)
                if diff == 0:
                    return curr_sum
                if diff < min_diff:
                    min_diff = diff
                    result = curr_sum
                if curr_sum <= target:
                    start += 1
                else:
                    end -= 1
        return result
