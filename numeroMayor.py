#determinar el mayor de tres numeros ingresados

n1 = int(input("Ingrese el primer numero: "))

n2 = int(input("Ingrese el segundo numero: "))

n3 = int(input("Ingrese el tercero numero: "))

if n1 > n2 and n1 > n3:
    print("El numero mayor es n1: ", n1)
elif n2 > n1 and n2 > n3:
    print("El numero mayor es n2: ", n2)
else:
    print("El numero mayor es n3: ", n3)