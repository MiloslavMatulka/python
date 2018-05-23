"""
The animals list

Sorted alphabetically.
Then sorted alphabetically (first letters ignored).

"""

pets = ["dog", "cat", "frog", "snake", "bird"]
pets_key = list()
sec_sort = list()

# Sorted alphabetically
alphabet_sort = sorted(pets)
print(f"List of pets sorted alphabetically:\n{alphabet_sort}\n")

# Sorted alphabetically (first letters ignored)
for pet in pets:
    pet = (pet[1], pet)
    pets_key.append(pet)
pets_key = sorted(pets_key)
for animal in pets_key:
    animal = animal[1]
    sec_sort.append(animal)
print(f"List of pets sorted alphab. (first letters ignored):\n{sec_sort}")
