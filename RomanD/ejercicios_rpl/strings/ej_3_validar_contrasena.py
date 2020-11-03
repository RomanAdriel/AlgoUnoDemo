"""Completar el cuerpo de la función. La misma debe retornar valor un valor booleano: True en caso de que la
contraseña sea válida, False en caso contrario.
Se considera válida una contraseña si:

    Tiene al menos un número.
    Tiene al menos una mayúscula.
    Tiene al menos un caracter no alfanumérico
    (Hint: Se puede evaluar utilizando la conjunción de la negación entre .isalpha() y
    la negación de .isnumeric())
    Tiene una longitud mayor a 7 caracteres pero menor a 15.

Ejemplo:

   validar_contraseña("!Algoritmos123") => True
   validar_contraseña("!Algoritmos123!Algoritmos123") => False
   validar_contraseña("algoritmos") => False
   validar_contraseña("algoritmos123") => False
   validar_contraseña("Algoritmos123") => False
   validar_contraseña("!Alg123") => False"""


def validar_contrasenia(contrasenia):
    contrasena_valida = True

    if contrasenia.isalnum():

        contrasena_valida = False

    elif not len(contrasenia) in range(7, 16):

        contrasena_valida = False

    tiene_mayuscula = False
    caracter = 0

    while contrasena_valida and not tiene_mayuscula and caracter <= len(contrasenia):

        if contrasenia[caracter].isupper():

            tiene_mayuscula = True

        elif caracter == len(contrasenia) - 1:

            contrasena_valida = False

        else:
            caracter += 1

    tiene_numeros = False
    caracter = 0

    while contrasena_valida and not tiene_numeros and caracter < len(contrasenia):

        if contrasenia[caracter].isdigit():

            tiene_numeros = True

        elif caracter == len(contrasenia) - 1:

            contrasena_valida = False

        else:
            caracter += 1

    return contrasena_valida
