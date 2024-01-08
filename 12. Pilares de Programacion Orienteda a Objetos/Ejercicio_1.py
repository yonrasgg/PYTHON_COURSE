class Estudiante(): #Clase Padre
    def __init__(self, nombre, nota): #Metodo Constructor
        self.nombre = nombre #Atributo
        self.nota = nota #Atributo
        
    @property #Metodo Getter
    def nombre(self): #Metodo
        return self._nombre #Atributo 
    
    @nombre.setter #Metodo Setter  
    def nombre(self, nombre): #Metodo   
        self._nombre = nombre #Atributo   
    
    @property #Metodo Getter
    def nota(self): #Metodo
        return self._nota #Atributo   
    
    @nota.setter #Metodo Setter    
    def nota(self, nota): #Metodo   
        self._nota = nota #Atributo   
        
    def imprimir(self): #Metodo
        print('Nombre: {}'.format(self.nombre)) #Atributo
        print('Nota: {}'.format(self.nota)) #Atributo

    def resultados(self): #Metodo
        if self.nota >= 7: #Condicion
            print('El estudiante {} aprobo'.format(self.nombre)) #Atributo
        else: #Condicion
            print('El estudiante {} reprobo'.format(self.nombre)) #Atributo
            
estudiante1 = Estudiante('Juan', 8) #Instancia 
estudiante1.imprimir() #Metodo  
estudiante1.resultados() #Metodo    
print('') #Salto de linea   
estudiante2 = Estudiante('Maria', 6) #Instancia    
estudiante2.imprimir() #Metodo  
estudiante2.resultados() #Metodo    
print('') #Salto de linea