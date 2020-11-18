"""Se tienen dos diccionarios, uno de precios de productos y otro de stock de
productos. Ambos tienen las mismas claves. Se pide
a. acceder a los dos diccionarios simultáneamente calculando la
multiplicación del precio por la cantidad de artículos para cada producto,
e imprimir los casos en que dicho monto supere los $100.000.
b. Calcular el monto total para el total del stock."""

lista_de_precios = {"agua": 60, "queso": 400, "leche": 60, "yogurt": 125}
lista_de_stock = {"agua": 1000, "queso": 2000, "leche": 1500, "yogurt": 500}

precio_por_producto = {}

# for producto in precios:
#     precio_por_producto[producto] = precios[producto] * stock[producto]
#
# for producto, precio in precio_por_producto.items():
#     if precio > 100000:
#         print(producto, precio)
#
# print("Precio total para todo el stock:", sum(precio_por_producto.values()))


indice_producto = 0
indice_precios = 1
indice_stocks = 1

for precios, stocks in zip(lista_de_precios, lista_de_stock):

    precio_por_producto[precios] = lista_de_precios[precios] * stocks[precios]