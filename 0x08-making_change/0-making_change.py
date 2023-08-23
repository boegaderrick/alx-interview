#!/usr/bin/python3
"""This module contains a function that solves the making change challenge"""


def makeChange(coins, total):
    """Solution logic"""
    coins.sort(reverse=True)
    numCoins = 0
    for coin in coins:
        if total <= 0:
            break
        numCoins += total // coin
        total %= coin

    return numCoins if numCoins and not total else -1
