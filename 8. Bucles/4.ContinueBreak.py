tareas = ['Tarea 1', 'Tarea 2', 'Tarea 3', 'Tarea 4', 'Tarea 5', 'Tarea 6', 'Tarea 7', 'Tarea 8', 'Tarea 9', 'Tarea 10']

for i in range(len(tareas)):
    if tareas[i] == 'Tarea 5':
        confirmacion = int(input('Ha llegado a la Tarea 5, ingrese el número 6 para confirmar que desea continuar: '))
        if confirmacion == 6:
            print('Procesando:', tareas[i])
            continue
        else:
            print('Proceso detenido por el usuario.')
            break
    print('Procesando:', tareas[i])
