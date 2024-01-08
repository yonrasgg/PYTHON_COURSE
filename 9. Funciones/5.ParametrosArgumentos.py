def suma(num1, num2):
    suma = num1 + num2
    return suma

print(suma(5, 10)) # 15
print(suma(10, 20)) # 30    
print(suma(20, 30)) # 50    
print(type(suma(5, 10))) # <class 'int'>    
print(suma(5.5, 10.5)) # 16.0   
print(type(suma(5.5, 10.5))) # <class 'float'>  
print(suma('Hola ', 'Mundo')) # Hola Mundo  
print(type(suma('Hola ', 'Mundo'))) # <class 'str'> 
print(suma([1,2,3], [4,5,6])) # [1, 2, 3, 4, 5, 6]  
print(type(suma([1,2,3], [4,5,6]))) # <class 'list'>    
print(suma((1,2,3), (4,5,6))) # (1, 2, 3, 4, 5, 6)  
print(type(suma((1,2,3), (4,5,6)))) # <class 'tuple'>   
print(suma({'nombre':'Juan'}, {'apellido':'Perez'})) # {'nombre': 'Juan', 'apellido': 'Perez'}  
print(type(suma({'nombre':'Juan'}, {'apellido':'Perez'}))) # <class 'dict'> 
print(suma(True, False)) # 1    
print(type(suma(True, False))) # <class 'int'>  
print(suma(None, None)) # None  
print(type(suma(None, None))) # <class 'NoneType'>  
print(suma(5, 10) + suma(10, 20)) # 45
    
    