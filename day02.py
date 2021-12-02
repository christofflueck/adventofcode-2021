from aocd import get_data, submit


def part_a(data):
    lines = data.split('\n')
    print(len(lines))

    hori = 0
    depth = 0

    for line in lines:
        match line.split(" "):
            case ["forward", x]:
                hori += int(x)
            case ["down", x]:
                depth += int(x)
            case ["up", x]:
                depth -= int(x)
            case _:
                print(f"received unknown line {line}")

    return str(hori * depth)


def part_b(data):
    lines = data.split('\n')
    print(len(lines))

    aim = 0
    hori = 0
    depth = 0
    for line in lines:
        match line.split(" "):
            case ["forward", x]:
                hori += int(x)
                depth += (aim * int(x))
            case ["down", x]:
                aim += int(x)
            case ["up", x]:
                aim -= int(x)
            case _:
                print(f"received unknown line {line}")

    return str(hori * depth)


def main():
    data = get_data()

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
