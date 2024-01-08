class Fabrica():
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio    
        
    @property   
    def llantas(self):  
        return self._llantas    
    
    @llantas.setter 
    def llantas(self, llantas): 
        self._llantas = llantas 
        
    @property   
    def color(self):    
        return self._color
    
    @color.setter   
    def color(self, color): 
        self._color = color 
        
    @property   
    def precio(self):   
        return self._precio 
    
    @precio.setter  
    def precio(self, precio):   
        self._precio = precio   
        
class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)
        
    def imprimir(self):
        print('Moto') 
        print('Llantas: {}'.format(self.llantas)) 
        print('Color: {}'.format(self.color)) 
        print('Precio: {}'.format(self.precio)) 

class Carro(Fabrica):   
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)
        
    def imprimir(self):
        print('Carro') 
        print('Llantas: {}'.format(self.llantas)) 
        print('Color: {}'.format(self.color)) 
        print('Precio: {}'.format(self.precio)) 
        
moto = Moto(2, 'Rojo', 1000000) 
moto.imprimir() 
print('')   
carro = Carro(4, 'Azul', 2000000)   
carro.imprimir()    
print('')