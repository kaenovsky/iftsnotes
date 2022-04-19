"""
anotaciones de la clase 08 - tema listas y tuplas
usamos ejemplo de nota promedio desde una lista
"""

notas = [5, 7, 2, 8, 4]

## muestro las notas una por una 
## vimos ejemplo con ingreso de notas

for dato in notas:
	print(dato)

## luego si quiero sacar promedio
## uso acumulador y divido en cant de elementos

sumatotal = 0

for dato in notas:
	sumatotal = sumatotal + dato

promedio = sumatotal / 5

print("el promedio es: ", promedio)