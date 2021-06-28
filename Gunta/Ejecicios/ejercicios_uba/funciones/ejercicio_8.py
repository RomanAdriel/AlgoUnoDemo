"""Dada una serie de datos de la forma mes (1 a 12, no vienen ordenados), cantidad
recaudada (en pesos) y costo total (en pesos), hacer un algoritmo que calcule e imprima cuál fue el mes que arrojó mayor ganancia. La serie termina con mes
igual a cero. No se deben guardar los datos."""

# -----------------------------------------------------------------


def ingresar_datos():
    mes = int(input("ingrese el mes (0 para salir): "))
    return mes


def cuanta_pobreza(a):
    mes_1 = 0
    ganancia_max = 0
    while a !=0:
        costo = float(input("ingesar el costo del producto: "))
        recaudacion = float(input("ingresar el monto recaudado: "))
        ganancia = recaudacion - costo
        if ganancia >= ganancia_max:
            ganancia_max = ganancia
            mes_1 = a
        a = int(input("ingrese el mes (0 para salir): "))
    return mes_1, ganancia_max


def resultado (a1, b1):
    print("Mes: " + str(a1) + " Monto: " + str(b1))


datos = ingresar_datos()
pobreza = cuanta_pobreza(datos)
mejor_mes, mejor_ganancia = pobreza
resultado(mejor_mes, mejor_ganancia)


# -----------------------------------------------------------------