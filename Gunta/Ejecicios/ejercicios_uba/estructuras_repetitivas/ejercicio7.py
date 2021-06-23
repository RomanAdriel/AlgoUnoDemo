# ejercicio 7
# Leer A y B, enteros. Calcular C = AxB mediante multiplicaciones sucesivas e
# imprimir el resultado. Tener en cuenta que son números enteros, por lo tanto
# pueden tomar valores positivos, negativos o cero.



# def multi(a, b):
#     if b == 0:
#         return 1
#     elif a == 0:
#         return 0
#     elif b == 1:
#         return a
#     else:
#         return  a * multi(a, b - 1)
#
# print(multi(5, 5))




def multi2(a, b):
    resultado = 1
    for mul in range(b):
        resultado = resultado * a
    return resultado


def mensaje(a, b):
    print(multi2(a, b))

mensaje(0, -5)


# def multi3(a, b):
#     resultado = 1
#     while b != 0:
#         resultado = resultado * a
#         b = b -1
#     return resultado
#
# print(multi3(5, 5))

# def persona(nombre):
#     print("Hola, {}, como estas?.".format(nombre))
#
# a = input()
# persona(a)
