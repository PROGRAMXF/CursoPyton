paises = ["Colombia", "Brasil", "Argentina"]
print("Ingrese el indice a modificar: ")
i = int(input())

print("Ingrese un nuevo valor: ")
val = input()

paises[i] = val
print(paises)

#otra manera de modificar listas es estableciendo el rango:

paises = ["Colombia", "Brasil", "Argentina", "Peru"]
paises[1:3] = ["Chile", "Ecuador"]
print(paises)

#ahora eliminamos elementos de nuestra lista

paises = ["Colombia", "Brasil", "Argentina", "Peru"]
paises.pop(2)
print(paises)

#otra manera de eliminar un indice es: 

paises = ["Colombia", "Brasil", "Argentina", "Peru"]
print("Ingrese un indice: ")
i = int(input())
paises.pop(i)
print(paises)

#ahora mediante un ciclo while vamos a recorrer todos los elementos de nuestra lista:

paises = ["Colombia", "Brasil", "Argentina", "Peru"]
j = 0

while j < len(paises):
    print("Indice: ", j, "valor: ", paises[j])
    j+=1
    
print("Ingrese un indice: ")
i = int(input())
paises.pop(i)
print(paises)
