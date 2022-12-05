"""Advent of Code Day 5

URL: https://adventofcode.com/2022/day/5
"""

FILENAME = "input.txt"


class Stacks(list):
    """Stacks of crates"""

    def __init__(self, width=9, multiple_crates=False):
        """Instantiate some stacks of crates.
        If multiple_crates is true, the crates will be moved while
        retaining order. Otherwise they will be moved one by one."""
        for _ in range(width):
            self.append([])
        self.__crate_order = 1 if multiple_crates else -1

    def build(self, stack, crate):
        """Put a crate at the bottom of a stack, if it's not a space"""
        if crate != " ":
            self[stack].insert(0, crate)

    def move(self, n, start, end):
        """Move n crates from start stack to end stack"""
        self[end] += self[start][-n:][:: self.__crate_order]
        self[start] = self[start][:-n]

    def top_crates(self):
        """Return string the crates at the top of each stack as a string"""
        return "".join(stack[-1] for stack in self)


def read_instructions():
    """Create some crates, read the instructions and move crates"""
    stacks_1 = Stacks()
    stacks_2 = Stacks(multiple_crates=True)
    with open(FILENAME, "r", encoding="ASCII") as filehandle:
        for line in filehandle:
            if "[" not in line:
                break
            for stack, crate in enumerate(line[1:36:4]):
                stacks_1.build(stack, crate)
                stacks_2.build(stack, crate)
        next(filehandle)

        for line in filehandle:
            (n, start, end) = map(int, line[5:].replace("from", "to").split(" to "))
            stacks_1.move(n, start - 1, end - 1)
            stacks_2.move(n, start - 1, end - 1)

        return (
            stacks_1.top_crates(),
            stacks_2.top_crates(),
        )


def main():
    """Run as script"""
    answer_1, answer_2 = read_instructions()

    print("Answer to part 1:")
    print(answer_1)
    print("Answer to part 2:")
    print(answer_2)


if __name__ == "__main__":
    main()
