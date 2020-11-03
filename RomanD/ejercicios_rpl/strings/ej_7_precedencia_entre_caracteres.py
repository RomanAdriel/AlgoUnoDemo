"""Completar el cuerpo de la función. La misma debe retornar la cantidad de veces que el caracter_1 se encuentra
inmediatamente antes (es decir, en el índice anterior) al caracter_2 en la cadena que se recibe como primer parámetro.

No resolver el ejercicio usando la función .count(). Iterar la cadena.

Ejemplos:

   precendencia_de_caracteres("hola hola", "h", "o") => 2
   precendencia_de_caracteres("la igualdad de genero es fundamental para
          el desarrollo de una sociedad", "a", "l") => 2
   precendencia_de_caracteres("la mejor verdura del universo es la pizza y el que
          diga lo contrario esta errado", "e", "r") => 3"""


def precendencia_de_caracteres(cadena, caracter_1, caracter_2):
    precedencia = 0
    indice = 0

    for caracter in cadena:
        if caracter == caracter_2:
            if cadena[indice - 1] == caracter_1:
                precedencia += 1
        indice += 1

    return precedencia


print(
    precendencia_de_caracteres("la mejor verdura del universo es la pizza y el que diga lo contrario esta errado", "e",
                               "r"))
