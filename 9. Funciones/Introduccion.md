# [Funciones en Python 🛠️](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/9.%20Funciones/Funciones.py)

Las funciones son uno de los componentes fundamentales de la programación en cualquier lenguaje. En Python, una función es un bloque de código reutilizable que realiza una tarea específica.

La forma más básica de definir una función en Python es utilizando la palabra clave `def` seguida del nombre de la función y paréntesis `()`.

```python
def saludo():
    print("¡Hola, mundo!")
```

Aquí, `saludo` es el nombre de la función, y la línea de código que imprime "¡Hola, mundo!" es el cuerpo de la función.

Para ejecutar la función, la llamamos por su nombre seguido de paréntesis:

```python
saludo()  # Llama a la función
```

## Argumentos y Parámetros 🧮

Las funciones se vuelven aún más poderosas cuando les pasamos datos, conocidos como argumentos, que pueden usar para realizar sus tareas. Estos argumentos se especifican entre los paréntesis en la definición de la función, y los tratamos como nuevas variables dentro del cuerpo de la función. A estas "variables" se les llama parámetros.

Por ejemplo, podríamos tener una función que salude a una persona por su nombre:

```python
def saludo_personalizado(nombre):  # 'nombre' es un parámetro
    print(f"¡Hola, {nombre}!")
    
saludo_personalizado("Alice")  # 'Alice' es un argumento
```

En este código, `nombre` es un parámetro de la función `saludo_personalizado`, y cuando llamamos a `saludo_personalizado("Alice")`, el argumento `"Alice"` se pasa a la función y se usa dondequiera que `nombre` aparezca en el cuerpo de la función.

Las funciones pueden tener múltiples parámetros, permitiéndonos pasar varios argumentos cuando llamamos a la función.

```python
def presentacion(nombre, edad):
    print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")
    
presentacion("Bob", 25)
```

Las funciones son una herramienta poderosa que permite reutilizar código y estructurar programas de una manera más comprensible y manejable.

[< Retroceder](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/8.%20Bucles/Ejercicios.md) | [Comenzar el Viaje](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/9.%20Funciones/1.FuncionesPython.md) | [Próxima Sección >](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/10.%20GestionErrores/Introduccion.md)
