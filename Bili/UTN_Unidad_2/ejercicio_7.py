# Ejercicio 7
# Intente realizar los ejercicios 1, 2 y 3 con tkinter.

from tkinter import *

#1
lista_de_frutas = ['banana', 'manazana', 'pera',
'coco', 'frutilla', 'cereza', 'uva']

Label(text=lista_de_frutas[2]).pack()
mainloop()

#2 Ya está hecho en tkinter

#3

claves = ['identificador', 'nombre', 'apellido','telefono']
valores = ['00', 'Juan', 'Perez', '0810 000 111']
d = dict(zip(claves,valores))

Label(text='El diccionario creado tiene '+ str(len(d)) + ' elementos y sus claves son ' + ', '.join(d.keys())).pack()
mainloop()