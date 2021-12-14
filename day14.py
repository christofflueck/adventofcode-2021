from collections import Counter, defaultdict
from typing import Tuple, List, Dict

from aocd import get_data, submit


def parse_data(data: str) -> Tuple[Dict[str, int], Dict[Tuple[str, str], str]]:
    raw_start, raw_rules = data.split('\n\n')
    rules = {}
    for line in raw_rules.splitlines():
        key, value = line.split(' -> ')
        key = list(key)
        rules[(key[0], key[1])] = value
    start = defaultdict(int)
    for i in range(len(raw_start) - 1):
        first, second = raw_start[i:i + 2]
        start[(first, second)] += 1
    return start, rules


def part_a(data):
    start, rules = parse_data(data)

    steps = 10

    return run_rules(rules, start, steps)


def run_rules(rules, start, steps):
    curr_data = start
    for step in range(steps):
        next_data = defaultdict(int)
        for key, amount in curr_data.items():
            if key in rules:
                next_data[(key[0], rules[key])] += amount
                next_data[(rules[key], key[1])] += amount
            else:
                next_data[key] += amount
        curr_data = next_data
    result = defaultdict(int)
    for key, amount in curr_data.items():
        result[key[0]] += amount
        result[key[1]] += amount

    # This is bad even for my standarts. But it works
    return round((max(result.values()) - min(result.values()) )/ 2)


def part_b(data):
    start, rules = parse_data(data)

    steps = 40
    return run_rules(rules, start, steps)


def main():
    data = get_data()
    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
