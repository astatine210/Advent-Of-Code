"""Advent of Code Day 7

URL: https://adventofcode.com/2022/day/7
"""

FILENAME = "input.txt"


def find_concealed(forest):
    """Find the number of concealed trees in a forest"""
    width = len(forest)  # Assume it's square

    concealed = tuple(bytearray(width) for _ in range(width))

    total_concealed = 0
    for a in range(width):
        # Tallest tree east, west, north or south of current position
        ewns = [0, 0, 0, 0]
        for b in range(width):
            c = -b - 1
            for i, (x, y) in enumerate(((a, b), (a, c), (b, a), (c, a))):
                tree_height = forest[x][y]
                max_height = ewns[i]
                if tree_height <= max_height:
                    concealed[x][y] += 1
                    if concealed[x][y] == 4:
                        total_concealed += 1
                elif tree_height > max_height:
                    ewns[i] = tree_height

    return total_concealed


def scenic_scores(forest):
    """Yield scenic scores for all trees not on the edge of the forest"""

    width = len(forest)
    for row in range(1, width - 1):
        for column in range(1, width - 1):
            height = forest[row][column]
            total_viewed = 1

            distance = 0
            for x in range(column - 1, -1, -1):
                distance += 1
                if forest[row][x] >= height:
                    break
            total_viewed *= distance

            distance = 0
            for y in range(row - 1, -1, -1):
                distance += 1
                if forest[y][column] >= height:
                    break
            total_viewed *= distance

            distance = 0
            for x in range(column + 1, width):
                distance += 1
                if forest[row][x] >= height:
                    break
            total_viewed *= distance

            distance = 0
            for y in range(row + 1, width):
                distance += 1
                if forest[y][column] >= height:
                    break
            total_viewed *= distance

            yield total_viewed


def main():
    """Run as script"""

    with open(FILENAME, "r", encoding="UTF8") as filehandle:
        forest = tuple(bytes(line.strip(), encoding="ASCII") for line in filehandle)

    answer_1 = len(forest) ** 2 - find_concealed(forest)
    answer_2 = max(scenic_scores(forest))

    print("Answer to part 1:")
    print(answer_1)
    print("Answer to part 2:")
    print(answer_2)


if __name__ == "__main__":
    main()
