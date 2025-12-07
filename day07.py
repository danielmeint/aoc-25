import copy

from utils import run_puzzle

EXAMPLE_DATA = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""


def parse(data):
    return [list(line) for line in data.splitlines() if line.strip()]


def part_a(grid):
    grid = copy.deepcopy(grid)
    ROWS = len(grid)
    COLS = len(grid[0])
    res = 0

    for r in range(1, ROWS):
        for c in range(COLS):
            cur = grid[r][c]
            above = grid[r - 1][c]
            if cur == '.' and above in ['|', 'S']:
                grid[r][c] = '|'
            if cur == '^' and above in ['|', 'S']:
                res += 1
                grid[r][c - 1] = '|' # bounds check not necessary
                grid[r][c + 1] = '|'

    return res


def part_b(grid):
    ROWS = len(grid)

    memo = {}

    def helper(r, c):
        if r >= ROWS - 1:
            # last row
            return 1

        if (r, c) in memo:
            return memo[(r, c)]

        next_row_elem = grid[r + 1][c]
        if next_row_elem == '^':
            res = helper(r + 1, c - 1) + helper(r + 1, c + 1)
        else:
            res = helper(r + 1, c)
        memo[(r, c)] = res
        return res

    return helper(0, grid[0].index('S'))


if __name__ == "__main__":
    run_puzzle(
        year=2025,
        day=7,
        parse=parse,
        part_a=part_a,
        part_b=part_b,
        example_data=EXAMPLE_DATA,
        expected_ans_a=21,  # 1649
        expected_ans_b=40   # 16937871060075?
    )
