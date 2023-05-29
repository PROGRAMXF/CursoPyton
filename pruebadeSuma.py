list = []
n = int(input("Cuantos numeros vas a sumar: "))

i = 1

while i <= n:
    num = int(input("Ingrese un numero: "))
    list.append(num)

    i += 1

sum = 0
x = 0

while x < len(list):  

    sum+=list[x]
    x+=1

print("Los numeros son: ", sum)