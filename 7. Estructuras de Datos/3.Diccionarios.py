diccionario = {'Usuario': 'agfare', 'Contrasenia': 123456}
 
print(diccionario) # Imprime: {'Usuario': 'agfare', 'Contrasenia': 123456}
print(type(diccionario)) # Imprime: <class 'dict'>
print(diccionario['Usuario']) # Imprime: agfare   
print(diccionario['Contrasenia']) # Imprime: 123456   
print(diccionario.get('Usuario')) # Imprime: agfare   
print(diccionario.get('Contrasenia')) # Imprime: 123456   
print(diccionario.get('Usuario', 'No existe')) # Imprime: agfare   
print(diccionario.get('Contrasenia', 'No existe')) # Imprime: 123456  
diccionario['Usuario'] = 'agdddare' # Modifica el valor de la llave Usuario   
diccionario['Contrasenia'] = 35646 # Modifica el valor de la llave Contrasenia
print(diccionario) # Imprime: {'Usuario': 'agdddare', 'Contrasenia': 35646}