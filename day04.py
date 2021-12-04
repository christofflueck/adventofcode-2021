from aocd import get_data, submit


def part_a(numbers, blocks):
    for drawn in numbers:
        for block in blocks:
            for row in block:
                for i, num in enumerate(row):
                    if num == drawn:
                        row[i] = None
                        if row.count(None) == len(row):
                            return get_total(block) * drawn
                        cols = zip(block)
                        for col in cols:
                            if col.count(None) == len(row):
                                return get_total(block) * drawn


def get_total(block):
    total = 0
    for row_2 in block:
        for num_2 in row_2:
            if num_2 is not None:
                total += num_2
    return total


def part_b(numbers, blocks):
    has_won = [False] * len(blocks)
    for drawn in numbers:
        for block_index, block in enumerate(blocks):
            if has_won[block_index]:
                continue
            for row in block:
                if has_won[block_index]:
                    break
                for i, num in enumerate(row):
                    if num == drawn:
                        row[i] = None
                        cols = list(zip(*block))
                        has_won_with_col = False
                        for col in cols:
                            if col.count(None) == len(row):
                                has_won_with_col = True
                                break
                        if row.count(None) == len(row) or has_won_with_col:
                            has_won[block_index] = True
                            if has_won.count(False) == 0:
                                total = 0
                                for row_2 in block:
                                    for num_2 in row_2:
                                        if num_2 is not None:
                                            total += num_2
                                return total * drawn


def main():
    data = get_data()
    blocks, numbers = parse_data(data)
    answer_a = part_a(numbers, blocks)
    submit(answer=answer_a, part="a")
    blocks, numbers = parse_data(data)

    answer_b = part_b(numbers, blocks)
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
