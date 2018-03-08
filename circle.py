from turtle import speed, forward, left, exitonclick
"""
95-angular-shape is almost a circle.

"""

speed(10)
n = 95
angle = 180 - (180 * (1 - (2 / n)))
side = 200 / n

for section in range(n):
    forward(side)
    left(angle)    

exitonclick()
