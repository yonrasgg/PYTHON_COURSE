cadena = "Este es un ejemplo de Substring (Longitud de una Cadena de Texto)"

print(len(cadena)) # Imprime: 65
print(len(cadena[0 : 15])) # Imprime: 15
print(len(cadena[0 : 15]) + len(cadena[16 : 65])) # Imprime: 64
print(len(cadena[0 : 15]) + len(cadena[16 : 65]) + 1) # Imprime: 65