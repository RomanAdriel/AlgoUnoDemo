# ejercicio 7
# Leer A y B, enteros. Calcular C = AxB mediante multiplicaciones sucesivas e
# imprimir el resultado. Tener en cuenta que son números enteros, por lo tanto
# pueden tomar valores positivos, negativos o cero.


a = 2
b = 3
def multi(a, b):
    if b == 0:
        return 0
    elif b == 1:
        return a
    elif b < 1:
        return multi(a, -b)
    else:
        return a + (multi(a, b + 1))



