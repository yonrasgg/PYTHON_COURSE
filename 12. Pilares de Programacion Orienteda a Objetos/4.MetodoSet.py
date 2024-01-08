class A(): # Clase Padre o Super Clase
    def __init__(self): # Metodo Constructor
        self._cuenta = 0 # Atributo de Clase
        self._contador = 0 # Atributo de Clase
    
    @property # Decorador para el metodo getter     
    def cuenta(self): # Metodo de Clase
        return self._cuenta # Retorno del Metodo de Clase
    
    @cuenta.setter # Decorador para el metodo setter
    def cuenta(self, cuenta): # Metodo de Clase
        self._cuenta = cuenta # Retorno del Metodo de Clase
    
    @property # Decorador para el metodo getter
    def contador(self): # Metodo de Clase
        return self._contador # Retorno del Metodo de Clase
    
    @contador.setter # Decorador para el metodo setter  
    def contador(self, contador): # Metodo de Clase
        self._contador = contador # Retorno del Metodo de Clase
        
a = A() # Instancia de la Clase
print(a.cuenta) # Impresion del Metodo Constructor marca
a.cuenta = 10 # Impresion del Metodo Constructor marca
print(a.cuenta) # Impresion del Metodo Constructor marca
print(a.contador) # Impresion del Metodo Constructor marca
a.contador = 20 # Impresion del Metodo Constructor marca
print(a.contador) # Impresion del Metodo Constructor marca