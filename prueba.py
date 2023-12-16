from num2words import num2words


def nombre_del_numero(n):
    return num2words(n, lang="es")


while True:
    try:
        x = int(input("Por favor, ingrese un número entero: "))
        break
    except ValueError:
        print("Eso no es un número entero válido. Por favor, intente de nuevo.")

nombres_de_numeros = {
    2: "Dos",
    3: "Tres",
    4: "Cuatro",
    5: "Cinco",
    6: "Seis",
    7: "Siete",
    8: "Ocho",
    9: "Nueve",
}

if x < 0:
    x = 0
    print("Negativo cambiado a cero")
elif x == 0:
    print("Cero")
elif x == 1:
    print("Uno")
elif 2 <= x <= 9:
    print(nombres_de_numeros[x])
elif x >= 10:
    print(nombre_del_numero(x))
