"""Completar los cuerpos de las distintas funciones. A continuación se encuentran los requerimientos que deben
cumplir cada una de las funciones. Las funciones deben ser resueltas realizando iteraciones sobre las listas,
no se pueden usar funciones de ordenamiento.

filtrar_pares: Recibe una lista con variables numéricas enteras. Retorna una nueva lista con todos los números pares
que estaban en la lista que se recibió como parámetro. Los elementos de la lista devuelta deben estar en el
orden original.

Ejemplo:

    filtrar_pares([5,6,13,7,11,9,10,11]) => [6,10]

filtrar_primos: Recibe una lista con variables numéricas enteras. Retorna una nueva lista con todos los números primos
que estaban en la lista que se recibió como parámetro Los elementos de la lista devuelta deben estar en el
orden original.

Hint: Utilizar la función programada en otra actividad que determina si un número es primo o no.

Ejemplo:

    filtrar_primos([5,6,13,7,11,9,10,11]) => [5,13,7,11,11]

sumar_elementos: Recibe una lista con variables numéricas. Retorna la suma de todos sus elementos.
No se puede utilizar la función sum(), ya existente en Python.

Ejemplo:

    sumar_elementos([5,6,13,7,11,9,10,11]) => 72

esta_ordenada: Recibe una lista con variables numericas. Retorna True en caso de que la lista este ordenada
ascendentemente (es decir, los mas chicos en las primeras posiciones), False en caso contrario.

Ejemplos:

    esta_ordenada([5,6,13,7,11,9,10,11]) => False
    esta_ordenada([5,6,7,11]) => True

producto_escalar: Recibe dos listas de variables numéricas con la misma longitud. Interpretarlas como vectores.
Retorna el producto escalar entre ambos vectores.

Ejemplos:

    producto_escalar([2,5,3], [4,6,7]) => 59

letras_en_palabras: Recibe una lista de letras y una cadena. La lista contiene en cada índice de la misma una letra
(string de longitud 1). Retorna True caso de que todas las letras se encuentren en la palabra, False en caso contrario.

Ejemplos:

    letras_en_palabras(["a","h","e"], "hola como estas") => True
    letras_en_palabras(["a","h","e"], "ola como estas") => Falsa """


def filtrar_pares(lista):
    return [numero for numero in lista if numero % 2 == 0]


def filtrar_primos(lista):
    is_primo = True
    divisor = 2
    lista_primos = []

    for numero in lista:

        if numero > 1:

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


def sumar_elementos(lista):
    suma = 0

    for numero in lista:
        suma += numero

    return suma


def esta_ordenada(lista):
    numero_inicial = lista[0]
    lista_ordenada = True
    indice = 1

    while lista_ordenada and indice < len(lista):
        if numero_inicial <= lista[indice]:
            numero_inicial = lista[indice]
            indice += 1
        else:
            lista_ordenada = False

    return lista_ordenada


def producto_escalar(vector_1, vector_2):
    productos = [x * y for x, y in zip(vector_1, vector_2)]

    return sum(productos)


def letras_en_palabra(letras, frase):
    hay_match = True
    indice = 0

    while hay_match and indice < len(letras):
        if letras[indice] not in frase:
            hay_match = False
        indice += 1

    return hay_match
