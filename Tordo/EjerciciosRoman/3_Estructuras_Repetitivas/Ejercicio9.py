"""Dada una serie de números enteros terminada en cero, imprimir los tres mayores. """


numero = int(input("Ingrese valor (0 para terminar): "))
oro = 0
plata = 0
bronce = 0

while numero != 0:

    if numero > oro:
        bronce = plata
        plata = oro
        oro = numero

    elif oro >= numero > plata:
        bronce = plata
        plata = numero

    elif plata >= numero > bronce:
        bronce = numero

    numero = int(input("Ingrese valor (0 para terminar): "))

print(oro, plata, bronce)
