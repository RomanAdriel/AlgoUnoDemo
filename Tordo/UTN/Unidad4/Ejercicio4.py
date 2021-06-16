"""Escriba un programa que permita tomar una palabra, retorne las vocales que contenga junto con la cantidad de veces
que se repite. """


def ingreso_palabra():
    palabra = input("Ingrese palabra: ")
    return palabra


def string_to_list(parametro):
    lista_convertida = list(parametro)
    return lista_convertida


def count_vocales(word):
    palabra = word
    cantidad_a = palabra.count('a')
    cantidad_A = palabra.count('A')
    cantidad_e = palabra.count('e')
    cantidad_E = palabra.count('E')
    cantidad_i = palabra.count('i')
    cantidad_I = palabra.count('I')
    cantidad_o = palabra.count('o')
    cantidad_O = palabra.count('O')
    cantidad_u = palabra.count('u')
    cantidad_U = palabra.count('U')
    return {'A': cantidad_a + cantidad_A,
            'E': cantidad_e + cantidad_E,
            'I': cantidad_i + cantidad_I,
            'O': cantidad_o + cantidad_O,
            'U': cantidad_u + cantidad_U}


def imprimir_vocales_palabra(mensaje, vocales):
    print(mensaje, vocales)


def imprimir_resultado(mensaje, resultado):
    print(mensaje, resultado)


def main():
    lista_contada = count_vocales(string_to_list(ingreso_palabra()))
    imprimir_resultado("Las vocales se repiten esta cantidad de veces: ", lista_contada)


__init__: main()
