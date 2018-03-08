from turtle import speed, forward, left, right, setpos, exitonclick

speed(10)

for square in range(18):
    for j in range(4):
        forward(50)
        left(90)
    left(20)

setpos(0, -150)

for i in range(2):
    for j in range(18):
        forward(5)
        left(5)
    left(90)

setpos(0, -300)

left(180)
for i in range(2):
    for j in range(18):
        forward(7)
        right(5)
    right(90)

exitonclick()
