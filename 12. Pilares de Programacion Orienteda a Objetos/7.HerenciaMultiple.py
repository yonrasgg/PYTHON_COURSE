class A(): #Clase Padre
    def primera(self): #Metodo
        return 'Esta es la clase A' #Atributo
    
class B(): #Clase Padre
    def segunda(self): #Metodo
        return 'Esta es la clase B' #Atributo
    
class C(A, B): #Clase Hija
    pass #No hace nada

c = C() #Instancia
print(c.primera()) #Metodo
print(c.segunda()) #Metodo