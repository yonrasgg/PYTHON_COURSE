class A(): # Clase Padre o Super Clase
    def __init__(self): # Metodo Constructor
        self._cuenta = 0 # Atributo de Clase
        self._contador = 0 # Atributo de Clase
    
    @property # Decorador para el metodo getter     
    def cuenta(self): # Metodo de Clase
        return self._cuenta # Retorno del Metodo de Clase
    
    @property # Decorador para el metodo getter
    def contador(self): # Metodo de Clase
        return self._contador # Retorno del Metodo de Clase
        
a = A() # Instancia de la Clase
print(a.cuenta) # Impresion del Metodo Constructor marca
print(a.contador) # Impresion del Metodo Constructor marca