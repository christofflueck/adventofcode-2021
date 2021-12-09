from typing import Dict, Tuple, List

from aocd import get_data, submit


def parse_data(data: str) -> Tuple[Dict[Tuple[int, int], int], int, int]:
    parsed_data = {}
    lines = [[int(num) for num in line] for line in data.split('\n')]
    max_y = len(lines)
    max_x = len(lines[0])
    for y, line in enumerate(lines):
        for x, num in enumerate(line):
            parsed_data[(x, y)] = num
    return parsed_data, max_x, max_y


def part_a(data):
    height_map, max_x, max_y = parse_data(data)
    low_points = []

    for x in range(max_x):
        for y in range(max_y):
            val = height_map[x, y]
            if y > 0 and val >= height_map[x, y - 1]:
                continue
            if y < max_y - 1 and val >= height_map[x, y + 1]:
                continue
            if x > 0 and val >= height_map[x - 1, y]:
                continue
            if x < max_x - 1 and val >= height_map[x + 1, y]:
                continue
            low_points.append((x, y))
    return sum([height_map[point] + 1 for point in low_points])


def _get_neighbor(height_map: Dict[Tuple[int, int], int], coords: Tuple[int, int], neighbors: List[Tuple[int, int]], basins):
    if coords in height_map and coords not in basins and height_map[coords] != 9:
        neighbors.append(coords)


def get_neighbors(height_map: Dict[Tuple[int, int], int], coords: Tuple[int, int], basins) -> List[Tuple[int, int]]:
    neighbors = []
    x = coords[0]
    y = coords[1]
    _get_neighbor(height_map, (x - 1, y), neighbors, basins)
    _get_neighbor(height_map, (x + 1, y), neighbors, basins)
    _get_neighbor(height_map, (x, y - 1), neighbors, basins)
    _get_neighbor(height_map, (x, y + 1), neighbors, basins)

    return neighbors


def part_b(data) -> int:
    height_map, max_x, max_y = parse_data(data)
    basins: List[Tuple[int, int]] = []
    all_basin_sizes = []
    for x in range(max_x):
        for y in range(max_y):
            val = height_map[x, y]
            if val == 9 or (x, y) in basins:
                continue
            current_basin = 0
            neighbors = get_neighbors(height_map, (x, y), basins)
            while len(neighbors) > 0:
                curr_neighbors = neighbors
                for neighbor in curr_neighbors:
                    neighbors.extend(get_neighbors(height_map, neighbor, basins))
                    neighbors.remove(neighbor)
                    basins.append(neighbor)
                    current_basin += 1
            all_basin_sizes.append(current_basin)
    all_basin_sizes = sorted(all_basin_sizes)
    print(all_basin_sizes)
    print(all_basin_sizes[-1], all_basin_sizes[-2], all_basin_sizes[-3])
    return all_basin_sizes[-1] * all_basin_sizes[-2] * all_basin_sizes[-3]


def main():
    data = get_data()

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    # submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
