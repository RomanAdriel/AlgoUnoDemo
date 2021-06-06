m = int(2)
primo = "T"

numero = int(input("Ingrese un número para determinar si es primo: "))
while primo == "T" and m < numero:
    if(numero % m) == 0:
        primo = "F"
    else:
        m = m + 1
if primo == "T":
    print("El número ingresado es primo")
else:
    print("El numero ingresado no es primo")
