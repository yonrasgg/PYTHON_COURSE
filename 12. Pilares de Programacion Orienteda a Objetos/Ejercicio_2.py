class Calculadora():
    def __init__(self):
        self.numero1 = int(input('Ingrese el primer numero: ')) 
        self.numero2 = int(input('Ingrese el segundo numero: ')) 
        
    @property
    def numero1(self):
        return self._numero1
    
    @numero1.setter 
    def numero1(self, numero1): 
        self._numero1 = numero1
    
    @property
    def numero2(self):
        return self._numero2    
    
    @numero2.setter 
    def numero2(self, numero2): 
        self._numero2 = numero2
        
    def sumar(self):
        return self.numero1 + self.numero2  
    
    def restar(self):
        return self.numero1 - self.numero2  
    
    def multiplicar(self):  
        return self.numero1 * self.numero2      
    
    def dividir(self):  
        return self.numero1 / self.numero2  
    
    def imprimir(self): 
        print('Numero 1: {}'.format(self.numero1)) 
        print('Numero 2: {}'.format(self.numero2)) 
        print('Suma: {}'.format(self.sumar())) 
        print('Resta: {}'.format(self.restar())) 
        print('Multiplicacion: {}'.format(self.multiplicar())) 
        print('Division: {}'.format(self.dividir()))    
        
    def resultados(self):   
        if self.numero1 > self.numero2: 
            print('El numero {} es mayor que el numero {}'.format(self.numero1, self.numero2)) 
        elif self.numero1 < self.numero2: 
            print('El numero {} es menor que el numero {}'.format(self.numero1, self.numero2)) 
        else: 
            print('El numero {} es igual que el numero {}'.format(self.numero1, self.numero2))  
            
calculadora = Calculadora()    
calculadora.imprimir()  
calculadora.resultados()    
