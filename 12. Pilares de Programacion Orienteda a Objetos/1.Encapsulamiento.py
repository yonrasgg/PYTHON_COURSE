class A(): # Clase Padre o Super Clase
    def __init__(self): # Metodo Constructor
        self.contador = 0 # Atributo de Clase
    
    def incrementar(self): # Metodo de Clase
        self.contador += 1 # Retorno del Metodo de Clase
        
    def cuenta(self): # Metodo de Clase
        return self.contador # Retorno del Metodo de Clase
    
class B(): # Clase Padre o Super Clase
    def __init__(self): # Metodo Constructor
        self.__contador = 0 # Atributo de Clase
    
    def incrementar(self): # Metodo de Clase
        self.__contador += 1 # Retorno del Metodo de Clase
        
    def cuenta(self): # Metodo de Clase
        return self.__contador # Retorno del Metodo de Clase

print('Objeto A') # Impresion del Metodo Constructor marca 
a = A() # Instancia de la Clase
print(a.cuenta()) # Impresion del Metodo Constructor marca
a.incrementar() # Impresion del Metodo Constructor marca
print(a.cuenta()) # Impresion del Metodo Constructor marca
print(a.contador) # Esto es incorrecto es clasificado como una mala practica, no deberia ser accesible desde fuera de la clase

print('Objeto B') # Impresion del Metodo Constructor marca
b = B() # Instancia de la Clase
print(b.cuenta()) # Impresion del Metodo Constructor marca
b.incrementar() # Impresion del Metodo Constructor marca
print(b.cuenta()) # Impresion del Metodo Constructor marca
print(b.__contador) # El atributo contador no es accesible desde fuera de la clase debido a que es privado '__contador'