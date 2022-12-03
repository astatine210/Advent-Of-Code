"""Advent of Code Day 2

URL: https://adventofcode.com/2022/day/2
"""


def games(filename):
    """Yield each line of the input, converted to integers.
    (A, B, C) and (X, Y, Z) are converted to (0, 1, 2)"""
    with open(filename, "r", encoding="ASCII") as filehandle:
        for line in filehandle:
            if line:
                yield (ord(line[0]) - 65, ord(line[2]) - 88)


def score(them, you):
    """Result of an RPS round where
    (Rock, Paper, Scissors) = (0, 1, 2)"""
    return you + (4, 7, 1)[you - them]


def score_with_guide(them, guide):
    """Result of an RPS round using
    (Rock, Paper, Scissors) = (0, 1, 2) and
    (Lose, Draw, Win) = (0, 1, 2)"""
    return score(them, (them + guide - 1) % 3)


def main():
    """Run as script"""
    rounds = tuple(games("input.txt"))
    print("Answer to part 1:")
    print(sum(score(*r) for r in rounds))
    print("Answer to part 2:")
    print(sum(score_with_guide(*r) for r in rounds))


if __name__ == "__main__":
    main()
