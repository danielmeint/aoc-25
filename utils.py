import sys

from aocd.models import Puzzle
from dotenv import load_dotenv

load_dotenv()


def run_puzzle(year, day, parse, part_a, part_b, example_data=None, expected_ans_a=None, expected_ans_b=None):
    # Initialize puzzle
    try:
        puzzle = Puzzle(year=year, day=day)
        title = puzzle.title
    except Exception:
        title = "Unknown (Session token might be missing)"

    print(f"--- Day {day}: {title} ---")

    # Determine mode (Real vs Example)
    mode = "example"
    if len(sys.argv) > 1 and sys.argv[1] == "real":
        mode = "real"

    if mode == "real":
        print("Using REAL input data")
        raw_data = puzzle.input_data
    else:
        print("Using EXAMPLE input data")
        if expected_ans_a is not None:
            print(f"Expected Answer A: {expected_ans_a}")
        if expected_ans_b is not None:
            print(f"Expected Answer B: {expected_ans_b}")
        raw_data = example_data.strip() if example_data else ""

    # Parse data
    data = parse(raw_data)

    # Run Part A
    print("\nPart A:")
    ans_a = part_a(data)
    print(f"Result: {ans_a}")

    if mode == "real" and ans_a is not None:
        # submit(ans_a, part="a", day=day, year=year)
        pass

    # Run Part B
    print("\nPart B:")
    ans_b = part_b(data)
    print(f"Result: {ans_b}")

    if mode == "real" and ans_b is not None:
        # submit(ans_b, part="b", day=day, year=year)
        pass
