s = int(input("Ingrese cantidad de segundos  "))
m = s/60
h = s/3600
d = (s/3600)/24

if s >= 172800:
    print(int(d), ":", int(round(h % 24)), ":", int(round(m % 60)),
          ":", (s % 60))
elif s > 86400:
    print(int(d), ":", int(round(h % 24)), ":", int(round(m % 60)),
          ":", (s % 60))
else:
    print(int(d), ":", int(round(h % 24)), ":", int(round(m % 60)),
          ":", (s % 60))
