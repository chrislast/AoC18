""" Advent of Code 2018
"""

from pathlib import Path

###########################

def read(fname):
    """."""
    with open(fname) as f:
        text = list(map(str.strip, f.readlines()))
    return text

PATH = Path(__file__)
DATA = "input" / PATH.with_suffix(".txt")
INPUT_TEXT = read(DATA)

##########################

def part1():
    """."""
    return sum(map(int, INPUT_TEXT))

###########################

def fn(x):
 s=set()
 tot=0
 while True:
  for _ in x:
   tot += _
   if tot in s:
    return tot
   s.add(tot)

def part2():
    """."""
    return fn(list(map(int, INPUT_TEXT)))

###########################

if __name__ == "__main__":
    print(
    f"""Output from {PATH} using {DATA}

    Part 1
    {part1()}

    Part 2
    {part2()}
    """)
