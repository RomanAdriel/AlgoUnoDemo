"""Escribir un programa que tome el valor del nombre del usuario por consola y luego lo imprima en pantalla."""


def saludo():
    persona = str(input("ingrese su nombre: "))
    print("Buenos dias " + str(persona) + " avisame si quieres ponerte en nota, if you know what i mean ;)")


saludo()
