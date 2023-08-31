#!/usr/bin/python3
"""This module contains a function that finds the perimeter of an island"""


def island_perimeter(grid):
    """Solution logic"""
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if j < 1 or grid[i][j - 1] == 0:
                    perimeter += 1
                if i < 1 or grid[i - 1][j] == 0:
                    perimeter += 1
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1

    return perimeter
