# dados los cateros de un triángulo,
# calcular la hipotenusa

from math import sqrt

cateto1 = float(input("ingrese el cateto 1: "))
cateto2 = float(input("ingrese el cateto 2: "))

hipotenusa = sqrt(cateto1 ** 2 + cateto2 ** 2)

print("el valor de la hipotenusa es: ", hipotenusa)