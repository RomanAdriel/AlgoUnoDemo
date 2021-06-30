def una_funcion(lista, valor):
    i = 0
    while i <= len(lista)-1:
        if lista[i] == valor:
            return True
        i += 1
    else:
        return False


def main():

    listab = [1, 2, 4, 3, 3, 3]
    valorb = 3

    print(una_funcion(listab, valorb))


__init__: main()
