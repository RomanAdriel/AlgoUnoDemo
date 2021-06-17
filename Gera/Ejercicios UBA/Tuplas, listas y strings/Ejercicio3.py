"""Por cada alumno que rindió un examen de una materia se lee el número de legajo
y la nota obtenida. Se desea saber la cantidad de alumnos que rindieron el
examen, el porcentaje de alumnos que obtuvieron cada nota, y el (o los) legajos
de la nota más alta.
"""

import random


def notas_por_alumno():
    notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    legajos = [123, 546, 114, 558, 798, 884, 881]
    alumnos = {}

    for i in legajos:
        alumnos[i] = random.choice(notas)

    return alumnos


def alumos_que_rindieron(alumnado):
    cantidad_rindieron = len(alumnado)

    return cantidad_rindieron


def main():
    alumnos_notas = notas_por_alumno()

    print(alumnos_notas)
    print(alumos_que_rindieron(alumnos_notas))


__init__: main()

