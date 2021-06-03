# Ejercicio 8
# Formar un menú con 4 opciones y al elegir una de ellas mostrar un cartel diciendo
# qué opción se eligió o si fue una opción incorrecta. (+)
#  Opción 1
#  Opción 2

print("""¡Bienvenido al supermercado aqui no se ahorra!
Por favor elegir el pasillo deseado y digitar su numero a continuacion: 
1)Panaderia         2)Carniceria        3)Verduleria
4)Pescaderia        5)Limpieza          0)Cerrar aplicacion""")

opcion = int(input("Pasillo #: "))
if opcion == 1:
        print("Elegiste la opcion Panaderia")
elif opcion == 2:
        print("Elegiste la opcion Carniceria")
elif opcion == 3:
        print("Elegiste la opcion Verduleria")
elif opcion == 4:
        print("Elegiste la opcion Pescaderia")
elif opcion == 5:
        print("Elegiste la opcion Limpieza")
elif opcion == 0:
        print("Gracias vuelva prontos")
else:
        print("Opcion incorrecta, por favor vuelva a seleccionar un pasillo utilizando su numero como referencia")
        opcion = int(input("Pasillo #: "))