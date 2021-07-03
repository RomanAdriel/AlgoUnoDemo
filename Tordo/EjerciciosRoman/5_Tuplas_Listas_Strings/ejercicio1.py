""" Desarrollar una función que devuelva en un vector (una lista) los números primos
entre 2 y 200. Reutilizar lo que ya se escribió y probó. """
lista = []


def calculo_primo():
    lista_primos = []

    for numero in range(2, 201):
        es_primo = True
        contador = 2

        # Alternativa 1
        while es_primo and contador < numero:

            if numero % contador == 0:
                es_primo = False
            contador += 1

        if es_primo:
            lista_primos.append(numero)

        # Alternativa 2 -
        for num in range(2, numero):
            resto = numero % num

            if resto == 0:
                es_primo = False

        if es_primo:
            lista_primos.append(numero)

    return lista_primos


lista = calculo_primo()

print(lista)
