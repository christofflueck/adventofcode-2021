from aocd import get_data, submit


def part_a(data: str):
    data = [line.split('|')[1] for line in data.split('\n')]
    output_lengths = [[len(c) for c in line.strip().split()] for line in data]
    return sum([line.count(2) + line.count(4) + line.count(3) + line.count(7) for line in output_lengths])


def get_number(segment: dict, num: list[str]) -> int:
    print(segment, num)
    match ''.join(sorted([segment.get(d) for d in num])):
        case 'abcefg':
            return 0
        case 'cf':
            return 1
        case 'acdeg':
            return 2
        case 'acdfg':
            return 3
        case 'bcdf':
            return 4
        case 'abdfg':
            return 5
        case 'abdefg':
            return 6
        case 'acf':
            return 7
        case 'abcdefg':
            return 8
        case 'abcdfg':
            return 9
        case _:
            print(''.join(sorted([segment.get(d) for d in num])))


def part_b(data):
    inputs = parse_data(data, 0)
    outputs = parse_data(data, 1)
    total = 0
    for line, out in zip(inputs, outputs):
        segments = {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None,
                    "g": None}

        one = line[0]
        seven = line[1]
        three = None
        four = None
        six = None
        eight = line[-1]
        # a is in 7 but not in one
        segments["a"] = diff_list(seven, one)[0]

        print('Looking for 6 length that one - 6l == 1')
        # f is in 1 but not in 6
        # if f is known c is known by 1-f = c
        for num in line:
            if len(num) == 4:
                # find four
                four = num
            if len(num) == 5:
                # If complete overlap top 1 so num == 3
                if len(diff_list(one, num)) == 0:
                    three = num
            if len(num) == 6:
                diff = diff_list(one, num)
                if len(diff) == 1:
                    print('found 6')
                    six = num
                    segments["f"] = diff[0]
                    segments["c"] = diff_list(one, diff[0])[0]
                    break

        # d is in 4 and 3 but not in 1
        for num in three:
            if num in four and num not in one:
                segments["d"] = num
                break

        # b is in 4 but not in 3
        for num in four:
            if num not in three:
                segments["b"] = num
                break

        # g is in 3 but not in 7 or 4
        for num in three:
            if num not in seven and num not in four:
                segments["g"] = num
                break

        # e is the last one left
        for num in eight:
            if num not in segments.values():
                segments["e"] = num
                break

        for num in out:
            total += get_number(segments, num)

    return total


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
