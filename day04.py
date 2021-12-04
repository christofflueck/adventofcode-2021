from aocd import get_data, submit
import pandas as pd


def part_a(numbers, blocks):
    for drawn in numbers:
        for block in blocks:
            for row in block:
                for i in range(len(row)):
                    if row[i] == drawn:
                        row[i] = None
                        row_done = True
                        for j in range(len(row)):
                            if row[j] is not None:
                                row_done = False
                                break
                        if row_done:
                            total = 0
                            for row_2 in block:
                                for num in row_2:
                                    if num is not None:
                                        total += num
                            return total * drawn


def part_b(numbers, blocks):
    has_won = [False] * len(blocks)
    for drawn in numbers:
        print(pd.DataFrame(blocks[18]))
        for block_index, block in enumerate(blocks):
            if has_won[block_index]:
                continue
            for row in block:
                if has_won[block_index]:
                    break
                for i, num in enumerate(row):
                    if has_won[block_index]:
                        break
                    if num == drawn:
                        row[i] = None
                        row_done = True
                        for j in range(len(row)):
                            if row[j] is not None:
                                row_done = False
                                break
                        if row_done:
                            has_won[block_index] = True
                            if has_won.count(False) == 0:
                                print("Block", block_index, "was last to win, with number", drawn)
                                print(pd.DataFrame(block))
                                total = 0
                                for row_2 in block:
                                    for num_2 in row_2:
                                        if num_2 is not None:
                                            total += num_2
                                return total * drawn


def main():
    data = get_data()
    blocks, numbers = parse_data(data)
    print(pd.DataFrame(blocks[18]))
    answer_a = part_a(numbers, blocks)
    print(answer_a)
    # submit(answer=answer_a, part="a")
    blocks, numbers = parse_data(data)

    answer_b = part_b(numbers, blocks)
    print(answer_b)
    submit(answer=answer_b, part="b")


def parse_data(data):
    blocks = data.split('\n\n')
    numbers = [int(num) for num in blocks[0].split(',')]
    blocks = [block.split('\n') for block in blocks[1:]]
    blocks = [[row.split() for row in block] for block in blocks]
    blocks = [[[int(num) for num in row] for row in block] for block in blocks]
    return blocks, numbers


if __name__ == '__main__':
    main()
