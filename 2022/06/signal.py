"""Advent of Code Day 6

URL: https://adventofcode.com/2022/day/6
"""
from collections import deque
from types import SimpleNamespace

FILENAME = "input.txt"


def listen(stream, **lengths):
    """Return the position of unique sequences of
    specified lengths in a stream"""
    searches = {name: deque(maxlen=length) for name, length in lengths.items()}
    result = {name: None for name in lengths}

    position = 0
    while searches:
        position += 1
        character = stream.read(1)
        if not character:
            break
        for name, d in tuple(searches.items()):
            d.append(character)
            if len(set(d)) == d.maxlen:
                del searches[name]
                result[name] = position

    return SimpleNamespace(**result)


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
