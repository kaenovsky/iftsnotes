# Escribir una función que reciba una frase y 
# devuelva un diccionario con las palabras que 
# contiene y su longitud.

strCustom = input("Ingrese una frase: ")
d = {}

def getWords(strCustom):
    listedWords = strCustom.split()
    for word in listedWords:
        d.update({'{}'.format(word) : '{}'.format(len(word)) })
    print(d)

getWords(strCustom)