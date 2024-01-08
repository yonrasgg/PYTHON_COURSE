class FabricaCarros(): # Clase Padre o Super Clase
    def __init__(self, marca, color, puertas, llantas, combustible): # Metodo Constructor
        self.marca = marca # Atributo de Clase
        self.color = color # Atributo de Clase
        self.puertas = puertas # Atributo de Clase
        self.llantas = llantas # Atributo de Clase
        self.combustible = combustible  # Atributo de Clase
        print("Se ha creado un nuevo carro".format(self.marca)) # Impresion del Metodo Constructor
        
    def __str__(self): # Metodo de Clase __str__
        return "Marca: {}\nColor: {}\nPuertas: {}\nLlantas: {}\nCombustible: {}".format(self.marca, self.color, self.puertas, self.llantas, self.combustible) # Retorno del Metodo de Clase
    
    def __len__(self): # Metodo de Clase len 
        return self.puertas # Retorno del Metodo de Clase
        
    def __del__(self): # Metodo Destructor
        print("Se ha eliminado el objeto {}".format(self.marca)) # Impresion del Metodo Destructor
        
carro = FabricaCarros('Toyota', 'Rojo', 4, 4, 'Gasolina') # Instancia de la Clase
print(carro.marca) # Impresion del Metodo Constructor marca 
print(carro) # Impresion del Metodo de Clase __str__ 
print(len(carro)) # Impresion del Metodo de Clase numero de puertas