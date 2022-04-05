"""
Realizar un programa que, ingresando los 
3 lados de un triángulo determine su tipo.

escaleno: todos los lados son diferentes
isosceles: 2 iguales y uno diferente
equilatero: todos los lados son iguales

"""

print("~~~~~ inicio del programa ~~~~~")

print("Ingrese en números (cm) los 3 lados de un triángulo")

lado1 = float(input("ingrese lado 1: "))
lado2 = float(input("ingrese lado 2: "))
lado3 = float(input("ingrese lado 3: "))

## verifico que los input sean mayores a 0

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("(!) error: todos los lados deben ser números mayores a 0")
else:

    # Determino el tipo de triángulo

    if lado1 == lado2:
        if lado1 == lado3:
            trian = "equilatero"
        else:
            trian = "isosceles"
    else:
        trian = "escaleno"

    # muestro resultado

    print("########################")
    print("el triángulo es: ", trian)
    print("########################")
    print("")
    print("~~~~~ fin del programa ~~~~~")
    