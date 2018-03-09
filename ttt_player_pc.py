"""
player_pc function

One player plays a game tic-tac-toe against a PC.
Player puts symbol "x" and PC puts "o"
into 20-position field alternately
until all fields are filled up.
The winner is who will manage to put three
same symbols next to each other.
player_pc function creates a game field
and calls player_draw and pc_draw functions.

"""

from ttt_player_draw import player_draw
from ttt_pc_draw import pc_draw

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
                if "ooo" in field:
                    print("PC is a winner.")
                    break
                elif "-" not in field:
                    print("No winner.")
                    break
                else:
                    pass

    print("End of game.")
