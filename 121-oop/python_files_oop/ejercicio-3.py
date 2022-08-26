"""
Solicitar al usuario 5 números,
imprimir el min y max
"""

numeros = []
i = 0

while(i < 5):
    inputNum = int(input('Ingrese un número: '))
    numeros.append(inputNum)
    i = i + 1

print(numeros)

menor = numeros[0]
mayor = numeros[0]

for item in numeros:
    if(item > mayor):
        mayor = item
    if(item < menor):
        menor = item

print('El mayor de los números es {}'.format(mayor))
print('El menor de los números es {}'.format(menor))