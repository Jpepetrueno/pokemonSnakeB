respuesta = ""
while respuesta not in ["a", "b", "c"]:
    respuesta = input("¿Qué opción prefieres: A, B, C? ")

if respuesta.lower() == "a":
    print("En hora buena, has elegido bien.")
elif respuesta.lower() == "b":
    print("No es una mala opción pero tampoco es la mejor.")
elif respuesta.lower() == "c":
    print("Mala respuesta.")
else:
    print("Debes dar una respuesta coherente.")
