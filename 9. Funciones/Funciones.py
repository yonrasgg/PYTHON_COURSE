def saludo(): # Definición de la función
    print("¡Hola, mundo!") # Cuerpo de la función
    
saludo()  # Llama a la función

def saludo_personalizado(nombre):  # 'nombre' es un parámetro
    print(f"¡Hola, {nombre}!")
    
saludo_personalizado("Alice")  # 'Alice' es un argumento

def presentacion(nombre, edad): # 'nombre' y 'edad' son parámetros
    print(f"Hola, mi nombre es {nombre} y tengo {edad} años.") # 'nombre' y 'edad' son argumentos
    
presentacion("Bob", 25) # 'Bob' y '25' son argumentos