#! /usr/bin/env python
# pm_utils.py

import pm_constants as constants

def is_valid_letter_sequence(letters):
    """
    Determines if |letters| is a valid sequence of Scrabble characters
    (i.e. sanity check).
    """
    for letter in letters:
        if letter not in constants.TILE_VALUES:
            return False
    return True

def powerset(word):
    """
    Get the powerset of a word (a string of letters).
    """
    pset = set()
    for i in xrange(len(word)):
        pset.add(word[i])
        psubset = powerset(word[:i] + word[i+1:])
        for subword in psubset:
            pset.add(word[i] + subword)
        pset.update(psubset)
    return pset

########################################
## score-computing functions
########################################

def get_word_value(word):
    """Compute the Scrabble value of the given word (string)."""
    return sum([constants.TILE_VALUES[letter] for letter in word.upper()])

def get_word_choices(letters, blank_letters=None):
    """
    Get a list of all possible word choices with the given letters,
    and their associated scores, taking into account blank tiles.
    """
    if blank_letters is None:
        blank_letters = []
        
    word_choices = {}

    # recursively handle blank tiles
    for l in letters:
        if l == constants.BLANK:
            for a in constants.LETTERS:
                new_letter_list = list(letters)
                new_letter_list.remove(constants.BLANK)
                new_letter_list.append(a)
                word_choices.update(get_word_choices(new_letter_list, blank_letters+[a]))

    # remove blanks from consideration
    letters = [l for l in letters if l != constants.BLANK]
    
    # find word permutations
    for word_permutation in powerset(letters):
        if word_permutation in constants.TWL:
            # handle blank tiles' score differently
            word = word_permutation
            blanks_used = []
            for l in blank_letters:
                if l in word:
                    word = word.replace(l, constants.BLANK, 1)
                    blanks_used.append(l)
            # in any case, store word, blanks used for it (if any), and score
            word_choices[(word_permutation, tuple(blanks_used))] = get_word_value(word)

    return word_choices

########################################
## word-finding functions
########################################

def words_such_that(condition):
    """
    Finds words in the TWL word list (in no particular order) that
    satisfy the given condition, which should be a Python expression.

    word should be used as the variable to test. For example:

    >>> words_such_that('len(word) == 1')
    set([])
    >>> ...
    
    since there is no valid word with a length of 1.
    """
    eval_dict = {
        "__builtins__" : None,
        "len" : len,
        "range" : range,
        "word" : None,
    }
    try:
        eval_expr = compile(condition, "<string>", "eval")
    except(Exception):
        raise ValueError("%s is not a valid condition" % condition)

    word_set = set()
    for word in constants.TWL:
        eval_dict["word"] = word
        try:
            if eval(eval_expr, eval_dict):
                word_set.add(word)
        except(Exception):
            pass

    return word_set
