n = int(input("Ingrese un número para calcular su factorial: "))


def factorial(n):
    factorial_total = 1
    while n > 1:
        factorial_total *= n
        n -= 1
    return factorial_total


print(factorial(n))
print("El factorial de " + str(n) + " es: " + str(factorial(n)))
