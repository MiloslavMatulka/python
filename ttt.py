"""
Functions relating to a Tic-Tac-Toe game.

"""

from ttt_pc_draw import pc_draw

# For general info go to ttt_evaluate.py
def evaluate(field):
    if ("xxx" in field):
        return "x"
    elif ("ooo" in field):
        return "o"
    elif ("-" not in field):
        return "!"
    else:
        return "-"


# For general info go to ttt_draw.py
def draw(field, number, symbol):
    if number > len(field):
        raise ValueError("Number {} is out of range.".format(number))
    else:
        field = field[:number] + symbol + field[(number + 1):]
    return field


# For general info go to ttt_player_draw.py
def player_draw(field):
    symbol = 'x'

    while True:
        try:
            number = int(input("Insert number of your draw (0-19): "))
            if number not in range(20):
                print("Number is out of range.")
                continue
            elif field[number] == "x" or field[number] == "o":
                print("Position is already populated.")
                continue
            else:
                break
        except ValueError:
            print("Not a number.")

    field = draw(field, number, symbol)

    return field


# For general info go to ttt_player_pc.py
def player_pc():
    print("This is a Tic-Tac-Toe game.")

    while True:
        start = input('Press "q" to quit a game. Any other key to play: ')
        if start.lower() == "q":
            break
        else:
            field = 20 * "-"
            print('Player "x", PC "o"')

            # The game has 10 rounds (20 fields for both player and PC).
            for round_ in range(10):
                # Call player_draw(field) function.
                field = player_draw(field)
                print(field)
                # Three same symbols next to each other are a winner.
                print("Evaluation:", evaluate(field))
                if "xxx" in field:
                    print("Player is a winner.")
                    break
                else:
                    pass

                # Call pc_draw(field) function.
                field = pc_draw(field)
                print("PC draws:")
                print(field)
                # Three same symbols next to each other are a winner.
                print("Evaluation:", evaluate(field))
                if "ooo" in field:
                    print("PC is a winner.")
                    break
                elif "-" not in field:
                    print("No winner.")
                    break
                else:
                    pass

    print("End of game.")
