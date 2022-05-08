"""
Realizar un programa que pida el ingreso de 5 palabras, 
las ingrese a una lista, cree una nueva lista en orden 
creciente en función de la cantidad de letras de cada 
palabra y mostrarlas en pantalla.

Ejemplo, si el ingreso fue:
["maria", "palabra", "elefante", "hola", "sol"].

El programa deberá mostrar lo siguiente:
["sol", "hola", "maria", "palabra", "elefante"].

Consideraciones:
1. Solo se aceptan palabras entre 5 y 20 caracteres.
2. Si dos palabras tienen la misma cantidad de caracteres, 
informar en el orden en que aparecieron.
"""

print("~~~~~ inicio del programa ~~~~~")
print()

i = 0
wordsList = []
sortList = []
isRepeat = None 

while(i < 5):
    word = input("Ingrese una palabra: ")
    while(len(word) <= 5 or len(word) >= 20):
        print("(!) Las palabras deben tener entre 5 y 20 caracteres")
        word = input("Ingrese una palabra: ")
    wordsList.append(word)
    i = i + 1

print()
print("El listado de palabras es: ")
print(wordsList)
print()

# nueva lista con mismas palabras

for word in wordsList:
    sortList.append(word)

print("Ahora las ordenamos de menor a mayor (cant. de caracteres): ")
sortList.sort(key=len)
print(sortList)

# mostramos la lista en cantidad de caracteres
# para que se vea más claro

orderByLen = []
for words in sortList:
    orderByLen.append(len(words))

print()
print("Si contamos los caracteres de cada palabra obtenemos: ")
print(orderByLen)

print()
print("Buscamos si hay valores repetidos (cant. de caracteres)")
print("(!) recorremos la lista ordenada, pero mostramos las posiciones de la lista original")
print()

lastWordLen = None
lastWord = None
isMatch = False

for item in sortList:
    if(lastWordLen == len(item)):
        isMatch = True
        indexItem = wordsList.index(item)
        indexLastWord = wordsList.index(lastWord)
        print()
        print("Misma cantidad de caracteres en las palabras {} y {}, en las posiciones {} y {} respectivamente".format(lastWord,item,indexLastWord,indexItem))
        lastWord = item
        lastWordLen = len(item)
    else:
        lastWord = item
        lastWordLen = len(item)

if(isMatch == False):
    print("No se encontraron palabras con la misma cantidad de caracteres")

print()
print("~~~~~ fin del programa ~~~~~")
