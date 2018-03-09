"""
Function "player_draw" receives a "field" string,
asks player for a "position" (0-19),
and returns a game field (string) with a symbol
populated the required position.
Function refuses number out of range,
already populated position.
Insertion must be a number.
Repetion until correct input inserted.

"""

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

    field = field[:number] + symbol + field[(number + 1):]

    return field
