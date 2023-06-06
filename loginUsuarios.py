class User:
    def __init__(self, nom, pwd):
        self.nom = nom
        self.pwd = pwd

u1 = User("adela", "123")
u2 = User("carlos", "321")

usuarios = [u1, u2]
n = input("Ingrese usuario: ")
p = input("Ingrese contraseña: ")

k=0

for i in range(len(usuarios)):
    if usuarios[i].nom == n and usuarios[i].pwd == p:
        print(usuarios[i].nom, "Bienvenido al programa")
    k = 1
    break

if k==0:
    print("Intente nuevamente")
        
