#!/usr/bin/python3
"""This module contains a function that rotates a 2d matrix"""


def rotate_2d_matrix(matrix):
    """Rotation logic"""
    n = len(matrix)
    diag = -1
    for i in range(n):
        diag += 1
        for j in range(n):
            if j <= diag:
                continue
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
        matrix[i].reverse()
