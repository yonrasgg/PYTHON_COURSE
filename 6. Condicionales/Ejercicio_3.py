palabra1 = input("Ingrese la primera palabra: ") # Solicita la primera palabra
palabra2 = input("Ingrese la segunda palabra: ") # Solicita la segunda palabra

# Ordena las letras de las palabras y verifica si son iguales
if sorted(palabra1) == sorted(palabra2): 
    print("Las palabras son anagramas") # Imprime: Las palabras son anagramas
else:
    print("Las palabras no son anagramas") # Imprime: Las palabras no son anagramas
