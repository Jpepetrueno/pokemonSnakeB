"""
Este módulo implementa un programa interactivo que solicita al usuario que elija una opción entre A, B y C.
El programa seguirá solicitando una entrada hasta que el usuario proporcione una respuesta válida.
Luego, el programa proporcionará una respuesta basada en la elección del usuario.
"""

respuesta = ""  # Inicializa la variable de respuesta

# El bucle iterará hasta que se reciba una respuesta válida ("a", "b" o "c")
for _ in iter(int, 1):
    respuesta = input("¿Qué opción prefieres: A, B, C? ")  # Solicita al usuario que elija una opción
    # Si la respuesta es válida, se rompe el bucle
    if respuesta.lower() in ["a", "b", "c"]:
        break

# Procesa la respuesta del usuario y proporciona una respuesta correspondiente
if respuesta.lower() == "a":
    print("En hora buena, has elegido bien.")  # Respuesta para la opción A
elif respuesta.lower() == "b":
    print("No es una mala opción pero tampoco es la mejor.")  # Respuesta para la opción B
elif respuesta.lower() == "c":
    print("Mala respuesta.")  # Respuesta para la opción C
else:
    print("Debes dar una respuesta coherente.")  # Respuesta para una entrada no válida
