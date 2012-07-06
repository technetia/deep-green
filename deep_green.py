#! /usr/bin/env python
# deep_green.py
#
# Computer program intended to help you play Scrabble on Facebook.
# Named (obviously) in tribute to Deep Blue, the infamous chess machine.

import sys
import pm_utils as utils

# sample client-side interface (placeholder until real one is created)
# outputs results to stdout and prompt to stderr, so you can redirect
# stdout to a file for easier reading
# alternatively, if you provide command-line arguments, each will be
# treated as a letter (again, use / for blanks)
def main():
    if len(sys.argv) > 1:
        letter_list = sys.argv[1:]
    else:
        print >>sys.stderr, "Enter letters given, separated by whitespace."
        print >>sys.stderr, "Use a / for blanks (e.g. A / B C D)."
        letter_list = raw_input().split()

    letter_list = [l.replace("/", " ") for l in letter_list]
    # sanity check
    if not utils.is_valid_letter_sequence(letter_list):
        raise ValueError("invalid Scrabble characters given")
    
    word_choices = utils.get_word_choices(letter_list).items()
    # want list desc. sorted by score, then asc. sorted alphabetically
    word_choices.sort()
    word_choices.sort(key=lambda x: x[1], reverse=True)
    
    for word_info_block in word_choices:
        word = word_info_block[0][0]
        blanks = word_info_block[0][1]
        score = word_info_block[1]
        if blanks:
            print "%s: score of %s using %s as blanks" % (
                word, score, ", ".join(blanks))
        else:
            print "%s: score of %s without using blanks" % (word, score)
    
if __name__ == "__main__":
    main()

