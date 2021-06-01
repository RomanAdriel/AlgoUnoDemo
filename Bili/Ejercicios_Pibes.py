"""
Guía de Ejercicios
"""



#Introducción .................................................................................................................................. 3
#Estructuras consecutivas o secuenciales....................................................................................... 5
#Estructuras selectivas o condicionales .......................................................................................... 6

# %% Ejercicio 3

distancia = int(input('entrar distancia: '))
h_salida = 10
h_llegada = 11
m_salida = 10
m_llegada = 20
s_salida = 40
s_llegada = 50
vel_promedio = distancia / (h_llegada - h_salida + m_llegada - m_salida + s_llegada)
print(vel_promedio)

# %% Ejercicio 4
# Escribir un algoritmo que determine si un número entero,
# que ingresa un usuario, es par.

numero = int(input('ingresar número: '))
if numero % 2 == 0:
    print(str(numero) + ' es par')
else:
    print(str(numero) + ' es inpar')

# %% Ejercicio 6
# Escribir un algoritmo que determine si un número N (entero),
# que ingresa un usuario, es divisible por M.

m = 10
numero = int(input('ingresar número: '))
if numero % m == 0:
    print(str(numero) + ' es divisible por M')
else:
    print(str(numero) + ' no es divisible por M')

# %% Ejercicio 7
# Leer dos números y, luego, una opción (puede ser suma, resta,
# multiplicación o división), según la opción elegida realizar
# el cálculo.

numero_1 = int(input('ingresar número: '))
numero_2 = int(input('ingresar número: '))
operador = input('elegir entre ["+", "-", "/", "*"]:')
if operador == '+':
    print(numero_1 + numero_2)
elif operador == '-':
    print(numero_1 - numero_2)
elif operador == '/':
    try:
        print(numero_1 / numero_2)
    except ZeroDivisionError:
        print('no se puede dividir por cero')
elif operador == '*':
    print(numero_1 * numero_2)

# %% Ejercicio 8
#Formar un menú con 4 opciones y al elegir una de ellas mostrar
#un cartel diciendo qué opción se eligió o si fue una opción
# incorrecta. (+) Opción 1 Opción 2 etc

def menu():
    print('[1] Opcion 1')
    print('[2] Opcion 2')
    print('[3] Opcion 3')
    print('[4] Opcion 4')
menu()

opcion = int(input('elegir la opción: '))

if opcion == 1:
    print('se eligió opcion 1')
elif opcion == 2:
    print('se eligió opcion 2')
elif opcion == 3:
    print('se eligió opcion 3')
elif opcion == 4:
    print('se eligió opcion 4')
else:
    print('opcion incorrecta')

#Estructuras repetitivas .................................................................................................................. 8

# %% Ejercicio 1
# Imprimir por pantalla una lista de 20 números consecutivos,
# los cuales comienzan con un número ingresado por teclado.

numero = int(input('ingresá un número:'))
for i in range(numero,numero + 21):
    print (i)

# %% Ejercicio 2
#Leer un número N y calcular su factorial.

numero = int(input('ingresá un número:'))
factorial = numero
for i in range(1,numero):
    factorial *= i
print('el factorial de '+ str(numero) + ' es ' + str(factorial))

#Funciones .................................................................................................................................... 10
#Tuplas, listas y strings .................................................................................................................. 14
#Registros y Tablas (Listas y Diccionarios) .................................................................................... 16
#Ejercicios tipo parcial .................................................................................................................. 19
#Recursividad ................................................................................................................................ 20
#Archivos ....................................................................................................................................... 21
#Anexo .......................................................................................................................................... 23





# %%
