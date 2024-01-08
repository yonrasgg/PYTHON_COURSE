while True: # Bucle infinito hasta que se cumpla una condición de salida
    nombre = input('Ingrese su nombre (o "salir" para terminar): ')
    
    if nombre.lower() == 'salir': # Si el usuario ingresa "salir", se rompe el bucle
        break
    
    fecha_nacimiento = input('Ingrese su fecha de nacimiento (dd/mm/aaaa): ')   

    fecha_nacimiento = fecha_nacimiento.split('/') # Separa la fecha de nacimiento en una lista con 3 elementos 
    fecha_nacimiento = list(map(int, fecha_nacimiento)) # Convierte los elementos de la lista en enteros    
    
    print(f'Hola {nombre}, tienes {2023 - fecha_nacimiento[2]} años') # Imprime la cantidad de años que tiene la persona
