"""Dado un texto terminado en “.” se pide determinar cuántas veces aparece
determinada letra que se indica por teclado. Sin utilizar funciones de string, salvo
len."""


def contar_palabras(texto):
    diccionario = "abcdefghijklmnñopqrstuvwxyzáéíóú"
    vocales = {}
    for vocal in texto:
        if vocal in diccionario and vocal in vocales:
            vocales[vocal] += 1
        else:
            vocales[vocal] = 1
    return vocales

def obtener_max(vocales):
    vocal_mas_usada = max(zip(vocales.values(), vocales.key()))
    return vocal_mas_usada



def imprimir_resultado(cantidades):
    print(cantidades)


texto = contar_palabras("aaaaaaaaeiiuuooo")
vocales = obtener_max(texto)
imprimir_resultado(vocales)

