""" La relación entre temperaturas Celsius y Fahrenheit está dada por: C = 5/9 * (F - 32) Escribir un algoritmo que haga
 una tabla de valores Celsius-Fahrenheit, para valores entre OF y 200ºF, con intervalos de 10º."""


def imprimir_celsius_a_farenheit():
    for i in range(0, 201, 10):
        celsius = float(5/9 * (i - 32))
        print(i, f'ºF es equivalente a {celsius:.2f}º Celsius')


imprimir_celsius_a_farenheit()
