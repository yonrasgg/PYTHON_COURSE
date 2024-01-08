cadena = 'Estoy mostrando un ejemplo de un método booleano para strings'
cadena2 = 'estoy mostrando un ejemplo de un método booleano para strings'
cadena3 = 'ESTOY MOSTRANDO UN EJEMPLO DE UN MÉTODO BOOLEANO PARA STRINGS'
cadena4 = '1234567890'

print(cadena.startswith('Estoy')) # Imprime: True
print(cadena.endswith('strings')) # Imprime: True
print(cadena.isalnum()) # Imprime: False
print(cadena4.isalnum()) # Imprime: True
print(cadena.isalpha()) # Imprime: False
print(cadena.isdigit()) # Imprime: False
print(cadena2.islower()) # Imprime: True
print(cadena3.isupper()) # Imprime: True