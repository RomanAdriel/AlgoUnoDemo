"""Dada una serie de números enteros terminada en cero, imprimir los tres mayores. """

# lista = [1, 6, 4, 8, 7, 5, -1, 0]
# mayor = 0
#
# for i in lista:
#     if mayor == 0:
#
#         mayor = i
#
#     elif i > mayor:
#         mayor = i
#
# print("El numero mayor es: " + str(mayor))


numero = int(input("Ingrese valor (0 para terminar): "))
oro = numero
plata = numero
bronce = numero

while numero != 0:
    numero = int(input("Ingrese valor (0 para terminar): "))
    if numero > oro:
        oro = numero
    elif oro > numero > plata:
        bronce = plata
        plata = numero
    elif plata > numero > bronce:
        bronce = numero

print(oro, plata, bronce)
