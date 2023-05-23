#creamos la clase:
class Jugador:
    
    """n = "Cristiano"

#creamos una variable que represente al jugador:

j1 = Jugador()
    

#print("Jugador: ", j1.n)"""

#ahora queremos crear diferentes objetos:

    def __init__(self, nombre, dorsal): #el parametro self nos permite agregar las propiedades
        self.nombre = nombre
        self.dorsal = dorsal
#init lleva doble guion de cada lado

j1 = Jugador("Cristiano Ronaldo", "7")
j2 = Jugador("Messi", "10")

print("Jugador 1: ",j1.nombre, "Dorsal: ",j1.dorsal)
print("Jugador 2: ",j2.nombre, "Dorsal: ",j2.dorsal)

