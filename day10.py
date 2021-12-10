from typing import List

from aocd import get_data, submit

syntax = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}


def parse_data(data: str) -> List[List[str]]:
    return [list(line) for line in data.split('\n')]


def part_a(data: str) -> int:
    scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    lines = parse_data(data)
    total = 0
    for line in lines:
        stack = []
        for char in line:
            if char in syntax:
                stack.append(char)
            else:
                closing = stack.pop()
                if syntax[closing] != char:
                    total += scores[char]
                    break
    return total


def part_b(data: str) -> int:
    scores = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }
    lines = parse_data(data)
    totals = []
    for line in lines:
        stack = []
        is_valid = True
        for char in line:
            if char in syntax:
                stack.append(syntax[char])
            else:
                closing = stack.pop()
                if closing != char:
                    is_valid = False
                    break
        if not is_valid:
            continue
        score = 0

        for char in reversed(stack):
            score *= 5
            score += scores[char]

        totals.append(score)

    totals = sorted(totals)
    return totals[int(len(totals) / 2)]


def main():
    data = get_data()

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
