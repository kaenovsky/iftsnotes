## clase 07 - ejercicio numeros pares

"""
Solicitar al usuario que ingrese num positivos y,
por cada uno, imprimir la suma de los dígitos
que lo componen. La condición de corte es que 
se ingrese el número -1. Al finalizar, mostrar
cuántos de los números ingresados son pares

ej con el siguiente input:
42 el resultado es 4 + 2 = 6
14 el resultado es 1 + 4 = 5
25 el resultado es 2 + 5 = 7
y el número de pares 2 (42 y 14)
"""

print("~~~~~ inicio del programa ~~~~~")
print()

es_par = 0
par_counter = 0

n = int(input("Ingrese número (-1 para exit): "))

while(n != -1):

    es_par = n % 2

    if (es_par == 0):
        par_counter = par_counter + 1
    
    suma = 0
    while(n != 0):
        ult_digito = n % 10
        pri_digito = n // 10
        suma = suma + ult_digito
        n = pri_digito
        
    print("Sumamos los dígitos y el resultado es : ",suma)
    n = int(input("Ingrese número (-1 para exit): "))

## fuera del loop

print("La cantidad de números pares es: ",par_counter)

print()
print("~~~~~ fin del programa ~~~~~")


    

