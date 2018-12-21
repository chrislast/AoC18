""" Advent of Code 2018
"""

from pathlib import Path
from utils import *
import re

###########################

PATH = Path(__file__)
DATA = "input" / PATH.with_suffix(".txt")
INPUT_TEXT = read(DATA)
SCAN = r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)"

##########################

def r(s, c=None):
    if c:
        x="(" + "|".join((chr(c)+chr(c+32))) + ")"
        s = re.sub(x,"",s)
    x="(" + "|".join([chr(65+z+32)+chr(65+z) for z in range(26)]) + ")"
    s = re.sub(x,"",s)
    x="(" + "|".join([chr(65+z)+chr(65+z+32) for z in range(26)]) + ")"
    s = re.sub(x,"",s)
    return s

def part1():
    """."""
    x = INPUT_TEXT[0][:]
    y = ""
    while True:
        y = r(x)
        if x == y:
            break
        x = y
    return len(y)

###########################

def part2():
    """."""
    results=list()
    for c in range(65,65+26):
        x = INPUT_TEXT[0][:]
        y = ""
        while True:
            y = r(x, c)
            if x == y:
                break
            x = y
        results.append(len(y))
    return min(results)

###########################

if __name__ == "__main__":
    print(
    f"""Output from {PATH} using {DATA}

    Part 1
    {part1()}

    Part 2
    {part2()}
    """)
