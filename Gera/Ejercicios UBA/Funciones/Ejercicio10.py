"""La relación entre temperaturas Celsius y Fahrenheit está dada por: C = 5/9 * (F-32)
Escribir un algoritmo que haga una tabla de valores Celsius-Fahrenheit, para
valores entre OF y 200ºF, con intervalos de 10º"""


def crear_graduacion_farenheit():
    origen_farenheit = []
    for i in range(0, 21):
        origen_farenheit.append(i*10)
    return origen_farenheit


def pasar_farenheit_a_celsius(grados_farenheit):
    i = 0
    resultado_celsius = []
    while i < len(grados_farenheit):
        resultado_celsius.append(5/9*(grados_farenheit[i]-32))
        i += 1
    return resultado_celsius


def imprimir_con_formato(origen, conversion):
    for i in range(0, len(origen)):
        print(str(origen[i]) + "°", "Farenheit son ", str(f'{conversion[i]:.2f}') + "° Celsius")


def main():

    origen = crear_graduacion_farenheit()
    conversion = pasar_farenheit_a_celsius(origen)
    imprimir_con_formato(origen, conversion)


__init__: main()
