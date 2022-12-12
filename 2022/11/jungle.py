"""Monkeys in the jungle"""


class Monkeys(list):
    """A collection of annoying monkeys"""

    def __init__(self, filename, worse=False):
        self.divider = 1
        with open(filename, "r", encoding="ASCII") as filehandle:
            while True:
                lines = [filehandle.readline() for _ in range(7)]
                if lines[0] == "":
                    break
                self.append(Monkey(lines, worse))
                self.divider *= self[-1].divisor

    def iterate(self):
        """Iterate over all monkeys"""
        for m in self:
            for next_monkey, item in m.inspect():
                item %= self.divider
                self[next_monkey].append(item)

    @property
    def business(self):
        """Return monkey business"""
        a, b = sorted(m.inspections for m in self)[-2:]
        return a * b


class Monkey(list):
    """An annoying monkey"""

    def __init__(self, lines, worse=False) -> None:
        self.worse = worse
        for item in lines[1][18:].split(", "):
            self.append(int(item))

        self.operator = int.__mul__ if lines[2][23] == "*" else int.__add__
        self.operand = None if lines[2][25] == "o" else int(lines[2][24:])

        self.divisor = int(lines[3][21:])
        self.throw_to = (int(lines[4][29:]), int(lines[5][30:]))
        self.inspections = 0

    def inspect(self):
        """Inspect all items, yielding (next_monkey, next_worry)"""
        while self:
            item = self.pop(0)
            new_value = self.operator(item, self.operand if self.operand else item)
            if not self.worse:
                new_value //= 3
            next_monkey = self.throw_to[bool(new_value % self.divisor)]
            self.inspections += 1
            yield (next_monkey, new_value)
