"""Escribir un algoritmo que indique si un número entero, ingresado por un usuario, es primo"""

m = int(2)
primo = "T"

numero = int(input("Ingrese un número para determinar si es primo: "))
while primo == "T" and m < numero:
    if(numero % m) == 0:
        primo = "F"
    else:
        m = m + 1
if primo == "T" and numero > 1:
    print("El número ingresado es primo")
else:
    print("El numero ingresado no es primo")
