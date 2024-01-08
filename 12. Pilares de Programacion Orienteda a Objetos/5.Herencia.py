class Animales(): #Clase Padre
    def habla(self): #Metodo
        print('El animal hace ruido') #Atributo
        
    def descripcion(self): #Metodo
        print('Es un {}'.format(self.animal)) #Atributo
        
class Perro(Animales): #Clase Hija
    pass #No hace nada

class Abeja(Animales): #Clase Hija
    def __init__(self, animal): #Metodo Constructor
        self.animal = animal #Atributo

animal = Animales() #Instancia
animal.habla() #Metodo

perro = Perro() #Instancia
perro.habla() #Metodo

abeja = Abeja('abeja') #Instancia
abeja.descripcion() #Metodo