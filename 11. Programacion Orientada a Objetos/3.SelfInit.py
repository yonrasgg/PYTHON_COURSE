class FabricaCarros(): # Clase Padre o Super Clase
    def __init__(self, marca, color): # Metodo Constructor
        self.marca = marca # Atributo de Clase
        self.color = color # Atributo de Clase
        print("Se ha creado un nuevo carro") # Impresion del Metodo Constructor
        
carro = FabricaCarros('Toyota', 'Rojo') # Instancia de la Clase
carro2 = FabricaCarros('Subaru', 'Azul') # Instancia de la Clase

print(carro.marca) # Toyota 
print(carro.color) # Rojo 
print(carro2.marca) # Subaru      
print(carro2.color) # Azul  