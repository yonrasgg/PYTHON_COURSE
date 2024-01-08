cadena1 = 'Hola, mundo!'
cadena2 = "Bienvenido a Python"
numero1 = 5

print(cadena1 + cadena2) # Imprime: Hola, mundo!Bienvenido a Python
print(cadena1 + ' ' + cadena2) # Imprime: Hola, mundo! Bienvenido a Python
print(cadena1 + ' ' + cadena2 + ' ' + 'desde Cero') # Imprime: Hola, mundo! Bienvenido a Python desde Cero
print(cadena1 * 3) # Imprime: Hola, mundo!Hola, mundo!Hola, mundo!
print(cadena1 * 3 + cadena2) # Imprime: Hola, mundo!Hola, mundo!Hola, mundo!Bienvenido a Python
print(numero1, cadena1) # Imprime: 5 Hola, mundo!
print(type(str(numero1) + cadena1)) # Imprime: <class 'str'>