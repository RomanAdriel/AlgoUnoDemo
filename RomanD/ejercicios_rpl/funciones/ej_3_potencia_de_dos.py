"""Completar el cuerpo de la función. La misma debe devolver True en caso de que el número recibido sea una potencia
de dos, y False en caso contrario.

Ejemplos:

es_potencia_de_dos(1) => True
es_potencia_de_dos(2) => True
es_potencia_de_dos(3) => False
es_potencia_de_dos(4) => True
es_potencia_de_dos(15) => False
es_potencia_de_dos(16) => True
es_potencia_de_dos(30) => False
es_potencia_de_dos(32) => True"""


def es_potencia_de_dos(numero):
    is_potencia = True
    cociente = numero

    if numero > 0:

        while is_potencia and cociente > 1:
            if cociente % 2 == 0:
                cociente = cociente / 2

            else:
                is_potencia = False

    else:

        is_potencia = False

    return is_potencia


print(es_potencia_de_dos(128))
