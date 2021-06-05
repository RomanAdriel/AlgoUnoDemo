# Ejercicio 3
# La librería random la cual puede ser agregada en nuestros scripts de la siguiente manera
# import random
# Permite obtener números aleatorios.
# Tarea 1:
# Realice un programa partiendo del Ejercicio 1 que multiplique el resultado por un número
# aleatorio y lo presente en pantalla.
# Tarea 2
# Presente un ejemplo y explique el funcionamiento de cómo se utiliza el siguiente metodo:
# random.randrange()

# Tarea 1

import random
from tkinter import *
root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
a = 5
b = random.randint(1, 20)
c = a * b
var = IntVar()
e.config(textvariable=var)
var.set(c)
mainloop()

# Tarea 2
import random
print(random.randrange(1, 25))

# randrange toma un numero aleatorio entre 1 y 24, el ultimo parametro no lo toma como valor, si el inicial