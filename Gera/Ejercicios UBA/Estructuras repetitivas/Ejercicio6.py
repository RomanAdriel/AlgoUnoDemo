"""Leer A y B, enteros. Calcular C = A x B mediante sumas sucesivas e imprimir el
resultado. """

A = int(input("ingresar el valor A: "))
B = int(input("ingresar el valor B: "))
C = 0
i = B

if B < 0:
    i = B * -1

for i in range(i, 0, -1):
    C = C + A
    print(C)

print("el resultado es: ", C)
