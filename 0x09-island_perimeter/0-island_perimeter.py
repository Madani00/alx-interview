#!/usr/bin/python3
""" a module to calculate the land perimeter of an island """


def island_perimeter(grid):
    """ code logic """

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if grid[i - 1][j] == 0 or i == 0:
                    perimeter += 1
                if grid[i][j - 1] == 0 or j == 0:
                    perimeter += 1
                if grid[i][j + 1] == 0 or j == cols - 1:
                    perimeter += 1
                if grid[i + 1][j] == 0 or i == rows - 1:
                    perimeter += 1

    return perimeter
