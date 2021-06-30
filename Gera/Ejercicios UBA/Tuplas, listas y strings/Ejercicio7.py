""" Escribir una función que reciba una lista y un valor y devuelva la posición en que
encuentra al valor en la lista, si el valor estuviera repetido devolver la primera
aparición, si no estuviera devolver –1. Escribirla sin utilizar funciones como in,
count, index, etc.
"""


def una_funcion(lista, valor):

    indice = -1
    i = 0
    while i < len(lista):
        if lista[i] == valor:
            indice = i
            i = len(lista)
        i += 1
    return indice


def main():

    listab = [1, 2, 4, 3, 3, 63]
    valorb = 3

    print(una_funcion(listab, valorb))


__init__: main()
