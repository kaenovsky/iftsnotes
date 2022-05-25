"""
Requerir al usuario que ingrese un número entero 
e informar si es primo o no, utilizando una función 
booleana que lo decida.
"""

num = int(input("Por favor ingrese un número entero: "))

def isPrime(num):
    
    menoresAnum = []
    divisores = []
    i = num

    # agregamos todos los numeros menores al num 
    # ingresado en un array que termina en 1

    while i != 1:
        menoresAnum.append(i)
        i = i - 1

    for d in menoresAnum:
        if(num % d == 0):
            divisores.append(d)
            # si hay divisores que su resto sea 0
            # los agregamos a un array de divisores

    print("Los números menores al ingresado son: ",menoresAnum)
    print()
    print("Los divisores del numero ingresado son: ",divisores)

    # chequeamos si tiene 1 solo divisor, por lo tanto es primo

    if(len(divisores) == 1):
        return True # es primo porque solo tiene un divisor
    else: 
        return False # es compuesto porque tiene más de un divisor

# llamamos a la función, chequeando si es True o False

isPrimeValue = isPrime(num)

if(isPrimeValue):
    print("El número {} es primo".format(num))
else:
    print("El número {} no es primo".format(num))


"""
Nota al pie:

Para encontrar los números compuestos usamos la siguiente idea:
https://es.wikipedia.org/wiki/N%C3%BAmero_compuesto

"La forma más sencilla para probar que un número n es compuesto, 
es encontrar un divisor d comprendido entre 1 y n (1 < d < n)."
"""