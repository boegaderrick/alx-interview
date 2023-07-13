#!/usr/bin/python3
"""This module contains solutions to the minimum operations challenge"""


def lFactor(n: int) -> int:
    """This function finds the largest factor of a number"""
    i: int = 2
    while True:
        if n % i == 0:
            return int(n / i)
        i += 1


def minOperations(n: int) -> int:
    """This function contains the logic to solve the challenge"""
    if n == 1:
        return 0
    f: int = lFactor(n)
    return int((n / f) + minOperations(f))
