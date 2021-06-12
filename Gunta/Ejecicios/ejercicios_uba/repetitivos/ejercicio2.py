# # Ejercicio 2
# # Leer un número N y calcular su factorial.


def fact(n):
  while n==0:
     return 1
  else:
     return n * fact(n-1)
n = int(input("ingrese un valor: "))
print("El factorial de " + str(n) + " es " + str(fact(n)))