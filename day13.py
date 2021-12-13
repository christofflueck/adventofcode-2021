import re
from typing import Set, Tuple, List

from aocd import get_data, submit


def parse_data(data: str) -> Tuple[Set[Tuple[int, int]], List[Tuple[str, int]]]:
    dots, folds = data.split('\n\n')
    dots = [line.split(',') for line in dots.splitlines()]
    dots = set([(int(line[0]), int(line[1])) for line in dots])
    folds = [re.search(r"fold along ([xy])=(\d+)", line).groups() for line in folds.splitlines()]
    folds = [(str(fold[0]), int(fold[1])) for fold in folds]
    return dots, folds


def part_a(data: str) -> int:
    dots, folds = parse_data(data)
    fold_once(dots, folds[0])
    return len(dots)


def fold_once(dots, fold):
    edge, pos = fold
    new_dots = set(dots)
    for dot in new_dots:
        dot_pos = 0 if edge == "x" else 1
        if dot[dot_pos] > pos:
            dots.remove(dot)
            list_dot = list(dot)
            list_dot[dot_pos] = pos - (list_dot[dot_pos] - pos)
            dots.add(tuple(list_dot))
        if dot[dot_pos] == pos:
            dots.remove(dot)


def part_b(data):
    dots, folds = parse_data(data)
    for fold in folds:
        fold_once(dots, fold)
    max_x = max(map(lambda dot: dot[0], dots))
    max_y = max(map(lambda dot: dot[1], dots))

    for y in range(max_y + 1):
        line = ''
        for x in range(max_x + 1):
            line += '#' if (x, y) in dots else '.'
        print(line)


def main():
    data = get_data()

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    part_b(data)
    # submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
