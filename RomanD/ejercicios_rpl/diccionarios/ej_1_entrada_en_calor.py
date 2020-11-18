"""Los ejercicios de esta sección tienen como objetivo empezar a jugar con diccionarios resolviendo una serie de
problemas que implican completar funciones a partir de ciertos requerimientos.

numeros_al_cuadrado: Recibe un numero entero positivo. Retorna un diccionario cuya claves comprenden el rango de
números positivos tomando como límite superior el número que se recibió como parámetro, y donde para cada clave su
valor asociado será el número de la clave al cuadrado.

Ejemplo:

    numeros_al_cuadrado(4) => {1: 1, 2: 4, 3: 9, 4: 16}

mezclar_diccionarios: Recibe dos diccionarios. Retorna un único diccionario, que resultad de realizar la mezcla entre
los dos. Las claves del nuevo diccionario deben ser las claves de ambos (asumir que no tienen claves iguales), con
sus respectivos valores.

Ejemplo:

    dicc_1 = {'clave1': 1, 'clave3': 3}
    dicc_2 = {'clave2': 2, 'clave4': valor4}

    numeros_al_cuadrado(dicc_1, dicc_2) =>

           {'clave1': 1, 'clave3': 3, 'clave2': 2, 'clave4': 4}

Aclaración: El orden de los pares asociados clave-valor puede ser cualquiera.

filtrar_por_sumar_diez: Recibe un diccionario cuyas claves son enteros, y también su valor asociado. Retorna un
diccionario que contiene únicamente los pares clave-valor del diccionario que se recibió por parámetro que al sumarlos
sean mayores o iguales a 10.

Ejemplo:

   filtrar_por_sumar_diez({8: 11, 3: 6, 9: 2, 1: 4}) => {8: 11, 9: 2}

ordenar_valores_por_longitud: Recibe un diccionario con claves de tipo string y valores asociados de tipo string.
Retorna una lista ordenada que contiene únicamente los valores del diccionario. Esta lista debe estar ordenada
descendentemente (mayor a menor) según la longitud que tienen las cadenas de caracteres que son valor.

Ejemplo:

   dicc = {'boca':'river', 'pablo':'guarna', 'hola':'algoritmos'}
   ordenar_valores_por_longitud(dicc) => ['algoritmos','guarna','river']"""


def numeros_al_cuadrado(numero):

    cuadrados = {}

    for key in range(1, numero + 1):

        cuadrados[key] = key ** 2

    return cuadrados


def mezclar_diccionarios(dicc_uno, dicc_dos):

    dic_mergeado = {}
    indice = 0

    for pares_uno, pares_dos in zip(dicc_uno.items(), dicc_dos.items()):

        dic_mergeado[pares_uno[indice]] = pares_uno[indice + 1]
        dic_mergeado[pares_dos[indice]] = pares_dos[indice + 1]

    return dic_mergeado


def filtrar_por_sumar_diez(diccionario):

    dic_filtrado = {}

    for key, value in diccionario.items():

        if key + value >= 10:

            dic_filtrado[key] = value

    return dic_filtrado


def ordenar_valores_por_longitud(diccionario):

    return sorted(diccionario.values(), key=len, reverse=True)