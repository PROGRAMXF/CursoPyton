preguntas = {
    "¿Cual es el animal mas grande del mundo? " : "La ballena azul",
    "¿Cual es el planeta mas cercano al sol?" : "Marcurio",
    "¿Que animal tiene la piel con rayas blancas y negras? " : "La cebra",
}

puntos = 0

for pregunta, respuesta in preguntas.items():
    print(pregunta)

    respuesta_usuario = input("Tu respuesta: ")

    if respuesta_usuario.lower() == respuesta.lower(): #lower: minuscula
        print("Correcto")
        puntos += 1

    else:
        print("Incorrecto, la respuesta correcta es: ", respuesta)

print(f"Finalizó el juego,  los puntos obtenidos fueron: {puntos} puntos")


