import cmath # Importa el módulo cmath para trabajar con números complejos

"""\(ax^3 + bx^2 + cx + d = 0\)"""
# Ingrese el valor de las variables que desea calcular
a = float(input("Ingrese el valor de a: ")) 
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
d = float(input("Ingrese el valor de d: "))

delta_0 = b**2 - 3*a*c # Discriminante 1
delta_1 = 2*b**3 - 9*a*b*c + 27*a**2*d # Discriminante 2
C = ((delta_1 + cmath.sqrt(delta_1**2 - 4*delta_0**3))/2)**(1/3) # Constante C

x1 = (-1/(3*a))*(b + C + delta_0/C) # Solución 1
x2 = (-1/(3*a))*(b + complex(-0.5, cmath.sqrt(3)/2)*C + delta_0/(complex(-0.5, cmath.sqrt(3)/2)*C)) # Solución 2
x3 = (-1/(3*a))*(b + complex(-0.5, -cmath.sqrt(3)/2)*C + delta_0/(complex(-0.5, -cmath.sqrt(3)/2)*C)) # Solución 3

print("Las soluciones de la ecuación son: ", x1, x2, x3) # Imprime: Las soluciones de la ecuación son:  <x1> <x2> <x3>