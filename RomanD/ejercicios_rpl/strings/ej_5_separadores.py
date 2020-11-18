"""Completar el cuerpo de la función. La misma debe tomar la cadena que se pasa como parámetro e insertar el separador
cada tantos caracteres como indique el parámetro "espaciado".

Ejemplos:

   insertar_separadores("255255255255", ".", 3) => "255.255.255.255"
   insertar_separadores("holacomoestas", "|", 4) => "hola|como|esta|s"  """


def insertar_separadores(cadena, separador, espaciado):

    lista_de_textos = []

    for i in range(0, len(cadena), espaciado):
        lista_de_textos.append(cadena[i:i+espaciado])

    texto_final = separador.join(lista_de_textos)

    return  texto_final
