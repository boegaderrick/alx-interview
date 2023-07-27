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
        binary then returns the 8 least significant bits in
        string format.
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
    count = 0
    for i in range(len(binList)):
        j = 0
        if count > 0:
            if binList[i][:2] != '10':
                return False
            count -= 1
            continue
        while binList[i][j] != '0':
            count += 1
            if count > 4:
                return False
            j += 1
        count = count - 1 if count > 1 else count
    return True if count == 0 else False
