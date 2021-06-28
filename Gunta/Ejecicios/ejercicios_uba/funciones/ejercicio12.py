"""Contar la cantidad de palabras, separadas por uno o más espacios, de un
telegrama que termina en punto. No utilizar funciones de string salvo la que
indica la longitud."""


##############_**_Forma facil_**_#################

# def formatear_telegrama(telegrama):
#     remover_caracteres = "!""#$%&/()=?¡¿'´+*¨¨]\n[{}_-:.;,\,,/"
#     for i in remover_caracteres:
#         telegrama = telegrama.replace(i, "")
#     telegrama = telegrama.lower()
#     telegrama = telegrama.split(" ")
#     telegrama_formateado = telegrama
#     return telegrama_formateado
#
#
# def imprimir_resultado(cantidades):
#     print(len(cantidades))
#
#
# telegrama = formatear_telegrama("El Estadio Antonio Vespucio Liberti, también conocido como Estadio Monumental o Monumental de Núñez, es un estadio ubicado en la intersección de las avenidas "
#                                 "Figueroa Alcorta y Udaondo del barrio porteño de Belgrano, Buenos Aires, Argentina. Es propiedad del Club Atlético River Plate y "
#                                 "fue inaugurado el 26 de mayo de 1938 por el presidente de ese entonces, Antonio Vespucio Liberti, quien, además, decidió su construcción; de allí su nombre.")
# imprimir_resultado(telegrama)

##############_**_Forma dificil_**_#################



def contar_palabras(telegrama):
    diccionario = "abcdefghijklmnñopqrstuvwxyzáéíóú"
    contador_palabras = 0
    for i in range(0, len(telegrama)):
        v = i - 1
        if telegrama[i] in diccionario:
            continue
        elif telegrama[v] in diccionario:
            contador_palabras += 1
    return contador_palabras


def imprimir_resultado(cantidades):
    print(cantidades)


telegrama = contar_palabras("El Estadio Antonio Vespucio Liberti, también conocido como Estadio Monumental o Monumental de Núñez, es un estadio ubicado en la intersección de las avenidas "
                                "Figueroa Alcorta y Udaondo del barrio porteño de Belgrano, Buenos Aires, Argentina. Es propiedad del Club Atlético River Plate y "
                                "fue inaugurado el 26 de mayo de 1938 por el presidente de ese entonces, Antonio Vespucio Liberti, quien, además, decidió su construcción; de allí su nombre.")
imprimir_resultado(telegrama)


