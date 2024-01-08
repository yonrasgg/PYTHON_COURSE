num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Lista de números del 1 al 10

for i in num1: # Recorre la lista num1
    print(i) # Imprime cada número de la lista

num2 = int(input('Ingrese un número: ')) # Pide un número al usuario
num3 = int(input('Ingrese otro número: ')) # Pide otro número al usuario

for i in range(num2, num3 + 1): # Recorre la lista num1 desde el número ingresado por el usuario hasta el número ingresado por el usuario + 1
    print(i) # Imprime cada número de la lista generada por el rango ingresado por el usuario en num2 y num3

