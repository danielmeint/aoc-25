from utils import run_puzzle

EXAMPLE_DATA = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


def parse(data):
    return [list(row) for row in data.splitlines() if row.strip()]


NEIGHBOR_OFFSETS = [
    (dr, dc)
    for dr in (-1, 0, 1)
    for dc in (-1, 0, 1)
    if not (dr == 0 and dc == 0)
]

def part_a(grid):
    ROWS = len(grid)
    COLS = len(grid[0])

    def can_access(r, c):
        if grid[r][c] != '@':
            return False
        roll_count = 0
        for dr, dc in NEIGHBOR_OFFSETS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == '@':
                roll_count += 1
        return roll_count < 4

    return sum(can_access(r, c) for r in range(ROWS) for c in range(COLS))


def part_b(grid):
    ROWS = len(grid)
    COLS = len(grid[0])

    def can_access(r, c):
        if grid[r][c] != '@':
            return False
        roll_count = 0
        for dr, dc in NEIGHBOR_OFFSETS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] in ["@", "x"]:
                roll_count += 1
        accessible = roll_count < 4
        if accessible:
            grid[r][c] = "x"
        return accessible

    def clean_grid():
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "x":
                    grid[r][c] = "."

    res = 0
    while True:
        cur_res = sum(can_access(r, c) for r in range(ROWS) for c in range(COLS))
        res += cur_res
        clean_grid()
        if not cur_res:
            break
    return res


if __name__ == "__main__":
    run_puzzle(
        year=2025,
        day=4,
        parse=parse,
        part_a=part_a,
        part_b=part_b,
        example_data=EXAMPLE_DATA,
        expected_ans_a=13,
        expected_ans_b=43 # 9173
    )
