from utils import run_puzzle

EXAMPLE_DATA = """
987654321111111
811111111111119
234234234234278
818181911112111
"""


def parse(data):
    return [list(line) for line in data.splitlines() if line.strip()]

def part_a(batteries):
    def find_max(row) -> int:
        first_dig = max(row[:-1])
        first_idx = row.index(first_dig)

        scnd_dig = max(row[first_idx + 1:])
        return int(f'{first_dig}{scnd_dig}')

    return sum(find_max(row) for row in batteries)


def part_b(batteries):
    def find_max(row) -> int:
        def helper(row, remaining_digits):
            if remaining_digits == 0:
                return max(row)
            # need to leave some at the end
            cur_dig = max(row[:-remaining_digits])
            cur_idx = row.index(cur_dig)

            return cur_dig + helper(row[cur_idx+1:], remaining_digits-1)

        return int(helper(row, 11))

    return sum(find_max(row) for row in batteries)


if __name__ == "__main__":
    run_puzzle(
        year=2025,
        day=3,
        parse=parse,
        part_a=part_a,
        part_b=part_b,
        example_data=EXAMPLE_DATA,
        expected_ans_a=357,
        expected_ans_b=3121910778619 # real: 170371185255900
    )
