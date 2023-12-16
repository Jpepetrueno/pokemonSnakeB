vocales = ["a", "e", "i", "o", "u"]
frase = "Hola, estoy aprendiendo Python"
vocales_encontradas = []

for vocal in frase:
    if vocal in vocales:
        print(f"He encontrado la {vocal}")
        vocales_encontradas += vocal
print(f"Las vocales encontradas son las siguientes {vocales_encontradas}")
print(f"Fueron encontradas {len(vocales_encontradas)} vocales")
