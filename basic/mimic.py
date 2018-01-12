#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""
    word_dict = dict()
    with open(filename, 'r') as file:
        read_data = file.read()
        content = read_data.replace('\n', ' ')
        word_list = content.split()
        word_dict[''] = [word_list[0]]
        idx = 0
        fix_idx = 0
        for word in word_list:
            # print(word_list)
                # if word in word_list[fix_idx:]:
            #     idx = word_list.index(word, fix_idx)
            idx = word_list.index(word)
            # print("====>>> PALAVRA {} ".format(word))

            fix_idx = idx
            if word in word_dict.keys():
                continue
            for next_word in word_list[fix_idx:]:

                # print("next word {} e fix idx {}".format(next_word, fix_idx))
                if next_word == word:
                    if fix_idx+1 < len(word_list):
                        if next_word not in word_dict:
                            # print("## NOVO add next word idx {} : {} ".format(fix_idx+1, word_list[fix_idx+1]))
                            word_dict[word] = [word_list[fix_idx+1]]
                        else:
                            # print("00 VELHO add next word idx {} : {} ".format(fix_idx+1, word_list[fix_idx+1]))
                            word_dict[word].append(word_list[fix_idx+1])
                fix_idx += 1
            idx += 1

    # for k, v in word_dict.items():
    #     print(k, v)

    return word_dict


def print_mimic(mimic_dict, word):
    """Given mimic dict and start word, prints 200 random words."""

    random_text = list()
    count = 200
    while count > 0:
        if word in mimic_dict:
            word = random.choice(mimic_dict[word])
        else:
            word = random.choice(mimic_dict[''])
        random_text.append(word)
        random_text.append(' ')
        count -= 1

    print(''.join(random_text))
    return


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print('usage: ./mimic.py file-to-read')
    sys.exit(1)
  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, 'we')


if __name__ == '__main__':
  main()
