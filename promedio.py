"""Calcular el promedio de una lista de numeros"""

nums = [] #la lista esta vacia para poder ingresar la cantidad que yo quiero
print("Cuantos numeros ingresara?")

n = int(input())
i=0

while i < n:
    print("Valor numero: ", i+1)
    val = float(input())
    nums.append(val)
    i+=1

    prom = sum(nums) / len(nums)

    print("El promedio es: ", prom)