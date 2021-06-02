# Ejercicio 6
# Escribir un algoritmo que determine si un número N (entero), que ingresa un usuario, es divisible por M.

n = int(input("Ingresar un numero entero: "))
m = 5
if (n%m) == 0:
    print("Es divisible por", m)
else:
    print("No es divisible por", m)