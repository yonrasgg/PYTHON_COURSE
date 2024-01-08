import turtle

# Configuración inicial
screen = turtle.Screen()
turt = turtle.Turtle()

turt.shape("turtle")

# Dibujar la figura original
turt.begin_fill()
turt.fillcolor("orange")
turt.circle(90)
turt.end_fill()

turt.shape("arrow")

turt.begin_fill()
turt.fillcolor("black")
turt.circle(35)
turt.end_fill()

turtle.shape("circle")

turt.begin_fill()
turt.fillcolor("brown")
turt.circle(15)
turt.end_fill()

# Girar la figura en 90 grados
turt.setheading(turt.heading() + 180)

# Dibujar la figura girada
turt.begin_fill()
turt.fillcolor("blue")
turt.circle(90)
turt.end_fill()

turtle.shape("triangle")

turt.begin_fill()
turt.fillcolor("green")
turt.circle(35)
turt.end_fill()

turtle.shape("turtle")

turt.begin_fill()
turt.fillcolor("yellow")
turt.circle(15)
turt.end_fill()

turt.penup()
turt.setpos(90, 90)
turt.forward(100)
turt.pendown()
turt.forward(100)
turt.left(90)
turt.forward(100)
turt.left(90)
turt.forward(100)
turt.left(90)
turt.forward(100)

turt.undo()
turt.reset()

turt.forward(100)
turt.stamp()
turt.forward(100)

# Finalizar el dibujo
turtle.done()
