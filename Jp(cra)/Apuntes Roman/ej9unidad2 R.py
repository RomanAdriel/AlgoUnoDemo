###9. Pasar un período expresado en segundos a un período expresado en días, horas,
### minutos y segundos. (1 dia = 86.400 segs)###

A = int(input("Ingrese un período expresado en segundos y lo convertiremos a dias, horas, minutos y segundos: "))
min = A/60
hor = A/3600
dia = (A/3600)/24

if A >= 172800:
    print(int(dia) , "días, " , int(round(hor % 24)) , "horas, " , int(round(min%60)) , "minutos, " , (A%60) , "segundos.")
elif A > 86400:
    print(int(dia) , "dia, " , int(round(hor % 24)) , "horas, " , int(round(min%60)) , "minutos, " , (A%60) , "segundos.")
else:print(int(dia) , "días, " , int(round(hor % 24)) , "horas, " , int(round(min%60)) , "minutos, " , (A%60) , "segundos.")
