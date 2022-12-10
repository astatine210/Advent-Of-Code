"""Advent of Code Day 10

URL: https://adventofcode.com/2022/day/10
"""

FILENAME = "input.txt"


def cycles(filename: str) -> tuple[int]:
    """Yield cycles from file"""
    count = 0
    register = 1
    with open(filename, "r", encoding="ASCII") as filehandle:
        for line in filehandle:
            count += 1
            yield (count, register)
            if line[0] == "a":
                count += 1
                yield (count, register)
                register += int(line[5:])


def main():
    """Run as script"""
    answer_1 = 0
    print("Answer to part 2:")
    for n, x in cycles(FILENAME):
        if ((n - 20) % 40) == 0:
            answer_1 += n * x

        column = (n - 1) % 40
        if column == 0:
            print()
        print('##' if abs(x - column) <= 1 else "  ", end="")
    print("\n")
    print(f"Answer to part 1: {answer_1}")


if __name__ == "__main__":
    main()
