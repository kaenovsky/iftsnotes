# import aritmetica
# from aritmetica import sumar,restar,dividir 
from matematicas.funciones import imprimir
from matematicas.aritmetica import sumar,restar,dividir

a = 10
b = 0

#c1 = sumar(a,b)
#c2 = restar(a,b)
c3 = dividir(a,b)

#print("resultado suma: ",c1)
#print("resultado resta: ",c2)
if c3 != None:
    print("resultado division: ",c3)

imprimir(a,b)