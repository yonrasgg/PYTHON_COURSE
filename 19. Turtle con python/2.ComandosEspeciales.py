from turtle import *
import turtle as trtl

# Configuración de la pantalla
screen = trtl.Screen()
screen.setup(500, 500)
screen.bgcolor('black')

# Definición de la función para dibujar
def draw(rad):
    for i in range(2):
        trtl.circle(rad, 90)
        trtl.circle(rad // 2, 90)

# Configuración de colores
col = ['#FF00FF', '#00FFFF', '#00FF00', '#FFFF00', '#FFA500', '#FF0000']

# Variables para animación
val = 10
ind = 0

trtl.speed(10)
trtl.hideturtle()

# Dibujo de la esfera artística
for i in range(36):
    trtl.seth(-val)
    trtl.color(col[ind])

    if ind == 5:
        ind = 0
    else:
        ind += 1

    draw(80)
    val += 10

trtl.done()
