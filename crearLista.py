#creamos una clase:
class Persona:

#definimos los atributos de la clase:
    def _init_(self, nom, tel):
     self.nom = nom
     self.tel = tel

i = 0
#creamos una lista vacia:
lista = []

#creamos un metodo para mostrar las personas guardadas
def Mostrar():
    k = 0
    while k < len(lista):
        print(lista[k].nom, " ", lista[k].tel)
        k+=1

while i == 0:
    print("Menú")
    print("1 - Registrar persona: ")
    print("2 - Consultar listado: ")
    print("3 - Salir")

    opcion = int(input())

    if opcion == 1:
        print("*** Registrar ***")
        n = input("Ingrese el nombre: ")
        t = input("Ingrese el telefono: ")
        #creamos el objeto tipo persona:
        per = Persona(n, t)
        #y lo guardamos en la lista:
        lista.append(per)

        print("Persona guardada con exito")

    elif opcion == 2:
        print("*** Mostrar ***")
        Mostrar()

    elif opcion == 3:
        exit()

    else:
        print("Opcion invalida")

