#!/usr/bin/python3
"""This script parses logs and outputs metrics"""
import sys

if __name__ == '__main__':
    fileSize = 0
    codeCount = {}
    iteration = 0

    def printCodes():
        """This function handles the output"""
        print('File size: {}'.format(fileSize))
        for code, count in sorted(codeCount.items()):
            print('{}: {}'.format(code, count))

    while True:
        try:
            line = sys.stdin.readline()
            splitLine = line.split(' ')
            if len(splitLine) < 9:
                continue

            fileSize, code = fileSize + int(splitLine[-1]), splitLine[-2]
            if not code.isdecimal():
                continue

            codeCount[code] = codeCount[code] + 1 if codeCount.get(code) else 1
            iteration += 1
            if iteration == 10:
                printCodes()
                iteration = 0

        except KeyboardInterrupt as error:
            printCodes()
            raise error
            exit(1)
