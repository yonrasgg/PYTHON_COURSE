num = '70'
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(type(num)) # Es una funcion propia de python que nos dice el tipo de dato de la variable  
print(num.isnumeric()) # Es una funcion propia de python que nos dice si el valor de la variable es numerico    
print(num.isalpha()) # Es una funcion propia de python que nos dice si el valor de la variable es alfanumerico  
print(type(int(num))) # Es una funcion propia de python que nos dice el tipo de dato de la variable 
print(type(float(num))) # Es una funcion propia de python que nos dice el tipo de dato de la variable   
print(type(str(num))) # Es una funcion propia de python que nos dice el tipo de dato de la variable 

print(len(lista)) # Es una funcion propia de python que nos dice la cantidad de elementos de la lista   
print(lista[0]) # Es una funcion propia de python que nos dice el elemento de la lista en la posicion 0 
print(max(lista)) # Es una funcion propia de python que nos dice el elemento de la lista con el valor maximo    
print(min(lista)) # Es una funcion propia de python que nos dice el elemento de la lista con el valor minimo    
print(sum(lista)) # Es una funcion propia de python que nos dice la suma de todos los elementos de la lista 
print(lista.count(1)) # Es una funcion propia de python que nos dice la cantidad de veces que se repite el elemento 1 en la lista   
print(lista.index(1)) # Es una funcion propia de python que nos dice la posicion del elemento 1 en la lista 
print(lista.append(11)) # Es una funcion propia de python que agrega el elemento 11 a la lista  
print(lista.insert(0, 0)) # Es una funcion propia de python que agrega el elemento 0 en la posicion 0 de la lista   
print(lista.pop(0)) # Es una funcion propia de python que elimina el elemento 0 de la lista 
print(lista.remove(11)) # Es una funcion propia de python que elimina el elemento 11 de la lista    
print(lista.reverse()) # Es una funcion propia de python que invierte el orden de los elementos de la lista 
print(lista.sort()) # Es una funcion propia de python que ordena los elementos de la lista de menor a mayor 
print(lista.clear()) # Es una funcion propia de python que elimina todos los elementos de la lista  
print(lista.copy()) # Es una funcion propia de python que copia todos los elementos de la lista en otra lista   
print(lista.extend([1, 2, 3])) # Es una funcion propia de python que agrega los elementos de la lista [1, 2, 3] a la lista original 
