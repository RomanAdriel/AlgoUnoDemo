""" Si los números de un vector representan los coeficientes de un polinomio (de
grado no mayor a 10), escribir un algoritmo que calcule la especialización de ese
polinomio con un número que elige el usuario. """


def generar_especializacion_polinomio(coeficientes, valor_de_x):
    lista_polinomio = []
    for i in range(0, len(coeficientes)):
        lista_polinomio.append(coeficientes[i] * valor_de_x ** i)

    return lista_polinomio


def calcular_polinomio_especializado(polinomio_listado):
    resultado = 0
    for termino in polinomio_listado:
        resultado += termino

    return resultado


def generar_terminos_con_x(coeficientes):
    cadena = ""
    for i in range(0, len(coeficientes)):
        if coeficientes[i] >= 0:
            cadena = cadena + "+" + str(coeficientes[i]) + str("X^" + str(i) + " ")
        else:
            cadena = cadena + str(coeficientes[i]) + str("X^" + str(i) + " ")
    return cadena


def main():
    coeficientes_ascendentes = [0, 0, 0, 0, 0, 0, 0]
    x = int(input("ingrese el valor de X: "))
    terminos = generar_especializacion_polinomio(coeficientes_ascendentes, x)
    resultado = calcular_polinomio_especializado(terminos)

    print("P(x) =", generar_terminos_con_x(coeficientes_ascendentes))
    print("El resultado de P(", x, ") es: ", resultado)


__init__: main()
