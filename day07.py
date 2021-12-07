from typing import List
import numpy as np

from aocd import get_data, submit


def parse_data(data: str) -> List[int]:
    return [int(x) for x in data.split(',')]


def part_a(data: str) -> int:
    pos = parse_data(data)
    median = int(np.median(pos))
    fuel = 0
    for x in pos:
        fuel += abs(x - median)
    return fuel


def triangular(num: int) -> int:
    return int((num * (num + 1)) / 2)


def part_b(data: str) -> int:
    pos = parse_data(data)
    min_fuel = 999999999999999
    for i in range(min(pos), max(pos)):
        fuel = 0
        for x in pos:
            fuel += triangular(abs(i - x))
        if fuel < min_fuel:
            min_fuel = fuel
    return min_fuel


def main():
    data = get_data()

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
