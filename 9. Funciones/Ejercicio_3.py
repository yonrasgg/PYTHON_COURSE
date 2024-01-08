num1 = int(input('Ingrese un número: ')) # Pide un número al usuario
num2 = int(input('Ingrese otro número: ')) # Pide otro número al usuario

while True: # Bucle infinito
    if num1 > num2:
        print('1')
    elif num1 < num2:
        print('-1')     
    else:   
        print('0')  
    break # Rompe el bucle infinito