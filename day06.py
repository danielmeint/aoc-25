import operator
from functools import reduce

from utils import run_puzzle

EXAMPLE_DATA = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

OPS = {
    '+': operator.add,
    '*': operator.mul
}


def parse(data):
    return data


def parse_a(data):
    lines = [line.split() for line in data.splitlines() if line.strip()]
    operators = [OPS[o] for o in lines[-1]]
    transposed = [list(map(int, row)) for row in zip(*lines[:-1])]
    return transposed, operators


def parse_b(data):
    # the "separator" column is always that before an operator
    lines = [line for line in data.splitlines() if line.strip()]
    operator_line = lines[-1]
    operators = [OPS[o] for o in operator_line.split()]
    split_idx = [i for i in range(len(operator_line) - 1) if operator_line[i + 1] != ' ']

    split_lines = []
    for line in lines[:-1]:
        split_line = [line[:split_idx[0]]]
        for i in range(1, len(split_idx)):
            prev, cur = split_idx[i - 1], split_idx[i]
            split_line.append(line[prev + 1:cur])
        split_line.append(line[split_idx[-1] + 1:])
        split_lines.append(split_line)

    transposed = [list(row) for row in zip(*split_lines)]
    operands = [[int(''.join(t)) for t in zip(*task)] for task in transposed]

    return operands, operators


def part_a(raw_data):
    tasks, operators = parse_a(raw_data)
    assert len(tasks) == len(operators)
    return sum(reduce(op, t) for op, t in zip(operators, tasks))


def part_b(raw_data):
    tasks, operators = parse_b(raw_data)
    assert len(tasks) == len(operators)
    return sum(reduce(op, t) for op, t in zip(operators, tasks))


if __name__ == "__main__":
    run_puzzle(
        year=2025,
        day=6,
        parse=parse,
        part_a=part_a,
        part_b=part_b,
        example_data=EXAMPLE_DATA,
        expected_ans_a=4277556,  # 4405895212738
        expected_ans_b=3263827   # 7450962489289
    )
