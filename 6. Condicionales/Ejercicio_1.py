consonante = input("Ingrese una letra: ") # Solicita una consonante

if consonante.lower() in 'bcdfghjklmnpqrstvwxyz': # Si la consonante es igual a bcdfghjklmnpqrstvwxyz
    print("Es una consonante") # Imprime: Es una consonante
else: # Si la consonante no es igual a bcdfghjklmnpqrstvwxyz
    print("Es una vocal") # Imprime: Es una vocal