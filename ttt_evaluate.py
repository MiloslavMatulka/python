"""
Function "evaluate" evaluates a Tic-Tac-Toe game inserted "field".
Function returns:
"x" - x-player is a winner (there are "xxx" in a field)
"o" - o-player is a winner (there are "ooo" in a field)
"!" - draw, no winner (there is no "-")
"-" - another situation (game not finished)

"""

def evaluate(field):
    if ("xxx" in field):
        return "x"
    elif ("ooo" in field):
        return "o"
    elif ("-" not in field):
        return "!"
    else:
        return "-"
