"""
crear un programa para ingresar un numero de tres cifras y luego 
mostrar la suma de sus cifras y elevarlas al cuadrado

"""

print("Ingrese una cifra de tres digitos: ")
num = int(input())

if(num >= 100 and num <= 999):
    numT = str(num)
    suma = int(numT[0]) + int(numT[1]) + int(numT[2])

    cuadrado = suma * suma
    print("La suma es: ", suma)
    print("El cudrado es: ", cuadrado)

else:
    print("Debe ingresar un numero de 3 cifras")