conjunto = {1, 2, 3, 4, 5} # Conjunto de números enteros    
conjunto2 = [(1, 2), (3, 4), (5, 6)] # Conjunto de tuplas
conjunto3 = (1, 2, 3, 4, 5) # Tupla de números enteros

print(conjunto) # Imprime: {1, 2, 3, 4, 5}  
print(type(conjunto)) # Imprime: <class 'set'>  
print(list(conjunto)) # Imprime: [1, 2, 3, 4, 5]
print(type(list(conjunto))) # Imprime: <class 'list'>
print(tuple(conjunto)) # Imprime: (1, 2, 3, 4, 5)

print(conjunto2) # Imprime: [(1, 2), (3, 4), (5, 6)]    
print(type(conjunto2)) # Imprime: <class 'list'>    
print(set(conjunto2)) # Imprime: {(1, 2), (3, 4), (5, 6)}
print(type(set(conjunto2))) # Imprime: <class 'set'>    
print(dict(conjunto2)) # Imprime: {1: 2, 3: 4, 5: 6}

print(conjunto3) # Imprime: (1, 2, 3, 4, 5)
print(type(conjunto3)) # Imprime: <class 'tuple'>
print(list(conjunto3)) # Imprime: [1, 2, 3, 4, 5]
print(type(list(conjunto3))) # Imprime: <class 'list'>
print(set(conjunto3)) # Imprime: {1, 2, 3, 4, 5}
print(type(set(conjunto3))) # Imprime: <class 'set'>
print(dict(conjunto3)) # Imprime: {1: 2, 3: 4, 5: 6}
print(type(dict(conjunto3))) # Imprime: <class 'dict'>
print(tuple(conjunto3)) # Imprime: (1, 2, 3, 4, 5)
