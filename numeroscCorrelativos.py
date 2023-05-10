"""
pedir a un usuario que ingrese un numero entero positivo
e imprimir todos los numeros correlativos entre el ingresado por el usuario
y uno menos del cuadruple del mismo

"""

num = int(input("Ingresar un numero: "))

if(num > 0):
    cuadruple = num * num * num * num
    print("El cuadruple es: ", cuadruple)

    while(num < cuadruple):
        print("", num)
        num+=1

else:
    print("Ingrese un numero entero positivo")