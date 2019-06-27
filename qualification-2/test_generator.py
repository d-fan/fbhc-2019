#!/bin/python3

import fileinput
import functools

ALPHA = 'A'
BETA = 'B'
EMPTY = '.'

def solve(i, line):
    reachable = line.count(BETA) >= line.count(EMPTY) and line.count(EMPTY) >= 1
    if reachable:
        return "Case #%d: Y" % i
    else:
        return "Case #%d: N" % i

if __name__ == '__main__':
    for i, line in enumerate(fileinput.input()):
        if fileinput.isfirstline():
            continue
        print(solve(i, line))