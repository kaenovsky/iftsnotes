## clase 05 - ejercicio descuentos

"""
En un almacén se rebaja 10% del precio 
al cliente si compra más de 20 artículos 
y 5% si se compra hasta 20 artículos. Dado el precio
unitario de artículo y la cantidad adquirida, muestre
lo que debe pagar el cliente.
"""

print("~~~~~ inicio del programa ~~~~~")
print("")

print("Ingrese cantidad de articulos y precio unitario: ")

cantidad = int(input("ingrese cantidad de art: "))
precio = float(input("ingrese precio: "))
monto = cantidad * precio

if cantidad > 0 and precio > 0:
    if cantidad > 20:
        descuento = 10
    elif cantidad <= 20 and cantidad > 10:
            descuento = 5
    else:
            descuento = 0
    
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

print("")
print("~~~~~ fin del programa ~~~~~")
