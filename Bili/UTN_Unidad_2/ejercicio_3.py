#  Ejercicio 3
#  Cree un diccionario con las claves:
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