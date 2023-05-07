#solicitar dos numeros y saber si son iguales o diferentes
print("Ingres el numero para la primer variable: ")
num1 = int(input())


print("Ingres el numero para la segunda variable: ")
num2 = int(input())

if(num1 == num2):
    suma = num1 + num2
    print("AMBOS NUMEROS SON IGUALES")
    print("La suma de ambos numeros es : ", suma)

else:
    print("AMBOS NUMEROS SON DIFERENTES")
    mul = num1 * num2
    print("La multiplicacion es de ambos numeros es: ", mul)

