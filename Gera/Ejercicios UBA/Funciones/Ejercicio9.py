"""Se leen 300 datos (usar constantes para poder achicar esta cantidad) que
representan el peso de la misma cantidad de niños que hay internados en un
hospital. Se desea confeccionar la siguiente tabla:
- Entre 0,000 y 10,000 kg. hay ............... niños.
- Entre 10,001 y 20,000 kg. hay ............. niños.
- Entre 20,001 y 30,000 kg. hay ............. niños.
- Más de 30,000 kg. hay .................... niños. """

import random


def ingreso_cantidad_ninios():
    ninios = int(input("ingresar la cantidad de niños totales: "))
    return ninios


def generar_ingreso_peso_aleatorio(cantidad_ninios):

    peso = []
    for i in range(0, cantidad_ninios):
        peso.append(random.uniform(float(0.000), float(40.000)))

    return peso


def contar_ninios_por_peso(cantidad_ninios, pesajes):
    cantidad_a = 0
    cantidad_b = 0
    cantidad_c = 0
    cantidad_d = 0
    i = 0

    while i <= cantidad_ninios - 1:
        if float(0.000) < pesajes[i] <= float(10.000):
            cantidad_a += 1
        elif float(10.000) < pesajes[i] <= float(20.000):
            cantidad_b += 1
        elif float(20.000) < pesajes[i] <= float(30.000):
            cantidad_c += 1
        else:
            cantidad_d += 1
        i += 1

    pesajes_ordenados = [cantidad_a, cantidad_b, cantidad_c, cantidad_d]

    return pesajes_ordenados


def imprimir_resultados(ninios_pesados):
    hasta_10 = ninios_pesados[0]
    hasta_20 = ninios_pesados[1]
    hasta_30 = ninios_pesados[2]
    mas_de_30 = ninios_pesados[3]
    if ninios_pesados:
        print("- Entre 0,000 y 10,000 kg. hay", hasta_10," niños.\n",
              "- Entre 10,001 y 20,000 kg. hay", hasta_20, "niños.\n",
              "- Entre 20,001 y 30,000 kg. hay ", hasta_30, "niños.\n",
              "- Más de 30,000 kg. hay ", mas_de_30, " niños.")
    else:
        print("No se ingresaron datos")


def main():
    ninios = ingreso_cantidad_ninios()
    pesajes = generar_ingreso_peso_aleatorio(ninios)
    ninios_pesados = contar_ninios_por_peso(ninios, pesajes)

    imprimir_resultados(ninios_pesados)


__init__: main()

