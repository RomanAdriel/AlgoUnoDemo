"""Se tienen dos diccionarios, uno de precios de productos y otro de stock de
productos. Ambos tienen las mismas claves. Se pide
a. acceder a los dos diccionarios simultáneamente calculando la
multiplicación del precio por la cantidad de artículos para cada producto,
e imprimir los casos en que dicho monto supere los $100.000.
b. Calcular el monto total para el total del stock."""

lista_de_precios = {"agua": 60, "queso": 400, "leche": 60, "yogurt": 125}
lista_de_stock = {"queso": 2000, "agua": 1000, "leche": 1500, "yogurt": 500}

totales = {}

for alimento in lista_de_precios:

    if alimento in lista_de_stock:
        totales[alimento] = lista_de_precios[alimento] * lista_de_stock[alimento]

    if totales[alimento] > 100000:
        print(alimento, totales[alimento])

print(sum(totales.values()))
