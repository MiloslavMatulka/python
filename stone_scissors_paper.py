"""
A game "Stone x Scissors x Paper"

This is a text analogy of the game that is played by hands.
Your adversary is your computer.

Stone beats scissors.
Scissors beats paper.
Paper beats stone.

"1" stone
"2" scissors
"3" paper
"4" end of game

"""

# Import of necessary modules.
from random import randrange

# Variables
win = "You are a winner."
lost = "You lost the game."
same = "The same choice as you. No winner."
exc = "Incorrect value."
end = "End of game."

# Name of the game printed on the screen.
print('This is a game "Stone x Scissors x Paper".')

while True:
    # User asked to insert his/her choice.
    # (User have to insert the correct value otherwise error.)
    try:
        inp = int(input('Insert "1" stone, "2" scissors, "3" paper, "4" end: '))
    except ValueError:
        print("Not a number.", "\n")
        continue
        
    if inp == 4:
        print(end, "\n")
        break

    pc = randrange(1, 4)

    print('Your computer gives {}.'.format(pc))

    if inp == 1 and pc == 1 or inp == 2 and pc == 2 or inp == 3 and pc == 3:
          print('{}'.format(same), "\n")
    elif inp == 1 and pc == 2 or inp == 2 and pc == 3 or inp == 3 and pc == 1:
          print('{}'.format(win), "\n")
    elif inp == 1 and pc == 3 or inp == 2 and pc == 1 or inp == 3 and pc == 2:
          print('{}'.format(lost), "\n")
    else:
        print(exc, "\n")
