import os
import random
import time
import readchar

TAMANO_MAPA = 18
CANTIDAD_OBSTACULOS = 25


class Pokemon:
    def __init__(self, nombre, vida, ataques):
        self.nombre = nombre
        self.vida = vida
        self.vida_total = vida
        self.ataques = ataques

    def imprimir_vida(self):
        porcentaje_vida = self.vida / self.vida_total
        cantidad_barras = int(porcentaje_vida * 20)
        print(
            f"{self.nombre}: [{'#' * cantidad_barras}{'-' * (20 - cantidad_barras)}] {self.vida}/{self.vida_total}"
            f"({porcentaje_vida * 100:.1f}%)"
        )


class Entrenador:
    def __init__(self, nombre, pokemon):
        self.nombre = nombre
        self.pokemon = pokemon


def operacion_aritmetica():
    cuenta = random.choice(["+", "-", "*"])
    if cuenta == "+":
        numero1 = random.randint(2, 9)
        numero2 = random.randint(2, 9)
        respuesta_buena = numero1 + numero2
    elif cuenta == "-":
        numero1 = random.randint(2, 19)
        numero2 = random.randint(
            1, numero1
        )  # Asegura que numero2 siempre sea menor o igual a numero1
        respuesta_buena = numero1 - numero2
    else:
        numero1 = random.randint(2, 3)
        numero2 = random.randint(1, 10)
        respuesta_buena = numero1 * numero2
    return numero1, numero2, cuenta, respuesta_buena


def seleccionar_ataque(pokemon):
    while True:
        print("Ataques disponibles: ")
        for i, ataque in enumerate(pokemon.ataques.keys(), start=1):
            print(f"{i}. {ataque}")
        opcion = input("Elige un ataque: ")
        try:
            opcion = int(opcion)
            if 1 <= opcion <= len(pokemon.ataques):
                return list(pokemon.ataques.keys())[opcion - 1]
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número.")


def generar_mapa(tamano, obstaculos, entrenadores):
    mapa = [[" " for _ in range(tamano)] for _ in range(tamano)]
    for entrenador in entrenadores:
        while True:
            x, y = random.randint(0, tamano - 1), random.randint(0, tamano - 1)
            if mapa[y][x] == " ":
                mapa[y][x] = entrenador.nombre[0]
                entrenador.posicion = (x, y)
                break
    for _ in range(obstaculos):
        while True:
            x, y = random.randint(0, tamano - 1), random.randint(0, tamano - 1)
            if mapa[y][x] == " ":
                mapa[y][x] = "#"
                break
    return mapa


def imprimir_mapa(mapa, posicion_usuario, entrenadores):
    os.system("cls" if os.name == "nt" else "clear")  # Limpia la terminal
    for y in range(len(mapa)):
        for x in range(len(mapa[y])):
            if (x, y) == posicion_usuario:
                print("@", end="")
            elif any(
                    entrenador.posicion == (x, y)
                    for entrenador in entrenadores
                    if entrenador.posicion is not None
            ):
                print("E", end="")
            else:
                print(mapa[y][x], end="")
        print()


def mover_usuario(mapa, posicion_usuario):
    while True:
        print("Usa las teclas w/a/s/d para moverte (arriba/izquierda/abajo/derecha): ")
        movimiento = readchar.readchar()
        x, y = posicion_usuario
        if movimiento == "w" and y > 0 and mapa[y - 1][x] != "#":
            return x, y - 1
        elif movimiento == "s" and y < len(mapa) - 1 and mapa[y + 1][x] != "#":
            return x, y + 1
        elif movimiento == "a" and x > 0 and mapa[y][x - 1] != "#":
            return x - 1, y
        elif movimiento == "d" and x < len(mapa) - 1 and mapa[y][x + 1] != "#":
            return x + 1, y
        else:
            print("Movimiento no válido. Intenta de nuevo.")


def realizar_ataque(pokemon_atacante, pokemon_defensor):
    ataque = seleccionar_ataque(pokemon_atacante)
    if ataque and ataque != "No atacar":
        pokemon_defensor.vida -= pokemon_atacante.ataques[ataque]
        pokemon_defensor.vida = max(0, pokemon_defensor.vida)
        print(
            f"{pokemon_atacante.nombre} usa {ataque}, {pokemon_defensor.nombre} "
            f"tiene {pokemon_defensor.vida} de vida restante."
        )
    else:
        print(f"{pokemon_atacante.nombre} elige no atacar.")


def turno_usuario(pokemon_usuario, pokemon_oponente):
    num1_op, num2_op, operacion, respuesta_correcta = operacion_aritmetica()
    tiempo_inicio = time.time()
    respuesta_usuario = input(
        f"Tienes 20 segundos para resolver la siguiente operación: {num1_op} {operacion} {num2_op} = "
    )
    tiempo_transcurrido = time.time() - tiempo_inicio
    if tiempo_transcurrido > 20:
        print("Tiempo agotado. Pierdes tu turno.")
        respuesta_usuario = None

    if respuesta_usuario:
        try:
            respuesta_usuario = int(respuesta_usuario)
        except ValueError:
            print("Por favor, ingresa un número.")
            return
        if respuesta_usuario == respuesta_correcta:
            print(
                f"¡Respuesta correcta! {num1_op} {operacion} {num2_op} = {respuesta_correcta}"
            )
            realizar_ataque(pokemon_usuario, pokemon_oponente)
        else:
            print(
                f"Respuesta incorrecta. La respuesta correcta es {respuesta_correcta}. Pierdes tu turno."
            )


