"""Contar la cantidad de letras de un telegrama que termina en punto sin utilizar
funciones de string, salvo la que indica la longitud """


def escribir_telegrama():
    texto = input("Escriba el telegrama: \n")
    return texto


def contador_caracteres(texto):
    letras = "abcdefghijklmnñopqrstuvwxyzáéíóúäëïöüàèìòù"
    contador = 0
    for i in texto:
        if i in letras:
            contador += 1
    return contador


telegrama = escribir_telegrama()
caracteres_contados = contador_caracteres(telegrama)

print(caracteres_contados)
