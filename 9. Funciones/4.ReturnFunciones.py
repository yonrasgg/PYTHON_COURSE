def entero():
    print('Este es un dato entero: ')
    return 100  

def decimal():  
    print('Este es un dato decimal: ')
    return 100.5    

def cadena():   
    print('Este es un dato cadena: ')
    return "cadena"     

def booleano(): 
    print('Este es un dato booleano: ')
    return True 

def lista():    
    print('Este es un dato lista: ')
    return [1,2,3]  

def tupla():    
    print('Este es un dato tupla: ')
    return (1,2,3)  

def diccionario():  
    print('Este es un dato diccionario: ')
    return {'nombre':'Juan'}    

def valorNulo():    
    print('Este es un dato None: ')
    return None 

def main(): 
    print(entero())
    print(decimal())
    print(cadena())
    print(booleano())
    print(lista())
    print(tupla())
    print(diccionario())
    print(valorNulo())  

if __name__ == '__main__':
    main()     
    