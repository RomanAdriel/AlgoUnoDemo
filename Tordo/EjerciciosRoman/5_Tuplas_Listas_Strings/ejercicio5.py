"""Escribir la misma función del punto anterior usando count"""

valor = 0

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def true_or_false(numero, list):
    if list.count(numero) > 0:
        return True
    else:
        return False


print(true_or_false(valor, lista))


