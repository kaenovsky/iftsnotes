"""
Escribir un programa que pida al usuario un 
número entero positivo y muestre por pantalla 
todos los números impares desde 1 hasta ese 
número separados por comas.
"""

print("~~~~~ inicio del programa ~~~~~")
print()

i = 0
number = int(input("ingrese un número (debe ser entero positivo): "))

while(number < 0):
    print("(!) error: ingrese un número positivo (mayor a 0)")
    print()
    number = int(input("ingrese un número (debe ser entero positivo): "))

while(i < number):
    if(i % 2 == 1):
        print(i, ",")
    i = i + 1

print()
print("~~~~~ fin del programa ~~~~~")