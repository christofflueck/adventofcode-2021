from aocd import get_data, submit


def part_a(data):
    return ''


def part_b(data):
    return ''

def main():
    data = get_data()

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()