def agregar_una_vez(lista, elemento):
    if elemento not in lista:
        lista.append(elemento)
        print('se agregó un elemento a la lista!')
    else:
        raise ValueError('Error: Imposible añadir elementos duplicados => ' + str(elemento))

def main():
    
    elementos = [1, 5, -2]
    nuevos_elementos = [10, -2, 4, 'hola']

    for i in nuevos_elementos:
        try:
            agregar_una_vez(elementos, i)
            print('Lista actual: ', elementos)
        except Exception as e:
            print(e)

main()