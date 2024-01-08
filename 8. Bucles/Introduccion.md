# 🔄 Bucles en Python 🐍

Un bucle, o _loop_ en inglés, nos permite repetir un bloque de código una y otra vez, como si estuviéramos en un carrusel de código 🎠. Python nos ofrece dos tickets para este carrusel: los bucles `while` y `for`.

## [🔄 El bucle `while`](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/8.%20Bucles/1.While.md)

El bucle `while` es nuestro carrusel que gira mientras una condición sea verdadera. Es como decir: "Mientras tenga energía, seguiré bailando 💃".

```python
energia = 5
while energia > 0:
    print("¡Sigo bailando!")
    energia -= 1
```

En este ejemplo, la fiesta sigue hasta que la energía llega a cero.

## [🔄 El bucle `for`](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/8.%20Bucles/2.For.md)

El bucle `for` es un carrusel que da un número específico de vueltas. Es como decir: "Daré 5 vueltas alrededor del parque 🏞️".

```python
for vuelta in range(5):
    print("Dando la vuelta número", vuelta+1)
```

Aquí, el bucle `for` se lleva a cabo para un rango de 5, imprimiendo el número de vuelta en cada iteración.

## [🎯 La función `range()`](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/8.%20Bucles/3.Range.md)

La función `range()` es el camino que seguimos en nuestro carrusel. Puede tener diferentes longitudes y ritmos:

- `range(n)` genera números desde 0 hasta n-1.
- `range(m, n)` genera números desde m hasta n-1.
- `range(m, n, p)` genera números desde m hasta n-1 con pasos de p.

```python
for paso in range(1, 10, 2):
    print("Dando el paso número", paso)
```

Aquí, seguimos el camino desde 1 hasta 9, pero sólo en pasos de 2.

## [⏭️🛑 La sentencia `continue`& `break` en Python 🐍](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/8.%20Bucles/4.ContinueBreak.md)

La sentencia `continue` es nuestro botón de "salto" 🦘. Nos permite saltar sobre algunas partes de nuestro camino.

```python
for num in range(5):
    if num == 3:
        continue
    print("Número", num)
```

Aquí, saltamos sobre el número 3 y continuamos con el siguiente número.

La sentencia `break` es nuestra parada de emergencia 🚦. Nos permite detener el carrusel completamente.

```python
vueltas = 0
while True:
    print("Vueltas", vueltas)
    vueltas += 1
    if vueltas >= 5:
        break
```

Aquí, aunque nuestro carrusel podría girar infinitamente, decidimos pararlo después de 5 vueltas.

## [💡 Ejercicios](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/8.%20Bucles/Ejercicios.md)

¡Es hora de poner a prueba tus habilidades de programación con Python! A continuación, se presentan algunos ejercicios diseñados para ayudarte a entender mejor los conceptos de bucles y control de flujo.

Espero que hayas disfrutado de este viaje por los bucles en Python. ¡Nos vemos en la próxima sección! 🚀🐍🏋️

[< Retroceder](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/7.%20Estructuras%20de%20Datos/Ejercicios.md) | [Comenzar el Viaje](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/8.%20Bucles/1.While.md) | [Próxima Sección >](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/9.%20Funciones/Introduccion.md)
