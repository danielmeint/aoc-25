import os
from dotenv import load_dotenv
from aocd import submit
from aocd.models import Puzzle

load_dotenv()


def parse(data):
    lines = data.splitlines()
    return lines


def part_a(data):
    lines = parse(data)
    print(lines[0])
    return None


def part_b(data):
    lines = parse(data)
    return None


if __name__ == "__main__":
    year = 2025
    day = 1

    puzzle = Puzzle(year=year, day=day)
    print(f"--- Day {day}: {puzzle.title} ---")

    data = puzzle.input_data

    print("Part A:")
    ans_a = part_a(data)
    print(ans_a)
    # if ans_a:
    #     submit(ans_a, part="a", day=day, year=year)

    print("\nPart B:")
    ans_b = part_b(data)
    print(ans_b)
    # if ans_b:
    #     submit(ans_b, part="b", day=day, year=year)
