"""Advent of Code Day 11

URL: https://adventofcode.com/2022/day/11
"""

from jungle import Monkeys

FILENAME = "test_input.txt"
FILENAME = "input.txt"


def main():
    """Run as script"""
    monkeys = Monkeys(FILENAME)
    for _ in range(20):
        monkeys.iterate()
    print(f"Answer to part 1: {monkeys.business}")

    monkeys = Monkeys(FILENAME, worse=True)
    for _ in range(10000):
        monkeys.iterate()
    print(f"Answer to part 2: {monkeys.business}")


if __name__ == "__main__":
    main()
