"""
Escribir un programa que pida números al usuario, 
mostrar el factorial de cada uno y, al finalizar, 
la cantidad total de números leídos en total. 
Utilizar una o más funciones, según sea necesario.
"""

count = 0
opt = True

num = int(input("Por favor ingrese un número: "))

while num < 0:
    print("(!) error: ingrese números mayores a 0 para encontrar su factorial")
    num = int(input("Por favor ingrese un número: "))

def esFactorial(num):
    if(num == 1 or num == 0):
        return 1
    else:
        return num * (esFactorial(num - 1)) 

while opt == True:
    print("El factorial de {} es {}.".format(num,esFactorial(num)))
    count = count + 1
    print("Puede continuar ingresando números o ingresar -1 para salir.")
    num = int(input("Por favor ingrese otro número: "))
    if(num == -1):
        opt = False

print()
print("Se ingresaron un total de {} números.".format(count))
print()
print("fin del programa")