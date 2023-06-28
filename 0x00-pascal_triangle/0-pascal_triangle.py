#!/usr/bin/python3
"""This script contains a function that creates the Pascal's triangle"""


def pascal_triangle(n):
    """Pascal's triangle function"""
    if n <= 0:
        return []

    lst = []
    for i in range(n):
        innerList = []
        if i == 0:
            innerList.append(1)
        else:
            for j in range(i + 1):
                lVal = 0 if j == 0 else lst[i - 1][j - 1]
                rVal = 0 if j >= len(lst[i - 1]) else lst[i - 1][j]
                innerList.append(lVal + rVal)
        lst.append(innerList)
    return lst
