# Ejercicio 4
# Dada una serie de números enteros, determinar el valor máximo, mínimo y las
# posiciones en que éstos se encontraban en la serie. El programa deberá ir
# preguntando si hay más números para ingresar.

n = int(input("ingrese un valor: "))
list = []
while n != 0:
    list.append(n)
    n_max = max(list)
    n_min = min(list)
    n = int(input("si lo desea ingrese otro valor: "))
else:
    print("Numeros ingresados " + str(len(list)) + "\nNumero maximo "
          + str(n_max) + "\nNumero minimo " + str(n_min)
          + "\nPosicion max: " + str(list.index(n_max))
          + "\nPosicion min: " + str(list.index(n_min)))