"""La idea de esta sección es completar las distintas funciones de acuerdo a los requerimientos especificados para
cada una de ellas, tal como se hizo para el resto del módulo de listas.

filtrar_primos: Recibe una lista de números enteros y un número adicional. Retorna una nueva lista filtrada, que
ontiene aquellos números que sean primos y además sean mayores al segundo número que se recibió como parámetro.

HINT: Pueden utilizar la función es_primo(), correspondiente al módulo de funciones.

Ejemplos:

    filtrar_primos([3, 7, 11, 13], 8) => [11, 13]
    filtrar_primos([11, 7, 3, 19], 15) => [19]

ordenar_por_longitud_de_tuplas: Recibe una lista de tuplas. Retorna una nueva lista ordenada de mayor a menor por
la longitud de las mismas. Aclaración: No importa el tipo de los elementos que se encuentran contenidos en las tuplas.

Ejemplo:

    lista_tuplas = [(1,5,6), (1,2), (1), (6,4,5,6), ("asd", 9, 5.6, "l", "s")]
    ordenar_por_longitud_de_tuplas(lista_tuplas) => [("asd", 9, 5.6, "l", "s"), (6,4,5,6), (1,5,6), (1,2), (1)]

concatenar_primeros_elementos: Recibe una lista de lista de listas. Se puede asumir que cada una de las listas
internas tiene una longitud mayor a 3. Retorna una única lista, que resulta de la concatenación de los primeros
2 elementos de cada una de las listas internas, en el orden original.

Ejemplo:

    lista = [[1,4,5,6], [2,3,4,5], [6,4,4,6,7,8], [5,6,7,3,5,6,4]]
    concatenar_primeros_elementos(lista) => [1,4,2,3,6,4,5,6]"""


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


def filtrar_primos(numeros, menor_numero):
    is_primo = True
    divisor = 2
    lista_primos = []

    for numero in numeros:

        if numero > 1 and numero > menor_numero:

            while is_primo and divisor < numero:
                if numero % divisor != 0:
                    divisor += 1
                else:
                    is_primo = False

            if is_primo:
                lista_primos.append(numero)

            is_primo = True
            divisor = 2

    return lista_primos


def ordenar_por_longitud_de_tuplas(tuplas):
    return sorted(tuplas, key=len, reverse=True)


def concatenar_primeros_elementos(lista):
    sublistas = [tupla[:2] for indice, tupla in enumerate(lista)]
    lista_de_listas = []

    for sublista in sublistas:
        lista_de_listas.extend(sublista)

    return lista_de_listas
