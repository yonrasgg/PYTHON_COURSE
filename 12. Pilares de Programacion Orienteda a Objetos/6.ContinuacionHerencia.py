class Animales(): #Clase Padre
    def __init__(self, nombre): #Metodo Constructor
        self.nombre = nombre #Atributo
        
class Perro(Animales):  #Clase Hija
    def __init__(self, nombre, sonido): #Metodo Constructor
        super().__init__(nombre) #Atributo
        self.sonido = sonido #Atributo
        
perro = Perro('Chaac', 'Raawff Raawff') #Instancia
print(perro.nombre) # No es la forma correcta de imprimir los atributos de una clase
print(perro.sonido) # No es la forma correcta de imprimir los atributos de una clase