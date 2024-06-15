# Time O(n), Mem O(1)

def merge(nums1: list[int], m: int, nums2: list[int], n: int):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    last = m + n - 1

    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1

    while n > 0:
        nums1[last] = nums2[n - 1]
        n, last = n - 1, last - 1

res = merge([1,2,3,0,0,0], 3, [2,5,6], 3)
