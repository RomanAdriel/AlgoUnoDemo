"""Escribir la misma función del punto anterior usando in"""

def otra_funcion_mas(lista, valor):

    return valor in lista



def main():

    listab = [1, 2, 3, 4, 5, 6, 7, 23]
    valorb = 56

    print(otra_funcion_mas(listab, valorb))

__init__: main()
