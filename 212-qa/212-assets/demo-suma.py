num1 = input("Ingrese numero 1: ")
num2 = input("Ingrese numero 2: ")

def suma_numeros(num1, num2):
    if num1 > 0 and num2 > 0:
        resultado = num1 + num2
    else:
        resultado = 0
    return resultado

print(suma_numeros(num1,num2))