import os
import random
import time


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


def operacion_aritmetica():
    cuenta = random.choice(["+", "-", "*"])
    if cuenta == "+":
        numero1 = random.randint(2, 10)
        numero2 = random.randint(2, 10)
        respuesta_buena = numero1 + numero2
    elif cuenta == "-":
        numero1 = random.randint(2, 20)
        numero2 = random.randint(
            1, numero1
        )  # Asegura que numero2 siempre sea menor o igual a numero1
        respuesta_buena = numero1 - numero2
    else:
        numero1 = random.randint(2, 10)
        numero2 = random.randint(2, 10)
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


def main():
    pikachu = Pokemon(
        "Pikachu", 80, {"Bola Voltio": 10, "Onda Trueno": 11, "No atacar": 0}
    )
    squirtle = Pokemon(
        "Squirtle",
        90,
        {"Placaje": 10, "Pistola de Agua": 12, "Burbuja": 9, "No atacar": 0},
    )
    calyrex = Pokemon(
        "Calyrex Jinete Espectral", 100, {"Orbes Espectro": 15, "No atacar": 0}
    )
    blacephalon = Pokemon(
        "Blacephalon", 90, {"Bola Sombra": 12, "Lanzallamas": 14, "No atacar": 0}
    )
    volcanion = Pokemon("Volcanion", 110, {"Chorro de Vapor": 16, "No atacar": 0})
    volcarona = Pokemon(
        "Volcarona",
        95,
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
    kyogre = Pokemon("Kyogre", 120, {"Cascada": 15, "Ventisca": 16, "No atacar": 0})

    pokemons = [pikachu, squirtle, calyrex, blacephalon, volcanion, volcarona, kyogre]

    # Elige tu Pokemon
    pokemon_usuario = input(
        "¿Qué Pokémon quieres controlar? (Pikachu/Squirtle/Calyrex Jinete Espectral/Blacephalon/Volcanion/Volcarona/Kyogre): "
    )
    pokemon_usuario = next(
        (
            pokemon
            for pokemon in pokemons
            if pokemon.nombre.lower() == pokemon_usuario.lower()
        ),
        None,
    )
    if pokemon_usuario is None:
        print("No se encontró el Pokémon. Por favor, intenta de nuevo.")
        return

    pokemons.remove(pokemon_usuario)
    pokemon_oponente = random.choice(pokemons)

    while pokemon_usuario.vida > 0 and pokemon_oponente.vida > 0:
        os.system("cls" if os.name == "nt" else "clear")  # Limpia la consola
        pokemon_usuario.imprimir_vida()
        pokemon_oponente.imprimir_vida()
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
                continue
            if respuesta_usuario == respuesta_correcta:
                ataque_usuario = seleccionar_ataque(pokemon_usuario)
                if ataque_usuario:
                    if ataque_usuario != "No atacar":
                        pokemon_oponente.vida -= pokemon_usuario.ataques[ataque_usuario]
                        pokemon_oponente.vida = max(0, pokemon_oponente.vida)
                        print(
                            f"{pokemon_usuario.nombre} usa {ataque_usuario}, {pokemon_oponente.nombre} tiene {pokemon_oponente.vida} de vida restante."
                        )
                    else:
                        print(f"{pokemon_usuario.nombre} elige no atacar.")
            else:
                print("Respuesta incorrecta. Pierdes tu turno.")

        if pokemon_oponente.vida > 0:
            ataque_oponente = random.choice(list(pokemon_oponente.ataques.keys()))
            if ataque_oponente != "No atacar":
                pokemon_usuario.vida -= pokemon_oponente.ataques[ataque_oponente]
                pokemon_usuario.vida = max(0, pokemon_usuario.vida)
                print(
                    f"{pokemon_oponente.nombre} usa {ataque_oponente}, {pokemon_usuario.nombre} tiene {pokemon_usuario.vida} de vida restante."
                )
            else:
                print(f"{pokemon_oponente.nombre} elige no atacar.")

    if pokemon_usuario.vida <= 0:
        print(f"¡{pokemon_oponente.nombre} gana la batalla!")
    elif pokemon_oponente.vida <= 0:
        print(f"¡{pokemon_usuario.nombre} gana la batalla!")


if __name__ == "__main__":
    main()
