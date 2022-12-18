"""Advent of Code Day 14

URL: https://adventofcode.com/2022/day/14
"""
import caves

FILENAME = "input.txt"


def main():
    """Run as script"""
    answer_1 = 0
    answer_2 = 0

    cave = caves.Cave(FILENAME)
    start = caves.XY(500, 0)

    count = 0
    while not answer_1:
        if cave.drop_grain(start).y == cave.floor - 1:
            answer_1 = count
        count += 1

    while not answer_2:
        count += 1
        if cave.drop_grain(start) == start:
            answer_2 = count

    cave.trim()
    print(cave)

    print("Answer to part 1:")
    print(answer_1)
    print("Answer to part 2:")
    print(answer_2)


if __name__ == "__main__":
    main()
