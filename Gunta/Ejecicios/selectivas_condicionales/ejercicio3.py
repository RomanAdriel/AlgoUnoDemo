# Ejercicio 3
# Dadas las horas de partida y de llegada de un móvil, expresadas en horas,
# minutos y segundos, calcular su velocidad promedio sabiendo que la distancia
# recorrida es D (D es un valor en km que se ingresa por teclado).


#Notas:
  #Referencias:
    #_1 = partida
    #_2 = salida

# hora_1 = float(input("Ingresar hora de partida: "))
# minuto_1 = float(input("Ingresar minutos de partida: "))
# segundo_1 = float(input("Ingresar segundos de partida: "))
# hora_2 = float(input("Ingresar hora de llegada: "))
# minuto_2 = float(input("Ingresar minutos de llegada: "))
# segundo_2 = float(input("Ingresar segundos de llegada: "))

hora_1 = 7
minuto_1 = 15
segundo_1 = 48
hora_2 = 14
minuto_2 = 23
segundo_2 = 55
distancia_total = float(input("Ingresar distancia total recorrida expresada en km: "))
tiempo_total = int((hora_2+(minuto_2/60)+(segundo_2/3600))-(hora_1+(minuto_1/60)+(segundo_1/3600)))
velocidad_promedio = distancia_total//tiempo_total
if (velocidad_promedio > 120 ):
    print("¡Tu velocidad promedio fue! ","\n", velocidad_promedio, "km/hora" "\n", "Fuiste rapido Chinwenwencha!!!")
else:
    print("¡Tu velocidad promedio fue!", "\n", velocidad_promedio, "km/hora" "\n", "Dele abuela!!!")
