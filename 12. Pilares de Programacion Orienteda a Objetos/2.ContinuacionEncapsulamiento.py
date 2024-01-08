class A():
    def __init__(self):
        self._contador = 0
        
    def incrementar(self):
        self._contador += 1
        
    def cuenta(self):
        return self._contador

a = A()
print(a.cuenta()) # Imprime: 0
a._cuenta = 5 # No es la manera correcta de cambiar el valor de un atributo privado
print(a.cuenta()) # Imprime: 5
#print(a._contador) # Imprime: 0
#a.incrementar()
#print(a._contador) # Imprime: 1
#a._contador = 5
#print(a._contador) # Imprime: 5
