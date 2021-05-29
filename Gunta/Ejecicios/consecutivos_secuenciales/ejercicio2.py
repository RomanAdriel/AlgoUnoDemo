# Ejercicio 2
# Pedir al usuario que ingrese dos números por teclado e imprimir
# - La suma de ambos
# - La resta (el primero menos el segundo)
# - La multiplicación
# - La división entera (suponer que el segundo número no es cero).
# # - La división con decimales.
#
numero_1 = float(input("ingresar numero 1: "))
numero_2 = float(input("ingresar numero 2: "))
suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2
division_entera = numero_1 // numero_2
division_decimales = numero_1 / numero_2
print("La Suma es: ", suma, "\n"
      "La Resta es: ", resta, "\n"
      "La Multiplicacion es: ", multiplicacion, "\n"
      "La division entera es: ", division_entera, "\n"
      "La division con decimales es: ", division_decimales)



