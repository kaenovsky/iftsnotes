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

print(numeros)

lastItem = numeros[0] 
repeat = False

for item in numeros:
    if(item == lastItem):
        repeat = True
        
if(repeat):
    print('Hay números repetidos')
else:
    print('No hay números repetidos')
