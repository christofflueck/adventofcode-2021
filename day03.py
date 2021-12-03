from aocd import get_data, submit
import numpy as np


def part_a(data):
    lines = data.split('\n')
    numbers = [list(num) for num in lines]
    numbers = [[1 if digit == '1' else -1 for digit in number] for number in numbers]
    sums = np.ndarray.sum(np.array(numbers), axis=0)

    gamma = int(''.join(['1' if digit > 0 else '0' for digit in sums]), 2)
    epsilon = int(''.join(['1' if digit < 0 else '0' for digit in sums]), 2)

    return gamma * epsilon


def find_common_bit(neg_num: list[list[int]], index: int):
    return np.ndarray.sum(np.array(neg_num), axis=0)[index]


def filter_list_index(neg_num: list[list[int]], least: bool, index: int):
    bit = find_common_bit(neg_num, index)
    if least:  # c02: least common
        bit = 1 if bit < 0 else -1
    else:  # oxygen: most common
        bit = 1 if bit >= 0 else -1
    return list(filter(lambda num: num[index] == bit, neg_num))


def filter_list(neg_num: list[list[int]], least: bool):
    new_list = neg_num
    for i in range(0, len(neg_num[0])):
        new_list = filter_list_index(new_list, least, i)
        if len(new_list) == 1:
            return new_list[0]


def part_b(data):
    lines = data.split('\n')
    numbers = [list(num) for num in lines]
    numbers = [[int(digit) for digit in number] for number in numbers]
    negative_numbers = [[1 if digit == 1 else -1 for digit in number] for number in numbers]

    oxygen = filter_list(negative_numbers, False)
    oxygen = int(''.join(['1' if digit > 0 else '0' for digit in oxygen]), 2)

    c02 = filter_list(negative_numbers, True)
    c02 = int(''.join(['1' if digit > 0 else '0' for digit in c02]), 2)

    return oxygen * c02


def main():
    data = get_data()

    answer_a = part_a(data)
    print(answer_a)
    submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    print(answer_b)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
