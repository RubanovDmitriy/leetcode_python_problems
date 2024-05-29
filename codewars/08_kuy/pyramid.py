def print_pyramid(n):
    if n == 0:
        return "\n"

    pyramid = ""
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        if i == n:
            pyramid += spaces + "/" + "_" * (2 * i - 2) + "\\" + "\n"
        else:
            pyramid += spaces + "/" + " " * (2 * i - 2) + "\\" + "\n"
    return pyramid
