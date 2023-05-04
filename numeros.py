#escribir un programa que pida un numero entre 0 y 99.999 y me diga cuantas cifras tiene

print("Ingrese un numero entre 0 y 99.999")
num = int(input())

if(num < 0 or num > 99999):
    print("El numero ingresado no es valido")
else:
    if(num<10):
        print("El numero ingresado tiene 1 cifra")
    elif(num<100):
        print("El numero ingresado tiene dos cifras")

    elif(num<1000):
        print("El numero ingresado tiene tres cifras")

    elif(num<10000):
        print("El numero ingresado tiene cuatro cifras")

    elif(num<100000):
        print("El numero ingresado tiene cinco cifras")



