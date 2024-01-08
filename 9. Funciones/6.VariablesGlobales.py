def variables(): # Esto es una funcion estatica o global
    global num1, num2 # Esto es una variable global
    num1 = 200
    num2 = 300
    resultado = num1 + num2 
    return resultado    

print(variables()) # 500

resta = num1 - num2 # NameError: name 'num1' is not defined 
print(resta) # -100