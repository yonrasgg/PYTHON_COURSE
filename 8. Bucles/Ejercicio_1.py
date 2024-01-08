numero = int(input("Ingrese un numero: ")) # Solicita un numero

i = 0
multiplicacion = 0 

while i <= 10: # Mientras i sea menor o igual a 10
    multiplicacion = numero * i # Multiplica el numero por i
    print(numero, "x", i, "=", multiplicacion) # Imprime: <numero> x <i> = <multiplicacion>
    i += 1 # Suma 1 a i