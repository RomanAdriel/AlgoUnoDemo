"""Ejercicio 9
Dada una serie de números enteros terminada en cero, imprimir los tres
mayores."""


num = int(input("Ingresar la cantidad de numeros a utilizar (minimo 4): " ))

max1 = 0
max2 = 0
max3 = 0

if num >= 4:

    for i in range(1, num + 1):

        num = int(input("Ingresar un numero: "))

        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif max1 >= num > max2:
                max3 = max2
                max2 = num
        elif max2 >= num > max3:
            max3 = num

    print(max1, max2, max3)

else:
    print("El numero ingresado es menor a 4: ")
