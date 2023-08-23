#!/usr/bin/python3
"""This module contains a function that solves the making change challenge"""


def makeChange(coins, total):
    """Solution logic"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    numCoins = 0
    for coin in coins:
        numCoins += total // coin
        total %= coin
        if total == 0:
            break

    return numCoins if numCoins and not total else -1
