"""
Cantidad de habitantes censados.
1) Nombre del jefe/a de familia con la mayor cantidad de caracteres (o sea, el nombre más
largo)
2) Cantidad de personas de viven solas.
3) Porcentaje de viviendas donde viven personas solas.
4) Cantidad de menores de 18 años registrados en el censo.
5) Informar el salario familiar registrado más bajo.
6) Informar cuantas familias no tienen vehículos.
7) Informar cuantas familias viven en departamentos y el promedio de metros cuadrados.
8) Exportar toda la información a un archivo csv.
"""

# 1) nombre más largo

def nombreLargo(resultados):
  
  masLargo = 0
  
  for item in resultados:
      if len(item['nombreJefe']) > masLargo:
        masLargo = len(item['nombreJefe'])
        nombreMasLargo = item['nombreJefe']
  print("El nombre más largo de la cuadra es: {}".format(nombreMasLargo))
  return 

# 2) cantidad que viven solas

def cantSolas(resultados,i):
  
  count = 0
  
  for item in resultados:
      if item['cantIntegrantes'] == 1:
        count = count + 1
  
  print("La cantidad de personas que viven solas en la cuadra es: {}".format(count))

  # 3) porcentaje de viviendas donde viven personas solas.
  # usamos la misma función tomando dos parámetros
  # siendo "i" la cantidad de casas censadas

  porcSolas = count * 100 / i
  print("El porcentaje de personas que viven solas en la cuadra es: {}%".format(porcSolas))
  return

# 4) cantidad de menores

def cantMenoresTotal(resultados):
    
  count = 0
  
  for item in resultados:
    count = count + item['cantMenores']
  
  print("Cantidad de menores en la cuadra: {}".format(count))
  return

# 5) menor salario de la cuadra

def salarioMenor(resultados):
    
  menorSalario = 99999999999
  
  for item in resultados:
    if item['ingresoSalarial'] < menorSalario:
        menorSalario = item['ingresoSalarial']
  
  print("El salario más bajo de la cuadra es: {}".format(menorSalario))
  return

# 6) familias que no tienen vehículo

def famNoVehiculo(resultados):
    
  count = 0
  
  for item in resultados:
    if item['cantidadVehiculos'] == 0:
        count = count + 1
  
  print("La cantidad de familias sin vehículo de la cuadra es: {}".format(count))
  return

# 7) familias en depto y promedio metros2

def deptos(resultados):
    
  count = 0
  totalMetros = 0
  
  for item in resultados:
    if item['metrosCuadrados'] > 0:
        count = count + 1
        totalMetros = totalMetros + item['metrosCuadrados']
  
  try:
    promedioMt2 = totalMetros / count
    print("La cantidad de familias que viven en departamento es: {}".format(count))
    print("El promedio de metros cuadrados (solo deptos) en la cuadra es: {:.2f}".format(promedioMt2))  
  except ZeroDivisionError:
    print("No hay deptos en la cuadra")  

  return

# registro extra: cantidad de dispositivos con conexión a Internet
# con eso sacamos el promedio de dispositivos por habitante

def dispositivos(resultados,totalHabitantes):
  
  count = 0
  
  for item in resultados:
    count = count + item['cantDispositivos']
  
  print("En promedio hay {:.2f} dispositivos por habitante.".format(count/totalHabitantes))
  return