"""Escribir un programa que permita tomar un número por consola e imprima los números entre cero
y el número de menor a mayor separados por coma y luego de mayor a menor separado por coma.
Ejemplo de salida para 5
0, 1, 2, 3, 4, 5
5, 4, 3, 2, 1, 0
"""



def ingresar_numero():
    numero = int(input("Ingrese un numero "))
    return numero

# def crear_lista_asc(numero):
#     list_asc = []
#     for a in range(0, numero + 1, 1):
#         if numero != 0:
#             list_asc.append(str(a))
#             list_a = ", ".join((list_asc))
#     return list_a
#
# def crear_lista_des(numero):
#     list_des = []
#     for b in range(numero, - 1, - 1):
#         list_des.append(str(b))
#         list_d = ", ".join(list_des)
#     return list_d

def crear_lista_asc(numero):
    list_asc = []
    for a in range(0, numero + 1, 1):
        list_asc.append(str(a))
    return list_asc

def crear_lista_des(numero):
    list_des = []
    for b in range(numero, - 1, - 1):
        list_des.append(str(b))
    return list_des

def convertir_lista_str_a(list_asc):
    list_a = ", ".join(list_asc)
    return list_a

def convertir_lista_str_d(list_des):
    list_d = ", ".join(list_des)
    return list_d

def mensaje_salida(ascendente, descendente, espacio):
    print(ascendente, descendente, espacio)


def main():
    main_num = ingresar_numero()
    mensaje_salida(convertir_lista_str_a(crear_lista_asc(main_num)),"<>",
                   convertir_lista_str_d(crear_lista_des(main_num)))



# def main():
#     main_num = ingresar_numero()
#     mensaje_salida(convertir_lista_str_a(main_num),"<>",
#                    convertir_lista_str_d(main_num))


__init__: (main())