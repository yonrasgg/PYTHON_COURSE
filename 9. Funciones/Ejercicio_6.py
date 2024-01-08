lista = [] # Creamos una lista vacia

def calcular_mediana(): # Definimos la funcion calcular_mediana
    iteraciones = int(input("Cuantos numeros desea ingresar? ")) # Pedimos la cantidad de numeros que se van a ingresar
    for i in range(iteraciones): # Iteramos la cantidad de veces que se ingresaron numeros
        lista.append(int(input("Ingrese un numero: "))) # Pedimos el numero y lo agregamos a la lista
    lista.sort() # Ordenamos la lista    
    if iteraciones % 2 == 0: # Si la cantidad de numeros es par     
        mediana = (lista[iteraciones // 2] + lista[iteraciones // 2 - 1]) / 2 # Calculamos la mediana
    else: # Si la cantidad de numeros es impar
        mediana = lista[iteraciones // 2] # Calculamos la mediana
    print("La mediana es: ", mediana) # Imprimimos la mediana   
    print("La lista es: ", lista) # Imprimimos la lista   
    lista.clear() # Limpiamos la lista para que no se acumulen los numeros
    
calcular_mediana() # Llamamos a la funcion calcular_mediana para que se ejecute
