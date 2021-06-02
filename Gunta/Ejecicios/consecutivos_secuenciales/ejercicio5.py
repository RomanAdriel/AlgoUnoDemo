# # Ejercicio 5
# # Leer la base y la altura de un rectángulo, calcular el perímetro y la superficie.
#
#
# base = float(input("Ingresar base del triangulo expresada en cm: "))
# altura = float(input("Ingresar altura del triangulo expresada en cm: "))
# area = (base * altura / 3)
# print(float(area), "cm2")
#



l_1 = float(input("Ingresar la base de un rectangulo expresada en cm: "))
l_2 = float(input("Ingresar la altura de un rectangulo expresada en cm: "))
perimetro = (l_1*2)+(l_2*2)
superficie = l_1*l_2
print("El perimetro es: ", perimetro,"\n"
      "La superficie es: ", superficie)