from utils import run_puzzle

EXAMPLE_DATA = """
L68

L30

R48

L5

R60

L55

L1

L99

R14

L82
"""


def parse(data):
    lines = [line for line in data.splitlines() if line.strip()]
    return lines


def part_a(lines):
    cur = 50
    res = 0
    for l in lines:
        direction, step = l[0], int(l[1:])
        cur = (cur + step) if direction == 'R' else (cur - step)
        cur %= 100
        if cur == 0:
            res += 1
    return res


def part_b(lines):
    cur = 50
    res = 0
    for l in lines:
        direction, step = l[0], int(l[1:])
        prev = cur
        cur = (cur + step) if direction == 'R' else (cur - step)
        x = abs(cur // 100)
        if (cur > 0 and cur % 100 == 0) or (prev == 0 and cur < 0):
            x -= 1
        res += x
        cur %= 100
        if cur == 0:
            res += 1
    return res


if __name__ == "__main__":
    run_puzzle(
        year=2025,
        day=1,
        parse=parse,
        part_a=part_a,
        part_b=part_b,
        example_data=EXAMPLE_DATA,
        expected_ans_a=3,
        expected_ans_b=6
    )
