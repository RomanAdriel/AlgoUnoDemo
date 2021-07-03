"""Escribir una función que reciba una lista y un valor y devuelva la posición en que
encuentra al valor en la lista, si el valor estuviera repetido devolver la primera
aparición, si no estuviera devolver –1. Escribirla sin utilizar funciones como in,
count, index, etc. """

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

valor = int(input("Ingrese un valor para verificar si se encuentra en la lista: "))


def verificar_lista(valor, list):
    indice = -1
    for i in range(0, len(list)):
        if list[i] == valor:
            indice = i
            i = len(list)+1
    return indice


print(verificar_lista(valor, lista))
