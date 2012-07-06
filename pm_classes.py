#! /usr/bin/env python
# pm_classes.py

import pm_constants as constants

class Board(object):
    """Class representing the Scrabble board."""
    
    def __init__(self):
        self.grid = [
            ["TW", "", "", "DL", "", "", "", "TW", "", "", "", "DL", "", "", "TW"],
            ["", "DW", "", "", "", "TL", "", "", "", "TL", "", "", "", "DW", ""],
            ["", "", "DW", "", "", "", "DL", "", "DL", "", "", "", "DW", "", ""],
            ["DL", "", "", "DW", "", "", "", "DL", "", "", "", "DW", "", "", "DL"],
            ["", "", "", "", "DW", "", "", "", "", "", "DW", "", "", "", ""],
            
        ]
        # horribly incomplete

    def __repr__(self):
        return "Board()"

    __hash__ = None

class Tile(object):
    """Simple class representing a Scrabble letter tile."""

    def __init__(self, letter):
        self.letter = letter
        self.value = constants.TILE_VALUES[letter]
        # horribly incomplete

    def __repr__(self):
        return "Tile('%s')" % self.letter
