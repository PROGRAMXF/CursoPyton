"""
programa que solicite una lista de numeros o nombres, los
almacene en una lista y luego los muestre ordenados
"""

lista = []
print("Ingrese una lista de numeros")
cantidad = int(input())
i = 0

while i < cantidad:
    print("Ingrese el elemento: ", i+1)
    nom = input()

    lista.append(nom)
    i+=1

    #ordenamos la lista
    lista.sort()
    print("La lista ordenada es: ", lista)
