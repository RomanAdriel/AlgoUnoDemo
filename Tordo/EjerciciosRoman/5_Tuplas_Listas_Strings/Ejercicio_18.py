"""Escribir una función que, dada una palabra, determine si es capicúa o no. """


def es_capicua(ingreso):

    return ingreso == ingreso[::-1]


palabra = input("Introduzca una palabra: ")

print(es_capicua(palabra))
