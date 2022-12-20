"""Advent of Code Day 15

URL: https://adventofcode.com/2022/day/1
"""
from types import SimpleNamespace
from xy import XY

FILENAME = "input.txt"


def readings(filename):
    """Read sensors and beacons from file"""
    with open(filename, "r", encoding="ASCII") as filehandle:
        for line in filehandle:
            s, b = (
                XY(*map(int, pair.split(", y=")))
                for pair in line[12:].split(": closest beacon is at x=")
            )
            yield SimpleNamespace(sensor=s, beacon=b, distance=(b - s).manhattan)


def eliminated_range(y, sensor):
    """Return the range on a y-axis where beacons cannot be"""
    dx = sensor.distance - abs(sensor.sensor.y - y)
    if dx < 0:
        return None
    return (sensor.sensor.x - dx, sensor.sensor.x + dx)


def merge_ranges(r):
    """Merge overlaps in a list of ranges"""
    r.sort()
    count = 1
    while count:
        count = 0
        for i in range(len(r) - 1):
            a, b = r[i], r[i + 1]
            if b[0] <= a[1]:
                r[i] = r[i + 1] = (a[0], max(a[1], b[1]))
                count += 1
        r = sorted(set(r))
    return r


def main():
    """Run as script"""
    answer_1 = 0
    answer_2 = 0

    sensors = tuple(readings(FILENAME))

    y = 2000000

    beacons = set((s.beacon.x, s.beacon.y) for s in sensors)

    eliminated = merge_ranges(
        list(
            filter(
                lambda n: n is not None,
                (eliminated_range(y, s) for s in sensors),
            )
        )
    )

    answer_1 = sum((b - a) + 1 for a, b in eliminated) - sum(b[1] == y for b in beacons)

    for y in range(4000000 + 1):
        eliminated = merge_ranges(
            list(
                filter(
                    lambda n: n is not None,
                    (eliminated_range(y, s) for s in sensors),
                )
            )
        )
        if (len(eliminated)) == 2:
            answer_2 = ((eliminated[0][1] + 1) * 4000000) + y
            break

    print("Answer to part 1:")
    print(answer_1)
    print("Answer to part 2:")
    print(answer_2)


if __name__ == "__main__":
    main()
