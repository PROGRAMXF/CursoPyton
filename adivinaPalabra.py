import random

palabras = ["futbol", "tenis", "golf"]

palabra = random.choice(palabras)

letras_adivinadas = []


while True:
    letra = input("Ingrese letra: ")
    letras_adivinadas.append(letra)

    palabra_oculta =""
    for c in palabra:
        if c in letras_adivinadas:
            palabra_oculta+=c
        else:
            palabra_oculta+="_"

    print(palabra_oculta)

    if "_" not in palabra_oculta:
        print("Felicidades, adivinaste la palabra")
        break