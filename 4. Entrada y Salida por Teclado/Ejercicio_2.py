# Ingresa los valores de las notas de las tareas, exámenes y proyecto
tarea1 = float(input("Ingrese la nota de la tarea 1: "))
tarea2 = float(input("Ingrese la nota de la tarea 2: "))
tarea3 = float(input("Ingrese la nota de la tarea 3: "))
examen1 = float(input("Ingrese la nota del examen 1: "))
examen2 = float(input("Ingrese la nota del examen 2: "))
proyecto = float(input("Ingrese la nota del proyecto: "))

promedio_tareas = (tarea1 + tarea2 + tarea3)/3 # Promedio de las tareas
promedio_examenes = (examen1 + examen2)/2 # Promedio de los exámenes
calificacion_final = 0.3 * promedio_tareas + 0.4 * promedio_examenes + 0.3 * proyecto # Calificación final

print("La calificación final es: ", calificacion_final) # Imprime: La calificación final es:  <calificacion_final>