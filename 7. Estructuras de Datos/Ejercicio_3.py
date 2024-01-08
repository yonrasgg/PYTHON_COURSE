student = {'name': 'John', 'age': 0, 'courses': ['Math', 'CompSci']} # Diccionario con llaves y valores

student['Grado'] = 'Junior' # Agrega una llave y un valor al diccionario
print(student) # Imprime: {'name': 'John', 'age': 0, 'courses': ['Math', 'CompSci'], 'Grado': 'Junior'}

student['age'] = int(input('Ingrese la edad de John: ')) # Solicita la edad de John
if student['age'] >= 21: # Si la edad de John es mayor o igual a 21
    print('John felicidades por tu cumpleaños No.', student['age']) # Imprime: John felicidades por tu cumpleaños No. <edad>
else: # Si la edad de John es menor a 21
    print('John, te faltan', 21 - student['age'],'años para tu cumpleaños') # Imprime: John, te faltan <años> años para tu cumpleaños
    
print(student)

student['courses'].remove('Math') # Elimina el valor 'Math' de la llave 'courses'   
print(student) # Imprime: {'name': 'John', 'age': 0, 'courses': ['CompSci'], 'Grado': 'Junior'}
