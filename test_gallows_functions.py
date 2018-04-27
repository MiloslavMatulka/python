"""
This is a testing file for the Gallows game.

"""

import pytest
import gallows_functions

# The example of a white box testing
def test_random_word_numbers():
    word = gallows_functions.random_word()
    assert (word == ("english", "language") or
            word == ("monday", "weekday") or
            word == ("mother", "parent"))


# The example of a black box testing
def test_update_string_yes():
    string = gallows_functions.update_string("______", 'o', "mother")
    assert string == "_o____"


def test_update_string_no():
    string = gallows_functions.update_string("______", 'a', "mother")
    assert string == "______"


def test_counter_yes():
    bad_attempts = gallows_functions.counter('a', "mother", 0)
    assert bad_attempts == 1


def test_counter_no():
    bad_attempts = gallows_functions.counter('o', "mother", 0)
    assert bad_attempts == 0


def test_evaluate_won():
    evaluation = gallows_functions.evaluate("mother", 9)
    assert evaluation == '*'


def test_evaluate_lost():
    evaluation = gallows_functions.evaluate("_other", 10)
    assert evaluation == '!'


def test_evaluate_continue():
    evaluation = gallows_functions.evaluate("_other", 9)
    assert evaluation == '?'
