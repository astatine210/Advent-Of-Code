"""Cave-handling objects and functions"""

from itertools import pairwise
from colorama import Fore, Back, Style


class XY:
    """Wrapper for (X, Y) coordinate pair"""

    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        return XY(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return XY(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __iter__(self):
        yield self.x
        yield self.y

    def __repr__(self):
        return f"<XY {tuple(self)}>"


TUMBLE = (XY(0, 1), XY(-1, 1), XY(1, 1))


class Cave:
    """A rock cave"""

    def __init__(self, filename):
        self.left = 0
        self.right = 700
        self.bottom = 200
        self._data = [bytearray(self.right - self.left + 1) for _ in range(self.bottom)]

        with open(filename, "r", encoding="ASCII") as filehandle:
            for line in filehandle:
                for start, end in pairwise(
                    XY(*map(int, pair.split(","))) for pair in line.split(" -> ")
                ):
                    self.draw_rock(start, end)

        self.floor = 0
        for y, line in enumerate(self._data):
            if any(line):
                self.floor = y + 2
        self.draw_rock(XY(self.left, self.floor), XY(self.right, self.floor))

    def draw_rock(self, start, end):
        """Draw solid rock in the cave from one coordinate to another"""
        d = end - start
        if d.x:
            d.x //= abs(d.x)
        if d.y:
            d.y //= abs(d.y)

        self[start] |= 1
        while start != end:
            start += d
            self[start] |= 1

    def trim(self):
        """Trim cave to section with sand"""
        left, right, bottom = self.right, self.left, 0
        for y, line in enumerate(self._data):
            for x, c in enumerate(line):
                if c > 1:
                    if x < left:
                        left = x
                    if x > right:
                        right = x
            if any(line):
                bottom = y
        self.left = left - 1
        self.right = right + 2
        self.bottom = bottom + 1
        self._data = [
            line[self.left : self.right] for line in self._data[: self.bottom]
        ]

    def drop_grain(self, start):
        """Return where a grain of sand stops when it's dropped into the cave"""
        grain = XY(start.x, start.y)
        while True:
            for d in TUMBLE:
                new_xy = grain + d
                if self[new_xy] == 0:
                    grain = new_xy
                    break
            else:
                self[grain] |= 2
                return grain

    def __getitem__(self, coord):
        return self._data[coord.y][coord.x - self.left]

    def __setitem__(self, coord, val):
        self._data[coord.y][coord.x - self.left] = val

    def __str__(self):
        s = ""
        for power in (100, 10, 1):
            s += "    "
            for x in range(self.left, self.right):
                s += str(int(x // power) % 10)
            s += "\n"

        for y, line in enumerate(self._data):
            s += Style.BRIGHT + f"{y:03} " + Style.RESET_ALL
            for c in line:
                if c == 1:
                    s += Fore.BLUE + Back.BLUE + Style.DIM
                    s += "▓"
                elif c > 1:
                    s += Fore.YELLOW
                    s += "o"
                else:
                    s += Style.DIM
                    s += "."
                s += Style.RESET_ALL
            s += "\n"
        return s
