"""Escribir un programa que permita tomar un número por consola e imprima los números entre cero
y el número de menor a mayor separados por coma y luego de mayor a menor separado por coma.
Ejemplo de salida para 5
0, 1, 2, 3, 4, 5
5, 4, 3, 2, 1, 0
"""


def ingreso_numero():
    num = int(input("Ingrese valor: "))
    return num


def create_list_asc(numero):
    list_asc = []
    for a in range(0, numero + 1, 1):
        list_asc.append(str(a))
    list_asc_string = ", ".join(list_asc)
    return list_asc_string


def create_list_des(numero):
    list_des = []
    for d in range(numero, - 1, -1):
        list_des.append(str(d))
    list_des_string = ", ".join(list_des)
    return list_des_string


def imprimir_listas(mensaje1, valor1, mensaje2, valor2):
    print(mensaje1, valor1, mensaje2, valor2)


def main():

    var_global = ingreso_numero()

    imprimir_listas("Lista ascendente:", create_list_asc(var_global),
                    "\nLista descendente:", create_list_des(var_global))


__init__ = main()