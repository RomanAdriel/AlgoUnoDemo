"""Escribir un programa que solicite al usuario el ingreso del nombre de un equipo local con la cantidad de goles
que metió en un partido, y del nombre de un equipo visitante con la cantidad de goles que metió en el mismo partido.
Luego, imprimir por pantalla el nombre del ganador o un mensaje indicando que hubo un empate.

    Ingrese equipo local: Boca
    Ingrese goles equipo local: 3
    Ingrese equipo local: River
    Ingrese goles equipo visitante: 1
    Boca

    Ingrese equipo local: Boca
    Ingrese goles equipo local: 0
    Ingrese equipo local: River
    Ingrese goles equipo visitante: 2
    River

    Ingrese equipo local: Boca
    Ingrese goles equipo local:2
    Ingrese equipo local: River
    Ingrese goles equipo visitante: 2
    Empate"""

equipo_local = input("Ingrese equipo local: ")
goles_local = int(input("Ingrese goles equipo local: "))
equipo_visitante = input("Ingrese equipo visitante: ")
goles_visitante = int(input("Ingrese goles equipo visitante: "))

if goles_local > goles_visitante:
    print(equipo_local)
elif goles_local < goles_visitante:
    print(equipo_visitante)
else:
    print("Empate")