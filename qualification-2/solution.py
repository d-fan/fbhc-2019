#!/bin/python3

import fileinput
import functools

from typing import List

ALPHA = 'A'
BETA = 'B'
EMPTY = '.'


def solve(i, line):
    reachable = (line.count(BETA) >= 2 and line.count(EMPTY) >= 1) or (
        line.count(BETA) == 1 and line.count(EMPTY) == 1)
    if reachable:
        return "Case #%d: Y" % i
    else:
        return "Case #%d: N" % i


def solve_slow(i: int, line: str) -> str:
    def swap(current, i, j):
        l = list(current)
        temp = l[i]
        l[i] = l[j]
        l[j] = temp
        return "".join(l)

    def get_possible_moves(current: str) -> (List[str], bool):
        alpha_loc = current.find(ALPHA)
        if alpha_loc == len(current) - 1:
            return [], True
        ret = []
        empty_loc = current.find(EMPTY, alpha_loc+1)
        if empty_loc > alpha_loc + 1 and empty_loc != -1:
            ret.append(swap(current, empty_loc, alpha_loc))
        empty_loc = current.rfind(EMPTY, 0, alpha_loc)
        if empty_loc < alpha_loc - 1 and empty_loc != -1:
            ret.append(swap(current, empty_loc, alpha_loc))

        for i in range(len(current)):
            if current[i] != BETA:
                continue
            if i > 0 and current[i-1] == EMPTY:
                ret.append(swap(current, i, i-1))
            if i < len(current) - 1 and current[i+1] == EMPTY:
                ret.append(swap(current, i, i+1))
        return ret, False

    seen = set([line])
    stack = [line]
    while stack:
        current = stack.pop()
        # print("trying " + current)
        possible_moves, success = get_possible_moves(current)
        if success:
            return "Case #%d: Y" % i
        for move in possible_moves:
            # print("  next " + move)
            if move in seen:
                continue
            seen.add(move)
            stack.insert(0, move)
    return "Case #%d: N" % i


if __name__ == '__main__':
    # print(solve_slow(1, "A..BB..B"))
    for i, line in enumerate(fileinput.input()):
        if fileinput.isfirstline():
            continue
        print(solve(i, line))
