"""Advent of Code Day 3

URL: https://adventofcode.com/2022/day/3
"""

from functools import reduce

FILENAME = "input.txt"

with open(FILENAME, "r", encoding="ASCII") as filehandle:
    rucksacks = tuple(map(str.strip, filehandle))


def rucksack_priorities():
    """Yield the priority of each rucksack"""
    for sack in rucksacks:
        middle = len(sack) // 2
        yield priority((set(sack[:middle]) & set(sack[middle:])).pop())


def grouped(seq, n=3):
    """Yield members of a sequence, grouped"""
    for i in range(0, len(seq), n):
        yield seq[i : i + n]


def elf_priorities():
    """Yield the priority of the one item a group of elves
    has in common"""
    for group in grouped(rucksacks):
        yield priority(reduce(set.__and__, map(set, group)).pop())


def priority(item):
    """Return the priority of an item"""
    return ord(item) - (96 if item >= "a" else 38)


def main():
    """Run as script"""
    print("Answer to part 1:")
    print(sum(rucksack_priorities()))
    print("Answer to part 2:")
    print(sum(elf_priorities()))


if __name__ == "__main__":
    main()
