import random
palabras = ["Azul", "Verde", "Rojo"]

#n = random.randint(0, 2)

#print(palabras[n])

#ahora lo hacemos con un ciclo while

while True:
    pal = input("Ingrese un color: ")
    n = random.randint(0, 2)

    if pal == palabras[n]:
        print("Muy bien, adivinaste la palabra")
        break
    else:
        print("Intentalo nuevamente ")