"""Se leen 300 datos (usar constantes para poder achicar esta cantidad) que
representan el peso de la misma cantidad de niños que hay internados en un
hospital. Se desea confeccionar la siguiente tabla:
- Entre 0,000 y 10,000 kg. hay ............... niños.
- Entre 10,001 y 20,000 kg. hay ............. niños.
- Entre 20,001 y 30,000 kg. hay ............. niños.
- Más de 30,000 kg. hay .................... niños. """

import random

def ingreso_cantidad_niños():
    niños = int(input("ingresar la cantidad de niños totales: "))
    return niños

def generar_ingreso_peso_aleatorio(cantidad_niños):

    peso = []
    for i in range(0, cantidad_niños):
        peso.append(random.uniform(float(0.00), float(40.00)))

    return peso


def contar_niños_por_peso(cantidad_niños, pesajes):
    cantidad_a = 0
    cantidad_b = 0
    cantidad_c = 0
    cantidad_d = 0
    i = 0

    while i <= cantidad_niños - 1:
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

def imprimir_resultados(niños_pesados):
    if niños_pesados:
        print("- Entre 0,000 y 10,000 kg. hay", niños_pesados[0] ," niños.\n",
              "- Entre 10,001 y 20,000 kg. hay", niños_pesados[1], "niños.\n",
              "- Entre 20,001 y 30,000 kg. hay ", niños_pesados[2], "niños.\n",
              "- Más de 30,000 kg. hay ", niños_pesados[3], " niños.")
    else:
        print("No se ingresaron datos")


def main():
    niños = ingreso_cantidad_niños()
    pesajes = generar_ingreso_peso_aleatorio(niños)
    niños_pesados = contar_niños_por_peso(niños, pesajes)

    imprimir_resultados(niños_pesados)

__init__ : main()