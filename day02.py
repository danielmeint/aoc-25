from utils import run_puzzle

EXAMPLE_DATA = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


def parse(data):
    ranges = data.split(',')
    parsed = [tuple(map(int, part.split('-', 1))) for part in ranges]
    return parsed


def part_a(ranges):
    def is_invalid(n):
        s = str(n)
        half = len(s) // 2
        return len(s) % 2 == 0 and s[:half] == s[half:]

    return sum(x for start, end in ranges for x in range(start, end + 1) if is_invalid(x))


def part_b(ranges):
    def repeats(s, offset):
        if len(s) % offset:
            return False

        num_slices = len(s) // offset  # 9 // 3 == 3 slices of length 3

        return all(
            s[i] == s[i + (offset * m)]
            for i in range(offset)
            for m in range(1, num_slices)
        )

    def is_invalid(n):
        s = str(n)
        max_offset = len(s) // 2
        return any(repeats(s, offset) for offset in range(1, max_offset + 1))

    return sum(x for start, end in ranges for x in range(start, end + 1) if is_invalid(x))


if __name__ == "__main__":
    run_puzzle(
        year=2025,
        day=2,
        parse=parse,
        part_a=part_a,
        part_b=part_b,
        example_data=EXAMPLE_DATA,
        expected_ans_a=1227775554,
        expected_ans_b=4174379265  # real: 20077272987
    )