def turno_oponente(pokemon_usuario, pokemon_oponente):
    if pokemon_oponente.vida > 0:
        realizar_ataque(pokemon_oponente, pokemon_usuario)


def batalla(pokemon_usuario, pokemon_oponente):
    while pokemon_usuario.vida > 0 and pokemon_oponente.vida > 0:
        pokemon_usuario.imprimir_vida()
        pokemon_oponente.imprimir_vida()
        turno_usuario(pokemon_usuario, pokemon_oponente)
        os.system("cls" if os.name == "nt" else "clear")
        turno_oponente(pokemon_usuario, pokemon_oponente)
        os.system("cls" if os.name == "nt" else "clear")

    if pokemon_usuario.vida <= 0:
        print(f"¡{pokemon_oponente.nombre} gana la batalla!")
        return False
    elif pokemon_oponente.vida <= 0:
        print(f"¡{pokemon_usuario.nombre} gana la batalla!")
        return True


def crear_pokemon():
    pikachu = Pokemon(
        "Pikachu",
        90,
        {"Bola Voltio": 13, "Onda Trueno": 12, "Rayo": 15, "No atacar": 0},
    )
    squirtle = Pokemon(
        "Squirtle",
        110,
        {"Placaje": 10, "Pistola de Agua": 11, "Burbuja": 10, "No atacar": 0},
    )
    calyrex = Pokemon(
        "Calyrex Jinete Espectral",
        100,
        {"Orbes Espectro": 12, "Rayo solar": 10, "Bola polen": 14, "No atacar": 0},
    )
    blacephalon = Pokemon(
        "Blacephalon",
        80,
        {"Bola Sombra": 12, "Lanzallamas": 15, "Energibola": 10, "No atacar": 0},
    )
    volcanion = Pokemon(
        "Volcanion",
        110,
        {"Chorro de Vapor": 11, "Lanzallamas": 13, "Tierra viva": 10, "No atacar": 0},
    )
    volcarona = Pokemon(
        "Volcarona",
        85,
        {
            "Giro Fuego": 13,
            "Picadura": 9,
            "Rayo Solar": 14,
            "Sofoco": 15,
            "Vendaval": 12,
            "Zumbido": 11,
            "No atacar": 0,
        },
    )
    kyogre = Pokemon(
        "Kyogre", 100, {"Cascada": 13, "Ventisca": 10, "Hidrobomba": 14, "No atacar": 0}
    )
    return [pikachu, squirtle, calyrex, blacephalon, volcanion, volcarona, kyogre]


def elegir_pokemon(pokemons):
    pokemon_usuario = None
    while pokemon_usuario is None:
        os.system("cls" if os.name == "nt" else "clear")
        print("¿Qué Pokémon quieres controlar?")
        for i, pokemon in enumerate(pokemons, start=1):
            print(f"{i}. {pokemon.nombre}")

        opcion = input("Introduce el número del Pokémon: ")
        try:
            opcion = int(opcion)
            if 1 <= opcion <= len(pokemons):
                pokemon_usuario = pokemons[opcion - 1]
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")
                time.sleep(2)
                os.system("cls" if os.name == "nt" else "clear")
        except ValueError:
            print("Por favor, ingresa un número.")
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")

    return pokemon_usuario


def main():
    pokemons = crear_pokemon()

    # Elige tu Pokemon
    pokemon_usuario = elegir_pokemon(pokemons)
    if pokemon_usuario is None:
        return

    pokemons.remove(pokemon_usuario)

    entrenadores = []
    for i in range(3):
        pokemon_entrenador = random.choice(pokemons)
        pokemons.remove(pokemon_entrenador)
        entrenadores.append(Entrenador(f"Entrenador {i + 1}", pokemon_entrenador))

    mapa = generar_mapa(TAMANO_MAPA, CANTIDAD_OBSTACULOS, entrenadores)
    posicion_usuario = (0, 0)

    entrenadores_derrotados = 0

    while entrenadores_derrotados < len(entrenadores):
        imprimir_mapa(mapa, posicion_usuario, entrenadores)
        posicion_usuario = mover_usuario(mapa, posicion_usuario)
        x, y = posicion_usuario
        for entrenador in entrenadores:
            if entrenador.posicion == posicion_usuario:
                print(f"¡Has encontrado a {entrenador.nombre}!")
                resultado_batalla = batalla(pokemon_usuario, entrenador.pokemon)
                if resultado_batalla:
                    entrenadores_derrotados += 1
                    entrenador.posicion = None
                    pokemon_usuario.vida = pokemon_usuario.vida_total
                else:
                    print("Has perdido la batalla. ¡Inténtalo de nuevo!")
                    return

    print("¡Felicidades! Has derrotado a todos los entrenadores y ganaste el juego.")


if __name__ == "__main__":
    main()
