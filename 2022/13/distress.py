"""Advent of Code Day 13

URL: https://adventofcode.com/2022/day/13
"""

import json
from itertools import zip_longest

FILENAME = "input.txt"


def signals(filename):
    """Get signal pairs from file"""
    with open(filename, "r", encoding="ASCII") as filehandle:
        while True:
            try:
                left = json.loads(filehandle.readline())
            except json.JSONDecodeError:
                break
            right = json.loads(filehandle.readline())
            filehandle.readline()
            yield CL(left), CL(right)


class CL(list):
    """Custom sorting list"""

    def __lt__(self, b):
        for x, y in zip_longest(self, b, fillvalue=None):
            result = self._lessthan(x, y)
            if result is not None:
                return result
        return None

    def _lessthan(self, a, b):
        """Compares ints, lists and None"""
        try:
            if a < b:
                return True
            if a > b:
                return False
            if a == b:
                return None
        except TypeError:
            pass

        if a is None:
            return True
        if b is None:
            return False

        if isinstance(a, int):
            a = [a]
        if isinstance(b, int):
            b = [b]

        return CL(a) < CL(b)


def main():
    """Run as script"""
    all_signals = []
    answer_1 = 0

    for n, (left, right) in enumerate(signals(FILENAME), start=1):
        answer_1 += (left < right) * n
        all_signals += [left, right]

    divider_1 = CL([[2]])
    divider_2 = CL([[6]])
    all_signals += [divider_1, divider_2]

    all_signals.sort()
    a = all_signals.index(divider_1) + 1
    b = all_signals.index(divider_2) + 1
    answer_2 = a * b

    print("Answer to part 1:")
    print(answer_1)
    print("Answer to part 2:")
    print(answer_2)


if __name__ == "__main__":
    main()
