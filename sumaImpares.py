
list = []
num = int(input("Cuantos numeros deseas sumar: "))
i = 1


while i <= num:
    numero = int(input("Ingrese un numero: "))
    list.append(numero)

    i+=1

    suma = 0
    j = 0

    while j < len(list):
        if list[j] % 2 == 1:
            suma+=list[j]
        j+=1

print(f"La suma es:  {suma}")
      
    