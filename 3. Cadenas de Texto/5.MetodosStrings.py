cadena = 'Esto es un metodo de cadena de texto en Python'

print(cadena.upper()) # Imprime: ESTO ES UN METODO DE CADENA DE TEXTO EN PYTHON`
print(cadena.lower()) # Imprime: esto es un metodo de cadena de texto en python
print(cadena.capitalize()) # Imprime: Esto es un metodo de cadena de texto en python`
print(cadena.title()) # Imprime: Esto Es Un Metodo De Cadena De Texto En Python
print(cadena.swapcase()) # Imprime: eSTO ES UN METODO DE CADENA DE TEXTO EN pYTHON
print(cadena.replace('Python', 'C++')) # Imprime: Esto es un metodo de cadena de texto en C++
print(cadena.replace('Python', 'C++', 1)) # Imprime: Esto es un metodo de cadena de texto en C++ (Solo reemplaza la primera coincidencia)
print(cadena.count('e')) # Imprime: 6
print(cadena.count('e', 0, 15)) # Imprime: 3
print(cadena.find('e')) # Imprime: 3
print(cadena.find('e', 0, 15)) # Imprime: 3
