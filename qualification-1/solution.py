#!/bin/python3

import fileinput
import functools

BETA = 'B'
EMPTY = '.'

def solve(line):
    reachable = line.count(BETA) >= line.count(EMPTY) and line.count(EMPTY) >= 1
    if reachable:
        return "Y"
    return "N"

if __name__ == '__main__':
    for i, line in enumerate(fileinput.input()):
        if fileinput.isfirstline():
            continue
        print("Case #%d: %s" % (i, solve(line)))