"""
Dice game

A game for 4 virtual players.
First player throws a dice untill number 6 emerges.
The rest of players throw a dice the same way.
A winner is the player who threw the most times.
In case there are more than one player with the same amount
a winner is who threw before the others.

"""

from random import randrange

# Print extract only variant
# Four players
# One throw is sure
# Throwing untill 6 emerges
# Count of throws
##for player in range(1, 5):
##    throw = 1
##    while randrange(1, 7) < 6:
##        throw += 1
##    print("Player {0} threw {1:2d}".format(player, throw), "x")

# All throws variant
count = list()
# Four players
for player in range(1, 5):
    # One throw is sure.
    throw = 1
    print("Player {} threw: ".format(player))
    # A single player throws until 6 emerges.
    while True:
        number = randrange(1, 7)
        if number < 6:
            print(number, end=", ")
            # Count of throws
            throw += 1
        else:
            print(number, "\n")
            break
    # The number of single-player throws appended to a list.
    count.append(throw)
# The first occurence of the highest score in a list is a winner.
winner = count.index(max(count)) + 1
print("A Winner is player {}.".format(winner))
# print(count)
