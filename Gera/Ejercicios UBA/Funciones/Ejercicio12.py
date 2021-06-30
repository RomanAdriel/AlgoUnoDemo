""" Contar la cantidad de palabras, separadas por uno o más espacios, de un
telegrama que termina en punto. No utilizar funciones de string salvo la que
indica la longitud.
"""


def ingresar_texto_telegrama():
    telegrama = input("ingrese el texto del telegrama: ")
    telegrama = telegrama.lower()
    return telegrama


def convertir_telegrama_en_lista(telegrama):
    lista_telegrama = list(telegrama)
    return lista_telegrama


def contar_palabras_en_telegrama(lista_caracteres):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyzáéíóú'
    palabras_contadas = 0
    i = 0
    p = i+1
    for i in range(i, len(lista_caracteres)-1):
        if lista_caracteres[i] in alfabeto and lista_caracteres[p] not in alfabeto:
            palabras_contadas += 1
            i += 1
            p += 1
        else:
            i += 1
            p += 1
    return palabras_contadas


def imprimir_resultado(cantidad_palabras):
    if cantidad_palabras:
        print("El telegrama ingresado contiene", cantidad_palabras, "palabra(s)")
    else:
        print("No se ingresaron datos")


def main():

    telegrama = convertir_telegrama_en_lista(ingresar_texto_telegrama())
    palabras_en_telegrama = contar_palabras_en_telegrama(telegrama)

    imprimir_resultado(palabras_en_telegrama)


__init__: main()
