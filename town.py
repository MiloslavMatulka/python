from turtle import speed, forward, left, penup, pendown, setpos, exitonclick

speed(10)
ypos = 0

for row in range(5):
    for number in range(10):
        
        side = 25
        diag = side * (2 ** (1 / 2))
        roof = (side * (2 ** (1 / 2))) / 2

        # Square
        for i in range(4):
            forward(side)
            left(90)

        # Diagonals and a roof
        #
        # Diagonal 1
        left(45)
        forward(diag)

        # Roof
        for r in range(2):
            left(90)
            forward(roof)

        # Diagonal 2
        left(90)
        forward(diag)

        # Space between houses
        left(45)
        forward(10)
    penup()
    ypos += 50
    setpos(0, ypos)
    pendown()

exitonclick()
