"""Se pide que ingresen por teclado pares de equipo – puntos ganados, el mismo
par se puede ingresar varias veces. Se pide
a. generar una tabla de puntos acumulados para cada equipo.
b. Mostrar la tabla de posiciones (equipo – total de puntos) ordenada por
el total de puntos en forma descendente."""

def ingreso_datos(mensaje):

    valor_ingresado = input(mensaje)

    return valor_ingresado

tabla_equipos = {}
corte = "y"


while corte != "n":

    equipo = ingreso_datos("Ingrese el equipo: ")
    puntos = ingreso_datos("Ingrese su puntaje: ")

    if equipo not in tabla_equipos:
        tabla_equipos[equipo] = puntos

    else:
        tabla_equipos[equipo] += puntos

    corte = ingreso_datos("Desea ingresar más equipos? (y/n) ")

lista_de_equipos = []

for registro in tabla_equipos.items():
    lista_de_equipos.append(registro)

lista_de_equipos.sort(key=lambda tupla: tupla[1], reverse=True)

print("{:<10} {:<10}".format("Equipo", "Puntaje"))

for equipos in range(0, len(lista_de_equipos)):
    print("{:<10} {:<10}".format(lista_de_equipos[equipos][0], lista_de_equipos[equipos][1]))