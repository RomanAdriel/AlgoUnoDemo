"""Leer A y B, enteros. Calcular C = A x B mediante sumas sucesivas e imprimir el resultado."""

valor_a = int(input("Ingrese el valor de A:  "))
valor_b = int(input("Ingrese el valor de B:  "))
c = int

while valor_b != 0:

    c = c + valor_a
    valor_b = valor_b - 1

print("El valor de C es: " + str(c))
