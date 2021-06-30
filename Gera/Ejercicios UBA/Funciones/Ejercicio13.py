"""Dado un texto terminado en punto, determinar cuál es la vocal que aparece con
mayor frecuencia. """


def ingresar_texto():
    texto = input("ingrese el texto del telegrama: ")
    texto = texto.lower()
    return texto

def contar_letras_en_texto(texto):
    vocales = 'aeiou'
    vocal_max = {}

    for i in texto:
        if i in vocales and i in vocal_max:
            vocal_max[i] += 1
        elif i in vocales:
            vocal_max[i] = 1

    cantidad_vocal_max = max(zip(vocal_max.values(), vocal_max.keys()))

# (("e", 2 ), ("i", 5))
    return cantidad_vocal_max

test = "test de priiiiint"
print(contar_letras_en_texto(test))