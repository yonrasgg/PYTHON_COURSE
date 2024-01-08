import turtle

screen =  turtle.Screen()
turt = turtle.Turtle()

screen.bgcolor("grey")
screen.title("Personalizando Turtle")

turt.shapesize(3, 4, 1)

turt.fillcolor("cyan")
turt.forward(100)

turt.pencolor("green")
turt.forward(100)

turt.color("red", "yellow")
turt.right(90)
turt.forward(100)

turt.pensize(5)
turt.forward(100)

turtle.done()