def remove_element(nums: list[int], val: int) -> int:
    left, right = 0, len(nums) - 1
    while right >= left and nums:
        if nums[left] == val:
            nums.pop(left)
            right -= 1
            continue
        elif nums[left] != val:
            left += 1
            continue
        if nums[right] == val:
            nums.pop(right)
            right -= 2
            continue
        elif nums[right] != val:
            right -= 1
            continue
    return len(nums)


assert remove_element([3,2,2,3], 3) == 2
assert remove_element([0,1,2,2,3,0,4,2], 2) == 5
assert remove_element([2,2,2], 2) == 0
