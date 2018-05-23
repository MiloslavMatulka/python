"""
This is a testing file for the animals functions.

"""

import pytest
import animals_functions

# The testing function for sets of lists.
def test_set_pets():
    set_animals = animals_functions.set_pets(["bird", "cat"], ["cat", "dog"])
    assert set_animals == (["cat"], ["bird"], ["dog"])
