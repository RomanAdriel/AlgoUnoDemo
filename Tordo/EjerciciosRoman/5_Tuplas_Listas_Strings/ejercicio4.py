"""Escribir una función que reciba una lista y un valor y devuelva verdadero (True)
si el valor está en la lista, falso (False) en caso contrario. Hacerlo sin usar in ni
count. """

valor = 1

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def true_or_false(numero, list):
    for i in range(0, len(list)):
        if list[i] == numero:
            return True
        else:
            return False


print(true_or_false(valor, lista))
