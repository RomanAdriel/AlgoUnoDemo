numero = int(input("Ingrese un numero (0 para salir) "))
lista = []
while numero != 0:
    lista.append(numero)
    max_num = max(lista)
    min_num = min(lista)
    numero = int(input("Ingrese un numero (0 para salir) "))
else:
    print("Números ingresados " + str(len(lista))
          + "\nNumero máximo " + str(max_num) + "\nNumero mínimo "
          + str(min_num) + "\nPosición del máximo "
          + str(lista.index(max_num))
          + "\nPosición del mínimo "
          + str(lista.index(min_num)))
