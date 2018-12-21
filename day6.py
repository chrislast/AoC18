""" Advent of Code 2018
"""

from pathlib import Path
from utils import *
import numpy as np

###########################

PATH = Path(__file__)
DATA = "input" / PATH.with_suffix(".txt")
INPUT_TEXT = read(DATA)
SCAN = r"(\d+), (\d+)"

INPUT = [tuple(map(int,sscanf(_,SCAN))) for _ in INPUT_TEXT]
print(INPUT)

MAP = np.zeros((400,400),int)

def closest(px, py):
    dist=dict()
    for i, (x, y) in enumerate(INPUT):
        dist[i] = max((px,x))-min((px,x)) + max((py,y))-min((py,y))
    return val

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
