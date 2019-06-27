#!/bin/python3

import fileinput
from functools import reduce

from typing import List


class Impossible(Exception):
    pass

def update_ancestors(parent_indices, child, ancestor, seen=None):
    print(parent_indices, "|", child, "|", ancestor)
    if not seen:
        seen = set()
    if ancestor in seen:
        raise Impossible
    seen.add(child)
    if child == ancestor or parent_indices[child] == ancestor:
        return parent_indices
    if parent_indices[child]:
        parent_indices = update_ancestors(
            parent_indices, ancestor, parent_indices[child], seen)
    parent_indices[child] = ancestor
    return parent_indices


def solve(i: int, n: int, constraints: List[List[int]]) -> str:
    parent_indices = [None] * (n+1)
    for x, y, z in constraints:
        try:
            parent_indices = update_ancestors(parent_indices, x, z)
            parent_indices = update_ancestors(parent_indices, y, z)
        except Impossible:
            return "Case #%d: Impossible" % i
    # return str(parent_indices)
    return "Case #%d: " % i

if __name__ == '__main__':
    with fileinput.input() as f:
        T = int(f.readline().strip())
        for case_number in range(1, T+1):
            N, M = map(int, f.readline().strip().split(' '))
            constraints = []
            for _ in range(M):
                line = f.readline().strip().split(' ')
                constraints.append([int(v) for v in line])
            # solve(case_number, N, constraints)
            print(solve(case_number, N, constraints))


# class UnmergeableException(Exception):
#     pass

# class Tree(object):
#     @staticmethod
#     def merge(tree1: Tree, tree2: Tree) -> Tree:
#         intersection = tree1.contents & tree2.contents
#         if not intersection:
#             new = Tree()
#             new.parent = None
#             new.children = [tree1, tree2]
#             new.contents = tree1.contents | tree2.contents
#             return new
#         for elem of intersection:
            
#         pass

#     def __init__(self, child1=None, child2=None, value=None):
#         self.children = []
#         self.contents = set()
#         if value:
#             self.value = value
#             self.contents.add(value)
#         if child1 and child1 != value:
#             self.children.append(Tree(value=child1))
#             self.contents.add(child1)
#         if child2 and child2 != value:
#             self.children.append(Tree(value=child2))
#             self.contents.add(child2)

# def solve(i: int, constraints: List[List[int]]) -> str:
#     try:
#         solution = str(reduce(Tree.merge, [Tree(*c) for c in constraints]))
#         return "Case %d: %s" % (i, solution)
#     except UnmergeableException:
#         return "Case %d: Impossible" % i