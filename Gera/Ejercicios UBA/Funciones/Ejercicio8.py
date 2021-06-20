"""Dada una serie de datos de la forma mes (1 a 12, no vienen ordenados), cantidad
recaudada (en pesos) y costo total (en pesos), hacer un algoritmo que calcule e
imprima cuál fue el mes que arrojó mayor ganancia. La serie termina con mes
igual a cero. No se deben guardar los datos.
"""


def ingresar_datos():
    recaudacion = float(input("ingrese recaudacion en $"))
    costo = float(input("ingrese costo en $ "))
    mes = int(input("ingrese numero de mes: "))

    return mes, recaudacion, costo


def calcular_mes_ganancia(datos_ingresados):
    mes, recaudacion, costo = datos_ingresados
    ganancia = recaudacion - costo

    return mes, ganancia


def comparar_ganancias(ganancia_mensual1, ganancia_mensual2):
    indice_ganancia = 1
    if ganancia_mensual1[indice_ganancia] > ganancia_mensual2[indice_ganancia]:
        mayor_ganancia = ganancia_mensual1
    else:
        mayor_ganancia = ganancia_mensual2
    return mayor_ganancia


def mes_maximo():
    indice_mes = 0
    ganancia_max = calcular_mes_ganancia(ingresar_datos())
    if ganancia_max[indice_mes] != 0:
        comparar_ganancia = calcular_mes_ganancia(ingresar_datos())
        while comparar_ganancia[indice_mes] != 0:
            valor1 = comparar_ganancias(ganancia_max, comparar_ganancia)
            comparar_ganancia = calcular_mes_ganancia(ingresar_datos())
    return ganancia_max


def imprimir_resultado(datos_mes_maximo):
    indice_mes = 0
    indice_ganancia = 1
    if datos_mes_maximo:
        print("El mes", datos_mes_maximo[indice_mes], "tuvo una ganancia de $", datos_mes_maximo[indice_ganancia], "y fue el máximo")
    else:
        print("Datos insuficientes")


def main():
    test = mes_maximo()
    imprimir_resultado(test)


__init__: main()
