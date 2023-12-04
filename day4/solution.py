import time


def get_numbers(input):
    for line in input:
        numbers = line.strip().split(":")[1].split("|")
        yield (numbers[0].split(), numbers[1].split())


def part1(input):
    score = 0
    for winning_numbers, numbers in get_numbers(input):
        winners = [n for n in numbers if n in winning_numbers]
        score += 2 ** (len(winners) - 1) if len(winners) > 0 else 0
    return score


def get_number_of_winners(input):
    for winning_numbers, numbers in get_numbers(input):
        winners = [n for n in numbers if n in winning_numbers]
        yield len(winners)


def part2(input):
    count = [1 for card in input]
    for card, n_winners in enumerate(get_number_of_winners(input)):
        for i in range(n_winners):
            count[card + i + 1] += count[card]
    return sum(count)


def main():
    # with open("day4/test_input.txt") as f:
    with open("day4/input.txt") as f:
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
