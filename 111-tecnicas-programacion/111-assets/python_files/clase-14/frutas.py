# falta bajar bien la consigna

lista_precios = {}

print("inicio de datos")

while True:
    fruta = input("Ingrese fruta (en blanco para terminar: ")

    if len(fruta) == 0:
        break
    
    precio = float(input("Ingrese precio: $ "))

    lista_precios[fruta] = precio

print(lista_precios)

print("inicio de la compra")

dict_compras = {}

while True:
    fruta_a_comprar = input("Ingrese fruta (en blanco para terminar: ")

    if fruta_a_comprar in lista_precios:
        cantidad = int(input("ingrese cantidad: "))
        dict_compras[fruta_a_comprar] = cantidad

        valor = lista_precios[fruta_a_comprar] * cantidad

        print("Se compro {} - {} unidades por un valor de {} pesos".format(fruta_a_comprar,cantidad,valor))
    else:
        print("Fruta no existe")

    opt = input("Seguir comprando (s/n): ")
    if opt == "n":
        break

print(dict_compras)
