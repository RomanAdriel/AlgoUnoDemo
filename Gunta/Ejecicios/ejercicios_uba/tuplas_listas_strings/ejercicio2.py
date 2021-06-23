"""Escribir una función que reciba una lista y un valor y devuelva verdadero (True)
si el valor está en la lista, falso (False) en caso contrario. Hacerlo sin usar in ni
count."""

def esta_no_esta(valor, lista):

    while valor == lista:
        return True
    else:
        return False


def mensaje(m):
    print(m)

def main():
    lista = [1, 2, 3, 4, 5, 6, 7]
    mensaje(esta_no_esta(3, lista))



__init__: (main())