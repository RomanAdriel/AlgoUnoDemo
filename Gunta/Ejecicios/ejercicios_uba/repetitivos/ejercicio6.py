# ejerciocio 6
# Leer A y B, enteros. Calcular el producto mediante sumas sucesivas e imprimir el
# resultado.

a = int(input("ingresar valor de a "))
b = int(input("ingresar valor de b "))
c = 0
while b != 0:
    c = c + a
    b = b - 1
print("el product es: " + str(c))
