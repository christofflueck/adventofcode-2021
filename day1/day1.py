from aocd import get_data, submit


def part_a(data):
    prev = 999999
    increases = 0

    for line in data.split('\n'):
        curr = int(line)
        if curr > prev:
            increases += 1
        prev = curr
    return increases


def part_b(data):
    sliding_increases = 0
    past = []

    for line in data.split('\n'):
        curr = int(line)
        if len(past) == 3:
            if sum(past) < (sum(past[1:]) + curr):
                sliding_increases += 1
            past = past[1:]
            past.append(curr)
        else:
            past.append(curr)
    return sliding_increases


def main():
    data = get_data()

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()

file = open('data.txt', 'r')

lines = file.readlines()
