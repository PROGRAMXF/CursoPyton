while True:
    a = int(input("Jugador 1: 1 = Piedra,  2 = Papel, 3 = Tijera: "))
    b = int(input("Jugador 2: 1 = Piedra,  2 = Papel, 3 = Tijera: "))

    if a == 1 and b == 3:
        print("Jugador 1 gana")

    elif a == 2 and b == 1:
        print("Jugador 1 gana")

    elif a == 3 and b == 2:
        print("Jugador 1 gana")

    elif b == 1 and a == 3:
        print("Jugador 2 gana")

    elif b == 2 and a == 1:
        print("Jugador 2 gana")

    elif b == 3 and a == 2:
        print("Jugador 2 gana")

    else:
        print("Ninguno gana!")




            