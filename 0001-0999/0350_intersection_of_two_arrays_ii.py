from collections import Counter

def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    counter = Counter(nums1)
    print(counter)
    res = []
    for num in nums2:
        if counter[num] > 0:
            res.append(num)
            counter[num] -= 1

    return res




print(intersection([4,9,5], [9,4,9,8,4]))