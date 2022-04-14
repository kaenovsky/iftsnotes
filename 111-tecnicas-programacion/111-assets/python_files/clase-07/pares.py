## clase 07 - ejercicio numerso pares

"""
Solicitar al usuario que ingrese num positivos y,
por cada uno, imprimir la suma de los dígitos
que lo componen. La condición de corte es que 
se ingrese el número -1. Al finalizar, mostrar
cuántos de los números ingresados son pares

ej input: 5223 
la suma debería ser = 5 + 2 + 2 + 3
y el número de pares 2
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


    

