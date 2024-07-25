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

"""
another way to do it

def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]  # Start with the first row
    
    for i in range(1, n):
        row = [1]  # Start each row with a 1
        previous_row = triangle[-1]  # Get the last row
        
        # Generate the middle values of the row
        for j in range(1, len(previous_row)):
            row.append(previous_row[j - 1] + previous_row[j])
        
        row.append(1)  # End each row with a 1
        triangle.append(row)  # Add the new row to the triangle
    
    return triangle
"""
