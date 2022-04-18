"""
Leer números enteros positivos de teclado, 
hasta que el usuario ingrese el 0. Informar 
cuál fue el mayor número ingresado.
"""

print("~~~~~ inicio del programa ~~~~~")
print()

num = "null"
mayorActual = 0

while(num != 0):

    num = int(input("ingrese un número (debe ser entero positivo): "))

    while(num < 0):
        print("(!) error: ingrese un número positivo (mayor a 0)")
        print()
        num = int(input("ingrese un número (debe ser entero positivo): "))

    if(num > mayorActual):
        mayorActual = num

print("El mayor de los números ingresados fue: ", mayorActual)

print()
print("~~~~~ fin del programa ~~~~~")