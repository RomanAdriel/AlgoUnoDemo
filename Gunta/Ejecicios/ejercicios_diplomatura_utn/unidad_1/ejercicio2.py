# Ejercicio 2
# Para pasar de un entero a un string se utiliza el método str(). Realice un programa con
# Tkinter que tome dos valores uno entero y el otro un string, concatene ambos como un
# string y presente el resultado en pantalla


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