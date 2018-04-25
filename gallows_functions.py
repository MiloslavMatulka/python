"""
Functions relating to the Gallows game.

"""

import random

# This function randomly chooses word from words as per dict keys.
# It returns dict values (guessed word, hint).
# It is possible to add another words with hints.
def random_word():
    words = {1 : ("english", "language"),
             2 : ("monday", "weekday"),
             3 : ("mother", "parent")}
    number = random.randrange(1, len(words) + 1)
    word = words[number]
    return word


# This function exchanges a "_" for an inserted letter
# if it is present in guessed word.
def update_string(string, letter, guessed_word):
    if letter in guessed_word:
        letter_pos = guessed_word.index(letter)
        string = string[:letter_pos] + letter + string[(letter_pos + 1):]
    else:
        pass
    return string


# This function counts bad attempts
# if the inserted letter is not present in a guessed word.
def counter(letter, guessed_word, bad_attempts):
    if letter not in guessed_word:
        bad_attempts += 1
    else:
        pass
    return bad_attempts


# Evaluation function.
def evaluate(string, bad_attempts):
    if '_' not in string:
        evaluation = '*'
    elif bad_attempts == 10:
        evaluation = '!'
    else:
        evaluation = '?'
    return evaluation
