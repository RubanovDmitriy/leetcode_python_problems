def countNegatives(grid: list[list[int]]) -> int:
    neg = 0
    for row in grid:
        neg+= len([num for num in row if num < 0])
    return neg