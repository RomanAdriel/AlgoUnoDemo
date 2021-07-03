"""Dada una serie de datos de la forma mes (1 a 12, no vienen ordenados), cantidad recaudada (en pesos) y costo total
en pesos), hacer un algoritmo que calcule e imprima cuál fue el mes que arrojó mayor ganancia. La serie termina con mes
igual a cero. No se deben guardar los datos. """

"""Modularizar más el código; crear una funcion para ingreso de datos, una para el cálculo y otra para imprimir los 
resultados"""


def ingresar_datos():
    mes = int(input("Ingresar el mes (0 para salir): "))
    return mes


def calcular_ganancia(valor):
    mes_max = 0
    ganancia_max = 0
    while valor != 0:
        recaudado = float(input("Ingresar el total recaudado: "))
        costo = float(input("Ingresar costo del mes: "))
        ganancia = recaudado - costo
        if ganancia >= ganancia_max:
            ganancia_max = ganancia
            mes_max = valor
        valor = int(input("Ingresar el mes (0 para salir): "))
    return mes_max, ganancia_max


def imprimir_resultados(mm, gm):
    print("El mes " + str(mm) + " fue el más provechoso, con una ganancia de: $" + str(gm))


ingresar = ingresar_datos()
calculos = calcular_ganancia(ingresar)
mejor_mes, mayor_ganancia = calculos
imprimir_resultados(mejor_mes, mayor_ganancia)
