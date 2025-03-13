def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    return list(set(nums1) & set(nums2))



print(intersection([4,9,5], [9,4,9,8,4]))