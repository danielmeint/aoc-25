from bisect import bisect

from utils import run_puzzle

EXAMPLE_DATA = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


def parse(data):
    ranges = []
    ids = []

    for line in data.split():
        if "-" in line:
            start, end = map(int, line.split("-"))
            ranges.append((start, end))
        else:
            ids.append(int(line))

    return ranges, ids


def merge_ranges(ranges):
    if not ranges:
        return []

    ranges = sorted(ranges)
    merged = [ranges[0]]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:  # overlap
            merged[-1] = (last_start, max(last_end, end))
        else:  # no overlap
            merged.append((start, end))

    return merged


def contains_id(merged_ranges, id_):
    idx = bisect(merged_ranges, id_, key=lambda r: r[0])
    if idx == 0:
        return False

    start, end = merged_ranges[idx - 1]
    return start <= id_ <= end


def part_a(parsed):
    ranges, ids = parsed
    merged = merge_ranges(ranges)
    return sum(contains_id(merged, id_) for id_ in ids)


def part_b(parsed):
    ranges, _ = parsed
    merged = merge_ranges(ranges)
    return sum((end - start + 1) for start, end in merged)


if __name__ == "__main__":
    run_puzzle(
        year=2025,
        day=5,
        parse=parse,
        part_a=part_a,
        part_b=part_b,
        example_data=EXAMPLE_DATA,
        expected_ans_a=3,   # 674
        expected_ans_b=-14  # 352509891817881
    )
