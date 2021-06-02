numero = int(input("Ingrese un número "))

if numero < 0:
    print("El número " + str(numero) + " es menor a 0")
elif numero == 0:
    print(str(numero) + " es 0")
else:
    print(str(numero) + " es mayor a 0")
