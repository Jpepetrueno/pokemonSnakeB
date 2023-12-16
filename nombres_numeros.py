from num2words import num2words


def nombre_del_numero(n, lang):
    try:
        return num2words(int(n), lang=lang)
    except NotImplementedError:
        return f"La conversión de números a palabras no está soportada en {lang}"


idiomas = {
    "1": ("es", "español"),
    "2": ("en", "inglés"),
    "3": ("pt", "portugués"),
    "4": ("de", "alemán"),
    "5": ("fr", "francés"),
    "6": ("it", "italiano"),
    "7": ("ru", "ruso"),
    "8": ("ja", "japonés"),
    "9": ("ko", "coreano"),
    "10": ("todos", "todos"),
}

while True:
    entrada = input("Por favor, ingrese un número o 'salir' para terminar: ")
    if entrada.lower() == "salir":
        break
    try:
        x = float(entrada)
        print("Por favor, elija un idioma: ")
        for idioma, (lang, nombre) in idiomas.items():
            print(f"{idioma} para {nombre}")
        idioma = input()
        if idioma == "10":
            for lang, nombre in idiomas.values():
                if lang != "todos":
                    print(f"{nombre}: {nombre_del_numero(x, lang)}")
        else:
            lang, nombre = idiomas[idioma]
            print(f"{nombre}: {nombre_del_numero(x, lang)}")
    except (ValueError, KeyError):
        print(
            "Eso no es un número válido o una opción de idioma válida. Por favor, intente de nuevo."
        )
