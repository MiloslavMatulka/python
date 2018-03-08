"""
Rendering of a octagonal spiral by using
the turtle module and the for loop.

"""

from turtle import speed, forward, left, exitonclick

speed(10)

for i in range(1, 60):
    left(45)
    forward(1 * i)

exitonclick()
