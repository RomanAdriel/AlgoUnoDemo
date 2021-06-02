hora_partida = 15
minuto_partida = 10
segundo_partida = 5
hora_llegada = 16
minuto_llegada = 0
segundo_llegada = 2
D = int(input("Ingrese distancia recorrida: "))
print(D , "KMs")
horariopartida = (hora_partida+minuto_partida/60+segundo_partida/3600)
horariollegada = (hora_llegada+minuto_llegada/60+segundo_llegada/3600)
print("Velocidad promedio: " , (str(int(D/(horariollegada - horariopartida))) + " km/h)"))