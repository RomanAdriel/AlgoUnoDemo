"""Leer A y B, enteros. Calcular C = A**B
 mediante multiplicaciones sucesivas e
imprimir el resultado. Tener en cuenta que son números enteros, por lo tanto
pueden tomar valores positivos, negativos o cero. """

A = int(input("ingresar el valor A: "))
B = int(input("ingresar el valor B: "))
C = 1
i = B

if B < 0:
    i = B * -1


if B == 0:
    C = 1
elif B < 0:
    A = 1/A
    for i in range(i, 0, -1):
        C = C * A
        print(C)
else:

    for i in range(i, 0, -1):
       C = C * A
       print(C)

print("el resultado es: ", C)
