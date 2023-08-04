#!/usr/bin/python3
"""This module contains a function that solves the nqueens challenge"""
import sys


def nqueens(x):
    """
        Finds all possible safe queen positioning on an NxN
        chessboard using backtracking
    """
    if x == n:
        print(indices)
        return
    for i in range(n):
        if i in columns or x + i in diag1 or x - i in diag2:
            continue
        columns.add(i)
        diag1.add(x + i)
        diag2.add(x - i)
        indices.append([x, i])
        nqueens(x + 1)

        columns.remove(i)
        diag1.remove(x + i)
        diag2.remove(x - i)
        indices.remove([x, i])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: nqueens N')
        exit(1)
    if not sys.argv[1].isdecimal():
        print('N must be a number')
        exit(1)
    if int(sys.argv[1]) < 4:
        print('N must be at least 4')
        exit(1)
    n = int(sys.argv[1])
    columns = set()
    diag1 = set()
    diag2 = set()
    indices = []

    nqueens(0)
