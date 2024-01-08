# Creación de un Videojuego Básico en Python con Turtle 🎮🐢

En este tutorial, vamos a explorar cómo crear un videojuego simple utilizando la biblioteca turtle de Python. Crearemos un juego en el que un personaje controlado por el jugador debe esquivar obstáculos que caen desde la parte superior de la pantalla.

## Paso 1: Configuración Inicial

En este paso, configuramos la pantalla del juego, creamos al jugador (que será una tortuga) en el centro inferior y definimos una lista vacía obstaculos para almacenar los obstáculos que caerán.

## Paso 2: Funciones para Crear y Mover Obstáculos

Creamos dos funciones: crear_obstaculo() que crea un obstáculo en una posición aleatoria en la parte superior de la pantalla, y mover_obstaculos() que mueve todos los obstáculos hacia abajo. Si un obstáculo se mueve fuera de la pantalla, lo eliminamos de la lista.

## Paso 3: Control de Movimiento del Jugador

Definimos funciones mover_izquierda() y mover_derecha() para mover al jugador hacia la izquierda y la derecha respectivamente. Luego, asociamos estas funciones con las teclas "Left" y "Right" usando screen.onkeypress().

## Paso 4: Bucle Principal del Juego

En este paso, creamos un bucle principal que se ejecuta constantemente. Dentro del bucle, creamos nuevos obstáculos y movemos los existentes. También verificamos si el jugador ha chocado con algún obstáculo, en cuyo caso el juego termina.

## Paso 5: Finalizar y Mostrar el Resultado

Finalmente, cuando el jugador pierde, terminamos el juego y mostramos el resultado.

[< Retroceder](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/19.%20Turtle%20con%20python/5.AutomatizacionTurtle.md) | [Ver Codigo Mini-Proyecto 1](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/20.%20Mini-Proyecto-1/MiniProyecto1.py) | [Siguiente >](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/21.%20Mini-Proyecto-2/Descripcion_Proyecto.md)
