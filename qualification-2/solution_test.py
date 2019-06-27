#!/bin/python3

import fileinput
import unittest
import random

from solution import solve, solve_slow  # pylint: disable=import-error

class TestSolution(unittest.TestCase):
    def _generate_case(self):
        beta_count = random.randint(0, 10)
        empty_count = random.randint(0, 10)
        tail = ['B'] * beta_count + ['.'] * empty_count
        random.shuffle(tail)
        line = "".join(['A'] + tail)
        return line, solve_slow(0, line)

    def setUp(self):
        inputs = list(fileinput.input("leapfrog_ch__sample_input.txt"))[1:]
        outputs = map(lambda s: s.strip(), list(fileinput.input("leapfrog_ch__sample_output.txt")))
        self.cases = zip(range(1, len(inputs)+1), inputs, outputs)

    def test_solution(self):
        for i, line, expected in self.cases:
            self.assertEqual(solve(i, line), expected, msg=("%s should be %s" % (line.strip(), expected[-1])))

    def test_generated(self):
        for _ in range(100):
            line, expected = self._generate_case()
            print("Testing %s -> %s" % (line, expected))
            self.assertEqual(solve(0, line), expected, msg=("%s should be %s" % (line.strip(), expected[-1])))


def generate_case():
    beta_count = random.randint(0, 10)
    empty_count = random.randint(0, 10)
    tail = ['B'] * beta_count + ['.'] * empty_count
    random.shuffle(tail)
    line = "".join(['A'] + tail)
    return line

if __name__ == '__main__':
    # unittest.main()

    for beta_count in range(10):
        for empty_count in range(10):
            line = "A" + "B" * beta_count + "." * empty_count
            # line = generate_case()
            print("Testing %s" % line)
            expected = solve_slow(0, line)
            actual = solve(0, line)
            if actual == expected:
                print("  %s -> %s: OK" % (line, expected))
            else:
                print("  %s -> %s: Got %s instead" % (line, expected, actual))