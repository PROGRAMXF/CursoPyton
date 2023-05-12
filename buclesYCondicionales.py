"""
juego: adivina el numero

se debe establecer el numero que se va a adivinar en una variable, 
luego se debe solicitar el numero, si el numero no es correcto, se debe mostrar un mensaje:
Mayor o Menor,  dependiendo del caso, el programa terminara cuando el usuario
acierta con el numero ingresado.

"""

numero = 45 #numero que se debe adivinar
control = 0 #variable de control de ciclo
intentos = 1 #controlar los intentos

print("Bienvenido al juego adivina el numero")

while(control == 0):
    print("Intento numero: ", intentos)
    print("Ingrese un numero:")
    num = int(input()) #solicitamos un numero para comparar
    
    if(num == numero):
        print("Adivinaste el numero")
        print("Utilizaste: ", intentos," intentos")
        print("Fin del juego")

        control = 1
    elif(num > numero):
        print("El numero ingresado es mayor, intenta nuevamente")
        intentos+=1
    elif(num < numero):
        print("El numero ingresado es menor, intenta nuevamente")
        intentos+=1
              