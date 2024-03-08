#!/usr/bin/python3
"""
a function def island_perimeter(grid):
that returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    grid is a list of list of integers:
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100
    """
    length = len(grid)
    breath = len(grid[0])
    perim = 0
    for x in range(length):
        for y in range(breath):
            if grid[x][y] == 1:
                perim += 4
                if (y < breath - 1 and grid[x][y + 1] == 1):
                    perim -= 2
                if (x < length - 1 and grid[x + 1][y] == 1):
                    perim -= 2
    return perim
