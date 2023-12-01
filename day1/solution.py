import time

def parse_line(l):
    d_l = [d for d in l if d.isdigit()]
    return int(d_l[0] + d_l[-1]) #if len(d_l) >= 1 else 0

def part1(input):
    res = 0
    for l in input:
        res += parse_line(l)
    return res

def replace_first_found(l):
    word_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    words = {word:str(i+1) for i, word in enumerate(word_list)}
    lowest_idx = len(l)
    word = ""
    for w in words:
        idx = l.find(w)
        if idx >= 0 and idx < lowest_idx:
            lowest_idx = idx
            word = w
    return l.replace(word, word[0] + words[word] + word[-1]) if word != "" else l

def replace_all(l):
    while (new_l := replace_first_found(l)) != l:
        l = new_l
    return new_l

def part2(input):
    res = 0
    for l in input:
        print(l.strip())
        l = replace_all(l)
        print(l, parse_line(l))
        res += parse_line(l)
    return res

def main():
    with open("day1/input.txt") as f:
    # with open("day1/test_input.txt") as f:
    # with open("day1/test_input2.txt") as f:
        input =  f.readlines()
        t0 = time.perf_counter_ns()
        print(f"solution for part 1 is: {part1(input)}")
        t1 = time.perf_counter_ns()
        print(f"part 1 took {t1-t0} ns")
        print(f"solution for part 2 is: {part2(input)}")
        t2 = time.perf_counter_ns()
        print(f"part 2 took {t2-t1} ns")

if __name__ == "__main__":
    main()