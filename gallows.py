"""
Gallows

This is the Gallows game.
PC randomly chooses one of three words but shows only dashes.
Player is asked for a letter.
If the letter is present in a chosen word, the letter is shown.
If it is not, the gallows is built gradually after every wrong answer.
The game is over when the word is guessed correctly or the gallows is built.
Score is to be seen after each draw.

"""

from gallows_functions import random_word, update_string, counter, evaluate

gallows = (
"""
""",
"""






~~~~~~~""",
"""
+
|
|
|
|
|
~~~~~~~""",
"""
+---.
|
|
|
|
|
~~~~~~~""",
"""
+---.
|   |
|
|
|
|
~~~~~~~""",
"""
+---.
|   |
|   O
|
|
|
~~~~~~~""",
"""
+---.
|   |
|   O
|   |
|
|
~~~~~~~""",
"""
+---.
|   |
|   O
| --|
|
|
~~~~~~~""",
"""
+---.
|   |
|   O
| --|--
|
|
~~~~~~~""",
"""
+---.
|   |
|   O
| --|--
|  /
|
~~~~~~~""",
r"""
+---.
|   |
|   O
| --|--
|  / \
|
~~~~~~~""")

while True:
    bad_attempts = 0
    
    print("This is the Gallows game.")
    print("You have to guess a word.")
    set_word = random_word()
    guessed_word = set_word[0]
    hint = set_word[1]
    length = len(guessed_word)
    string = length * "_"

    while True:
        print(f"The word consists of {length} letters. Hint: {hint}")
        letter = input("Insert a letter and press enter: ").lower()
        if letter in ('a', 'b', 'c', 'd', 'e', 'f', 'g',
                      'h', 'i', 'j', 'k', 'l', 'm', 'n',
                      'o', 'p', 'q', 'r', 's', 't', 'u',
                      'v', 'w', 'x', 'y', 'z'):
            pass
        else:
            print("Insert a single letter from alphabet! Please try again.")
            continue
        string = update_string(string, letter, guessed_word)
        bad_attempts = counter(letter, guessed_word, bad_attempts)
        print(f"The word is: {string}")
        print(f"Count of bad attempts: {bad_attempts} of 10")
        
        # Depicting of the gallows.
        print(gallows[bad_attempts])
        
        evaluation = evaluate(string, bad_attempts)
        if evaluation == '*':
            print("Congratulations, you are a winner!\nEnd of game.")
            break
        elif evaluation == '!':
            print("You lost the game!\nEnd of game.")
            break
        # For evaluation == '?'
        else:
            print("Let's continue.\n")
            continue

    # A new game option.
    repeat = input("Do you want to play again (y/n)?").lower()
    if repeat == 'y':
        continue
    elif repeat == 'n':
        break
    else:
        print("You pressed neither 'y' nor 'n'! End of game.")
        break
