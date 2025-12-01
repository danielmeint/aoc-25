# Advent of Code 2025

My solutions for [Advent of Code 2025](https://adventofcode.com/2025).

## Setup

1. Install `uv` if you haven't already.
2. Clone this repository.
3. Install dependencies:
   ```bash
   uv sync
   ```

## Session Token

To fetch input data automatically, you need to find your session cookie from adventofcode.com.

1. Log in to [Advent of Code](https://adventofcode.com/).
2. Open Developer Tools (F12) -> Application -> Cookies.
3. Copy the value of the `session` cookie.
4. Create a file named `.env` (optional, `aocd` also looks in `~/.advent-of-code.session`) or export it:
   ```bash
   export AOC_SESSION=your_session_cookie_here
   ```
   Or simpler, just paste it into `~/.config/aocd/token` or `~/.advent-of-code.session`.

## Running

To run a specific day:

```bash
uv run day01.py
```

