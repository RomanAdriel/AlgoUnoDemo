# Ejercicio 1
# Realice un programa con Tkinter que tome dos valores, uno entero y el otro un string,
# realice la suma como enteros y lo presente en pantalla

from tkinter import *
root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
a = 5
b = '2'
c = str(a) + b
var = IntVar()
e.config(textvariable=var)
var.set(c)
mainloop()