""" Contar la cantidad de palabras, separadas por uno o más espacios, de un
telegrama que termina en punto. No utilizar funciones de string salvo la que
indica la longitud.
"""


def ingresar_texto_telegrama():
    telegrama = input("ingrese el texto del telegrama: ")
    telegrama = telegrama.lower()
    return telegrama



def contar_palabras_en_telegrama(telegrama):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyzáéíóú'
    palabras_contadas = 0
    i = 0
    p = i+1
    for i in range(i, len(telegrama)-1):
        if telegrama[i] in alfabeto and telegrama[p] not in alfabeto:
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

    telegrama = ingresar_texto_telegrama()
    palabras_en_telegrama = contar_palabras_en_telegrama(telegrama)

    imprimir_resultado(palabras_en_telegrama)


__init__: main()
