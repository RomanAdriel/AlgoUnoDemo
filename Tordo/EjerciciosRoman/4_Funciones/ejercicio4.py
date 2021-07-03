"""Hacer una función que indique si un número grande es primo o no. Utilizar lo
realizado en el ejercicio 8 de la práctica anterior."""


# def numero_primo(numero):
#     for n in range(2, numero):
#         if numero % n == 0:
#             return False
#         else:
#             print("Es primo")

def es_primo(numero):
    divisor = 2
    primo = "Si"
    while divisor < numero and primo == "Si":
        if (numero % divisor) == 0:
            primo = "No"
        else:
            divisor += 1
    if primo != "Si" or numero < 2:
        print("No es primo.")
    else:
        print("Es primo.")


variable_numero = int(input("Ingrese un número para verificar si es primo: "))

es_primo(variable_numero)
