"""Se leen 300 datos (usar constantes para poder achicar esta cantidad) que representan el peso de la misma cantidad de
niños que hay internados en un hospital.
Se desea confeccionar la siguiente tabla:
- Entre 0,000 y 10,000 kg. hay ............... niños.
- Entre 10,001 y 20,000 kg. hay ............. niños.
- Entre 20,001 y 30,000 kg. hay ............. niños.
- Más de 30,000 kg. hay .................... niños.
- Nota: Probar el ejercicio modificando 300 por 15, tratar de repartir los valores en diferentes rangos. Verificar.
Luego, utilizando la función random, simular el ingreso de los 300 datos. """

import random


def cantidad_pibes():
    pibes = int(input("Ingrese la cantidad de pibes que hay en el hospital: "))
    return pibes


def asignar_peso(cantidad_pibes):
    peso_pibes = []
    for a in range(0, cantidad_pibes):
        peso_pibes.append(random.uniform(float(0.001), float(50.000)))
    return peso_pibes


def categorizar_pesos(pibes, peso):
    hasta_10 = 0
    hasta_20 = 0
    hasta_30 = 0
    mas_de_30 = 0
    contador = 0
    while contador < pibes:
        if 0.001 < peso[contador] <= 10.000:
            hasta_10 += 1
        elif 10.001 <= peso[contador] <= 20.000:
            hasta_20 += 1
        elif 20.001 <= peso[contador] <= 30.000:
            hasta_30 += 1
        else:
            mas_de_30 += 1
        contador += 1
    pesos_ordenados = [hasta_10, hasta_20, hasta_30, mas_de_30]
    return pesos_ordenados


def resultados(pesos_ordenados):
    print(" - Entre 0,000 y 10,000 kg. hay", pesos_ordenados[0], " niños.\n",
          "- Entre 10,001 y 20,000 kg. hay", pesos_ordenados[1], "niños.\n",
          "- Entre 20,001 y 30,000 kg. hay ", pesos_ordenados[2], "niños.\n",
          "- Más de 30,000 kg. hay ", pesos_ordenados[3], " niños.")


pibes = cantidad_pibes()
pesos = asignar_peso(pibes)
pesos_ordenados = categorizar_pesos(pibes, pesos)
resultados(pesos_ordenados)
