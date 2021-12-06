from aocd import get_data, submit


def parse_data(data):
    return [int(x) for x in data.split(',')]


def part_a(data):
    initial = parse_data(data)

    curr_gen = [x for x in initial]
    next_gen = []

    for _ in range(80):
        for day in curr_gen:
            if day == 0:
                next_gen.append(6)
                next_gen.append(8)
            else:
                next_gen.append(day - 1)
        curr_gen = next_gen
        next_gen = []

    return len(curr_gen)


def part_b(data):
    initial = parse_data(data)

    curr_gen = [0] * 9
    for x in initial:
        curr_gen[x] += 1

    next_gen = [0] * 9

    for day in range(256):
        for i, count in enumerate(curr_gen):
            if i == 0:
                next_gen[6] += count
                next_gen[8] += count
            else:
                next_gen[i - 1] += count
        curr_gen = next_gen
        next_gen = [0] * 9

    return sum(curr_gen)


def main():
    data = get_data()

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
