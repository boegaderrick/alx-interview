#!/usr/bin/python3
"""This module contains a function that solves the lockbox challenge"""


def canUnlockAll(boxes):
    """
        This function checks to see if all the lockboxes in the passed
        parameter can be opened using keys contained in the lockboxes
    """
    keys = [False if i > 0 else True for i in range(len(boxes))]
    remaining = []

    for i in range(len(boxes)):
        if keys[i] is False:
            remaining.append(i)
            continue
        for key in boxes[i]:
            if key < len(keys):
                keys[key] = True

    for i in remaining:
        if keys[i] is False:
            return False
        for key in boxes[i]:
            if key < len(keys):
                keys[key] = True

    return True
