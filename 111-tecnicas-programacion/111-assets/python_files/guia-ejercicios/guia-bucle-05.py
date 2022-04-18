"""
Mostrar un menú con tres opciones: 
1- comenzar programa, 
2- imprimir listado, 
3-finalizar programa. 
A continuación, el usuario debe poder seleccionar 
una opción (1, 2 ó 3). Si elige una opción 
incorrecta, informarle del error. El menú se debe 
volver a mostrar luego de ejecutada cada opción, 
permitiendo volver a elegir. Si elige las opciones 
1 ó 2 se imprimirá un texto. Si elige la opción 
3, se interrumpirá la impresión del menú y el 
programa finalizará.
"""

print("~~~~~ inicio del programa ~~~~~")
print()

opt = 0

while(opt != 3):

    print("Eliga con su teclado una de las siguientes opciones: ")
    print()
    print("opción [1]: comenzar programa")
    print("opción [2]: imprimir listado")
    print("opción [3]: finalizar programa")

    opt = int(input("Ingresar opción (1, 2 o 3): "))

    while(opt != 1 and opt != 2 and opt != 3):
        print("(!) error: Ingrese únicamente 1, 2 o 3")
        print()
        opt = int(input("Ingresar opción (1,2 o 3): "))

    if(opt == 1):
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        print("eligió opción 1. nice :)")
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
    elif(opt == 2):
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        print("eligió opción 2. OMG! :|")
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        print("eligió opción 3. chau x)")
        print("~~~~~~~~~~~~~~~~~~~~~~~~")

print()
print("~~~~~ fin del programa ~~~~~")