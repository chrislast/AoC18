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
START = re.compile(r'\[\d\d\d\d-\d\d-\d\d \d\d:\d\d\] Guard #(\d+) begins shift')
ASLEEP = re.compile(r'\[\d\d\d\d-\d\d-\d\d 00:(\d\d)\] falls asleep')  # [1518-06-22 00:26] falls asleep
AWAKE = re.compile(r'\[\d\d\d\d-\d\d-\d\d 00:(\d\d)\] wakes up')  # [1518-06-22 00:34] wakes up

##########################


def part1():
    """."""
    d = dict()
    asleep = 0
    awake = 0
    guard = None
    for _ in sorted(INPUT_TEXT):
        if START.match(_):
            if asleep > awake:
                for m in range(asleep, 60):
                    d[guard][m] += 1
            awake = 0
            guard = START.match(_).groups()[0]
            if guard not in d:
                d[guard] = [0] * 60
        if ASLEEP.match(_):
            asleep = int(ASLEEP.match(_).groups()[0])
        if AWAKE.match(_):
            awake = int(AWAKE.match(_).groups()[0])
            for m in range(asleep, awake):
                d[guard][m] += 1

    d_sleptfor = dict()
    for _ in d:
        guard = _
        sleptfor = sum(d[_])
        mostfrequentcount = max(d[_])
        mostfrequentmin = d[_].index(mostfrequentcount)
        cksum = mostfrequentmin * int(guard)
        d_sleptfor[sleptfor] = guard, mostfrequentmin, cksum

    sleepy = d_sleptfor[max(d_sleptfor)]

    return sleepy[2]

###########################

def part2():
    """."""
    d = dict()
    asleep = 0
    awake = 0
    guard = None
    for _ in sorted(INPUT_TEXT):
        if START.match(_):
            if asleep > awake:
                for m in range(asleep, 60):
                    d[guard][m] += 1
            awake = 0
            guard = START.match(_).groups()[0]
            if guard not in d:
                d[guard] = [0] * 60
        if ASLEEP.match(_):
            asleep = int(ASLEEP.match(_).groups()[0])
        if AWAKE.match(_):
            awake = int(AWAKE.match(_).groups()[0])
            for m in range(asleep, awake):
                d[guard][m] += 1

    d_sleptfor = dict()
    for _ in d:
        guard = _
        sleptfor = sum(d[_])
        mostfrequentcount = max(d[_])
        mostfrequentmin = d[_].index(mostfrequentcount)
        cksum = mostfrequentmin * int(guard)
        d_sleptfor[mostfrequentcount] = guard, mostfrequentmin, cksum

    sleepy = d_sleptfor[max(d_sleptfor)]

    return sleepy[2]

###########################

if __name__ == "__main__":
    print(
    f"""Output from {PATH} using {DATA}

    Part 1
    {part1()}

    Part 2
    {part2()}
    """)
