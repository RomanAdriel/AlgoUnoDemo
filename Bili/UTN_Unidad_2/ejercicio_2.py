# Ejercicio 2
# Para concatenar texto se utiliza el signo +
# Cree una lista de frutas de 2 elementos, y
# realice un programa con tkinter que muestre dos elementos de la lista
# concatenándolos con texto para una oración conteniendo los formar una
# oración con sentido.

from tkinter import *

lista = ['banana', 'manzana']

Label(text='Me comí una '+ lista[0] + ' y una ' + lista[1]).pack()
mainloop()