import turtle
import random

screen = turtle.Screen()
screen.title("Esquivar Obstáculos")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Crear el jugador
jugador = turtle.Turtle()
jugador.shape("turtle")
jugador.color("white")
jugador.penup()
jugador.goto(0, -250)
jugador.speed(100)

obstaculos = [] # Lista de obstáculos

def crear_obstaculo():
    obstaculo = turtle.Turtle()
    obstaculo.shape("square")
    obstaculo.color("red")
    obstaculo.speed(100) 
    obstaculo.penup()
    x_pos = random.randint(-290, 290)
    y_pos = 290
    obstaculo.goto(x_pos, y_pos)
    obstaculos.append(obstaculo)
    
def mover_obstaculos():
    for obstaculo in obstaculos:
        y_pos = obstaculo.ycor()
        y_pos -= 5
        obstaculo.sety(y_pos)
        
        if y_pos < -290:
            obstaculo.hideturtle()
            obstaculos.remove(obstaculo)
            
def mover_izquierda():
    x_pos = jugador.xcor()
    x_pos -= 20
    if x_pos < -290:
        x_pos = -290
    jugador.setx(x_pos)
    
def mover_derecha():
    x_pos = jugador.xcor()
    x_pos += 20
    if x_pos > 290:
        x_pos = 290
    jugador.setx(x_pos)
    
# Asociar teclas con funciones de movimiento
screen.listen()
screen.onkeypress(mover_izquierda, "Left")
screen.onkeypress(mover_derecha, "Right")

while True:
    crear_obstaculo()
    mover_obstaculos()
    
    if jugador.ycor() >= 290:
        jugador.sety(290)
        
    for obstaculo in obstaculos:
        if (jugador.distance(obstaculo) < 20):
            print("Perdiste")
            screen.bye()
            exit()
            
    screen.update()
    
turtle.done()