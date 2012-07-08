#! /usr/bin/env python
# pm_classes.py

import pm_constants as constants
import pm_utils as utils

class Board(object):
    """Class representing the Scrabble board."""
    
    def __init__(self):
        self.grid = constants.SCRABBLE_BOARD
        self.grid_height = len(self.grid)
        self.grid_width = len(self.grid[0]) if self.grid_height > 0 else 0
        self.tiles_in_play = set()
    
    def __repr__(self):
        return "Board()"

    __hash__ = None

    def play_word(word, start_pos, direction):
        """
        Adds |word| to the board. |word| should be an ordered sequence
        of tuples, with format (letter, is_blank), e.g.

        ('A', True)
        
        if the letter is A and a blank tile is being used for it.
        
        |start_pos| is a tuple marking the coordinate of the board
        where the word starts.

        |direction| is either 'right' or 'down', indicating which way
        the word is played.

        Returns the score from playing said word.
        """
        assert direction in ("right", "down")
        
        if direction == 'right':
            self.tiles_in_play.add((Tile(*word[0]), start_pos[0], start_pos[1]))
        
    def clear(self):
        self.tiles_in_play.clear()
    
class Tile(object):
    """Simple class representing a Scrabble letter tile."""

    def __init__(self, letter, blank=False):
        self.letter = letter
        self.is_blank = blank
        if self.is_blank:
            self.value = constants.TILE_VALUES[constants.BLANK]
        else:
            self.value = constants.TILE_VALUES[letter]
        
    def __repr__(self):
        return "Tile('%s', %s)" % (self.letter, self.is_blank)
