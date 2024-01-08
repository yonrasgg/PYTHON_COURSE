fruits = {'apple', 'banana', 'cherry', 'apple', 'cherry'}

fruits.add('orange') # Agrega un elemento al conjunto
print(fruits) # Imprime: {'banana', 'cherry', 'orange', 'apple'}

fruits.remove('banana') # Elimina un elemento del conjunto
print(fruits) # Imprime: {'cherry', 'orange', 'apple'}

fruits = list(fruits) # Convierte el conjunto en una lista
print(fruits[2]) # Imprime: 'apple'
