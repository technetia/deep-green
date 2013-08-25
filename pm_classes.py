#! /usr/bin/env python
# pm_classes.py

import pm_constants as constants
import pm_utils as utils

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

    def __str__(self):
        return (self.letter if not self.is_blank else self.letter.lower())

    __hash__ = None


class Board(object):
    """Class representing the Scrabble board."""
    
    def __init__(self):
        self.grid = constants.SCRABBLE_BOARD
        self.grid_height = len(self.grid)
        self.grid_width = len(self.grid[0]) if self.grid_height > 0 else 0
        self.tiles_in_play = [[None] * self.grid_width for i in range(self.grid_height)]
    
    def __repr__(self):
        return "Board()"

    def __str__(self):
        s = "-" + ("--" * self.grid_width) + "\n"
        for row in self.tiles_in_play:
            s += "|"
            for cell in row:
                s += (str(cell) if cell is not None else " ") + "|"
            s += "\n"
            s += "-" + ("--" * self.grid_width) + "\n"
        return s

    __hash__ = None

    def verify_word(self, word, start_pos):
        """
        Check that the word can be played from the given position.

        Returns a two-element tuple with each element specifying
        whether the word can be played (right, down), e.g.

        (True, False)

        which says the word can be played horizontally but not
        vertically.
        """

        status = [False, False]

        # TWL
        if "".join([l[0] for l in word]) not in constants.TWL:
            return tuple(status)

        # width
        if len(word) <= self.grid_width - start_pos[0]:
            status[0] = True

        # height
        if len(word) <= self.grid_height - start_pos[1]:
            status[1] = True

        return tuple(status)

    def play_word(self, word, start_pos, direction):
        """
        Adds |word| to the board. |word| should be an ordered sequence
        of Tile objects.
        
        |start_pos| is a tuple marking the coordinate of the board
        where the word starts.

        |direction| is either 'right' or 'down', indicating which way
        the word is played.

        verify_word is assumed to have been called prior to this function.

        Returns the score from playing said word.
        """
        
        curr_row, curr_col = start_pos
         
        if direction == "right":
            for letter in word:
                self.tiles_in_play[curr_row][curr_col] = Tile(*letter)
                curr_col += 1
        elif direction == "down":
            for letter in word:
                self.tiles_in_play[curr_row][curr_col] = Tile(*letter)
                curr_row += 1
        
        return 0

    def clear(self):
        self.tiles_in_play = [[None] * self.grid_width for i in range(self.grid_height)]


