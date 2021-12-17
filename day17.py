import re

from aocd import get_data, submit


def parse_data(data: str):
    m = re.match(r'target area: x=([-\d]+)\.\.([-\d]+), y=([-\d]+)..([-\d]+)', data)
    return (int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))


def ends_in_target(target, velocities):
    pos = [0, 0]

    y_max = 0

    while pos[0] < max(target[0]) and pos[1] > min(target[1]):
        pos[0] += velocities[0]
        pos[1] += velocities[1]
        y_max = max(pos[1], y_max)

        if target[0][0] <= pos[0] <= target[0][1] and target[1][0] <= pos[1] <= target[1][1]:
            return y_max

        if velocities[0] > 0:
            velocities[0] -= 1
        elif velocities[0] < 0:
            velocities[0] += 1
        velocities[1] -= 1

    return -1


def part_a(data):
    target = parse_data(data)
    y_max = (0, 0, 0)
    for x_vel in range(1, 500):
        for y_vel in range(-500, 500):
            result = ends_in_target(target, [x_vel, y_vel])
            if result > -1 and result > y_max[1]:
                y_max = (result, x_vel, y_vel)
    return y_max[0]


def part_b(data):
    target = parse_data(data)
    in_target = []
    for x_vel in range(1, 500):
        for y_vel in range(-500, 500):
            result = ends_in_target(target, [x_vel, y_vel])
            if result > -1:
                in_target.append([x_vel, y_vel])
    return len(in_target)


def main():
    data = get_data()

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
