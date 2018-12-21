""" Advent of Code 2018
"""

from pathlib import Path
from collections import *

###########################

def read(fname):
    """."""
    with open(fname) as f:
        text = list(map(str.strip, f.readlines()))
    return text

PATH = Path(__file__)
DATA = "input" / PATH.with_suffix(".txt")
try:
    INPUT_TEXT = read(DATA)
    print(f'INPUT_TEXT={INPUT_TEXT}'[:75] + '...]')
except:
    pass

##########################

def part1():
    """."""
    acc2 = 0
    acc3 = 0
    for _ in INPUT_TEXT:
        __ = Counter(_)
        if 2 in __.values():
            acc2 += 1
        if 3 in __.values():
            acc3 += 1
    return acc2 * acc3

###########################

def ss(s1,s2):
    acc = ''
    for idx,c in enumerate(s1):
        if s2[idx] == c:
            acc += c
    return acc

def part2():
    """."""
    for _ in INPUT_TEXT:
        for __ in INPUT_TEXT:
            s = ss(_,__)
            if len(s) == 25:
                return s
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
