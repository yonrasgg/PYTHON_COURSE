# 📚 Guía de Cadenas de Texto en Python 🐍

¡Bienvenido a esta guía introductoria a las cadenas de texto en Python! Las cadenas de texto, también conocidas como `str`, son una parte esencial de la programación en Python. Son utilizadas para representar texto y se pueden crear usando comillas simples, dobles o triples. ¡Empecemos!

## [🎉 Crear una Cadena de Texto][def]

En Python, puedes crear una cadena de texto simplemente colocando texto entre comillas:

```python
cadena1 = 'Hola, mundo!'
cadena2 = "Bienvenido a Python"
```

>Sigue viendo la explicación para Crear una Cadena de Texto [aquí][def]

## [👥 Concatenación de Cadenas de Texto][def2]

Puedes unir dos o más cadenas de texto en una sola utilizando el operador `+`:

```python
saludo = 'Hola' + ', mundo!'
print(saludo)  # Esto imprimirá: Hola, mundo!
```

>Sigue viendo la explicación para Concatenación de Cadenas de Texto [aquí][def2]

## [📏 Longitud de una Cadena de Texto][def3]

Puedes obtener la longitud de una cadena de texto utilizando la función `len`:

```python
cadena = 'Python'
print(len(cadena))  # Esto imprimirá: 6
```

>Sigue viendo la explicación para Longitud de una Cadena de Texto [aquí][def3]

## [🎯 Acceder a los Caracteres de una Cadena de Texto][def4]

Puedes acceder a un carácter específico en una cadena de texto utilizando su índice. Los índices en Python comienzan en 0:

```python
cadena = 'Python'
print(cadena[0])  # Esto imprimirá: P
```

>Seguir viendo la explicación para Acceder alos Caracteres de una Cadena de Texto [aquí][def4]

## [🔄 Métodos de las Cadenas de Texto][def5]

Las cadenas de texto en Python vienen con muchos métodos útiles incorporados. Aquí hay algunos ejemplos:

- **`upper()`:** Convierte la cadena de texto a mayúsculas.
- **`lower()`:** Convierte la cadena de texto a minúsculas.
- **`replace(old, new)`:** Reemplaza todas las ocurrencias de la cadena de texto `old` con la cadena de texto `new`.
- **`split(delimiter)`:** Divide la cadena de texto en una lista de cadenas de texto usando `delimiter` como el carácter delimitador.

```python
cadena = 'Python es genial'
print(cadena.upper())  # Esto imprimirá: PYTHON ES GENIAL
print(cadena.lower())  # Esto imprimirá: python es genial
print(cadena.replace('genial', 'increíble'))  # Esto imprimirá: Python es increíble
print(cadena.split(' '))  # Esto imprimirá: ['Python', 'es', 'genial']
```

>Sigue viendo la explicación para Métodos de las Cadenas de Texto [aqui][def]

## [🏋️ Ejercicios de Práctica][def6]

¡Pon en práctica lo que has aprendido con algunos ejercicios de codificación de cadenas de texto! Encontrarás estos ejercicios [aqui][def6].

¡Eso es todo por ahora! Espero que esta guía te haya ayudado a entender mejor las cadenas de texto en Python. ¡Sigue practicando y explorando! 🚀🐍💻

[< Retroceder](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/2.%20Operadores%20Aritmeticos/Ejecercicios.md) | [Comenzar el Viaje](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/3.%20Cadenas%20de%20Texto/1.Strings.md) | [Próxima Sección >](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/4.%20Entrada%20y%20Salida%20por%20Teclado/Introduccion.md)

[def]: https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/3.%20Cadenas%20de%20Texto/1.Strings.md
[def2]: https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/3.%20Cadenas%20de%20Texto/2.ConcatenacionStrings.md
[def3]: https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/3.%20Cadenas%20de%20Texto/3.LongitudStrings.md
[def4]: https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/3.%20Cadenas%20de%20Texto/4.SubStrings.md
[def5]: https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/3.%20Cadenas%20de%20Texto/5.MetodosStrings.md
[def6]: https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/3.%20Cadenas%20de%20Texto/Ejercicios.md
