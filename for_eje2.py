# Solicitar al usuario que ingrese un texto
texto = input("Por favor, ingresa un texto: ")

# Inicializar un contador para las letras mayúsculas
mayusculas = 0

# Iterar a través de cada carácter en el texto
for caracter in texto:
    # Si el carácter es una letra mayúscula, incrementar el contador
    if "A" <= caracter <= "Z":
        mayusculas += 1

# Imprimir la cantidad de letras mayúsculas
print("Cantidad de letras mayúsculas:", mayusculas)
