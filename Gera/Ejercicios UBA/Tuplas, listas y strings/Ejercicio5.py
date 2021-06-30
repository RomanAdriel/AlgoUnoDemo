def otra_funcion(lista, valor):
    if lista.count(valor) >= 1:
        return True
    else:
        return False

def main():

    listab = [1, 2, 3, 4, 5, 6, 7, 23]
    valorb = 9

    print(otra_funcion(listab, valorb))


__init__: main()
