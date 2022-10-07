def agregar_una_vez(lista, elemento):
    if elemento not in lista:
        lista.append(elemento)
        print('se agregó un elemento a la lista!')
    else:
        raise ValueError('Error: Imposible añadir elementos duplicados', elemento)

def main():
    
    elementos = [1, 5, -2]
    add = [10, -2, 4, 'hola']

    for i in add:
        try:
            agregar_una_vez(elementos, i)
            print(elementos)
        except Exception as e:
            print('error: ', e)

main()