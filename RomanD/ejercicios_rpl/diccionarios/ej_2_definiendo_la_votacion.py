"""Este ejercicio requiere la construcción de un pequeño programa que sirva para registrar votos correspondientes a
una votación y determinar cuál fue el partido ganador.

Para esto, deberemos comenzar solicitando al usuario que ingrese votos para los distintos partidos hasta que decida
finalizar la carga. En un diccionario, se tienen que ir contabilizando los votos que llegan para los distintos partidos.
Es posible que haya votos que lleguen al centro de votación para un partido para el cual se recibieron votos
previamente.

Finalmente, se tienen que imprimir ordenadamente una lista con todos los partidos con su correspondiente cantidad de
votos, ordenados de mayor a menor. (HINT: Usar alguna función para formatear strings, por ejemplo .format())

En el siguiente ejemplo se detallan los mensajes que deben ser mostrados al usuario. Recordar que para que el ejercicio
pase las pruebas, se tiene que mostrar exactamente el mismo.

Ejemplo:

>> Ingrese el partido a sumarle votos: Blanco
>> Ingrese la cantidad de votos a sumarle: 2
>> Desea seguir ingresando?(s/n): s
>> Ingrese el partido a sumarle votos: Rosa
>> Ingrese la cantidad de votos a sumarle: 3
>> Desea seguir ingresando?(s/n): s
>> Ingrese el partido a sumarle votos: Rosa
>> Ingrese la cantidad de votos a sumarle: 4
>> Desea seguir ingresando?(s/n): s
>> Ingrese el partido a sumarle votos: Blanco
>> Ingrese la cantidad de votos a sumarle: 4
>> Desea seguir ingresando?(s/n): n
El partido Rosa obtuvo 7 votos.
El partido Blanco obtuvo 6 votos.

Notar que se puede asumir que se ingresa al menos un par partido-votos.
Pensar bien la modularización del programa."""


def ingreso_datos(mensaje):

    valor_ingresado = input(mensaje)

    return valor_ingresado

def carga_datos():

    tabla_partidos = {}
    corte = "s"

    while corte != "n":

        partido = ingreso_datos("Ingrese el partido a sumarle votos: ")
        votos = ingreso_datos("Ingrese la cantidad de votos a sumarle: ")

        if partido not in tabla_partidos:
            tabla_partidos[partido] = int(votos)

        else:
            tabla_partidos[partido] += int(votos)

        corte = ingreso_datos("Desea seguir ingresando?(s/n): ")

    return tabla_partidos

def ordenar_datos(tabla):

    lista = []

    for registro in tabla.items():
        lista.append(registro)

    lista.sort(key=lambda tupla: tupla[1], reverse=True)

    return lista

def imprimir_datos(lista):

    for elementos in lista:
        print("El partido {partido} obtuvo {votos} votos.".format(partido=elementos[0], votos=elementos[1]))


def main():

    tabla_de_partidos = carga_datos()
    partidos_ordenados = ordenar_datos(tabla_de_partidos)
    imprimir_datos(partidos_ordenados)

main()




