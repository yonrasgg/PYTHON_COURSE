# Importar librerias necesarias
import turtle
import time
import random

delay = 0.1 # Velocidad de la serpiente
score = 0 # Puntuacion
high_score = 0 # Puntuacion mas alta

screen = turtle.Screen() # Configuracion de la pantalla
screen.setup(650, 650) # Tamaño de la pantalla
screen.bgcolor('black') # Color de fondo
screen.title('Snake') # Titulo de la pantalla

snake = turtle.Turtle() # Configuracion de la serpiente
snake.speed(1) # Velocidad de la serpiente
snake.shape('square') # Forma de la serpiente
snake.penup() # Levantar lapiz
snake.goto(0, 0) # Posicion inicial de la serpiente
snake.direction = 'stop' # Direccion inicial de la serpiente 
snake.color('green') # Color de la serpiente

food = turtle.Turtle() # Configuracion de la comida
food.shape('turtle') # Forma de la comida
food.color('blue') # Color de la comida 
food.penup() # Levantar lapiz
food.goto(0, 100) # Posicion inicial de la comida
food.speed(0) # Velocidad de la comida

body = [] # Lista donde se almacenare el cuerpo de la serpiente
text = turtle.Turtle() # Configuracion del texto
text.speed(0) # Velocidad del texto de la puntuacion
text.color('white') # Color del texto de la puntuacion
text.penup() # Levantar lapiz del texto
text.hideturtle() # Ocultar el lapiz del texto
text.goto(0, 260) # Posicion inicial del texto
text.write('Score: 0  High Score: 0', align='center', font=('Courier', 24, 'normal')) # Texto inicial de la puntuacion 

def go_up(): # Funcion para mover la serpiente hacia arriba
    snake.direction = 'up' # Cambiar la direccion de la serpiente

def go_down(): # Funcion para mover la serpiente hacia abajo
    snake.direction = 'down' # Cambiar la direccion de la serpiente

def go_left(): # Funcion para mover la serpiente hacia la izquierda
    snake.direction = 'left' # Cambiar la direccion de la serpiente

def go_right(): # Funcion para mover la serpiente hacia la derecha
    snake.direction = 'right' # Cambiar la direccion de la serpiente

def move_snake(): # Funcion para mover la serpiente
    x, y = snake.xcor(), snake.ycor() # Posicion de la serpiente

    if snake.direction == 'up': # Si la direccion de la serpiente es hacia arriba
        y += 20 # Mover la serpiente 20 pixeles hacia arriba
    elif snake.direction == 'down': # Si la direccion de la serpiente es hacia abajo
        y -= 20 # Mover la serpiente 20 pixeles hacia abajo
    elif snake.direction == 'left': # Si la direccion de la serpiente es hacia la izquierda
        x -= 20 # Mover la serpiente 20 pixeles hacia la izquierda
    elif snake.direction == 'right': # Si la direccion de la serpiente es hacia la derecha
        x += 20 # Mover la serpiente 20 pixeles hacia la derecha

    if x > 290: # Si la serpiente se sale de la pantalla por la derecha
        x = -290 # Mover la serpiente a la izquierda de la pantalla
    elif x < -290: # Si la serpiente se sale de la pantalla por la izquierda
        x = 290 # Mover la serpiente a la derecha de la pantalla
    if y > 290: # Si la serpiente se sale de la pantalla por arriba
        y = -290 # Mover la serpiente hacia abajo de la pantalla
    elif y < -290: # Si la serpiente se sale de la pantalla por abajo
        y = 290 # Mover la serpiente hacia arriba de la pantalla

    snake.goto(x, y) # Mover la serpiente a la posicion x, y

    for segment in body: # Para cada segmento en el cuerpo de la serpiente
        segment_x, segment_y = segment.xcor(), segment.ycor() # Posicion del segmento
        if segment_x > 290: # Si el segmento se sale de la pantalla por la derecha
            segment_x = -290 # Mover el segmento a la izquierda de la pantalla
        elif segment_x < -290: # Si el segmento se sale de la pantalla por la izquierda
            segment_x = 290 # Mover el segmento a la derecha de la pantalla
        if segment_y > 290: # Si el segmento se sale de la pantalla por arriba
            segment_y = -290 # Mover el segmento hacia abajo de la pantalla
        elif segment_y < -290: # Si el segmento se sale de la pantalla por abajo
            segment_y = 290 # Mover el segmento hacia arriba de la pantalla
        segment.goto(segment_x, segment_y) # Mover el segmento a la posicion segment_x, segment_y

