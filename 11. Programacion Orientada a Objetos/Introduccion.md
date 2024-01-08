# 📘 Programación Orientada a Objetos (POO) en Python

La Programación Orientada a Objetos (POO) es un paradigma de programación que se basa en el concepto de "objetos". Un objeto es una entidad que puede contener tanto datos (atributos) como comportamientos (métodos). Los objetos se crean a partir de plantillas llamadas clases.

## Clases y Objetos 🏫🔵

Una clase en Python es como un plano para crear un objeto. Define un conjunto de atributos que caracterizarán cualquier objeto que sea fabricado a partir de la clase.

Un objeto, también conocido como una instancia de una clase, es una colección de datos y métodos que operan sobre esos datos.

```python
class MiClase:
    atributo = "Soy un atributo"

objeto = MiClase()
print(objeto.atributo)  # Salida: Soy un atributo
```

## Atributos y Métodos 🏷️🛠️

Los atributos son las variables que definen las características de una clase, mientras que los métodos son funciones que definen el comportamiento de la clase.

```python
class MiClase:
    atributo = "Soy un atributo"

    def metodo(self):
        return "Soy un método"

objeto = MiClase()
print(objeto.atributo)  # Salida: Soy un atributo
print(objeto.metodo())  # Salida: Soy un método
```

## Self e Init 🤳🛠️

`self` es una referencia a la instancia actual de la clase y se utiliza para acceder a las variables y métodos de la clase.

`__init__` es un método especial que se utiliza en Python para inicializar los atributos de una clase. Se llama automáticamente cuando se crea una nueva instancia de la clase.

```python
class MiClase:
    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        return self.atributo

objeto = MiClase("Soy un atributo")
print(objeto.metodo())  # Salida: Soy un atributo
```

## Métodos Especiales 🛠️🌟

Python proporciona varios métodos especiales, también conocidos como "dunder methods" (por "double underscore"), que puedes definir para agregar funcionalidad especial a tus clases. Algunos ejemplos comunes son `__init__`, `__str__`, y `__len__`.

```python
class MiClase:
    def __init__(self, atributo):
        self.atributo = atributo

    def __str__(self):
        return self.atributo

    def __len__(self):
        return len(self.atributo)

objeto = MiClase("Soy un atributo")
print(str(objeto))  # Salida: Soy un atributo
print(len(objeto))  # Salida: 14
```

## Profundizando en POO 🏊‍♂️

A medida que te adentras en la Programación Orientada a Objetos, encontrarás conceptos más avanzados como la herencia (donde una clase puede heredar atributos y métodos de otra), la encapsulación (donde se restringe el acceso a los métodos y atributos de la clase), y el polimorfismo (donde una clase puede compartir la misma interfaz que otras clases).

La POO es un enfoque muy útil para la programación, ya que puede hacer que tu código sea más modular, más fácil de entender y de mantener, y más flexible y reutilizable.

[< Retroceder](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/10.%20GestionErrores/Introduccion.md) | [Comenzar el Viaje](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/11.%20Programacion%20Orientada%20a%20Objetos/1.ClasesObjetos.md) | [Próxima Sección >](https://github.com/YonRasgg/Curso-de-Python-Desde-Cero/blob/main/12.%20Pilares%20de%20Programacion%20Orienteda%20a%20Objetos/Introduccion.md)
