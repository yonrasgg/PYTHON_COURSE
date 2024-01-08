while(True): # Bucle infinito
    try: # Intenta ejecutar el código
        edad = int(input("Introduce tu edad: ")) # Si no es un número, salta al except 
        print("Tu edad es: ", edad)  # Si es un número, imprime la edad
        break # Si todo ha ido bien, sal del bucle
    except: # Si ha ocurrido un error, ejecuta el código
        print("Ha ocurrido un error, introduce bien la edad") # Imprime el mensaje
    finally: # Siempre se ejecuta
        print("Fin de la iteración") # Imprime el mensaje