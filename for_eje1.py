texto = "Seré un pro en Python, mejor que el mismo Guido van Rossum. ¿Será que si?"

espacios = 0
puntos = 0
comas = 0

for caracter in texto:
    if caracter == " ":
        espacios += 1
    elif caracter == ".":
        puntos += 1
    elif caracter == ",":
        comas += 1

print("Cantidad de espacios:", espacios)
print("Cantidad de puntos:", puntos)
print("Cantidad de comas:", comas)
