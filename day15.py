import heapq
import math
from collections import defaultdict
from typing import Dict, Tuple

from aocd import get_data, submit


def reconstruct_path(came_from, current):
    total_path = []
    while current != (0, 0):
        total_path.append(current)
        current = came_from[current]
    return total_path


# A* finds a path from start to goal.
# h is the heuristic function. h(n) estimates the cost to reach goal from node n.
def a_star(start, goal, h, data):
    # The set of discovered nodes that may need to be (re-)expanded.
    # Initially, only the start node is known.
    # This is usually implemented as a min-heap or priority queue rather than a hash-set.
    open_set = [start]
    heapq.heapify(open_set)

    # For node n, came_from[n] is the node immediately preceding it on the cheapest path from start
    # to n currently known.
    came_from = dict()

    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    g_score = defaultdict(lambda: 9999999)
    g_score[start] = 0

    # For node n, f_score[n] = gScore[n] + h(n). f_score[n] represents our current best guess as to
    # how short a path from start to finish can be if it goes through n.
    f_score = defaultdict(lambda: 9999999)
    f_score[start] = h(start)

    while open_set:
        # This operation can occur in O(1) time if open_set is a min-heap or a priority queue
        current = heapq.heappop(open_set)
        if current == goal:
            return reconstruct_path(came_from, current)

        neighbors = []
        x, y = current
        if (x + 1, y) in data:
            neighbors.append((x + 1, y))
        if (x - 1, y) in data:
            neighbors.append((x - 1, y))
        if (x, y + 1) in data:
            neighbors.append((x, y + 1))
        if (x, y - 1) in data:
            neighbors.append((x, y - 1))
        for neighbor in neighbors:
            # d(current,neighbor) is the weight of the edge from current to neighbor
            # tentative_g_score is the distance from start to the neighbor through current
            tentative_g_score = g_score[current] + data[neighbor]
            if tentative_g_score < g_score[neighbor]:
                # This path to neighbor is better than any previous one. Record it!
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h(current)
                if neighbor not in open_set:
                    heapq.heappush(open_set, neighbor)

    # Open set is empty but goal was never reached
    return False


def parse_data(data: str) -> Dict[Tuple[int, int], int]:
    lines = [[int(num) for num in list(line)] for line in data.splitlines()]
    res = dict()
    for y, line in enumerate(lines):
        for x, num in enumerate(line):
            res[(x, y)] = num

    return res


def part_a(data):
    data = parse_data(data)
    goal = max(data.keys(), key=lambda i: i[0] * i[1])
    result = a_star((0, 0), goal, lambda current: math.sqrt(
        (goal[0] - current[0]) ** 2 + (goal[1] - current[1]) ** 2), data)

    print(result)

    return sum([data[pos] for pos in result if result != (0, 0)])


def part_b(data):
    data = parse_data(data)
    goal = max(data.keys(), key=lambda i: i[0] * i[1])
    len_x = goal[0] + 1
    for i in range(1, 5):
        for x in range(len_x):
            for y in range(goal[1] + 1):
                next_pos = (x + (i * len_x), y)
                data[next_pos] = data[(x, y)] + i
                if data[next_pos] > 9:
                    data[next_pos] = data[next_pos] % 9

    goal = max(data.keys(), key=lambda i: i[0] * i[1])
    for i in range(1, 5):
        for x in range(goal[0] + 1):
            for y in range(goal[1] + 1):
                next_pos = (x, y + (i * (goal[1] + 1)))
                data[next_pos] = data[(x, y)] + i
                if data[next_pos] > 9:
                    data[next_pos] = data[next_pos] % 9

    goal = max(data.keys(), key=lambda i: i[0] * i[1])
    result = a_star((0, 0), goal, lambda current: math.sqrt(
        (goal[0] - current[0]) ** 2 + (goal[1] - current[1]) ** 2), data)

    print(result)

    return sum([data[pos] for pos in result if result != (0, 0)])


def main():
    data = get_data()
    example_data = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
    answer_a = part_a(example_data)
    print(answer_a)
    assert answer_a == 40

    submit(answer=part_a(data), part="a")

    example_b = part_b(example_data)
    print(example_b)
    assert example_b == 315
    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
