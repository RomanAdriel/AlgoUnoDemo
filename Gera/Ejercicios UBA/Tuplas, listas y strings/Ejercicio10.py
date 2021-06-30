"""Se leen dos vectores A y B, de N y M elementos respectivamente. Construir un
algoritmo que halle los vectores unión e intersección de A y B. Desarrollarlo sin
usar conjuntos (set) en Python. """


def union_de_vectores(vector_a, vector_b):
    vector_extendido = vector_a + vector_b
    vector_union = []
    for elemento in vector_extendido:
        if elemento not in vector_union:
             vector_union.append(elemento)

    return vector_union


def interseccion_de_vectores(vector_a, vector_b):
    vector_union = []
    for elemento in vector_a:
        if elemento in vector_b and elemento not in vector_union:
            vector_union.append(elemento)

    return vector_union


def main():

    vector_a = [0, 1, 5, 5, 6, 9, 1, 2, 0]
    vector_b = [1, 0, 9, 6, 1, 2, 2, 4]

    print("El vector unión de A y B es: ", union_de_vectores(vector_a, vector_b))
    print("El vector intersección de A y B es: ", interseccion_de_vectores(vector_a, vector_b))


__init__: main()