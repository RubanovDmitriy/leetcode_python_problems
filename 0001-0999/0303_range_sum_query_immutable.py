class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def sum_range(self, left: int, right: int) -> int:
        return sum(self.nums[left: right + 1])
