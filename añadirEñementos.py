paises = ["Argentina", "Brasil", "Colombia", "Peru", "Uruguay"]
paises2 = ["Bolivia", "Venezuela"]

print(paises)

paises.append("chile")
paises.append("España")

print(paises)

paises.insert(1, "Ecuador")

print(paises)

#ahora ingresamos un nuevo elemento a traves de una variable

print("Ingrese un nuevo pais")
p = input()
paises.append(p)
print(paises)

#ahora ingresamos paises2 dentro de paises
paises.extend(paises2)
print(paises)