#n! = n × (n - 1) × (n - 2) × ... × 3 × 2 × 1
n = int(input('Ingrese un número entero positivo: ')) # Pide un número al usuario

def factorial(n): # Definición de la función
    if n > 0: # Verifica si el número es entero positivo
        factorial = 1 # Variable factorial inicializada en 1
        for i in range(1, n + 1): # Recorre la lista desde 1 hasta el número ingresado por el usuario + 1
            factorial *= i # Multiplica cada número de la lista por el número anterior
        print(f'El factorial de {n} es {factorial}') # Imprime el factorial del número ingresado por el usuario
    else: # Si el número no es entero positivo
        print('El número debe ser entero positivo') # Imprime un mensaje de error
        
factorial(n) # Llama a la función