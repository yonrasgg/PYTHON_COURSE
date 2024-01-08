factura = input("Ingrese el número de factura: ") # Pide el número de factura al usuario
monto = float(input("Ingrese el monto de la factura: ")) # Pide el monto de la factura al usuario

def calculo_iva(monto):
    iva = monto * 0.13 # Calcula el IVA
    Total = monto + iva # Calcula el total
    print(f"El IVA de la factura #{factura} es de ${iva} \nTotal ${Total} IVI") # Imprime el IVA
    
calculo_iva(monto) # Llama a la función