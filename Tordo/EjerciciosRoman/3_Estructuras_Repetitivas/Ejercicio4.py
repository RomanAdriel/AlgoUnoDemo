numero = int(input("Ingrese un numero (0 para salir) "))
lista = []
while numero != 0:
    lista.append(numero)
    numero = int(input("Ingrese un numero (0 para salir) "))
else:
    print("Números ingresados " + str(len(lista))
          + "\nNumero máximo " + str(max(lista))
          + "\nNumero mínimo " + str(min(lista))
          + "\nPosición del máximo " + str(lista.index(max(lista)))
          + "\nPosición del mínimo " + str(lista.index(min(lista))))
