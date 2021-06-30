"""Escribir la misma función del punto anterior usando funciones específicas de
Python.
"""


def misma_funcion(lista, valor):
    indice = -1
    if valor in lista:
        indice = lista.index(valor)

    return indice

def main():

    listab = [1, 2, 3, 6, 8, 7, 99, 4, 6, 0, 665, 36, 3, 1, 6989, 46, 2, 5, 4]
    valorb = int(input("ingrese valor a buscar: "))

    print(misma_funcion(listab, valorb))


__init__: main()
