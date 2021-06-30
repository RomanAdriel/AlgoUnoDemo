"""Escribir un programa que calcule la traza de una matriz cuadrada. Recordar que
la traza de una matriz es la suma de los elementos de su diagonal principal.
"""


def calculo_traza_matriz(matriz):
    traza = 0
    for i in range(0, len(matriz)):
        traza += matriz[i][i]
    return traza


def matriz_en_cadena(matriz):
    matriz_cadena = ""
    for i in range(0, len(matriz)):
        matriz_cadena += str(matriz[i]) + "\n"
    return matriz_cadena


def main():
    matriz_test = [[1, 2, 3], [4, 5, -6], [-7, 8, -9]]

    traza = calculo_traza_matriz(matriz_test)

    print("La matriz es: \n", matriz_en_cadena(matriz_test))
    print("El valor de la traza es de ", traza)


__init__: main()
