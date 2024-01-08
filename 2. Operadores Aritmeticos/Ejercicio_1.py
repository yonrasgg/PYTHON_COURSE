# Variables

a = 2
b = 7
c = 8

#Ejemplo 1

suma = a + b
multiplicacion = a * c

ejemplo1 = (suma/multiplicacion)**a

print(f"El resultado del ejemplo 1 es: {ejemplo1}") # Resultado 0.31640625


#Ejemplo 2

ejemplo2 = ((a + b) / (a * c)) ** a

print(f"El resultado del ejemplo 2 es: {ejemplo2}") # Resultado 0.31640625


# Ejemplo 3

ejemplo3 = pow((a + b) / (a * c), a)

print(f"El resultado del ejemplo 3 es: {ejemplo3}") # Resultado 0.31640625


# Ejemplo 4

print((2+7)/(2*8)**2) # Resultado 0.00390625