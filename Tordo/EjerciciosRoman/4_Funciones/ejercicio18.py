"""Escribir un algoritmo que lea un número real cualquiera y lo redondee con dos
decimales. Verificar con distintas entradas. """


def ingreso_valores():
    numero = float(input("Ingrese un valor para redondear: "))
    return numero


def redondear_valor(valor):
    resultado = round(valor, 2)
    return resultado


def imprimir_resultados(numero_redondeado):
    print(numero_redondeado)


ingreso = ingreso_valores()
redondeo = redondear_valor(ingreso)
imprimir_resultados(redondeo)
