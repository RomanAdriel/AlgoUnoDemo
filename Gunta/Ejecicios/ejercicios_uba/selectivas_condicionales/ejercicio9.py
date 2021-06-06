# Ejercicio 9
# Pasar un período expresado en segundos a un período expresado en días, horas,
# minutos y segundos.


segundos = int(input("ingrese hora expresada en segundos: "))
dia = segundos // 86400 % 24
hora = segundos // 60 // 60 % 60
minuto = segundos // 60 % 60
segundos = segundos % 60
print(dia, "dias", hora, "horas", minuto, "minutos", segundos, "segundos")
