"""Dado un texto terminado en punto, determinar cuál es la vocal que aparece con
mayor frecuencia"""


def contar_palabras(texto):
    diccionario = "aeiouáéíóú"
    vocales = {}
    for vocal in texto:
        if vocal in diccionario and vocal in vocales:
            vocales[vocal] += 1
        elif vocal in diccionario:
            vocales[vocal] = 1
  #  print(vocales)
    return vocales

def obtener_max(vocales):
    vocal_mas_usada = max(zip(vocales.values(), vocales.keys()))
    return vocal_mas_usada



def imprimir_resultado(cantidades):
    print(cantidades)


texto = contar_palabras("aaaaa234242ttttttt34234aaaeiiuuooo")
vocales = obtener_max(texto)
imprimir_resultado(vocales)

