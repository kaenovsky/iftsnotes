## clase 07 - ejercicio descuentos con nuevas condiciones

"""
En un almacén se rebaja 10% del precio 
al cliente si compra más de 20 artículos 
y 5% si se compra entre 10 y 20.

Dado el precio unitario de artículo y la cantidad 
adquirida, muestre lo que debe pagar el cliente.

update: 13/04

si se compran más de 30 art desc 12% y
si se compran más de 40 art desc 15%
"""

print("~~~~~ inicio del programa ~~~~~")
print()

print("Ingrese cantidad de articulos y precio unitario: ")
print()

cantidad = int(input("ingrese cantidad de art: "))
precio = float(input("ingrese precio: "))
monto = cantidad * precio

if(cantidad > 0 and precio > 0):
    if (cantidad > 40):
        descuento = 15
    elif (cantidad > 30):
        descuento = 12
    elif (cantidad > 20):
        descuento = 10
    elif (cantidad > 10):
        descuento = 5
    
    valorDescuento = precio * cantidad * descuento / 100
    precioFinal = monto - valorDescuento 

    print("########################")
    print("El monto total es: $", monto)
    print("Su porcentaje de descuento: ", descuento, "%")
    print("El monto de descuento es: $", valorDescuento)
    print("Usted debe pagar: $", precioFinal)
    print("########################")    

else:
    print("Ingrese cantidades mayores que cero.")

print()
print("~~~~~ fin del programa ~~~~~")
