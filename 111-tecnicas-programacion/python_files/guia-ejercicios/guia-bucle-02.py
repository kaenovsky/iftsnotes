"""
Escribir un programa que pregunte el nombre 
del usuario en la consola y un número entero 
e imprima por pantalla en líneas distintas 
el nombre del usuario tantas veces como el 
número introducido.
"""

print("~~~~~ inicio del programa ~~~~~")
print()

i = 0
nombre = input("ingrese su nombre: ")
cant = int(input("ingrese un número: "))

while(i < cant):
    print(nombre)
    i = i + 1

print()
print("~~~~~ fin del programa ~~~~~")