screen.listen() # Escuchar los eventos del teclado
screen.onkeypress(go_up, 'Up') # Si se presiona la tecla arriba
screen.onkeypress(go_down, 'Down') # Si se presiona la tecla abajo
screen.onkeypress(go_left, 'Left') # Si se presiona la tecla izquierda
screen.onkeypress(go_right, 'Right') # Si se presiona la tecla derecha

while True: # Ciclo infinito
    screen.update() # Actualizar la pantalla

    if snake.distance(food) < 20: # Si la serpiente se come la comida
        x = random.randint(-290, 290) # Posicion x aleatoria
        y = random.randint(-290, 290) # Posicion y aleatoria
        food.goto(x, y) # Mover la comida a la posicion x, y

        body_segment = turtle.Turtle() # Configuracion del segmento del cuerpo
        body_segment.shape('square') # Forma del segmento del cuerpo
        body_segment.color('green') # Color del segmento del cuerpo
        body_segment.penup() # Levantar lapiz
        body_segment.goto(0, 0) # Posicion inicial del segmento del cuerpo
        body_segment.speed(0) # Velocidad del segmento del cuerpo
        body.append(body_segment) # Agregar el segmento del cuerpo a la lista
        
        score += 10 # Aumentar la puntuacion en 10 puntos
        if score > high_score: # Si la puntuacion es mayor a la puntuacion mas alta
            high_score = score # La puntuacion mas alta es igual a la puntuacion
        text.clear() # Limpiar el texto de la puntuacion
        text.write('Score: {}  High Score: {}'.format(score, high_score), align='center', font=('Courier', 24, 'normal')) # Escribir el texto de la puntuacion

    total_body = len(body) # Total de segmentos del cuerpo
    for i in range(total_body - 1, 0, -1): # Para cada segmento del cuerpo
        x = body[i - 1].xcor() # Posicion x del segmento anterior
        y = body[i - 1].ycor() # Posicion y del segmento anterior 
        body[i].goto(x, y) # Mover el segmento a la posicion x, y

    if total_body > 0: # Si hay mas de un segmento en el cuerpo
        x = snake.xcor() # Posicion x de la serpiente
        y = snake.ycor() # Posicion y de la serpiente
        body[0].goto(x, y) # Mover el primer segmento a la posicion x, y

    move_snake() # Mover la serpiente
    
    for i in body:  # Para cada segmento en el cuerpo
        if i.distance(snake) < 20: # Si la serpiente choca con el segmento
            time.sleep(1) # Esperar 1 segundo
            snake.goto(0, 0) # Mover la serpiente a la posicion inicial
            snake.direction = 'stop' # Cambiar la direccion de la serpiente
            for segment in body: # Para cada segmento en el cuerpo 
                segment.goto(1000, 1000)    # Mover el segmento a una posicion fuera de la pantalla
            body.clear() # Limpiar el cuerpo
            
            score = 0 # Puntuacion igual a 0
            text.clear() # Limpiar el texto de la puntuacion
            text.write('Score: {}  High Score: {}'.format(score, high_score), align='center', font=('Courier', 24, 'normal')) # Escribir el texto de la puntuacion
    
    time.sleep(delay) # Esperar delay segundos

turtle.done() # Mantener la ventana abierta
