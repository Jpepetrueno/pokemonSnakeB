colores = [
    "rojo",
    "naranja",
    "amarillo",
    "verde",
    "azul",
    "índigo",
    "violeta",
    "rosa",
    "marrón",
    "negro",
]
numeros_en_palabras = [
    "primer",
    "segundo",
    "tercer",
    "cuarto",
    "quinto",
    "sexto",
    "séptimo",
    "octavo",
    "noveno",
    "décimo",
]

for numero, color in zip(numeros_en_palabras, colores):
    print(f"El {numero} color de tu caja de colores es el {color}")
