"""
This module consists of a house function.
After passing two arguments (base, wall)
into this function a house will be drawn.

"""

# Import of necessary components.
from math import degrees, atan
from turtle import speed, forward, left, exitonclick

# house function
def house(base, wall):
    # Variables and turtle speed.
    diagonal = ((base ** 2) + (wall ** 2)) ** (1 / 2)
    angle_base_rad = atan(wall / base)
    angle_base = degrees(angle_base_rad)
    angle_roof = 2 * (90 - angle_base)
    angle_roof_top = 180 - (180 - (2 * angle_base))
    roof = diagonal / 2
    speed(10)

    # Outer walls of the house.
    for i in range(2):
        forward(base)
        left(90)
        forward(wall)
        left(90)
        
    # The first diagonal of the house.
    left(angle_base)
    forward(diagonal)

    # A roof of the house.      
    left(angle_roof)        
    forward(roof)
    left(angle_roof_top)
    forward(roof)
        
    # The second diagonal of the house.
    left(angle_roof)
    forward(diagonal)

    exitonclick()
