import turtle


turtle.speed(1000)
turtle.bgcolor("black")


for i in range (5) :
    for colours in ["red", "magenta", "blue", "cyan", "green", "yellow", "white"] :
        turtle.color(colours)
        turtle.pensize(3)
        turtle.left(12)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)

