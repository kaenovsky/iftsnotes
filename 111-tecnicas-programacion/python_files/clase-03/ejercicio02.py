"""
calcular el perimetro y área de un rectángulo 
ingresando su base y altura
(A + B) * 2
"""

base = int(input("ingrese la base del rectángulo: "))
altura = int(input("ingrese la altura del rectángulo: "))
perimetro = (2 * base + 2 * altura)
area = (base * altura)

print("el perimetro de su rectángulo es: {} ".format(perimetro))
print("el área de su rectángulo es: {} ".format(area))

print()
print('Fin del programa')

