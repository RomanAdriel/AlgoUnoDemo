numero = int(input("Ingrese un valor (0 para salir) "))
lista = []
while numero != 0:
    lista.append(numero)
    numero = int(input("Ingrese un valor (0 para salir) "))
    mayor = max(lista)
    menor = min(lista)
    cantidad_mayor = lista.count(max(lista))
    cantidad_menor = lista.count(min(lista))
else:
    print("El mayor número de la lista es " +str(mayor) + "."
          + "\nEl menor número de la lista es " + str(menor) + "."
          + "\nEl mayor aparece " + str(cantidad_mayor) + " veces."
          + "\nEl menor aparece " + str(cantidad_menor) + " veces.")
