#!/usr/bin/python3
"""This module contains functions that perform utf-8 validation"""


def validUTF8(data):
    """
        This function takes in the data to be analysed and calls
        helper functions that perform the validation.
    """
    binList = []
    for num in data:
        binList.append(getBin(num))
    return validate(binList)


def getBin(num):
    """
        This function takes in a decimal number, converts it to
        binary then returns it in string format.
    """
    binString = ''
    while num > 0 and len(binString) < 8:
        mod, num = num % 2, num // 2
        binString = str(mod) + binString
    if len(binString) < 8:
        for i in range(8 - len(binString)):
            binString = '0' + binString
    return binString


def validate(binList):
    """
        This function takes the list of numbers received by the
        calling function in string binary format and checks if
        each binary number of the sequence conforms to the utf-8
        encoding scheme
        If the sequence has valid utf-8 encoded bits True is
        returned, else False is.
    """
    stack = ''
    for i in range(len(binList)):
        j = 0
        if len(stack) > 0:
            if binList[i][:2] != '10':
                return False
            stack = stack[:-1]
            continue
        while binList[i][j] != '0':
            stack += '1'
            j += 1
    return True if len(stack) == 0 else False
