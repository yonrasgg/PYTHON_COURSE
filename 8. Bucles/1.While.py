contador = int(input("Ingrese el número de vueltas que desea que gire el carrusel: "))

while contador > 0:
    print(f"El carrusel sigue girando. Vueltas restantes: {contador}")
    contador -= 1
else:
    print("El carrusel se ha detenido.")
    