""" Advent of Code 2018
"""

import re

###########################

def read(fname):
    """."""
    text=""
    try:
        with open(fname) as f:
            text = list(map(str.strip, f.readlines()))
        print(f'INPUT_TEXT={text}'[:75] + '...]')
    except:
        pass
    return text

def sscanf(text, regex):
    _ = re.compile(regex)
    return _.match(text).groups()

