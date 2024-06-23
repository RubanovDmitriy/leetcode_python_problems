import pytest


def search_insert(nums: list[int], target: int) -> int:
    first = 0
    last = len(nums) - 1

    while last >= first:
        mid = (first + last) // 2

        if nums[mid] == target:
            return mid

        if target > nums[mid]:
            first = mid + 1
        else:
            last = mid - 1

    return first


@pytest.mark.parametrize(
    "nums, target, result",
    [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
    ],
)
def test_search_insert(nums: list[int], target: int, result: int):
    assert search_insert(nums, target) == result
