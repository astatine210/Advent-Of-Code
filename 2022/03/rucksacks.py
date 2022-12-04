"""Advent of Code Day 3

URL: https://adventofcode.com/2022/day/3

Refactored to work with a single pass of the data, and use as
little memory use as possible.
"""

from functools import reduce

FILENAME = "input.txt"


def rucksack_groups(group_size=3):
    """Yield groups of rucksacks"""
    with open(FILENAME, "r", encoding="ASCII") as filehandle:
        group = []
        while True:
            try:
                group.append(next(filehandle).strip())
            except StopIteration:
                break
            if len(group) == group_size:
                yield tuple(group)
                group = []


def priority(item):
    """Return the priority of an item.
    a-z maps to 1-26, A-Z maps to 27-52"""
    return ord(item) - (96 if item >= "a" else 38)


def rucksack_priority(sack):
    """Return the priority of a rucksack"""
    middle = len(sack) // 2
    return priority((set(sack[:middle]) & set(sack[middle:])).pop())


def group_priority(group):
    """Return the priority of the one item a group of elves
    has in common"""
    return priority(reduce(set.__and__, map(set, group)).pop())


def main():
    """Run as script"""
    answer_1 = 0
    answer_2 = 0
    for group in rucksack_groups():
        for rucksack in group:
            answer_1 += rucksack_priority(rucksack)
        answer_2 += group_priority(group)

    print("Answer to part 1:")
    print(answer_1)
    print("Answer to part 2:")
    print(answer_2)


if __name__ == "__main__":
    main()
