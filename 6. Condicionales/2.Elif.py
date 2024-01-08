letra = input("Ingrese una vocal: ") # Solicita una vocal

if letra == "a":
    print("Es una vocal y es la A")
elif letra.lower() == "e":
    print("Es una vocal y es la E")
elif letra.lower() == "i":
    print("Es una vocal y es la I")
elif letra.lower() == "o":
    print("Es una vocal y es la O")
elif letra.lower() == "u":
    print("Es una vocal y es la U")
else:
    print("No es una vocal")