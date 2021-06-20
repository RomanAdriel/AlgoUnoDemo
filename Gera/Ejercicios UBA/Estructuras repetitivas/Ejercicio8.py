"""Escribir un algoritmo que indique si un número entero, ingresado por un usuario,
es primo.
"""
"""Para calcular si un número es primo o no lo que tenemos que hacer es dividirlo
 de forma ordenada por todos los números primos menores que él.
 Si no obtenemos divisiones exactas y conseguimos llegar a tener un cociente menor o igual al divisor,
  entonces estamos ante un número primo."""

num = int(input("ingresar un número: "))
es_primo = 'No es un número primo'


if num > 1:
    i = 0
    while i == 0 and num % 2 != 0:
        for j in range(2, num-1):
            verificar = num % j
            if verificar != 0 or num == 2:
                es_primo = 'Es numero primo'
                i += 1
            elif j == num-1 and verificar == 0:

else:
    es_primo = 'No es numero primo'

print(num, es_primo)