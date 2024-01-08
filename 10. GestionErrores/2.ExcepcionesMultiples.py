# Video: 37. Excepciones múltiples
while(True): 
    try:
        num1 = int(input("Introduce el primer número: "))
        resultado = 10/num1
        print("El resultado es: ", resultado)   
        break
    except ZeroDivisionError:
        print("No se puede dividir entre 0")

# El bloque finally se ejecuta siempre, tanto si se ha producido un error como si no.       
while(True):
    try:
        edad = int(input("Introduce tu edad: "))
        print("Tu edad es: ", edad) 
        break   
    except ValueError:  
        print('Has introducido un valor erróneo')   

# KeyboardInterrupt se produce cuando se pulsa Ctrl+C.       
while(True):    
    try:
        nombre = input("Introduce tu nombre: ")
        print(nombre)
        break
    except KeyboardInterrupt:
        print("Has cancelado la ejecución") 
        break   

# EOFError se produce cuando se intenta leer más allá del final de un archivo. 
while(True):    
    try:
        nombre = input("Introduce tu nombre: ")
        print(nombre)
        break
    except EOFError:
        print("Has cancelado la ejecución") 
        break   

while(True):    
    try:
        nombre = input("Introduce tu nombre: ")
        print(nombre)
        break
    except Exception as e:
        print(type(e).__name__) 
        break   

# De esta forma, podemos capturar varios tipos de excepciones en un mismo bloque try-except.   
while(True):    
    try:
        edad = int(input("Introduce tu edad: "))    
        promedio = 10/edad  
        print("Tu edad es: ", edad) 
        print("El promedio de edad es: ", promedio) 
        break
    except ArithmeticError as e:    
        print("Error aritmético: ", type(e).__name__) 
        break   
    except ValueError as e: 
        print("Error de valor: ", type(e).__name__) 
        break   
    except Exception as e:  
        print("Error: ", type(e).__name__) 
        break   
    finally: 
        print("Fin de la iteración") 
        break   
