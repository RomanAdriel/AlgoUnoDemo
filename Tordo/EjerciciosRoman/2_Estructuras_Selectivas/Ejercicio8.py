opciones = ["1",
            "2",
            "3",
            "4"]
print("Seleccione una opción " + str(opciones[0]) + ", " + str(opciones[1])
      + ", " + str(opciones[2]) + ", " + str(opciones[3]))
seleccion = input()
if seleccion == opciones[0]:
    print("Seleccionó opción 1")
elif seleccion == opciones[1]:
    print("Seleccionó opción 2")
elif seleccion == opciones[2]:
    print("Seleccionó opción 3")
elif seleccion == opciones[3]:
    print("Seleccionó opción 4")
else:
    print("Opción inválida")
