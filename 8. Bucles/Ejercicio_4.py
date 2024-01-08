num1 = int(input('Ingrese un número: ')) # Pide un número al usuario
num2 = int(input('Ingrese otro número: ')) # Pide otro número al usuario

for i in range(num1, num2 + 1): # Recorre la lista num1 desde el número ingresado por el usuario hasta el número ingresado por el usuario + 1
    if i % 2 == 0: # Verifica si el número es par
        print(i) # Si el número es par, imprime el número