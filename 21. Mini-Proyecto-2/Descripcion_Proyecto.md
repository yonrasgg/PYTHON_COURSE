# 🎮 Proyecto: Videojuego Snake

- 📦 **Importa los módulos necesarios:** `turtle`, `time` y `random`.
- 🚀 **Configura las variables iniciales:**
  - `delay`: Controla la velocidad del juego.
  - `score`: Puntuación actual del jugador.
  - `high_score`: Puntuación más alta alcanzada.

- ⚙️ **Configura la ventana del juego:**
  - Tamaño: 650 x 650 píxeles.
  - Fondo negro.
  - Título: "Snake".

- 🐍 **Configura la serpiente:**
  - Crea una instancia de Turtle llamada `snake`.
  - Establece su velocidad, forma, color y posición inicial.
  - Inicializa su dirección como 'stop'.

- 🍏 **Configura la comida:**
  - Crea una instancia de Turtle llamada `food`.
  - Establece su forma (turtle), color y posición inicial.

- 🐍 **Configura el cuerpo de la serpiente:**
  - Crea una lista llamada `body` para almacenar los segmentos del cuerpo.

- 📊 **Configura el texto para mostrar puntuación:**
  - Crea una instancia de Turtle llamada `text`.
  - Establece su velocidad, color y posición.
  - Oculta el cursor.
  - Muestra la puntuación actual y la puntuación más alta en la parte superior de la ventana.

- 🎮 **Define las funciones de movimiento:**
  - `go_up()`, `go_down()`, `go_left()`, `go_right()`
    - Cambian la dirección de la serpiente según la tecla presionada.

  - `move_snake()`
    - Calcula la nueva posición de la serpiente según su dirección.
    - Ajusta la posición si la serpiente cruza los bordes de la pantalla.
    - Mueve la serpiente y ajusta la posición de los segmentos del cuerpo.

- 🎮 **Configura la detección de teclas:**
  - Asigna las funciones de movimiento a las teclas de dirección usando el método `onkeypress()`.

- 🔄 **Inicia el bucle principal del juego:**
  - Actualiza la ventana.
  - Verifica si la serpiente ha comido la comida:
    - Genera nueva comida en una posición aleatoria.
    - Crea un nuevo segmento de cuerpo.
    - Aumenta la puntuación y actualiza la puntuación más alta si es necesario.
    - Actualiza el texto de puntuación en la ventana.
  - Mueve los segmentos del cuerpo para seguir a la serpiente.
  - Actualiza la posición del primer segmento del cuerpo al lugar de la cabeza.
  - Mueve la serpiente.
  - Verifica colisiones con el cuerpo de la serpiente:
    - Si la cabeza de la serpiente colisiona con un segmento del cuerpo, reinicia el juego.
  - Espera un tiempo antes de la próxima iteración del bucle.

Esta guía te proporciona una estructura básica para crear un juego tipo Snake en Python. Puedes expandirlo añadiendo características como un puntaje, efectos de sonido, obstáculos, niveles de dificultad, entre otros. ¡Experimenta y diviértete desarrollando tu propio juego Snake! 🐍🎮

[< Retroceder](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/20.%20Mini-Proyecto-1/Descripcion_Proyecto.md) | [Ver Codigo Mini-Proyecto 2](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/21.%20Mini-Proyecto-2/snake.py)
