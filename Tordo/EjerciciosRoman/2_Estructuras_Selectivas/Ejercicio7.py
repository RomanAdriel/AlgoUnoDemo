numero1 = int(input("Ingrese un número "))
numero2 = int(input("Ingrese otro número "))
opciones = ["Sumar",
            "Restar",
            "Multiplicar",
            "Dividir"]
print("Seleccione la operación matemática a realizar"
      + " " + str(opciones[0]) + ", " + str(opciones[1])
      + ", " + str(opciones[2]) + "ó " + str(opciones[3]))
seleccion = input()
if seleccion == opciones[0]:
    print(str(numero1+numero2))
elif seleccion == opciones[1]:
    print(str(numero1-numero2))
elif seleccion == opciones[2]:
    print(str(numero1*numero2))
else:
    print(str(numero1/numero2))
