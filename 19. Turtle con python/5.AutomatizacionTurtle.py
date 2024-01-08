import turtle

# Configuración inicial
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Dibujando el Perímetro de una Pirámide 3D")

# Crear una tortuga
turt = turtle.Turtle()
turt.speed(1)

# Coordenadas de la base de la pirámide
base_x = [0, 100, 100, 0]
base_y = [0, 0, 100, 100]

# Altura de la pirámide
altura = 150

# Calcular las coordenadas de los vértices superiores
top_x = sum(base_x) / len(base_x)
top_y = sum(base_y) / len(base_y)
top_z = altura

# Definir una función para dibujar una línea entre dos puntos
def dibujar_linea(x1, y1, x2, y2):
    turt.penup()
    turt.goto(x1, y1)
    turt.pendown()
    turt.goto(x2, y2)

# Dibujar las líneas que conectan los vértices de la base y la cima
for i in range(len(base_x)):
    dibujar_linea(base_x[i], base_y[i], top_x, top_y)

# Conectar los vértices de la base
for i in range(len(base_x)):
    dibujar_linea(base_x[i], base_y[i], base_x[(i+1) % len(base_x)], base_y[(i+1) % len(base_y)])

# Conectar los vértices superiores y la cima de la pirámide
for i in range(len(base_x)):
    dibujar_linea(top_x, top_y, base_x[i], base_y[i])
    dibujar_linea(base_x[i], base_y[i], top_x, top_y)

# Finalizar el dibujo
turtle.done()
