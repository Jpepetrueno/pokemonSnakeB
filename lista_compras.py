# Lista de productos disponibles en el supermercado
productos_disponibles = [
    "arroz",
    "frijoles",
    "pasta",
    "salsa de tomate",
    "aceite de oliva",
    "sal",
    "pimienta",
    "azúcar",
    "harina",
    "leche",
    "huevos",
    "mantequilla",
    "queso",
    "yogur",
    "pan",
    "cereales",
    "avena",
    "galletas",
    "chocolate",
    "café",
    "té",
    "jugo de naranja",
    "agua embotellada",
    "refrescos",
    "papas",
    "zanahorias",
    "tomates",
    "cebollas",
    "ajo",
    "pimientos",
    "lechuga",
    "espinacas",
    "manzanas",
    "plátanos",
    "naranjas",
    "uvas",
    "fresas",
    "pollo",
    "carne de res",
    "pescado",
    "camarones",
    "tofu",
    "pan integral",
    "miel",
    "mermelada",
    "mostaza",
    "mayonesa",
    "vinagre",
    "papel higiénico",
    "jabón",
]

# Lista de compras del usuario
lista_de_compras = []

while True:
    producto = input(
        "¿Qué producto deseas agregar a la lista de compras? (escribe 'q' para terminar): "
    )

    if producto.lower() == "q":
        break

    # Verifica si el producto está disponible en el supermercado
    if producto.lower() in productos_disponibles:
        lista_de_compras.append(producto.lower())
        print(f"El producto {producto} ha sido agregado a la lista de compras.")
    else:
        print(
            f"Lo siento, el producto {producto} no está disponible en el supermercado."
        )

print("Tu lista de compras es:")
for producto in lista_de_compras:
    print("- " + producto)
