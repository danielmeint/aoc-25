from utils import run_puzzle

EXAMPLE_DATA = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""


def parse(data):
    return [tuple(map(int, line.split(','))) for line in data.splitlines() if line.strip()]


def get_size(p1, p2):
    return (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)


def part_a(points):
    n = len(points)
    return max(get_size(points[i], points[j]) for i in range(n) for j in range(i + 1, n))


def part_b(points):
    # todo: needs ray casting to check if rect center is inside polygon
    pass


if __name__ == "__main__":
    run_puzzle(
        year=2025,
        day=9,
        parse=parse,
        part_a=part_a,
        part_b=part_b,
        example_data=EXAMPLE_DATA,
        expected_ans_a=50,  # 4735222687
        expected_ans_b=24   # ???
    )
