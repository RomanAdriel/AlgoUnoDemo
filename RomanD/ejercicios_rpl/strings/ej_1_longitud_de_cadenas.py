"""Completar el cuerpo de la función. La misma recibe tres cadenas previamente inicializadas y debe retornar la suma
de la longitud de la concatenación de las tres cadenas.

Ejemplo:

    longitud_cadenas("hola", "como", "estas") => 13
    longitud_cadenas("a", "b", "c") => 3"""


def longitud_cadenas(cadena_1, cadena_2, cadena_3):

    return len(cadena_1 + cadena_2 + cadena_3)

print(longitud_cadenas("hola", "como", "estas"))