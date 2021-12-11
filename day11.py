from typing import Dict, Tuple

from aocd import get_data, submit


def parse_data(data: str) -> Dict[Tuple[int, int], int]:
    lookups = dict()
    for y, line in enumerate(data.splitlines()):
        for x, num in enumerate(list(line)):
            lookups[(x, y)] = int(num)
    return lookups


def part_a(data: str) -> int:
    octos = parse_data(data)

    total = 0
    for i in range(100):
        to_flash = []
        for point in octos.keys():
            octos[point] += 1
            if octos[point] >= 10:
                octos[point] = 0
                to_flash.append(point)

        while to_flash:
            total += 1
            x, y = to_flash.pop()
            check_neighbor(octos, (x + 1, y), to_flash)
            check_neighbor(octos, (x + 1, y + 1), to_flash)
            check_neighbor(octos, (x + 1, y - 1), to_flash)
            check_neighbor(octos, (x - 1, y), to_flash)
            check_neighbor(octos, (x - 1, y + 1), to_flash)
            check_neighbor(octos, (x - 1, y - 1), to_flash)
            check_neighbor(octos, (x, y + 1), to_flash)
            check_neighbor(octos, (x, y - 1), to_flash)

    return total


def check_neighbor(octos, point, to_flash):
    if point in octos and octos[point] != 0:
        octos[point] += 1
        if octos[point] >= 10:
            octos[point] = 0
            to_flash.append(point)


def part_b(data):
    octos = parse_data(data)
    i = 0
    while True:
        to_flash = []
        for point in octos.keys():
            octos[point] += 1
            if octos[point] >= 10:
                octos[point] = 0
                to_flash.append(point)

        while to_flash:
            x, y = to_flash.pop()
            check_neighbor(octos, (x + 1, y), to_flash)
            check_neighbor(octos, (x + 1, y + 1), to_flash)
            check_neighbor(octos, (x + 1, y - 1), to_flash)
            check_neighbor(octos, (x - 1, y), to_flash)
            check_neighbor(octos, (x - 1, y + 1), to_flash)
            check_neighbor(octos, (x - 1, y - 1), to_flash)
            check_neighbor(octos, (x, y + 1), to_flash)
            check_neighbor(octos, (x, y - 1), to_flash)

        i += 1
        if len(octos) == list(octos.values()).count(0):
            return i


def main():
    data = get_data()

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
