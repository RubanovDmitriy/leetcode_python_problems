def binary_search(col, target):
    left = 0
    right = len(col) - 1
    mid = (left + right) // 2
    while right >= left and col[mid] != target:
        a = col[mid]
        if target > col[mid]:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2

    return mid


assert binary_search([6, 17, 21, 27, 32, 35, 35, 36, 37, 48], 27) == 3
