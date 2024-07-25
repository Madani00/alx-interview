#!/usr/bin/python3
"""
returns a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """pascal"""
    if n <= 0:
        return []

    result = [[1]]
    for row in range(1, n):
        newRow = result[row - 1].copy()
        newRow.append(1)
        for ele in range(0, len(result[row - 1])):
            if row - 1 >= 0 and ele - 1 >= 0:
                newRow[ele] = result[row - 1][ele - 1] + result[row - 1][ele]
        result.append(newRow)

    return result
