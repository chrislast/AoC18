""" Advent of Code 2018
"""

from pathlib import Path
from utils import *

###########################

PATH = Path(__file__)
DATA = "input" / PATH.with_suffix(".txt")
INPUT_TEXT = read(DATA)
SCAN = r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)"

##########################

def part1():
    """."""
    return

###########################

def part2():
    """."""
    return

###########################

if __name__ == "__main__":
    print(
    f"""Output from {PATH} using {DATA}

    Part 1
    {part1()}

    Part 2
    {part2()}
    """)
