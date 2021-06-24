"""La relación entre temperaturas Celsius y Fahrenheit está dada por: C = 5/9 * (F-
32) Escribir un algoritmo que haga una tabla de valores Celsius-Fahrenheit, para
valores entre OF y 200ºF, con intervalos de 10º."""


# def tabla_valores(inicial, final):
#     tab_val = [[], []]
#     for i in range(inicial, final + 1, 10):
#         tab_val[0].append(i)
#         tab_val[1].append((i - 32) * 5 / 9)
#     return tab_val
#
#
# def imprimir(a):
#     for i in a
#         (print
#
#
# valores = tabla_valores(0, 201)
# resultado = imprimir(valores1, valores2)
#

def crear_tablas(a, b):  # Funcion que crea las tablas F y C
    tab_cel = []
    tab_far = []
    for i in range(a, b+1, 10):
        tab_cel.append(i)
        tab_far.append((i - 32) * 5 / 9)
    return tab_far, tab_cel


def imprimir_resultados(a, b):
    for valor_far, valor_cel in zip(a, b):
        print(round(valor_far), "Fahrenheit son ", round(valor_cel), " grados celsius")


valores = crear_tablas(0, 200)
valor_far, valor_cel = valores
imprimir_resultados(valor_cel, valor_far)