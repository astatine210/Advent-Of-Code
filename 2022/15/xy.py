"""Coordinate pair wrapper class"""

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

    @property
    def manhattan(self):
        """Manhattan distance of this vector"""
        return abs(self.x) + abs(self.y)
