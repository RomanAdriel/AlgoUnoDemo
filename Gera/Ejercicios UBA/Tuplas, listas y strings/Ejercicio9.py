"""Se lee un vector X de N elementos (enteros). Escribir un algoritmo que devuelva
un vector que tenga todos los elementos de X, pero sin elementos repetidos.
"""


def crear_vector_elementos_unicos(vector):
    nuevo_vector = []

    for elemento in vector:
        if elemento not in nuevo_vector:
            nuevo_vector.append(elemento)

    return nuevo_vector


def main():
    vector_a = [1, 2, 3, 6, 8, 7, 99, 4, 6, 0, 665, 36, 3, 1, 6989, 46, 2, 5, 4]
    print(crear_vector_elementos_unicos(vector_a))


__init__: main()
