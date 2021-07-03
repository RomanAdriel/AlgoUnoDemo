"""Realizar un algoritmo que lea una serie de números reales y verifique si están
ordenados en forma ascendente, descendente o si no están ordenados,
informando por pantalla."""


def armado_lista():
    lista = []
    ingreso_numero = int(input("Ingrese un número (0 para salir): "))
    while ingreso_numero != 0:
        lista.append(ingreso_numero)
        ingreso_numero = int(input("Ingrese un número (0 para salir): "))
    return lista


def lista_asc(valor):
    orden_asc = 1
    indice = 0
    flag = 0
    while indice < len(valor) - 1:
        if valor[indice] < valor[indice + 1]:
            flag += 1
        indice += 1
    if len(valor) - 1 == flag:
        orden_asc = 0
    return orden_asc


def lista_desc(valor):
    orden_des = 1
    indice = 0
    flag = 0
    while indice < len(valor) - 1:
        if valor[indice] > valor[indice + 1]:
            flag += 1
        indice += 1
    if len(valor) - 1 == flag:
        orden_des = 0
    return orden_des


def imprimir_resultados(asc, des):
    if asc == 0:
        print("La serie de numeros reales ingresada está ordenada de forma ascendente.")
    elif des == 0:
        print("La serie de numeros reales ingresada está ordenada de forma descendente.")
    else:
        print("La serie de nuneros ingresada no está ordenada.")


lista_final = armado_lista()

ascendente = lista_asc(lista_final)

descendente = lista_desc(lista_final)

imprimir_resultados(ascendente, descendente)
