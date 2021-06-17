""" Escribir una función que reciba una lista y un valor y devuelva la posición en que
encuentra al valor en la lista, si el valor estuviera repetido devolver la primera
aparición, si no estuviera devolver –1. Escribirla sin utilizar funciones como in,
count, index, etc.
"""

# def una_funcion(lista, valor):
#     i = 0
#     corte = 0
#     while i <= len(lista)-1 and corte == 0:
#     #     if lista[i] == valor:
#     #         return i
#     #     i += 1
#     # else:
#     #     return -1
#         if lista[i] == valor:
#             corte += 1
#         elif lista[i] != valor and i < len(lista)-1:
#             i += 1
#         elif lista[i] != valor and i == len(lista)-1:
#             corte += 1
#             i = -1
#
#     return i
def una_funcion(lista, valor):

    i = 0
    corte = 0
    retorno = False

    while i < len(lista) and corte == 0:

        if lista[i] == valor:
            corte += 1
            retorno = True

        elif i == len(lista) - 1:
            corte += 1
            # i = -1

        else:

            i += 1

    return retorno




def main():

    listab = [1, 2, 4, 3, 3, 63]
    valorb = 8

    print(una_funcion(listab, valorb))

__init__: main()
