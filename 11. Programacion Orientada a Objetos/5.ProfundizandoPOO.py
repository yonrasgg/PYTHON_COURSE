class FabricaCarros(): # Clase Padre o Super Clase
    def __init__(self, marca, modelo, color, llantas, combustible): # Metodo Constructor
        self.marca = marca # Atributo de Clase
        self.modelo = modelo  # 'modelo' is now a dictionary of models
        self.color = color  # 'color' is now a list of colors
        self.llantas = llantas # Atributo de Clase
        self.combustible = combustible  # 'combustible' is now a list of types of fuel
        print(f"Se ha creado un nuevo carro de marca {self.marca}")
        
carro = FabricaCarros('Toyota', {'modelo1': 'Corolla', 'modelo2': 'Prius', 'modelo3': 'Celica', 'modelo4': 'Supra', 'modelo5': 'Land Cruiser', 'modelo6': 'FJ Cruiser'}, ['Rojo', 'Azul', 'Verde'], 4, ['Gasolina', 'Diesel', 'Electrico']) # Instancia de la Clase 
print('Marca del Carro: ', carro.marca) # Impresion del Metodo Constructor marca
print('Modelo del Carro: ', carro.modelo) # Impresion del Metodo Constructor modelo
print('Color: ', carro.color) # Impresion del Metodo Constructor color
print('Cantidad de llantas: ', carro.llantas) # Impresion del Metodo Constructor llantas
print('Tipo de combustible: ', carro.combustible) # Impresion del Metodo Constructor combustible
