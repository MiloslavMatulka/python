"""
A tic-tac-toe 1-D game

Two players put symbols "x" and "o" into 20-position field alternately
until all fields are filled up. The winner is who will manage to put three
same symbols next to each other.

"""

# Creating of a playing field through a list.
field = list()
for i in range(20):
    field.append("-")

# Question if to quit or to start a game.
print("This is a Tic-Tac-Toe game.")
query = input('Press "q" for quit. Press any other key to start a game. ')
if query == 'q':
    print("End of game.")
else:
    # Game is starting. For loop for 20 rounds.
    print("Insert number of a free field: 1-20.", "\n")
    for round_ in range(1, 21):
        if round_ % 2 != 0:
            player = "Player 1: "
            symbol = "x"
        else:
            player = "Player 2: "
            symbol = "o"

        # Players insert a number of the field.
        # A correct value has to be inserted otherwise repetition.
        # A symbol of players assigned to the number of a field.
        while True:
            inp = input(player)
            try:
                field_element = int(inp)
                if field_element not in range(1, 21):
                    print("Number is out of range.")
                    continue
                elif field[field_element - 1] != "-":
                    print("Already populated. Try another field.")
                    continue
                else:
                    field[field_element - 1] = symbol
                break
            except ValueError:
                print("Not a number.")

        # Creating of the field as a string. Print of an actual field.
        print("{}. round: ".format(round_), end="")
        field_str = "".join(field)
        print(field_str, "\n")

        # Three same symbols next to each other are a winner.
        if "xxx" in field_str:
            print("Player 1 is a winner.")
            break
        elif "ooo" in field_str:
            print("Player 2 is a winner.")
            break
        else:
            pass

    print("End of game.")
