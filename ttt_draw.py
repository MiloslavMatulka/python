"""
Function "draw" receives a "field" string, a field "number" (0-19),
a "symbol" (x or o), and returns a game field (string) with a symbol
populated the required position.

"""

def draw(field, number, symbol):
    field = field[:number] + symbol + field[(number + 1):]
    return field
