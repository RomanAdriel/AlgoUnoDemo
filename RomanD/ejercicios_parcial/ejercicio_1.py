"""Solicitar al usuario el ingreso de un texto. A continuación:
a. Mostrar el texto, pero ordenado por palabra y todo en mayúsculas.
b. Informar cuantos caracteres tiene la palabra más larga.
c. Generar una nueva lista sin palabras repetidas.
d. Armar un ranking de palabras, informando palabra y cantidad de
ocurrencias, ordenado por la cantidad de ocurrencias."""


def dividir_texto(cadena):
    cadena = cadena.upper()
    lista_palabras = cadena.split()

    return lista_palabras


def eliminar_duplicados(lista_palabras):
    lista_limpia = []

    for palabra in lista_palabras:
        if palabra not in lista_limpia:
            lista_limpia.append(palabra)

    return lista_limpia


def cantidad_ocurrencias(lista_palabras):
    dict_ocurrencias = {}

    for palabra in lista_palabras:
        if palabra not in dict_ocurrencias:
            dict_ocurrencias[palabra] = 1
        else:
            dict_ocurrencias[palabra] += 1

    lista_ocurrencias = [registro for registro in dict_ocurrencias.items()]

    lista_ocurrencias.sort(key=lambda tupla: tupla[1], reverse=True)

    return lista_ocurrencias


def main():
    cadena_dividida = dividir_texto("Hola Hola Hola Hola que         tal como estas")
    lista_palabras_ordenada = sorted(cadena_dividida)
    cadena_ordenada = " ".join(lista_palabras_ordenada)
    cadena_ordenada_longitud = sorted(cadena_dividida, key=len, reverse=True)
    cadena_sin_duplicados = " ".join(eliminar_duplicados(cadena_dividida))
    ranking_palabras = cantidad_ocurrencias(cadena_dividida)

    print("La cadena ordenada es la siguiente: " + cadena_ordenada, end="\n\n")
    print(
        "La palabra más larga tiene {caracteres} caracteres.".format(caracteres=str(len(cadena_ordenada_longitud[0]))),
        end="\n\n")
    print("La cadena ingresada sin repetidos es la siguiente: " + cadena_sin_duplicados, end="\n\n")

    print("{:-^42}".format("RANKING DE PALABRAS"))
    print("{:<10} {:<10}".format("Palabra", "Ocurrencias"))

    for palabra in range(0, len(ranking_palabras)):
        print("{:<10} {:<10}".format(ranking_palabras[palabra][0], ranking_palabras[palabra][1]))


main()
