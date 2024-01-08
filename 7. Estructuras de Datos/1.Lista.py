lista = ['Python', 420, 'Nombre', 220, 110, 'Apellido']

print(type(lista)) # Imprime: <class 'list'>
print(lista[2]) # Imprime: Nombre   
print(lista[1:4]) # Imprime: [420, 'Nombre', 220]   
print(lista[-1]) # Imprime: Apellido    
print(lista[::2]) # Imprime: ['Python', 'Nombre', 110]  
print(lista[::-1]) # Imprime: ['Apellido', 110, 220, 'Nombre', 420, 'Python']   
print(lista + lista[::-1]) # Imprime: ['Python', 420, 'Nombre', 220, 110, 'Apellido', 'Apellido', 110, 220, 'Nombre', 420, 'Python']
lista[0] = 'python' # Cambia el valor de la posición 0 de la lista  
print(lista) # Imprime: ['python', 420, 'Nombre', 220, 110, 'Apellido'] 
lista.append('2do Apellido') # Agrega un elemento al final de la lista  
print(lista) # Imprime: ['python', 420, 'Nombre', 220, 110, 'Apellido', '2do Apellido'] 
lista.insert(2, '2do Nombre') # Agrega un elemento en la posición 2 de la lista 
print(lista) # Imprime: ['python', 420, '2do Nombre', 'Nombre', 220, 110, 'Apellido', '2do Apellido']   
lista.pop() # Elimina el último elemento de la lista    
print(lista) # Imprime: ['python', 420, '2do Nombre', 'Nombre', 220, 110, 'Apellido']   
lista.pop(2) # Elimina el elemento de la posición 2 de la lista 
print(lista) # Imprime: ['python', 420, 'Nombre', 220, 110, 'Apellido'] 
lista.remove(220) # Elimina el elemento 220 de la lista 
print(lista) # Imprime: ['python', 420, 'Nombre', 110, 'Apellido']  
lista.reverse() # Invierte el orden de la lista 
print(lista) # Imprime: ['Apellido', 110, 'Nombre', 420, 'python']  
lista.sort() # Ordena la lista  
print(lista) # Imprime: [110, 420, 'Apellido', 'Nombre', 'python']  
lista.clear() # Elimina todos los elementos de la lista 
print(lista) # Imprime: []  
lista = ['Python', 420, 'Nombre', 220, 110, 'Apellido'] 
print(lista) # Imprime: ['Python', 420, 'Nombre', 220, 110, 'Apellido'] 
del lista[0] # Elimina el elemento de la posición 0 de la lista 
print(lista) # Imprime: [420, 'Nombre', 220, 110, 'Apellido']   
del lista # Elimina la lista    
print(lista) # Imprime: NameError: name 'lista' is not defined  
