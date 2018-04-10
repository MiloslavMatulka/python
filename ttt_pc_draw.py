"""
Function "pc_draw" receives a "field" string,
randomly populate "position" (0-19),
and returns a game field (string) with a symbol
populating the random position.
Repetion until used a free position.

"""

from random import randrange
from util import draw

def pc_draw(field):
    try:
        symbol = 'o'
        size = len(field)

        while True:
            number = randrange(0, size)

            if "-" in field and field[number] == "x":
                # No need to execute: print("Position is already populated.")
                continue
            elif "-" in field and field[number] == "o":
                continue
            # Offensive and defensive strategy.
            elif "-oo" in field:
                number = field.index("-oo")
                break
            elif "o-o" in field:
                number = field.index("o-o") + 1
                break
            elif "oo-" in field:
                number = field.index("oo-") + 2
                break
            elif "-xx" in field:
                number = field.index("-xx")
                break
            elif "x-x" in field:
                number = field.index("x-x") + 1
                break
            elif "xx-" in field:
                number = field.index("xx-") + 2
                break
            elif "-o-" in field:
                number = field.index("-o-")
                break
            elif "-x-" in field:
                number = field.index("-x-")
                break
            else:
                break

        if "-" in field:
            field = draw(field, number, symbol)
        else:
            print("Field is full.")

    except ValueError:
        print("There is no field.")

    return field
