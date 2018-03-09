from turtle import speed, forward, left, exitonclick

def house(size):
    diagonal = 2 ** (1 / 2) * size
    roof = diagonal / 2
    speed(10)
    
    for i in range(4):
        forward(size)
        left(90)
        
    left(45)
    forward(diagonal)
    
    for j in range(2):        
        left(90)        
        forward(roof)
        
    left(90)
    forward(diagonal)

    exitonclick()
