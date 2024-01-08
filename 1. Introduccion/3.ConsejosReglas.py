# 1. Palabras clave incorporadas en Python
import keyword
print(keyword.kwlist)  # Imprime todas las palabras clave de Python

# 2. Las variables deben empezar con una letra o un guión bajo
variable1 = "válida"
_1variable = "válida"
# 1variable = "inválida"  # Descomenta para ver el error

# 3. Las variables son sensibles a mayúsculas y minúsculas
Variable = "valor1"
variable = "valor2"
VARIABLE = "valor3"
# Imprime los valores de las variables
print(Variable, variable, VARIABLE) 

# 4. No se pueden usar espacios en los nombres de las variables
mi_variable = "válida"
# mi variable = "inválida"  # Descomenta para ver el error

# 5. Evita usar los caracteres especiales de Python en los nombres de las variables
# mi=variable = "inválida"  # Descomenta para ver el error

# 6. Usa nombres descriptivos y significativos para las variables
lista_de_nombres = ["Alice", "Bob", "Charlie"]
# Imprime la lista de nombres
print(lista_de_nombres)

# 7. Las constantes se escriben en mayúsculas
PI = 3.14159
# Imprime el valor de PI
print(PI)

# Palabras reservadas en Python
# Intenta usar una palabra reservada como nombre de variable
# for = "inválida"  # Descomenta para ver el error
