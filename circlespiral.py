"""
Rendering of a circular spiral by using
the turtle module and the for loop.

"""

from turtle import speed, left, forward, exitonclick

speed(10)
n = 250

for i in range(n):
    left(20)
    forward(0.1 * i)

exitonclick()
