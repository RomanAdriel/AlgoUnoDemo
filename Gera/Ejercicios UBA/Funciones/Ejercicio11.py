""". Contar la cantidad de letras de un telegrama que termina en punto sin utilizar
funciones de string, salvo la que indica la longitud"""


def ingresar_texto_telegrama():
    telegrama = input("ingrese el texto del telegrama: ")
    telegrama = telegrama.lower()
    return telegrama


# def convertir_telegrama_en_lista(telegrama):
#     lista_telegrama = list(telegrama)
#     return lista_telegrama


def contar_letras_en_telegrama(telegrama):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyzáéíóú'
    letras_contadas = 0
    for letra in telegrama:
        if letra in alfabeto:
            letras_contadas += 1
    return letras_contadas


def imprimir_resultado(letras_contadas):
    if letras_contadas:
        print("El telegrama contiene", letras_contadas, "letras")
    else:
        print("Hacen falta letras, amigo")


def main():

    ingreso = ingresar_texto_telegrama()
    cantidad_letras = contar_letras_en_telegrama(ingreso)
    imprimir_resultado(cantidad_letras)


__init__: main()
