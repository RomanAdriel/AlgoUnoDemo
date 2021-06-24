"""Contar la cantidad de letras de un telegrama que termina en punto sin utilizar
funciones de string, salvo la que indica la longitud"""


def contar_telegrama(telegrama):
    letras = "abcdefghijklmnñopqrstuvwxyz"
    contador_letras = 0
    i = 0
    #corte = 0
    while i < len(telegrama): #and corte != 1:
        if telegrama[i] in letras:
            i += 1
            contador_letras += 1
        elif telegrama[i] == ".":
            #corte += 1
            i = len(telegrama)
        else:
            i += 1
    return contador_letras


def contar_telegrama(telegrama):
    letras = "abcdefghijklmnñopqrstuvwxyz"
    contador_letras = 0
    corte = "."
    for i in telegrama:
        if i in letras:
            contador_letras += 1
    return contador_letras


def imprimir_resultado(cantidades):
    print(cantidades)


telegrama = contar_telegrama("12as-r-eEEEéé22,,,,,,,,,,#$%&/() aaa".lower())
cant_letras = telegrama
imprimir_resultado(cant_letras)
