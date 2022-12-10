"""Advent of Code Day 9

URL: https://adventofcode.com/2022/day/9
"""

FILENAME = "input.txt"


class XY:
    """Wrapper for (x, y) coordinate pair"""

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return XY(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return XY(self.x - other.x, self.y - other.y)

    def __iter__(self):
        yield self.x
        yield self.y


def instructions(filename: str) -> XY:
    """Yield instructions from file"""
    vectors = {c: XY(*v) for c, v in zip("LRUD", ((-1, 0), (1, 0), (0, 1), (0, -1)))}
    with open(filename, "r", encoding="ASCII") as filehandle:
        for line in filehandle:
            direction = vectors[line[0]]
            for _ in range(int(line[2:])):
                yield direction


def pull(d: XY) -> XY:
    """Return the vector to move a knot given the vector to the previous knot"""
    if abs(d.x) == 2:
        if abs(d.y) == 2:
            return XY(d.x // 2, d.y // 2)
        return XY(d.x // 2, d.y)
    if abs(d.y) == 2:
        return XY(d.x, d.y // 2)
    return XY()


def main():
    """Run as script"""
    rope = [XY() for _ in range(10)]

    second_positions = set()
    last_positions = set()

    for move in instructions(FILENAME):
        rope[0] += move
        for i, knot in enumerate(rope[1:], start=1):
            rope[i] += pull(rope[i - 1] - knot)

        second_positions.add(tuple(rope[1]))
        last_positions.add(tuple(rope[-1]))

    print("Answer to part 1:")
    print(len(second_positions))
    print("Answer to part 2:")
    print(len(last_positions))


if __name__ == "__main__":
    main()
