class FabricaCarros(): # Clase
    pass # No hace nada

print(type(FabricaCarros)) # <class 'type'>

carro = FabricaCarros() # Instanciacion de la clase
carro2 = FabricaCarros() # Instanciacion de la clase

print(type(carro)) # <class '__main__.FabricaCarros'>
print(type(carro2)) # <class '__main__.FabricaCarros'>

def FabricaCarros(): # No es una clase, es una funcion
    pass # No hace nada

print(type(FabricaCarros())) # <class 'NoneType'>