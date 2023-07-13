#!/usr/bin/python3
"""This module contains solutions to the minimum operations challenge"""


def lFactor(n):
    """This function finds the largest factor of a number"""
    i = 2
    while True:
        if n % i == 0:
            return int(n / i)
        i += 1


def minOperations(n):
    """This function contains the logic to solve the challenge"""
    if n < 2:
        return 0
    f = lFactor(n)
    return int((n / f) + minOperations(f))
