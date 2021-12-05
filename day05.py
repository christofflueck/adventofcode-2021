from aocd import get_data, submit


def part_a(lines):
    grid, total = get_hor_and_vert_grid(lines)
    return total


def get_hor_and_vert_grid(lines):
    grid = []
    for i in range(1000):
        grid.append([0] * 1000)
    filtered_lines = [line for line in lines if line[0][0] == line[1][0] or line[0][1] == line[1][1]]
    total = 0
    for line in filtered_lines:
        x1 = min(line[0][0], line[1][0])
        x2 = max(line[0][0], line[1][0])
        xs = range(x1, x2 + 1)

        y1 = min(line[0][1], line[1][1])
        y2 = max(line[0][1], line[1][1])
        ys = range(y1, y2 + 1)

        for x in xs:
            for y in ys:
                grid[y][x] += 1
                if grid[y][x] == 2:
                    total += 1
    return grid, total


def part_b(lines):
    grid, total = get_hor_and_vert_grid(lines)

    diagonal_lines = [line for line in lines if abs(line[0][0] - line[1][0]) == abs(line[0][1] - line[1][1])]

    for line in diagonal_lines:
        x1 = line[0][0]
        x2 = line[1][0]
        y1 = line[0][1]
        y2 = line[1][1]
        dist = abs(x2 - x1)
        x_dir = 1 if x1 < x2 else -1
        y_dir = 1 if y1 < y2 else -1
        for i in range(dist + 1):
            y = y1 + i * y_dir
            x = x1 + i * x_dir
            grid[y][x] += 1
            if grid[y][x] == 2:
                total += 1

    return total


def main():
    data = get_data()

    lines = data.split('\n')
    lines = [line.split(' -> ') for line in lines]
    lines = [[pair.split(',') for pair in line] for line in lines]
    lines = [[[int(num) for num in pair] for pair in line] for line in lines]

    answer_a = part_a(lines)
    submit(answer=answer_a, part="a")

    answer_b = part_b(lines)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
