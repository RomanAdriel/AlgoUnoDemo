"""Se leen datos (usar constantes para poder achicar esta cantidad) que
representan el peso de la misma cantidad de niños que hay internados en un
hospital. Se desea confeccionar la siguiente tabla:
- Entre 0,000 y 10,000 kg. hay ............... niños.
- Entre 10,001 y 20,000 kg. hay ............. niños.
- Entre 20,001 y 30,000 kg. hay ............. niños.
- Más de 30,000 kg. hay .................... niños.
- Nota: Probar el ejercicio modificando 300 por 15, tratar de repartir los valores
en diferentes rangos. Verificar. Luego, utilizando la función random, simular el
ingreso de los datos."""

import random


def cantidad_pendejes():
    pendejes = int(input("ingrese la cantidad de pendex: "))
    return pendejes


def gestion_peso(pen):
    pesos = []
    for a in range(0, pen):
        pesos.append(random.uniform(float(0.001), float(40.001)))
    return pesos


def asigisgnacion_peso(pen, pes):
    peso1 = []
    peso2 = []
    peso3 = []
    peso4 = []
    for b in range(0, pen):
        if pes[b] <= 10.000:
            peso1.append(b)
        elif pes[b] >= 10.001 and pes[b] <= 20.000:
            peso2.append(b)
        elif pes[b] >= 20.001 and pes[b] <= 30.000:
            peso3.append(b)
        else:
            peso4.append(b)
    return len(peso1), len(peso2), len(peso3), len(peso4)


# def asigisgnacion_peso(pen, pes):
#     peso1 = 0
#     peso2 = 0
#     peso3 = 0
#     peso4 = 0
#     contador = 0
#     while contador < pen:
#         if pes[contador] <= 10.000:
#             peso1 += 1
#         elif pes[contador] >= 10.001 and pes[contador] <= 20.000:
#             peso2 += 1
#         elif pes[contador] >= 20.001 and pes[contador] <= 30.000:
#             peso3 += 1
#         else:
#             peso4 += 1
#         contador += 1
#     return peso1, peso2, peso3, peso4


def imprimir_resultados(a, b, c, d):
    print("Entre 0,000 y 10,000 kg. hay " + str(a), "\n"
          "Entre 10,001 y 20,000 kg. hay " + str(b), "\n"
          "Entre 20,001 y 30,000 kg. hay " + str(c), "\n"
          "Más de 30,000 kg. hay " + str(d))


pendejes = cantidad_pendejes()
aleatorio = gestion_peso(pendejes)
asignacion = asigisgnacion_peso(pendejes, aleatorio)
# cant_pendejes, cant_pesos = asignacion
peso_1, peso_2, peso_3, peso_4 = asignacion
imprimir_resultados(peso_1, peso_2, peso_3, peso_4)
