"""Desarrollar una función que devuelva en un vector (una lista) los números primos
entre 2 y 200. Reutilizar lo que ya se escribió y probó."""

def lista_numeros_primos(inicial, final):
    lista = []
    for n in range(inicial, final+1):
        count = 0
        for i in range(1, n+1):
            if n % i == 0:
                count += 1
        if count == 2:
            lista.append(str(n))
            lista_pulida = ", ".join(lista)
    return lista_pulida


def mensaje(a):
    print(a)


def main():
    mensaje(lista_numeros_primos(1, 200))

__init__: (main())