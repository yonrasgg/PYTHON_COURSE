# 📚 Errores y excepciones en Python

En Python, hay dos tipos principales de errores: errores de sintaxis y excepciones.

## 1️⃣ Errores de sintaxis (Syntax Errors)

Los errores de sintaxis, también conocidos como errores de interpretación, son quizás los más fáciles de resolver. Ocurren cuando la sintaxis de una línea de código no es válida y Python no puede interpretarla.

Aquí tienes un ejemplo de un error de sintaxis:

```python
print("Hello world"
```

Como puedes ver, nos hemos olvidado de cerrar el paréntesis, por lo que Python lanzará un `SyntaxError` diciendo que hay un paréntesis de cierre esperado.

## 2️⃣ Excepciones

Incluso si una declaración o expresión es sintácticamente correcta, puede causar un error cuando se intenta ejecutar. Los errores detectados durante la ejecución se llaman excepciones.

Aquí tienes un ejemplo de una excepción:

```python
num1 = 5
num2 = "5"
print(num1 + num2)
```

En este caso, estamos intentando sumar un entero y una cadena, lo que no está permitido en Python. Por lo tanto, Python lanzará un `TypeError`.

## 🎭 Manejo de excepciones

Python proporciona declaraciones try y except para manejar las excepciones. El bloque de código que puede lanzar una excepción se coloca dentro del bloque `try` y el manejo de la excepción se implementa en el bloque `except`.

Aquí tienes un ejemplo de manejo de excepciones:

```python
try:
    num1 = 5
    num2 = "5"
    print(num1 + num2)
except TypeError:
    print("Los tipos de los datos no son compatibles para la operación.")
```

En este caso, si ocurre un `TypeError`, Python ejecutará el código dentro del bloque `except`, imprimiendo "Los tipos de los datos no son compatibles para la operación.".

## 🏁 Excepciones múltiples

Podemos manejar múltiples excepciones utilizando varios bloques `except`. Aquí tienes un ejemplo de cómo manejar múltiples excepciones:

```python
try:
    num1 = 5
    num2 = 0
    print(num1 / num2)
except ZeroDivisionError:
    print("No se puede dividir por cero.")
except TypeError:
    print("Los tipos de los datos no son compatibles para la operación.")
```

En este caso, si ocurre un `ZeroDivisionError` o un `TypeError`, Python ejecutará el bloque `except` correspondiente.

Es importante recordar que es una buena práctica manejar solo las excepciones que esperas y sabes cómo manejar. No es aconsejable manejar todas las excepciones de forma general, ya que puede ocultar errores en tu código.

[< Retroceder](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/9.%20Funciones/Ejercicios.md) | [Comenzar el Viaje](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/10.%20GestionErrores/1.Errores.md) | [Próxima Sección >](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/11.%20Programacion%20Orientada%20a%20Objetos/Introduccion.md)
