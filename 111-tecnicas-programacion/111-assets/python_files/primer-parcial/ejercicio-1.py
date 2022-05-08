"""
Usted fue seleccionado para realizar el programa del CENSO Argentina. 
Como primera prueba, el programa simula el ingreso de los integrantes 
de una familia en toda una cuadra. 

El programa deber registrar lo siguiente

a.	Cantidad de integrantes en la familia. 
b.	Cantidad de menores de 18 años.
c.	Edad de la persona más vieja y edad de la persona más joven.
d.	Ingreso salarial de la familia.
e.	Informar si tiene vehículos (s/n) y si tiene, cuantos.
f.	El fin de ingreso se indica con cantidad de integrantes = 0
"""

print("~~~~~ inicio del programa ~~~~~")
print()

# declaramos variables

line = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
i = 0
cantIntegrantes = None
edad = 0
cantMenores = 0
masJoven = 200
masJovenTotal = 200
masAnciano = 0
masAncianoTotal = 0
totalIngresos = 0
totalVehiculos = 0
cantidadVehiculos = 0
hogaresConVehiculo = 0
totalHabitantes = 0
totalMenores = 0

print(line)
print("Demo Censo Argentina 2022 [v0.1]")
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
        
        if(edad < 18):
            cantMenores = cantMenores + 1
        
        if(edad < masJoven):
            masJoven = edad

        if(edad > masAnciano):
            masAnciano = edad

        countHabitante = countHabitante - 1 # restamos 1 vuelta al loop, hasta que sea 0

    print(":: Otros datos del hogar ::")

    ingresoSalarial = float(input("Ingreso salarial de la familia en pesos: "))
    tieneVehiculo = input("La familia tiene vehículos? [S/n]: ")
    
    if(tieneVehiculo == "S" or tieneVehiculo == "s"):
        cantidadVehiculos = int(input("Ingrese cantidad de vehículos en la familia: "))
        hogaresConVehiculo = hogaresConVehiculo + 1
    else:
        cantidadVehiculos = 0

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

    # contamos cada vez que itera el loop
    # que es lo mismo que decir "cantidad de hogares censados"
    i = i + 1

    """
    Condiciones de la consigna:

    Se pide calcular e informar lo siguiente:
    1. Cantidad de habitantes censados.
    2. Promedio de habitantes por hogar censados.
    3. Porcentaje de menores.
    4. Informar cuantos años tiene la persona más vieja y la más joven.
    5. Informar el promedio de ingreso familiar de todos los hogares censados.
    6. Informar cuantos vehículos fueron censados.
    7. Porcentaje de vehículos por familia censados.
    """

    # acumulador para punto 1)

    totalHabitantes = totalHabitantes + cantIntegrantes

    # comparaciones más ancianos y más jóvenes para punto 4)

    if(masAnciano > masAncianoTotal):
        masAncianoTotal = masAnciano
    
    if(masJoven < masJovenTotal):
        masJovenTotal = masJoven

    # acumulador para punto 5)

    totalIngresos = totalIngresos + ingresoSalarial

    # acumulador para punto 6)

    totalVehiculos = totalVehiculos + cantidadVehiculos

    # Por último, modificamos el valor cantIntegrantes
    # para continuar ingresando hogares o salir del loop [0]

    cantIntegrantes = int(input("Ingrese cantidad de integrantes del hogar N° {}: ".format(i+1)))
    if(cantIntegrantes == 0):
        print("(!) saliendo | No se censarán más hogares.")
    else:
        # reseteamos los valores de masJoven / masAnciano
        # luego continua el loop
        masJoven = 200
        masAnciano = 0

# fuera del while loop principal, dejamos de registrar hogares

print(line)
print(" Gracias por ingresar la información de la cuadra.\n Aquí están los resultados: ")
print(line)

# Mostramos los resultados solicitados

print("Cantidad de habitantes censados: {}".format(totalHabitantes))
print("Promedio de habitantes por hogar censado: {:.2f}".format(totalHabitantes / i))
print("Cantidad de menores de edad censados: {}".format(cantMenores))
print("Porcentaje de menores por cuadra: {:.0f}%".format(cantMenores / totalHabitantes * 100))
print("La persona más anciana de la cuadra tiene {} años.".format(masAncianoTotal))
print("La persona más joven de la cuadra tiene {} años.".format(masJovenTotal))
print("El ingreso promedio de la cuadra es ${:.2f} por hogar".format(totalIngresos / i))
print("Fueron censados un total de {} vehículos en la cuadra".format(totalVehiculos))
print("Hay un promedio de {:.0f} vehículos por hogar".format(totalVehiculos / i))
print("El {:.0f} por ciento de los hogares tienen vehículo".format(hogaresConVehiculo / i * 100))

print()
print("~~~~~ fin del programa ~~~~~")