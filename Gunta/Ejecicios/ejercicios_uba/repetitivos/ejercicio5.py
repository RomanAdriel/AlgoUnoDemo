# # Ejercicio 5
# # Leer un valor N y, luego, N números enteros. Se pide imprimir el mayor, el menor
# # y las veces que aparece cada uno.

numero = int(input("ingrese un valor distinto a 0: "))
list = []
while numero != 0:
    list.append(numero)
    numero = int(input("ingrese un valor distinto a 0: "))
    n_max = max(list)
    n_min = min(list)
    cant_mayor = list.count(max(list))
    cant_menor = list.count(min(list))
else:
    print("EL mayor es :" + str(n_max) + "\nEl menor es: " + str(n_min)
          + "\n La cantidad de veces que aparece el numero mayor es " + str(cant_mayor)
          + "\n La cantidad de veces que aparece el numero menor es " + str(cant_menor))