def ingreso_valor():
    numero = int(input("ingresa un valor: "))
    return numero

def cacluo_factorial(num):
    numero = num
    factorial_por_defecto = 1
    while num > 1:
        fact_default = factorial_por_defecto * num
        num = num - 1

    return factorial_por_defecto

def imprimir_respuesta(mensaje,valor):
    print(mensaje, valor)


imprimir_respuesta("sarasa", cacluo_factorial(ingreso_valor()))