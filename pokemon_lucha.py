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


pikachu = Pokemon("Pikachu", 80, {"Bola Voltio": 10, "Onda Trueno": 11, "No atacar": 0})
squirtle = Pokemon(
    "Squirtle", 90, {"Placaje": 10, "Pistola de Agua": 12, "Burbuja": 9, "No atacar": 0}
)

while pikachu.vida > 0 and squirtle.vida > 0:
    os.system("cls" if os.name == "nt" else "clear")  # Limpia la consola
    pikachu.imprimir_vida()
    squirtle.imprimir_vida()
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
            ataque_squirtle = seleccionar_ataque(squirtle)
            if ataque_squirtle:
                if ataque_squirtle != "No atacar":
                    pikachu.vida -= squirtle.ataques[ataque_squirtle]
                    pikachu.vida = max(0, pikachu.vida)
                    print(
                        f"Squirtle usa {ataque_squirtle}, Pikachu tiene {pikachu.vida} de vida restante."
                    )
                else:
                    print("Squirtle elige no atacar.")
        else:
            print("Respuesta incorrecta. Pierdes tu turno.")

    if pikachu.vida > 0:
        ataque_pikachu = random.choice(list(pikachu.ataques.keys()))
        if ataque_pikachu != "No atacar":
            squirtle.vida -= pikachu.ataques[ataque_pikachu]
            squirtle.vida = max(0, squirtle.vida)
            print(
                f"Pikachu usa {ataque_pikachu}, Squirtle tiene {squirtle.vida} de vida restante."
            )
        else:
            print("Pikachu elige no atacar.")

if pikachu.vida <= 0:
    print("¡Squirtle gana la batalla!")
elif squirtle.vida <= 0:
    print("¡Pikachu gana la batalla!")
