# Brute force O(nlogn)

def sorted_squares_brute_force(nums: list[int]) -> list[int]:
    sqrt_nums = list(map(lambda m: m * m, nums))
    print(sqrt_nums)
    return sorted(sqrt_nums)


def sorted_squares_two_pointers(nums: list[int]) -> list[int]:
    result_list = []
    left, right = 0, len(nums) - 1
    while right >= left:
        if nums[left] ** 2 > nums[right] ** 2:
            result_list.append(nums[left] ** 2)
            left += 1
        else:
            result_list.append(nums[right] ** 2)
            right -= 1

    return result_list[::-1]
