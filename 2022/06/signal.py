"""Advent of Code Day 6

URL: https://adventofcode.com/2022/day/6
"""
from collections import deque
from types import SimpleNamespace

FILENAME = "input.txt"


def listen(stream, **lengths):
    """Listen to a stream and returns the position of unique
    sequences of specified lengths"""
    deques = []
    names = []
    found = []
    for name, length in lengths.items():
        deques.append(deque(maxlen=length))
        names.append(name)
        found.append(False)

    position = 0
    while not all(found):
        position += 1
        character = stream.read(1)
        for index, f in enumerate(found):
            if not f:
                d = deques[index]
                d.append(character)
                if len(set(d)) == d.maxlen:
                    found[index] = position

    return SimpleNamespace(**dict(zip(names, found)))


def main():
    """Run as script"""
    with open(FILENAME, "r", encoding="UTF8") as filehandle:
        answers = listen(filehandle, packet=4, message=14)

    print("Answer to part 1:")
    print(answers.packet)
    print("Answer to part 2:")
    print(answers.message)


if __name__ == "__main__":
    main()
