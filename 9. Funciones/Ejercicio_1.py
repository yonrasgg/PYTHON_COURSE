lista = [] # Lista vacía
num = 0 # Variable num inicializada en 0

def ingrese_numero(): # Definición de la función
    i = 0 # Variable i inicializada en 0
    while i < 10: # Mientras i sea menor a 10
        num = int(input('Ingrese un número: ')) # Pide un número al usuario
        lista.append(num) # Agrega el número ingresado por el usuario a la lista
        i += 1 # Incrementa i en 1
        
def mostrar_lista(): # Definición de la función
    lista.sort() # Ordena los elementos de la lista de menor a mayor
    pares = [] # Lista vacía
    imapares = [] # Lista vacía
    for i in lista: # Recorre la lista
        if i % 2 == 0: # Verifica si el número es par
            pares.append(i) # Agrega el número par a la lista pares
        else: # Si el número no es par
            imapares.append(i) # Agrega el número impar a la lista imapares
    print(f'Lista de números pares: {pares}') # Imprime la lista pares
    print(f'Lista de números impares: {imapares}') # Imprime la lista imapares
    
ingrese_numero() # Llama a la función
mostrar_lista() # Llama a la función
