# Ejercicio 1
# Leer un número real y decir si es mayor, menor o igual a cero.

numero = float(input("Ingresar cualquier numero: "))
if(numero > 0):
    print(numero, "es mayor a 0")
elif(numero < 0):
    print(numero, "es menor a 0")
else:
    print(numero, "es igual a 0")
