"""Advent of Code Day 7

URL: https://adventofcode.com/2022/day/7
"""

FILENAME = "input.txt"


def read_filesystem(stream):
    """Infers a file system structure from the input"""
    filesystem = {"/": 0}

    cwd = "/"
    for line in stream:
        if line.startswith("$ cd"):
            next_dir = line[5:-1]
            if next_dir == "..":
                cwd = cwd[: cwd.rfind("/")]
            elif next_dir == "/":
                cwd = ""
            else:
                cwd = cwd + "/" + next_dir
                if cwd not in filesystem:
                    filesystem[cwd + "/"] = 0
        elif "0" <= line[0] <= "9":
            size = int(line.split()[0])
            filesystem[cwd + "/"] += size
    return filesystem


def main():
    """Run as script"""

    with open(FILENAME, "r", encoding="UTF8") as filehandle:
        filesystem = read_filesystem(filehandle)

    def sizeof(path):
        """Return the total size of a directory at a given path"""
        total = filesystem[path]
        depth = path.count("/") + 1
        for p in filesystem:
            if p.count("/") == depth and p.startswith(path):
                total += sizeof(p)
        return total

    sizes = {
        p: sizeof(p)
        for p in sorted(filesystem, key=lambda f: f.count("/"), reverse=True)
    }

    answer_1 = sum(n for n in sizes.values() if n <= 100000)
    print("Answer to part 1:")
    print(answer_1)

    space = 70000000 - sizes["/"]
    clearance = 30000000 - space
    answer_2 = min(n for n in sizes.values() if n >= clearance)
    print("Answer to part 2:")
    print(answer_2)


if __name__ == "__main__":
    main()
