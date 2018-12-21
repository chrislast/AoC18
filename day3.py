""" Advent of Code 2018
"""

from pathlib import Path
from utils import *
import numpy as np

###########################

PATH = Path(__file__)
DATA = "input" / PATH.with_suffix(".txt")
INPUT_TEXT = read(DATA)
SCAN = r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)"

##########################

b = np.zeros((1000,1000),int)


def claim(k, x, y, w, h):
    c = True
    for i in range(x,x+w):
        for j in range(y,y+h):
            if b[i][j]:
                if c:
                    c = False
                b[i][j] = -1
            else:
                b[i][j]=k

def check(k, x, y, w, h):
    for i in range(x,x+w):
        for j in range(y,y+h):
            if b[i][j] == -1:
                return -1
    return k

def part1():
    """."""
    for _ in INPUT_TEXT:
        i, x, y, w, h = sscanf(_, SCAN)
        claim(int(i),int(x),int(y),int(w),int(h))

    return len([1 for _ in range(1000) for __ in range(1000) if b[_][__]==-1])

###########################

def part2():
    """."""
    for _ in INPUT_TEXT:
        i, x, y, w, h = sscanf(_, SCAN)
        __ = check(int(i),int(x),int(y),int(w),int(h))
        if __ != -1:
            return __

###########################

if __name__ == "__main__":
    print(
    f"""Output from {PATH} using {DATA}

    Part 1
    {part1()}

    Part 2
    {part2()}
    """)
