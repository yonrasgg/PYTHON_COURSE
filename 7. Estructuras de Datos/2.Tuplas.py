tupla = ('Python', 420, 'Nombre', 220, 110, 'Apellido')

print(type(tupla)) # Imprime: <class 'tuple'>
print(tupla[2]) # Imprime: Nombre   
print(tupla[1:4]) # Imprime: (420, 'Nombre', 220)   
print(tupla[-1]) # Imprime: Apellido
print(tupla[::2]) # Imprime: ('Python', 'Nombre', 110)
print(tupla[::-1]) # Imprime: ('Apellido', 110, 220, 'Nombre', 420, 'Python')
print(tupla + tupla[::-1]) # Imprime: ('Python', 420, 'Nombre', 220, 110, 'Apellido', 'Apellido', 110, 220, 'Nombre', 420, 'Python')
tupla2 = tuple('python') # Convierte la cadena 'python' en una tupla
print(tupla2) # Imprime: ('p', 'y', 't', 'h', 'o', 'n')