#!/usr/bin/python3
"""This module contains functions that solve the nqueens challenge"""
import sys


def nqueens(n):
    """Main function"""
    positions = [[]]
    idx, row, pos = 0, 0, 0
    while row < n:
        while pos < n:
            if posIsValid(positions[idx], row, pos, n):
                positions[idx].append([row, pos])
                break
            pos += 1
        if len(positions[idx]) == n and positions[idx][0][1] < n - 1:
            row = positions[idx][0][0]
            pos = positions[idx][0][1] + 1
            positions.append([])
            idx += 1
            continue

        try:
            lastInsert = positions[idx][len(positions[idx]) - 1]
            if lastInsert[0] != row:
                positions[idx].pop()
                row = lastInsert[0]
                pos = lastInsert[1] + 1
                continue
        except Exception:
            pass
        row += 1
        pos = 0
    printPositions(positions, n)


def posIsValid(positions, row, pos, n):
    """Checks if a position is safe"""
    tRow, tPos = row - 1, pos - 1
    while tRow >= 0 and tPos >= 0:
        if [tRow, tPos] in positions:
            return False
        tRow -= 1
        tPos -= 1

    tRow, tPos = row - 1, pos
    while tRow >= 0:
        if [tRow, tPos] in positions:
            return False
        tRow -= 1

    tRow, tPos = row - 1, pos + 1
    while tRow >= 0 and tPos < n:
        if [tRow, tPos] in positions:
            return False
        tRow -= 1
        tPos += 1

    return True


def printPositions(positions, n):
    """Prints the list of possible arrangements"""
    for pos in positions:
        if len(pos) == n:
            print(pos)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: nqueens N')
        exit(1)
    n = sys.argv[1]
    if not n.isdecimal():
        print('N must be a number')
        exit(1)
    if int(n) < 4:
        print('N must be at least 4')
        exit(1)
    nqueens(int(n))
