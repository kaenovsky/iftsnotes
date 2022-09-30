"""
Solicitar al usuario 5 números,
imprimir si hay num duplicados
o son todos distintos
"""

numeros = []
i = 0

while(i < 5):
    inputNum = int(input('Ingrese un número: '))
    numeros.append(inputNum)
    i = i + 1

print('Los numeros ingresados son: ', numeros)

if len(numeros) == len(set(numeros)):
    print('No hay números repetidos')
else:
    print('Hay números repetidos')
