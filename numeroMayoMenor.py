lista = []
cantidad = int(input("Ingrese la cantidad de numeros: "))
i = 1
while i <= cantidad:
    n = int(input(f"{i} Ingrese un numero: ")) # es una variable temporal que se va a ir sobre escribiendo en cada iteracion del ciclo por que la estamos llenando con un numero nuevo en cada iteracion

    lista.append(n) #la variable n la almacenamos en nuestra lista
    i+=1

print("Numero mayor: ", max(lista))
print("Numero minimo: ", min(lista))