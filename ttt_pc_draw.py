"""
Function "pc_draw" receives a "field" string,
randomly populate "position" (0-19),
and returns a game field (string) with a symbol
populating the random position.
Repetion until used a free position.

"""

from random import randrange

def pc_draw(field):
    symbol = 'o'
    size = len(field)

    while True:
            number = randrange(0, size)
            if field[number] == "x" or field[number] == "o":
                # No need to execute: print("Position is already populated.")
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

    field = field[:number] + symbol + field[(number + 1):]

    return field
