#!/usr/bin/python3
"""This module contains functions that solve the prime game challenge"""


def isWinner(x, nums):
    """Solution logic"""
    """if type(nums) is not list:
        return None"""

    scores = {'Maria': 0, 'Ben': 0}
    players = ['Maria', 'Ben']

    for i in range(x):
        curr = [j for j in range(1, nums[i] + 1)]
        if len(curr) < 1:
            scores['Ben'] += 1
            continue
        gameIsOn = True
        while gameIsOn:
            for player in players:
                prime = findPrime(curr)
                if prime is None:
                    scores[player] -= 1
                    gameIsOn = False
                    break
                curr = [j for j in curr if j % prime != 0 and j != prime]

    return 'Maria' if scores['Maria'] > scores['Ben'] else 'Ben'


def findPrime(nums):
    """This function finds the smallet prime number in a list"""
    for num in nums:
        if num < 2:
            continue
        if num == 2:
            return num
        prime = num
        for i in range(num - 1, 1, -1):
            if num % i == 0:
                prime = None
        if prime is not None:
            return prime

    return None
