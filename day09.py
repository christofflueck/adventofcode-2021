from typing import Dict, Tuple, List, Set

from aocd import get_data, submit


def parse_data(data: str) -> Dict[Tuple[int, int], int]:
    parsed_data = {}
    lines = [[int(num) for num in line] for line in data.split('\n')]
    for y, line in enumerate(lines):
        for x, num in enumerate(line):
            parsed_data[(x, y)] = num
    return parsed_data


def part_a(data):
    height_map = parse_data(data)
    low_points = []

    for point in height_map.keys():
        val = height_map[point]
        x = point[0]
        y = point[1]
        if (x, y - 1) in height_map and val >= height_map[x, y - 1]:
            continue
        if (x, y + 1) in height_map and val >= height_map[x, y + 1]:
            continue
        if (x - 1, y) in height_map and val >= height_map[x - 1, y]:
            continue
        if (x + 1, y) in height_map and val >= height_map[x + 1, y]:
            continue
        low_points.append((x, y))
    return sum([height_map[point] + 1 for point in low_points])


def is_valid_neighbor(height_map: Dict[Tuple[int, int], int], coords: Tuple[int, int], basins) -> bool:
    return coords in height_map and coords not in basins and height_map[coords] != 9


def get_neighbors(height_map: Dict[Tuple[int, int], int], coords: Tuple[int, int], basins) -> Set[Tuple[int, int]]:
    neighbors = set()
    x = coords[0]
    y = coords[1]

    if is_valid_neighbor(height_map, (x - 1, y), basins):
        neighbors.add((x - 1, y))
    if is_valid_neighbor(height_map, (x + 1, y), basins):
        neighbors.add((x + 1, y))
    if is_valid_neighbor(height_map, (x, y - 1), basins):
        neighbors.add((x, y - 1))
    if is_valid_neighbor(height_map, (x, y + 1), basins):
        neighbors.add((x, y + 1))

    return neighbors


def part_b(data) -> int:
    height_map = parse_data(data)
    basins: Set[Tuple[int, int]] = set()
    all_basin_sizes = []
    for point in height_map.keys():
        val = height_map[point]
        if val == 9 or point in basins:
            continue
        current_basin = 0
        neighbors = get_neighbors(height_map, point, basins)
        while neighbors:
            curr_neighbors = set(neighbors)
            for neighbor in curr_neighbors:
                neighbors.update(get_neighbors(height_map, neighbor, basins))
                neighbors.remove(neighbor)
                if neighbor not in basins:
                    basins.add(neighbor)
                    current_basin += 1
        all_basin_sizes.append(current_basin)
    all_basin_sizes = sorted(all_basin_sizes)
    return all_basin_sizes[-1] * all_basin_sizes[-2] * all_basin_sizes[-3]


def main():
    data = get_data()

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
