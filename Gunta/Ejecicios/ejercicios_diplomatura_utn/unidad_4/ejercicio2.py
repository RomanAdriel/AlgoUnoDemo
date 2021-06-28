"""Escribir un programa que permita ingresar un número y calcule el factorial. """

num = int(input("ingrese un numero: "))
factorial = 1
i = 0
if num != 0:
    for i in range(1, num+1):
        factorial = factorial * i
else:
    factorial = 0
print(factorial)
