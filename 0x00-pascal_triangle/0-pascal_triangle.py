#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.
    
    Parameters:
        n (int): Number of rows to generate.
        
    Returns:
        list of lists: Pascal's triangle represented as a list of lists of integers.
    """
    # Edge case: return an empty list if n is less than or equal to 0
    if n <= 0:
        return []
    
    # Initialize Pascal's triangle with the first row
    triangle = [[1]]
    
    # Generate subsequent rows
    for i in range(1, n):
        # Initialize the new row with the first element always being 1
        row = [1]
        # Calculate the elements in between based on the previous row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # Add the last element of the row, always being 1
        row.append(1)
        # Append the new row to the triangle
        triangle.append(row)
    
    return triangle
