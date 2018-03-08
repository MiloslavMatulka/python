from turtle import speed, forward, left, exitonclick

n = int(input("Insert number n for n-anglular-shape: "))

speed(10)
angle = 180 - (180 * (1 - (2 / n)))
side = 200 / n

for section in range(n):
    forward(side)
    left(angle)    

exitonclick()
