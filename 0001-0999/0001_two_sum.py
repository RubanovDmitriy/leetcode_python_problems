# Brute force O(n^2)

def two_sum(nums: list[int], target: int):
    for x in range(len(nums)):
        for y in range(x, len(nums) - 1):
            res = nums[x] + nums[y+1]
            if res == target:
                return [x, y+1]


# With hash map O(n)

def two_sum_hash(nums: list[int], target: int):
    hash_map = {}
    for x in range(len(nums)):
        if target - nums[x] in hash_map:
            return [hash_map[target - nums[x]], x]
        hash_map[nums[x]] = x


"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""