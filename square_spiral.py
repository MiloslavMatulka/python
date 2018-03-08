"""
Rendering of a square spiral through the turtle module.

"""

from turtle import speed, forward, left, exitonclick

speed(10)

for i in range(1, 20):
    left(90)
    forward(5 * i)

exitonclick()
