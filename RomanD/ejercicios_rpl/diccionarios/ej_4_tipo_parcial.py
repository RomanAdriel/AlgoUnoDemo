"""Para comenzar, se deben comenzar cargando en un diccionario pares de datos localidad-personas, donde el valor de
las personas hace referencia a la cantidad de personas que se encuentra en edad de trabajar.
Debe tenerse en cuenta que, como los datos se obtienen de distintas planillas, es posible que se ingrese más de un par
clave-valor asociada a una localidad.

Una vez que el usuario terminar de realizar la carga, se deben imprimir:

a) El total de personas en edad laboral y el total de empleados para cada localidad.

b) Un listado ordenado de mayor a menor por porcentaje de desocupación. Debe tenerse en cuenta que para determinar el
porcentaje de desocupación se puede utilizar la fórmula:

% desocupacion = (1 - empleados / personas en edad de trabajar) * 100

En el siguiente ejemplo se detallan los mensajes que deben ser mostrados al usuario. Recordar que para que el ejercicio
pase las pruebas, se tiene que mostrar exactamente el mismo.

Ejemplo:

>> Ingrese localidad: CABA
>> Ingrese la cantidad de personas que pueden trabajar: 10
>> Ingrese la cantidad de empleados: 9
>> Desea seguir ingresando?(s/n): s
>> Ingrese localidad: Lanus
>> Ingrese la cantidad de personas que pueden trabajar: 10
>> Ingrese la cantidad de empleados: 7
>> Desea seguir ingresando?(s/n): s
>> Ingrese localidad: CABA
>> Ingrese la cantidad de personas que pueden trabajar: 10
>> Ingrese la cantidad de empleados: 6
>> Desea seguir ingresando?(s/n): s
>> Ingrese localidad: Lanus
>> Ingrese la cantidad de personas que pueden trabajar: 10
>> Ingrese la cantidad de empleados: 6
>> Desea seguir ingresando?(s/n): s
>> Ingrese localidad: Chascomus
>> Ingrese la cantidad de personas que pueden trabajar: 10
>> Ingrese la cantidad de empleados: 6
>> Desea seguir ingresando?(s/n): n
En la localidad de CABA hay 20 personas en edad laboral y 17 trabajando.
En la localidad de Lanus hay 20 personas en edad laboral y 15 trabajando.
En la localidad de Chascomus hay 10 personas en edad laboral y 6 trabajando.
La tasa de desocupacion en Chascomus es 40.0%.
La tasa de desocupacion en Lanus es 35.0%.
La tasa de desocupacion en CABA es 25.0%."""


def ingreso_datos(mensaje):
    valor_ingresado = input(mensaje)

    return valor_ingresado


def carga_datos():
    tabla_localidades = {}
    corte = "s"

    while corte != "n":

        localidad = ingreso_datos("Ingrese localidad: ")
        trabajadores = int(ingreso_datos("Ingrese la cantidad de personas que pueden trabajar: "))
        empleados = int(ingreso_datos("Ingrese la cantidad de empleados: "))

        if localidad not in tabla_localidades:
            tabla_localidades[localidad] = [trabajadores, empleados]

        else:
            tabla_localidades[localidad][0] += trabajadores
            tabla_localidades[localidad][1] += empleados

        corte = ingreso_datos("Desea seguir ingresando?(s/n): ")

    return tabla_localidades


def calcular_desocupacion(tabla):
    lista = []

    for registro in tabla.items():
        desocupacion = registro[0], (1 - registro[1][1] / registro[1][0]) * 100
        lista.append(desocupacion)

    lista.sort(key=lambda tupla: tupla[1], reverse=True)

    return lista


def imprimir_datos(tabla, lista):
    for registro in tabla.items():
        print(
            "En la localidad de {localidad} hay {trabajadores} personas en edad laboral y {empleados} trabajando.".format(
                localidad=registro[0], trabajadores=registro[1][0], empleados=registro[1][1]))

    for elementos in lista:
        print("La tasa de desocupacion en {localidad} es {desocupacion}%.".format(localidad=elementos[0],
                                                                                  desocupacion=elementos[1]))


def main():
    tabla_localidades = carga_datos()
    cantidad_desocupados = calcular_desocupacion(tabla_localidades)
    imprimir_datos(tabla_localidades, cantidad_desocupados)


main()
