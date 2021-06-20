"""Dada una serie de datos de la forma mes (1 a 12, no vienen ordenados), cantidad
recaudada (en pesos) y costo total (en pesos), hacer un algoritmo que calcule e
imprima cuál fue el mes que arrojó mayor ganancia. La serie termina con mes
igual a cero. No se deben guardar los datos.
"""


def ingresar_datos():
    recaudacion = int(input("ingrese recaudacion en $"))
    costo = int(input("ingrese costo en $ "))
    mes = int(input("ingrese numero de mes: "))

    return mes, recaudacion, costo


def calcular_mes_ganancia(datos):
    mes, recaudacion, costo = datos
    ganancia = recaudacion - costo

    return mes, ganancia


def comparar_ganancias(dato1, dato2):
    if dato1[1] > dato2[1]:
        mayor_ganancia = dato1
    else:
        mayor_ganancia = dato2
    return mayor_ganancia


def mes_maximo():
    valor1 = calcular_mes_ganancia(ingresar_datos())
    if valor1[0] != 0:
        valor2 = calcular_mes_ganancia(ingresar_datos())
        while valor2[0] != 0:
            valor1 = comparar_ganancias(valor1, valor2)
            valor2 = calcular_mes_ganancia(ingresar_datos())
        return valor1


def imprimir_resultado(datos_mes_maximo):
    if datos_mes_maximo:
        print("El mes", datos_mes_maximo[0], "tuvo una ganancia de $", datos_mes_maximo[1], "y fue el máximo")
    else:
        print("Datos insuficientes")


def main():
    test = mes_maximo()
    imprimir_resultado(test)


__init__: main()
