"""Monkeys in the jungle"""

from functools import reduce

DEBUG = False

ADD = 0
MULTIPLY = 1
SQUARE = 2


def debug(s):
    """Print debugging"""
    if DEBUG:
        print(s)


class Monkeys(list):
    """A collection of annoying monkeys"""

    def __init__(self, filename, worse=False):
        with open(filename, "r", encoding="ASCII") as filehandle:
            while True:
                lines = [filehandle.readline() for _ in range(7)]
                if lines[0] == "":
                    break
                self.append(Monkey(lines, worse))
        self.divider = reduce(int.__mul__, (m.divisor for m in self))

    def iterate(self):
        """Iterate over all monkeys"""
        for n, m in enumerate(self):
            debug(f"Monkey {n}:")
            for next_monkey, item in m.inspect():
                item %= self.divider
                self[next_monkey].append(item)
        debug(self.worry_levels())

    def __repr__(self):
        return "Monkeys:\n" + "\n".join(map(str, self))

    @property
    def business(self):
        """Return monkey business"""
        a, b = sorted(m.inspections for m in self)[-2:]
        return a * b

    def worry_levels(self):
        """Worry level dump for this iteration"""
        text = "Worry levels:\n"
        for n, m in enumerate(self):
            text += f"Monkey {n}: " + ", ".join(map(str, m)) + "\n"
        return text


class Monkey(list):
    """An annoying monkey"""

    def __init__(self, lines, worse=False) -> None:
        self.worse = worse
        for item in lines[1][18:].split(", "):
            self.append(int(item))

        self.operation_text = lines[2][19:].strip()
        self.operator = self._op(self.operation_text)
        self.divisor = int(lines[3][21:])
        self.throw_to = (int(lines[5][30:]), int(lines[4][29:]))
        self.inspections = 0

    def _op(self, op_text):
        if op_text[4] == "*":
            if op_text[6] == "o":
                return (SQUARE, None)
            return (MULTIPLY, int(op_text[6:]))
        return (ADD, int(op_text[6:]))

    def operate(self, n):
        """Perform this monkey's operation"""
        operator, operand = self.operator
        if operator == ADD:
            new_value = n + operand
            debug(f"    Worry level increases by {operand} to {new_value}")
        elif operator == MULTIPLY:
            new_value = n * operand
            debug(f"    Worry level is multiplied by {operand} to {new_value}")
        else:
            new_value = n * n
            debug(f"    Worry level is multipiled by itself to {new_value}")
        if not self.worse:
            new_value //= 3
            debug(
                f"    Monkey gets bored with item. Worry level is divided by 3 to {new_value}."
            )
        remainder = new_value % self.divisor
        return new_value, remainder

    def inspect(self):
        """Inspect all items, yielding (next_monkey, next_worry)"""
        while self:
            item = self.pop(0)
            debug(f"  Monkey inspects an item with a worry level of {item}.")
            new_value, remainder = self.operate(item)
            debug(
                "    Current worry level is"
                + (" not" if remainder else "")
                + f" divisible by {self.divisor}."
            )
            next_monkey = self.throw_to[not remainder]
            debug(
                f"    Item with worry level {new_value} is thrown to monkey {next_monkey}."
            )
            self.inspections += 1
            yield (next_monkey, new_value)

    def __repr__(self):
        return (
            f"<Monkey items:{list(self)}, "
            f"Divisor: {self.divisor}, "
            f"Throws to: {self.throw_to}, "
            f"Operation: {self.operation_text}, "
            f"Worse: {self.worse}>"
        )
