#! /usr/bin/env python
# pm_constants.py

from __future__ import with_statement

# can be imported with from * if desired
TILE_VALUES = {
    'A' : 1,
    'B' : 3,
    'C' : 3,
    'D' : 2,
    'E' : 1,
    'F' : 4,
    'G' : 2,
    'H' : 4,
    'I' : 1,
    'J' : 8,
    'K' : 5,
    'L' : 1,
    'M' : 3,
    'N' : 1,
    'O' : 1,
    'P' : 3,
    'Q' : 10,
    'R' : 1,
    'S' : 1,
    'T' : 1,
    'U' : 1,
    'V' : 4,
    'W' : 4,
    'X' : 8,
    'Y' : 4,
    'Z' : 10,
    ' ' : 0,
}
BLANK = ' '
LETTERS = sorted(TILE_VALUES.keys())
LETTERS.remove(BLANK)

def _get_twl():
    """
    Get the Scrabble tournament word list
    (as a frozenset for performance reasons).
    """
    word_list = set()
    with open("TWL06.txt", "rU") as f:
        for line in f:
            word_list.add(line.strip().upper())
    return frozenset(word_list)

TWL = _get_twl()

SCRABBLE_BOARD = (
    ("TW", "", "", "DL", "", "", "", "TW", "", "", "", "DL", "", "", "TW"),
    ("", "DW", "", "", "", "TL", "", "", "", "TL", "", "", "", "DW", ""),
    ("", "", "DW", "", "", "", "DL", "", "DL", "", "", "", "DW", "", ""),
    ("DL", "", "", "DW", "", "", "", "DL", "", "", "", "DW", "", "", "DL"),
    ("", "", "", "", "DW", "", "", "", "", "", "DW", "", "", "", ""),
    ("", "TL", "", "", "", "TL", "", "", "", "TL", "", "", "", "TL", ""),
    ("", "", "DL", "", "", "", "DL", "", "DL", "", "", "", "DL", "", ""),
    ("TW", "", "", "DL", "", "", "", "S", "", "", "", "DL", "", "", "TW"),
    ("", "", "DL", "", "", "", "DL", "", "DL", "", "", "", "DL", "", ""),
    ("", "TL", "", "", "", "TL", "", "", "", "TL", "", "", "", "TL", ""),
    ("", "", "", "", "DW", "", "", "", "", "", "DW", "", "", "", ""),
    ("DL", "", "", "DW", "", "", "", "DL", "", "", "", "DW", "", "", "DL"),
    ("", "", "DW", "", "", "", "DL", "", "DL", "", "", "", "DW", "", ""),
    ("", "DW", "", "", "", "TL", "", "", "", "TL", "", "", "", "DW", ""),
    ("TW", "", "", "DL", "", "", "", "TW", "", "", "", "DL", "", "", "TW"),
)
