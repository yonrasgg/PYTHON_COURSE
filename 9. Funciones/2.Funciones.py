def saludo(): # Definición de la función
    print("¡Hola, desde el curso de python en github!") # Cuerpo de la función

saludo()  # Llama a la función

nombre = input("Ingrese su nombre: ") # Pide un nombre al usuario

def saludo_personalizado(nombre):  # 'nombre' es un parámetro   
    print(f"¡Hola, {nombre}!") # Cuerpo de la función
    
saludo_personalizado(nombre)  # 'nombre' es un argumento

def tabla5(): # Definición de la función 
    for i in range(10): # Recorre la lista tabla5
        print(f"5 * {i} = {5 * i}") # Imprime cada número de la lista tabla5
        
tabla5() # Llama a la función