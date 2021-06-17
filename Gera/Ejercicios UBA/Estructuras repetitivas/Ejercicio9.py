"""Dada una serie de números enteros terminada en cero, imprimir los tres
mayores. """

num = int(input("ingrese numero: "))
oro = 0
plata = 0
bronce = 0

while num != 0:

    if num > oro:
        bronce = plata
        plata = oro
        oro = num
    elif oro >= num > plata:
        bronce = plata
        plata = num
    elif plata >= num > bronce:
        bronce = num

    num = int(input("ingrese numero: "))

print(oro, plata, bronce)
