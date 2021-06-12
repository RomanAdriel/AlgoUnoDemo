def ingreso_valor():
    numero = int(input("ingresa un valor: "))
    return numero

def cacluo_factorial(num):
    numero = num
    fact_default = 1
    while num > 1:
        fact_default = fact_default * num
        num = num - 1

    return fact_default

def imprimir_respuesta(mensaje,valor):
    print(mensaje, valor)


imprimir_respuesta("sarasa", cacluo_factorial(ingreso_valor()))