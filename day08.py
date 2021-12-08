from aocd import get_data, submit


def part_a(data: str):
    data = [line.split('|')[1] for line in data.split('\n')]
    output_lengths = [[len(c) for c in line.strip().split()] for line in data]
    return sum([line.count(2) + line.count(4) + line.count(3) + line.count(7) for line in output_lengths])


def part_b(data):
    inputs = parse_data(data, 0)
    outputs = parse_data(data, 1)

    for line, out in zip(inputs, outputs):
        segments = {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None,
                    "g": None}

        # find a with 7
        segments["a"] = diff_list(line[1], line[0])[0]

        one = line[0]
        three = None
        four = None
        six = None
        eight = line[-1]

        # find f and c with 6
        for num in line:
            if len(num) == 6:
                diff = diff_list(one, num)
                if len(diff) == 1:
                    six = num
                    segments["f"] = diff[0]
                    segments["c"] = diff_list(line[0], diff[0])[0]

        # find d with 3 and 4
        for num in line:
            if len(num) == 4:
                four = num
            if len(num) == 5:
                # If complete overlap top 1 so num == 3
                if len(diff_list(one, num)) == 0:
                    three = num

        for num in three:
            if num in four and num not in one:
                segments["d"] = num
                break

        for num in four:
            if num not in one and num != segments["d"]:
                segments["b"] = num
                break

        for num in three:
            if num not in [segments["a"], segments["c"], segments["d"], segments["f"]]:
                segments["g"] = num
                break

        for num in eight:
            if num not in segments.values():
                segments["e"] = num
                break
        print(segments)



    return ''


def diff_list(list1, list2):
    return list(set(list1) - set(list2))


def parse_data(data, index):
    return [[sorted(list(num)) for num in sorted(line.split('|')[index].strip().split(), key=len)] for line in
            data.split('\n')]


def main():
    data = get_data()

    answer_a = part_a(data)
    # submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    # submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
