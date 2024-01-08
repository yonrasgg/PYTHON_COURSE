import math # Importamos la libreria math para poder usar la funcion pi y pow

def area_cuadrado(base, altura): # Definimos la funcion area_cuadrado
    area = base * altura # Calculamos el area
    return area # Retornamos el area

def area_circulo(radio): # Definimos la funcion area_circulo
    area = math.pi * (pow(radio, 2)) # Calculamos el area
    return area # Retornamos el area

def area_triangulo(base, altura): # Definimos la funcion area_triangulo 
    area = (base * altura) / 2 # Calculamos el area 
    return area # Retornamos el area    

def main(): # Definimos la funcion main
    opcion = input("1. Cuadrado \n2. Circulo \n3. Triangulo \nDesea calcular el area de un cuadrado, un circulo o un Triangulo?") # Pedimos la opcion
    global base, altura, radio # Definimos las variables como globales
    if opcion == "1": # Si la opcion es 1   
        base = float(input("Ingrese la base del cuadrado: ")) # Pedimos la base 
        altura = float(input("Ingrese la altura del cuadrado: ")) # Pedimos la altura   
        print("El area del cuadrado es: ", area_cuadrado(base, altura)) # Imprimimos el area del cuadrado   
    elif opcion == "2": # Si la opcion es 2 
        radio = float(input("Ingrese el radio del circulo: ")) # Pedimos el radio   
        print("El area del circulo es: ", area_circulo(radio)) # Imprimimos el area del circulo 
    elif opcion == "3": # Si la opcion es 3 
        base = float(input("Ingrese la base del triangulo: ")) # Pedimos la base    
        altura = float(input("Ingrese la altura del triangulo: ")) # Pedimos la altura  
        print("El area del triangulo es: ", area_triangulo(base, altura)) # Imprimimos el area del triangulo    
    else: # Si la opcion no es 1 ni 2   
        print("Opcion invalida") # Imprimimos que la opcion es invalida 
        
main() # Llamamos a la funcion main para que se ejecute