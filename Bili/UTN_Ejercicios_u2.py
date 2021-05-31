#################################
# TRABAJOS A PRESENTAR EN EL FORO
#################################

# %% Ejercicio 1

#  Cree una lista de frutas de 7 elementos,
#  y realice un programa que muestre el
#  tercer elemento de la lista en pantalla

lista_de_frutas = ['banana', 'manazana', 'pera','coco', 'frutilla',
'cereza', 'uva']

print(lista_de_frutas[2])

# %% Ejercicio 2
# Para concatenar texto se utiliza el signo +
# Cree una lista de frutas de 2 elementos, y
# realice un programa con tkinter que muestre dos elementos de la lista
# concatenándolos con texto para una oración conteniendo los formar una
# oración con sentido.

from tkinter import *

lista = ['banana', 'manzana']

Label(text='Me comí una '+ lista[0] + ' y una ' + lista[1]).pack()
mainloop()

# %% Ejercicio 3
# Cree un diccionario con las claves:
#· identificador
#· nombre
#· apellido
#· telefono

#Nota: al utilizar claves no utilice acentos u
# otros caracteres en español, por ejemplo no
# ponga “teléfono” sino “telefono”.

#Realice un programa que a partir del
# diccionario creado retorne en una oración:
#1) El número de elementos del diccionario
#2) Las claves del diccionario

#Pregunta: ¿Cree que para guardar y recuperar
# información es mejor un diccionario o una
# lista? Justifique su respuesta.

claves = ['identificador', 'nombre', 'apellido',
'telefono']
valores = ['00', 'Juan', 'Perez', '0810 000 111']
d = dict(zip(claves,valores))


print('El diccionario creado tiene ' + str(len(d))
+ ' elementos y sus claves son ' + ', '.join(d.keys()))

print('\n')

print("""¿Cree que para guardar y recuperar información es mejor un diccionario
 o una lista?""")

print('\n')

print(""" Respuesta: no hay uno mejor que el otro. La lista trabaja con
elementos ordenados mientras que a los elementos del diccionario se accede
por las llaves. """)
# %% Ejercicio 4
nombre = input('ingrese nombre: ')
print('hola ' + nombre + ' bienvenido!')

# %% Ejercicio 5
primer_valor = input('ingrese 1er valor: ')
segundo_valor = input('ingrese 1er valor: ')
lista = [primer_valor, segundo_valor, int(primer_valor) + int(segundo_valor)]
print(lista)
# %% Ejercicio 6
primer_valor = input('ingrese 1er valor: ')
segundo_valor = input('ingrese 1er valor: ')
d = {1: primer_valor,
     2: segundo_valor,
     3: int(primer_valor) + int(segundo_valor)}
print(d)

# %% Ejercicio 7
# Intente realizar los ejercicios 1, 2 y 3 con tkinter.

from tkinter import *

#1
lista_de_frutas = ['banana', 'manazana', 'pera',
'coco', 'frutilla', 'cereza', 'uva']

Label(text=lista_de_frutas[2]).pack()
mainloop()

#2
# Ya está hecho en tkinter
#3

claves = ['identificador', 'nombre', 'apellido','telefono']
valores = ['00', 'Juan', 'Perez', '0810 000 111']
d = dict(zip(claves,valores))

Label(text='El diccionario creado tiene '+ str(len(d)) + ' elementos y sus claves son ' + ', '.join(d.keys())).pack()
mainloop()

# %%
