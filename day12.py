from collections import defaultdict, Counter
from typing import List, Tuple, Dict, Set

from aocd import get_data, submit


def parse_data(data: str) -> Dict[str, Set[str]]:
    lines = data.splitlines()
    col = defaultdict(set)
    result = [line.split('-') for line in lines]
    for cave1, cave2 in result:
        col[cave1].add(cave2)
        col[cave2].add(cave1)
    return col


def part_a(data):
    d = parse_data(data)

    finished_paths = set()
    running_paths = set()

    for cave in d["start"]:
        running_paths.add("start," + cave)

    while running_paths:
        print(len(running_paths))
        next_paths = set(running_paths)
        print(running_paths)
        for path in next_paths:
            path_split = path.split(',')
            curr_cave = path_split[-1]
            for next_cave in d[curr_cave]:
                if next_cave == next_cave.lower() and next_cave in path_split:
                    continue
                next_path = f"{path},{next_cave}"
                if next_cave == "end":
                    finished_paths.add(next_path)
                    continue
                if next_path not in running_paths:
                    running_paths.add(next_path)
            running_paths.remove(path)

    return len(finished_paths)


def part_b(data):
    d = parse_data(data)

    finished_paths = set()
    running_paths = set()

    for cave in d["start"]:
        running_paths.add("start," + cave)

    while running_paths:
        next_paths = set(running_paths)
        for path in next_paths:
            path_split = path.split(',')
            curr_cave = path_split[-1]
            has_two_small = False
            counts = Counter(path_split)
            for cave, count in counts.items():
                if cave == cave.lower() and count == 2:
                    has_two_small = True
                    break
            for next_cave in d[curr_cave]:
                if (
                        next_cave == next_cave.lower() and next_cave in path_split and has_two_small) or next_cave == "start":
                    continue
                next_path = f"{path},{next_cave}"
                if next_cave == "end":
                    finished_paths.add(next_path)
                    continue
                if next_path not in running_paths:
                    running_paths.add(next_path)
            running_paths.remove(path)

    return len(finished_paths)


def main():
    data = get_data()
    answer_a = part_a(data)
    print(answer_a)
    submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    print(answer_b)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
