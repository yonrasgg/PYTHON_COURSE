class Marino():
    def hablar(self):
        print('Hola! Soy un animal marino')
        
class pulpo(Marino):
    def hablar(self):
        print('Hola! Soy un pulpo') 
        
class foca(Marino):
    def hablar(self, mensaje):
        self.mensaje = mensaje
        print(self.mensaje)
        
marino = Marino()   
marino.hablar()
pulpo = pulpo()
pulpo.hablar()
foca = foca()
foca.hablar('Hola! Soy una foca')