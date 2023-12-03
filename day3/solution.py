import time
import re
import string
from itertools import combinations


def get_numbers(input):
    for i, line in enumerate(input):
        matches = re.finditer(r"\d+", line)
        for match in matches:
            yield (i, *match.span())


def get_neighbor_positions(input, i, start, end):
    first = start - 1 if start > 0 else start
    last = end
    for j in range(first, last + 1):
        if i > 0:
            yield (i - 1, j)
        if i < len(input) - 1:
            yield (i + 1, j)
    # FIXME: returns first/last element instead of neighbor if at boundary but good enough for this day
    yield (i, first)
    yield (i, last)


def get_neighbors(input, i, start, end):
    for pos in get_neighbor_positions(input, i, start, end):
        yield input[pos[0]][pos[1]]


def is_partnumber(input, pos):
    neighbors = list(get_neighbors(input, *pos))
    # print(f"number: {pos_to_num(input, pos)} neighbors: {neighbors}")
    symbols = string.punctuation.replace(".", "")
    for symbol in symbols:
        if symbol in neighbors:
            return True
    return False


def pos_to_num(input, pos):
    num = int(input[pos[0]][pos[1] : pos[2]])
    # print(num)
    return num


def get_partnumbers(input):
    for number_pos in get_numbers(input):
        if is_partnumber(input, number_pos):
            yield pos_to_num(input, number_pos)


def part1(input):
    return sum(get_partnumbers(input))


def part2(input):
    res = 0
    candidates = {}
    for number_pos in get_numbers(input):
        if "*" in get_neighbors(input, *number_pos):
            candidates[number_pos] = frozenset(
                get_neighbor_positions(input, *number_pos)
            )
    # not the most performant way but saves thinking :)
    for c1, c2 in combinations(candidates, 2):
        common_neighbor_positions = candidates[c1].intersection(candidates[c2])
        common_neighbors = [input[n[0]][n[1]] for n in common_neighbor_positions]
        if "*" in common_neighbors:
            res += pos_to_num(input, c1) * pos_to_num(input, c2)

    return res


def main():
    # with open("day3/test_input.txt") as f:
    with open("day3/input.txt") as f:
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
