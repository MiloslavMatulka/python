"""
The animals functions

"""

pets = ["dog", "cat", "rabbit", "snake"]
pets1 = ["bird", "fly", "horse"]
pets2 = ["nightingale", "horse", "bird"]

# This function returns the animal that is shorter than 5 letters.
def short_pets(pets):
    short_animals = list()
    for pet in pets:
        if len(pet) < 5:
            short_animals.append(pet)
        else:
            pass
    return short_animals


# This function returns the animal that has 'c' at the beginning.
def c_pets(pets):
    c_animals = list()
    for pet in pets:
        if pet[0] == 'c':
            c_animals.append(pet)
        else:
            pass
    return c_animals


# This function returns True if assigned word is in the animals list.
def in_pets(word):
    return word in pets


# This function receives 2 lists of pets and returns:
# 1. animals present in both lists
# 2. animals present only in the first list
# 3. animals present only in the second list
def set_pets(pets1, pets2):
    animals1 = set(pets1)
    animals2 = set(pets2)
    both_animals = list(animals1.intersection(animals2))
    first_animals = list(animals1.difference(animals2))
    second_animals = list(animals2.difference(animals1))
    return both_animals, first_animals, second_animals
