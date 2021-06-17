"""Leer A y B, enteros. Calcular C = A**B mediante multiplicaciones sucesivas e imprimir el resultado. Tener en cuenta que
 son números enteros, por lo tanto pueden tomar valores positivos, negativos o cero. """

valor_a = int(input("Ingrese el valor de A:  "))
valor_b = int(input("Ingrese el valor de B:  "))
c = 1


if valor_b < 0:
    valor_a = 1 / valor_a
    for i in range(0, valor_b, -1):
        c = c * valor_a
elif valor_b == 0:
    c = 1
elif valor_a == 0 and valor_b < 0:
    print("Error salame")
else:
    for i in range(0, valor_b):
        c = c * valor_a

print("El valor de C es: " + str(c))
# A**B
# 22 = 22
# 2**(-2)= (1/2)(1/2)
# 20= 2(1-1)= 21 * 2(-1) = 2/2 = 1
# 0(-2) = (1/0)2 = Error