"""Advent of Code Day 4

URL: https://adventofcode.com/2022/day/4
"""

FILENAME = "input.txt"


def section_iterator():
    """Yield each elf pairing as four integers"""
    with open(FILENAME, "r", encoding="ASCII") as filehandle:
        for line in filehandle:
            yield tuple(map(int, line.replace(",", "-").split("-")))


def full_overlap(a, b, c, d):
    """Return True if the two elves' sections fully overlap"""
    return (a <= c and b >= d) or (c <= a and d >= b)


def any_overlap(a, b, c, d):
    """Return True if any of the elves' sections overlap"""
    return (c <= a <= d) or (c <= b <= d) or (a <= c <= b) or (a <= d <= b)


def main():
    """Run as script"""
    answer_1 = 0
    answer_2 = 0
    for sections in section_iterator():
        answer_1 += full_overlap(*sections)
        answer_2 += any_overlap(*sections)
    print("Answer to part 1:")
    print(answer_1)
    print("Answer to part 2:")
    print(answer_2)


if __name__ == "__main__":
    main()
