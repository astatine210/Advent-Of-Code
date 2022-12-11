"""Advent of Code Day 10

URL: https://adventofcode.com/2022/day/10
"""

FILENAME = "input.txt"


def cycles(filename: str) -> tuple[int]:
    """Yield cycles from file"""
    register = 1
    with open(filename, "r", encoding="ASCII") as filehandle:
        for line in filehandle:
            yield register
            if line[0] == "a":
                yield register
                register += int(line[5:])


def main():
    """Run as script"""
    answer_1 = 0
    print("Answer to part 2:")
    for n, x in enumerate(cycles(FILENAME)):
        if (n - 19) % 40 == 0:
            answer_1 += (n + 1) * x

        column = n % 40
        if column == 0:
            print()
        print("##" if abs(x - column) <= 1 else "  ", end="")
    print("\n")
    print(f"Answer to part 1: {answer_1}")


if __name__ == "__main__":
    main()
