"""Desarrollar una función que devuelva en un vector (una lista) los números primos
entre 2 y 200. Reutilizar lo que ya se escribió y probó."""

# def lista_numeros_primos(inicial, final):
#     lista = []
#     for n in range(inicial, final+1):
#         count = 0
#         for i in range(1, n+1):
#             if n % i == 0:
#                 count += 1
#         if count == 2:
#             lista.append(str(n))
#             lista_pulida = ", ".join(lista)
#     return lista_pulida
#
#
# def mensaje(a):
#     print(a)
#
#
# def main():
#     mensaje(lista_numeros_primos(1, 200))
#
# __init__: (main())
# Variables del ejercicio (no las modifiques)

# cadena_corrupta = "airotsiH,6.7,aícraG nómaR"
#
# # Completa el ejercicio
# cadena_volteada = cadena_corrupta[::-1]
# nombre = cadena_volteada[:12]
# nota = cadena_volteada[13:16]
# materia = cadena_volteada[17:]
# cadena_formateada = nombre + " ha sacado un " + nota + " en " + materia + "."
#
# print(cadena_formateada)

# lista1 = [1, 12, 123]
# lista2 = ["Bye", "Ciao", "Agur", "Adieu"]
#
# # completa el ejercicio
# lista1 += [1234, "hola"]
# lista2 += ["Adiós", 1234]
# lista3 = lista1[:-1]
# lista4 = lista2[1:-1]
# lista5 = lista4 + lista3
#
# print(lista1)
# print(lista2)
# print(lista3)
# print(lista4)
# print(lista5)
#
# nombre = input("ingrese nombre: ")
# apellido = input("ingrese apellidop: ")
# numero = int(input("ingrese un numero entero: "))
# numero_magico = float(input("ingrese un numero flotantr: "))
# cadena_final = nombre + " " + apellido + " Tu numero de la suerte es el " + str(numero * numero_magico) + "."
# print(cadena_final)
#
# matriz = [
#             [1, 1, 1, 3],
#             [2, 2, 2, 7],
#             [3, 3, 3, 9],
#             [4, 4, 4, 13]
#          ]
# matriz[1][-1] = sum(matriz[1][:-1])
# matriz[-1][-1] = 12
#
# print(matriz)
# """10,Juan Perez"""
# cadena = "zereP nauJ,01"
# cadena_volteada = cadena[::-1]
#
# print(cadena_volteada[3:] +" ha sacado un " +cadena_volteada[:2])

# numero = -1
#
# while numero % 5 != 0:
#     numero = int(input())

# matriz
#
# for i, fila in enumerate(matriz):
#     for j, columna in enumerate(fila):
#         if matriz[i][j] % 2 == 0:
#             matriz[i][j] = 0
#         else:
#             matriz[i][j] = 1

multiplos = []

# Completa el ejercicio
# numero = int(input())
# while numero < 0 or numero > 9:
#     numero = int(input())
#
# multiplos = list(range(0, 101, numero))
# print(multiplos)
#
# n = int(input("Ingresar un numero: "))
# while n % 2 == 0:
#     n = int(input("ingrese un numero: "))
# else:
#     print("Al fin pusiste un numero impar: ","<",n,">")
#
# suma = 0
# for numero in range(1, 100):
#     if numero % 2 == 0:
#         suma += numero
# print(suma)



