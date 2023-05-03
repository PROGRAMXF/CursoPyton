#pedir un numero e indicar si es positivo, negativo o cero

print("Ingrese un numero para verificar")
n = int(input())

if(n>0):
    print("Es un numero positivo")
elif(n<0):
    print("Es un numero negativo")
else:
    print("El numero ingresado es 0")