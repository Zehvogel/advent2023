import time
import re
from math import prod


colors = ["red", "green", "blue"]


def parse_line(line):
    results = {}
    for color in colors:
        results[color] = re.findall(r"(\d+) " + color, line)
    return results


def get_maxes(counts):
    maxes = {}
    for color in counts:
        maxes[color] = max((int(count) for count in counts[color]))
    return maxes


def part1(input):
    res = 0
    max_counts = {"red": 12, "green": 13, "blue": 14}
    for i, line in enumerate(input):
        counts = parse_line(line)
        maxes = get_maxes(counts)
        valid = True
        for color in maxes:
            if maxes[color] > max_counts[color]:
                valid = False
        if valid:
            res += i + 1

    return res


def part2(input):
    res = 0
    for i, line in enumerate(input):
        counts = parse_line(line)
        maxes = get_maxes(counts)
        power = prod(maxes.values())
        res += power

    return res


def main():
    # with open("day2/test_input.txt") as f:
    with open("day2/input.txt") as f:
        input = f.readlines()
        t0 = time.perf_counter_ns()
        print(f"solution for part 1 is: {part1(input)}")
        t1 = time.perf_counter_ns()
        print(f"part 1 took {t1-t0} ns")
        print(f"solution for part 2 is: {part2(input)}")
        t2 = time.perf_counter_ns()
        print(f"part 2 took {t2-t1} ns")


if __name__ == "__main__":
    main()
