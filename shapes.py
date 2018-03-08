"""N-angular shapes through
the turtle module.
"""

from turtle import speed, forward, left, penup, pendown, exitonclick

speed(10)

for n in range(5, 9):
    # Variables setting
    side = 200 / n
    angle = 180 - (180 * (1 - (2 / n)))
    # Drawing of the shape
    for shape in range(n):
        forward(side)
        left(angle)
    # Shift to the position of the next shape.
    penup()
    shift = 80
    forward(shift)
    pendown()
        
exitonclick()
