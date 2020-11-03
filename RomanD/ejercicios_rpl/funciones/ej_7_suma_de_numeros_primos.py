"""Completar el cuerpo de la función. La misma recibe como parámetro un número que será tomado como límite superior del
cálculo que debemos realizar.
La función debe retornar la suma de todos los números positivos primos existentes entre el 0 y el número ingresado
inclusive.
Recordar que el 1 no se considera primo y el 2 por definición sí lo es. Se puede asumir que el parámetro de entrada ha
sido verificado previamente y siempre es mayor que 0.

Ejemplos:

suma_de_numeros_primos(1) => 0
suma_de_numeros_primos(2) => 2
suma_de_numeros_primos(3) => 5
suma_de_numeros_primos(4) => 5
suma_de_numeros_primos(5) => 10
suma_de_numeros_primos(17) => 2 + 3 + 5 + 7 + 11 + 13 + 17 = 67

Hint: Pueden utilizar la función es_primo(numero) definida en la segunda actividad de la categoría, logrando un mayor
grado de modularización."""


def es_primo(numero):
    is_primo = True
    divisor = 2

    if numero > 1:

        while is_primo and divisor < numero:
            if numero % divisor != 0:
                divisor += 1
            else:
                is_primo = False

    else:
        is_primo = False

    return is_primo


def suma_de_numeros_primos(numero):

    primos_sumados = 0

    if numero > 1:

        for i in range(2, numero+1):
            if es_primo(i):
                primos_sumados = primos_sumados + i

    return primos_sumados
