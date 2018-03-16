"""
This is a shared module.

"""

# This function is used in a Tic-Tac-Toe game. Shared into ttt_pc_draw.py
def draw(field, number, symbol):
    field = field[:number] + symbol + field[(number + 1):]
    return field
