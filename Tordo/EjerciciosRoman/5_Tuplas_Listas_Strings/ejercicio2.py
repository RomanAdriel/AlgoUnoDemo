"""Dados dos vectores A y B, de N elementos cada uno, se desean calcular:
a. el vector suma.
b. el producto escalar."""


def vector_suma(a, b):
    resultado = []

    for i in a:
        # Alternativa 1 - Elegir una de las dos
        #     for i in range(0, len(a)):
        #         resultado.append(a[i] + b[i])

        # Alternativa 2 - Elegir una de las dos
        for numeroa, numerob in zip(a, b):
            resultado.append(numeroa[i] + numerob[i])

    return resultado


def producto_escalar(a, b):
    resultados = []

    # Alternativa 1 - Elegir una de las dos
    # for i in range(0, len(a)):
    #     resultados.append(a[i] * b[i])

    # Alternativa 2 - Elegir una de las dos
    for numeroa, numerob in zip(a, b):
        resultados.append(numeroa * numerob)

    return sum(resultados)


vector_a = [1, 2, 3]

vector_b = [4, 5, 6]

vector_resultado = vector_suma(vector_a, vector_b)
resultado_escalar = producto_escalar(vector_a, vector_b)

print(vector_resultado, resultado_escalar)
