"""Completar el cuerpo de la función. La misma debe devolver True en caso de que el número que se recibe como
parámetro sea primo, y False en caso contrario.

Ejemplos:

es_primo(3) => True
es_primo(4) => False
es_primo(11) => True
es_primo(15) => False"""

def es_primo(numero):

    is_primo = True
    divisor = 2

    if numero > 1:

        while is_primo and divisor < numero:
            if numero % divisor != 0:
                divisor += 1
            else:
                is_primo = False

    else:
        is_primo = False

    return is_primo



