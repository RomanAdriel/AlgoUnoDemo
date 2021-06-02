print("Ingrese dos números para empezar a operar")
A = int(input("Primer Número: "))
B = int(input("Segundo: "))
print("Que desea hacer a continuación: a)sumar, b)restar, c)multiplicar")
C = input()
if C == "a":
    print(A+B)
elif C == "b":
    print(A-B)
elif C == "c":
    print(A*B)
else: print("opcion inválida")
