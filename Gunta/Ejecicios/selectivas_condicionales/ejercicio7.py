# Ejercicio 7
# Leer dos números y, luego, una opción (puede ser suma, resta, multiplicación o división), según la opción elegida realizar el cálculo.

n1 = float(input("Ingresar un valor: "))
n2 = float(input("Ingresar otro valor: "))
print("""¿Que operacion desea realizar?
1)Sumar              2)Restar
3)Multiplicar        4)Dividir """)
opcion = 0
while True:
    opcion = int(input("Opcion #: "))
    if opcion == 1:
        print("La suma es", n1+n2)
    elif opcion == 2:
        print("La resta es", n1-n2)
    elif opcion == 3:
        print("La multiplicacion es", n1*n2)
    elif opcion == 4:
        print("La division es", n1/n2)
    else:
        break
