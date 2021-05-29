# El ejemplo que hicimos del usuario que ingresa una edad e indica si es mayor o no"
#
# edad = int(input("Ingrese su edad"))
# if (edad >= 18):
#     print("Miren el siguiente numero, ya es legal papa", edad)
# else:
#     print(edad, "Posibilidad de ir en cana")
#
# Se pide ingresar dos notas que corresponden a un primer parcial y
# segundo parcial del CBC. Luego decidir si el estudiante promociona (si suma 13),
# va a final (si suma 8 pero menos de 13) o recursa
#
# parcial_1 = int(input("Ingresar nota del primerl parcial: "))
# parcial_2 = int(input("Ingresar nota del segundo parcial: "))
# parcial_suma = parcial_1 + parcial_2
#
# if (parcial_suma >= 13):
#     print("PROMOCIONASTE CAMPEON!")
# elif (parcial_suma >= 8):
#     print ("Vas a final muñeco")
# else:
#     print("kbio por drogon ameo")
#
#
# ¿Cómo arreglarían el programa anterior para que promocione si suma 13
# o más pero que no tenga un aplazo en uno de los dos parciales? Es decir, no se
# puede tener un 10 y un 3. Tratá de pensarlo y hacerlo. Luego, mirá la solución
# propuesta.

# parcial_1 = int(input("Ingresar nota del primerl parcial: "))
# parcial_2 = int(input("Ingresar nota del segundo parcial: "))
# parcial_suma = parcial_1 + parcial_2
#
# if (parcial_suma >= 13) and (parcial_1 != 3) and (parcial_2 != 3):
#     print("PROMOCIONASTE CAMPEON!")
# elif (parcial_suma >= 8):
#     print ("Vas a final muñeco")
# else:
#     print("kbio por drogon ameo")

# # Estructuras repetitivas
#
# for i in range(1,11,9):
#     print(i)

# Por ejemplo, para listar los números del 1 al 10 con un while sería:
i = 1
while (i <= 10):
    print(i)
    i += 1