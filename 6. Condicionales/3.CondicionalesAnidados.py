nombre = input('Ingresa tu nombre en minusculas: ') # Solicita el nombre del usuario en minúsculas
edad = int(input('Ingresa tu edad: ')) # Solicita la edad del usuario

if nombre == nombre.lower(): # Si el nombre está en minúsculas
    if edad >= 18: # Si la edad es mayor o igual a 18
        print('Eres', nombre, 'y eres mayor de edad') # Imprime: Eres <nombre> y eres mayor de edad
    else: # Si la edad es menor a 18
        print('Eres', nombre, 'pero eres menor de edad') # Imprime: Eres <nombre> pero eres menor de edad
else: # Si el nombre no está en minúsculas
    print('No eres', nombre) # Imprime: No eres <nombre>