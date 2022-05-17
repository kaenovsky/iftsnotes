# Escribir un programa que nos permita guardar los nombres
# de los alumnos de una clase y las notas que han
# obtenido. Cada alumno puede tener distinta 
# cantidad de notas. Generar un diccionario con los
# nombres de los alumnos y las notas de cada uno

alumnos = {}
alumno = input("Nombre del alumno: ")

while len(alumno) > 0:
    nota = int(input("Agregar nota (0 para terminar): "))

    notas = []

    while nota > 0:
        notas.append(nota)
        nota = int(input("Agregar nota (0 para terminar): "))
    
    print(notas)
    alumnos[alumno] = notas
    alumno = input("Nombre del alumno: ")

for clave, valores in alumnos.items(): # el par de elementos
    print(clave, valores)

    suma = 0
    for i in valores:
        suma = suma + i
    
    promedio = suma / len(valores)

    print("{} tiene un promedio de nota igual a {}".format(clave,promedio))


# print(alumnos)
