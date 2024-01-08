class Animales(): #Clase Padre
    def __init__(self, mensaje): #Metodo Constructor
        self.mensaje = mensaje #Atributo
        
    def hablar(self): #Metodo
        print(self.mensaje) #Atributo
        
class Perro(Animales): #Clase Hija
    def hablar(self): #Metodo
        print('Raawff Raawff') #Atributo
        
class Gato(Animales): #Clase Hija
    def hablar(self): #Metodo
        print('Miau Miau') #Atributo
        
class Vaca(Animales): #Clase Hija
    def hablar(self): #Metodo 
        print('Muu Muu') #Atributo
        
perro = Perro('Raawff Raawff Raawff')# Se imprime el mensaje de la clase padre
perro.hablar() # Se imprime el mensaje de la clase hija

animal = Animales('Miaw Miaw Miaw') # Se imprime el mensaje de la clase padre
animal.hablar() # Se imprime el mensaje de la clase padre

gato = Gato('Miau Miau Miau') # Se imprime el mensaje de la clase padre
gato.hablar() # Se imprime el mensaje de la clase hija