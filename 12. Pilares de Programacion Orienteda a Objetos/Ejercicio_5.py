class Universidad(): #Clase Padre
    
    def nombre(self): #Metodo
        print('Universidad Autodidacta') #Atributo
        
class Carrera(): #Clase Padre
    
    def especialidad(self): #Metodo
        print('Programacion') #Atributo
        
class Estudiante(Universidad, Carrera): #Clase Hija
    
    @property #Metodo Getter
    def nombre_estudiante(self): #Metodo
        nombre_estudiante = input('Ingrese su nombre: ') #Atributo
        return nombre_estudiante #Atributo
    
    def edad (self): #Metodo
        print('25') #Atributo
    
persona = Estudiante() #Instancia
print(persona.nombre_estudiante) #Metodo
Estudiante().edad() #Metodo
Estudiante().especialidad() #Metodo
Estudiante().nombre() #Metodo