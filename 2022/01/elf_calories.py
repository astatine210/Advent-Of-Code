"""Advent of Code Day 1

URL: https://adventofcode.com/2022/day/1
"""


def elf_calories(filename):
    """Yield the total calorie value for each elf"""
    with open(filename, "r", encoding="ASCII") as filehandle:
        calories = 0
        for line in filehandle:
            if line == "\n":
                yield calories
                calories = 0
            else:
                calories += int(line)
        if calories:
            yield calories


def highest_n(iterable, n=3):
    """Return an n-tuple of the highest values in an iterable."""
    highest = sorted(next(iterable) for _ in range(n))
    for value in iterable:
        if value > highest[0]:
            highest[0] = value
            highest.sort()

    return tuple(highest)


def main():
    """Run as script"""
    most_calories = highest_n(elf_calories("input.txt"))
    print("Answer to part 1:")
    print(most_calories[-1])
    print("Answer to part 2:")
    print(sum(most_calories))


if __name__ == "__main__":
    main()
