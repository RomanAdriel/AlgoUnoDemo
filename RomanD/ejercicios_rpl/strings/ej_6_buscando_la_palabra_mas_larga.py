"""Completar el cuerpo de la función. La misma recibe un texto y debe retornar cuál es la palabra más larga del 
mismo. Se puede asumir que todas las palabras están separadas por espacios y no hay caracteres especiales.

No se pueden utilizar funciones de otras estructuras de datos. El ejercicio se debe resolver iterando la cadena, 
llevando el registro de las variables que se consideren adecuadas.

Ayuda: Tener cuidado con el caso en el que la palabra más larga es la última de todo el texto.

Ejemplos:

    palabra_mas_larga("Hola como estas este es un texto de prueba") => "prueba"
    palabra_mas_larga("Quiero aprobar algoritmos y algebra") => "algoritmos"""""


def palabra_mas_larga(texto):

    texto_limpio = texto.strip()
    cadena_mas_larga = ""
    nueva_palabra = ""

    for caracter in texto_limpio:
        if caracter != " ":
            nueva_palabra = nueva_palabra + caracter

            if len(nueva_palabra) > len(cadena_mas_larga):
                cadena_mas_larga = nueva_palabra

        elif caracter == " ":
            nueva_palabra = ""

    return cadena_mas_larga


print(palabra_mas_larga("Quiero aprobar algoritmos y algebra"))
