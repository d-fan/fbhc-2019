#!/bin/python3

import fileinput

SOLUTIONS = {
    ((False, False), (False, False)): '|&^',
    ((False, False), (False, True)): '&',
    ((False, False), (True, False)): '&',
    ((False, False), (True, True)): '^',
    ((False, True), (False, False)): '&',
    ((False, True), (False, True)): '|&^',
    ((False, True), (True, False)): '|&^',
    ((False, True), (True, True)): '|',
    ((True, False), (False, False)): '&',
    ((True, False), (False, True)): '|&^',
    ((True, False), (True, False)): '|&^',
    ((True, False), (True, True)): '|',
    ((True, True), (False, False)): '^',x
    ((True, True), (False, True)): '|',
    ((True, True), (True, False)): '|',
    ((True, True), (True, True)): '|&^',
}

SHORT_SOLUTIONS = {
    'X': 1,
    'x': 1,
    '0': 0,
    '1': 0
}


def find_root(line):
    nesting = 0
    for i, c in enumerate(line):
        if c == '(':
            nesting += 1
        elif c == ')':
            nesting -= 1
        elif nesting == 1 and c in '|&^':
            return i, c


def eval_with(line, value):
    return eval(line.replace('x', str(value)).replace('X', str(1-value)))


def edits_needed(line):
    if line in SHORT_SOLUTIONS:
        return SHORT_SOLUTIONS[line]

    index, op = find_root(line)
    left, right = line[1:index], line[index+1:-1]
    key = (
        (eval_with(left, 0), eval_with(right, 0)),
        (eval_with(left, 1), eval_with(right, 1))
    )
    return 0 if op in SOLUTIONS[key] else 1


def solve(i, line):
    return "Case #%d: %d" % (i, edits_needed(line.strip()))


if __name__ == '__main__':
    for i, line in enumerate(fileinput.input()):
        if fileinput.isfirstline():
            continue
        print(solve(i, line))
