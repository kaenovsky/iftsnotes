"""
Reformulando ejercicio para parcial N°2:
Misma idea que el anterior pero guardando los datos
en un diccionario. Luego agregando cada diccionario 
a una lista.
"""
import csv
import json # para mostrar los diccionarios ordenados como JSON
from funciones import nombreLargo, cantSolas, cantMenoresTotal, salarioMenor 
from funciones import famNoVehiculo, deptos, dispositivos

print("~~~~~ inicio del programa ~~~~~")
print()

# declaramos variables

line = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
i = 0
cantIntegrantes = None
edad = 0
cantMenores = 0
cantMayores65 = 0
masJoven = 200
masAnciano = 0
deptosCuadra = 0
totalHabitantes = 0
totalMenores = 0
cantDispositivos = 0
resultados = [] # upgrade: mostrar resultados en array

print(line)
print("Demo Censo Argentina 2022 [v0.2]")
print(line)
print("Como censista usted ingresará información de múltiples hogares.")
print("Si elige cantidad de integrantes 0, el programa finalizará.")
print()

cantIntegrantes = int(input("Ingrese cantidad de integrantes del hogar N° {}: ".format(i+1)))
print(line)

while(cantIntegrantes != 0):

    # todo el programa corre dentro de este loop
    # cuando el valor cantIntegrantes sea 0, finaliza
    
    countHabitante = cantIntegrantes
    
    print(":: Hogar N° {} ::".format(i+1))
    print("Ingrese la edad de cada habitante del hogar: ")
    
    # en el siguiente while loop ingresamos uno a uno los integrantes del hogar
    # usando como referencia el contador de habitantes
    # que va disminuyendo su valor en cada vuelta del loop

    while(countHabitante > 0):        
        edad = int(input("Ingrese edad del habitante N° {}: ".format(countHabitante)))
        
        if(edad < masJoven):
            masJoven = edad

        if(edad > masAnciano):
            masAnciano = edad

        if(edad <= 18):
            cantMenores = cantMenores + 1
        
        if(edad >= 65):
            cantMayores65 = cantMayores65 + 1

        countHabitante = countHabitante - 1 # restamos 1 vuelta al loop, hasta que sea 0

    print(":: Otros datos del hogar ::")

    nombreJefe = input("Ingrese el nombre del jefe o jefa de hogar: ") 
    ingresoSalarial = float(input("Ingreso salarial de la familia en pesos: $"))
    tieneVehiculo = input("La familia tiene vehículos? [S/N]: ")
    
    if(tieneVehiculo == "S" or tieneVehiculo == "s"):
        cantidadVehiculos = int(input("Ingrese cantidad de vehículos en la familia: "))
    else:
        cantidadVehiculos = 0
    
    esDepto = input("La familia vive en un departamento? [S/N]: ")
    
    metrosCuadrados = 0

    if(esDepto == "S" or esDepto == "s"):
        metrosCuadrados = int(input("Ingrese cantidad de m2 del depto: "))
        deptosCuadra = deptosCuadra + 1
    else:
        print("No es un departamento, continue.")

    # registro adicional elegido

    cantDispositivos = int(input("Ingrese cantidad de dispositivos con conexión a Internet: "))

    print()
    print(line)
    print(":: Finalizó el ingreso ::")
    
    if(cantIntegrantes >= 2):
        if(masJoven != masAnciano):         
            print("La persona más joven del hogar N° {} tiene {} años.".format(i+1,masJoven))
            print("La persona más anciana del hogar N° {} tiene {} años.".format(i+1,masAnciano))
        else:
            print("Todos los habitantes del hogar tienen la misma edad.")

    print(":: Puede continuar con el siguiente hogar ::")
    print(line)
    print()

    # acumulador para punto 1)
    totalHabitantes = totalHabitantes + cantIntegrantes

    # contamos cada vez que itera el loop
    # que es lo mismo que decir "cantidad de hogares censados"
    i = i + 1

    # Definimos el diccionario por cada familia

    flia = {
        'familiaNumero': i,
        'cantIntegrantes': '',
        'nombreJefe': '',
        'cantMenores': '',
        'cantMayores65': '',
        'masAnciano': '',
        'masJoven': '',
        'esDepto': '',
        'metrosCuadrados': '',
        'ingresoSalarial': '',
        'cantidadVehiculos': '',
        'cantDispositivos': ''
        }
    
    # Y lo completamos con los datos de ingreso

    flia['cantIntegrantes'] = cantIntegrantes
    flia['nombreJefe'] = nombreJefe
    flia['cantMenores'] = cantMenores
    flia['cantMayores65'] = cantMayores65
    flia['masAnciano'] = masAnciano
    flia['masJoven'] = masJoven
    flia['esDepto'] = esDepto
    flia['metrosCuadrados'] = metrosCuadrados
    flia['ingresoSalarial'] = ingresoSalarial
    flia['cantidadVehiculos'] = cantidadVehiculos
    flia['cantDispositivos'] = cantDispositivos

    # Agregamos cada diccionario a la lista principal
    resultados.append(flia)

    # Por último, modificamos el valor cantIntegrantes
    # para continuar ingresando hogares o salir del loop [0]

    cantIntegrantes = int(input("Ingrese cantidad de integrantes del hogar N° {}: ".format(i+1)))
    if(cantIntegrantes == 0):
        print("(!) saliendo | No se censarán más hogares.")
    else:
        # reseteamos los valores que no son pisados en las preguntas
        # luego continua el loop
        masJoven = 200
        masAnciano = 0
        cantMenores = 0
        cantMayores65 = 0

# fuera del while loop principal, dejamos de registrar hogares

# Mostramos el array de diccionarios

print(line)
print("Le recordamos los datos ingresados: \n")
print(json.dumps(resultados, indent=4))

print(line)
print(" Gracias por ingresar la información de la cuadra.\n Aquí están los resultados: ")
print(line)

# Mostramos los resultados solicitados
print("Cantidad de habitantes censados: {}".format(totalHabitantes)) # esto quedó como el parcial 1

# El resto los mostramos llamando a las funciones
nombreLargo(resultados)
cantSolas(resultados,i)
cantMenoresTotal(resultados)
salarioMenor(resultados)
famNoVehiculo(resultados)
deptos(resultados)
dispositivos(resultados,totalHabitantes)

# Exportamos a csv

nombres_columnas = [
'familiaNumero',
'cantIntegrantes',
'nombreJefe',
'cantMenores',
'cantMayores65',
'masAnciano',
'masJoven',
'esDepto',
'metrosCuadrados',
'ingresoSalarial',
'cantidadVehiculos',
'cantDispositivos']

with open('censo_export.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = nombres_columnas)
    writer.writeheader()
    writer.writerows(resultados)

print()
print("~~~~~ fin del programa ~~~~~")