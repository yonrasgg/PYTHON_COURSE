class FabricaCarros(): # Clase Padre o Super Clase
    marca = "Toyota" # Atributo de Clase
    color = "Rojo" # Atributo de Clase
    puertas = 4 # Atributo de Clase 
    llantas = 4 # Atributo de Clase
    combustible = "Gasolina" # Atributo de Clase    
    
    def manejar(self, mensaje): # Metodo de Clase
        return mensaje # Retorno del Metodo de Clase
    
    def frenar(self): # Metodo de Clase 
        print("El carro esta frenando") # Impresion del Metodo de Clase
    
carro = FabricaCarros() # Instancia de la Clase 
carro.marca 
carro.color
carro.puertas
carro.llantas   
carro.combustible

print(carro.manejar("Estoy manejando un carro")) # Impresion del Metodo de Clase
carro.frenar() # Impresion del Metodo de Clase