print("Ingrese un numero inicial: ")
i = int(input())
print("Ingrese un numero final: ")
f = int(input())

suma = 0 #inicializamos suma con 0

print("***Los numeros pares del rango***")

while i <= f:
    if i % 2 == 0:
        print(i)
    i+= 1