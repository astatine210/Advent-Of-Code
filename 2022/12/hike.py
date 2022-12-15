"""Advent of Code Day 12

URL: https://adventofcode.com/2022/day/12
"""

FILENAME = "input.txt"


class Node:
    """A node"""

    def __init__(self, y_x, height, parent):
        self.y, self.x = y_x
        self.height = height
        self.parent = parent
        self.children = []

    def path_home(self):
        """Recursive parentage of node"""
        if self.parent:
            return ((self.y, self.x),) + self.parent.path_home()
        return ((self.y, self.x),)

    def __repr__(self):
        return str((self.y, self.x, chr(self.height)))


def get_grid(filename: str) -> tuple:
    """Return the map grid, and its end point and start point"""
    grid = []
    with open(filename, "rb") as filehandle:
        for y, line in enumerate(filehandle):
            grid.append(bytearray(line[:-1]))
            if (end := line.find(ord("E"))) >= 0:
                endpoint = (y, end)
                grid[y][end] = ord("z")
            if (end := line.find(ord("S"))) >= 0:
                startpoint = (y, end)
                grid[y][end] = ord("a")
        return grid, endpoint, startpoint


def neighbours(y, x, height, width):
    """Return the neighbours of a square in a grid"""
    if y > 0:
        yield (y - 1, x)
    if y < height - 1:
        yield (y + 1, x)
    if x > 0:
        yield (y, x - 1)
    if x < width - 1:
        yield (y, x + 1)


def path_to_endpoint(grid, endpoint, front):
    """Find the steps to reach an endpoint from a front of nodes,
    using day 12's rules of ascending"""
    dimensions = (len(grid), len(grid[0]))

    visited = [bytearray(dimensions[1]) for _ in range(dimensions[0])]
    for f in front:
        visited[f.y][f.x] = 1

    while front:
        new_front = []
        for f in front:
            height_limit = f.height + 2
            for y, x in neighbours(f.y, f.x, *dimensions):
                if grid[y][x] < height_limit and not visited[y][x]:
                    new_node = Node((y, x), grid[y][x], f)
                    f.children.append(new_node)
                    if (y, x) == endpoint:
                        return new_node.path_home()
                    new_front.append(new_node)
                    visited[y][x] = 1
        front = new_front
    return False


def main():
    """Run as script"""
    grid, endpoint, startpoint = get_grid(FILENAME)

    # Part one - start at startpoint
    front = [Node(startpoint, ord("a"), None)]
    first_path = path_to_endpoint(grid, endpoint, front)
    answer_1 = len(first_path) - 1

    # Part two - start at all elevation 'a' squares
    front = []
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == ord("a"):
                front.append(Node((y, x), ord("a"), None))

    scenic_route = path_to_endpoint(grid, endpoint, front)

    answer_2 = len(scenic_route) - 1

    print("Answer to part 1:")
    print(answer_1)
    print("Answer to part 2:")
    print(answer_2)


if __name__ == "__main__":
    main()
