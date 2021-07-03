"""Hacer un programa que liste todos los números primos desde 2 hasta un número ingresado por el usuario utilizando
 la función realizada en el ejercicio anterior. """

# Realizar una funcion para el ingreso del número en la cual se pueda validar que cumpla con

ingreso = int(input("Ingrese un número: "))


def primo(num):
    lista_primos = []
    for n in range(2, num):
        divisor = 2
        es_primo = True
        while es_primo and divisor < n:
            if n % divisor == 0:
                es_primo = False
            else:
                divisor += 1
        if es_primo:
            lista_primos.append(n)
    return lista_primos


primos = primo(ingreso)

print(primos)
